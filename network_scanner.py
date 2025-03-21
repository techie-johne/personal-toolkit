#!/usr/bin/env python3
"""
Basic Network Scanner
--------------------
Performs simple network scanning operations.
For educational purposes only.
"""
import socket
import ipaddress
import argparse
import concurrent.futures
import subprocess
import platform
import sys

def ping(ip):
    """Check if host is up using ping"""
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', str(ip)]
    
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        if "ttl=" in output.lower() or "time=" in output.lower():
            return (str(ip), True)
    except:
        pass
    return (str(ip), False)

def scan_port(ip, port):
    """Check if a specific port is open"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((str(ip), port))
    sock.close()
    return port, result == 0

def scan_host(ip, ports):
    """Scan specific ports on a host"""
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(lambda port: scan_port(ip, port), ports)
        for port, is_open in results:
            if is_open:
                service = "unknown"
                try:
                    service = socket.getservbyport(port)
                except:
                    pass
                open_ports.append((port, service))
    
    return ip, open_ports

def print_results(ip, open_ports):
    """Display scan results for a host"""
    if open_ports:
        print(f"\nScan results for {ip}:")
        print("-" * 30)
        print("PORT\tSTATE\tSERVICE")
        for port, service in open_ports:
            print(f"{port}/tcp\topen\t{service}")
    else:
        print(f"\nNo open ports found on {ip}")

def main():
    parser = argparse.ArgumentParser(description="Simple Network Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP address/range (e.g., 192.168.1.0/24)")
    parser.add_argument("-p", "--ports", default="22,80,443,8080", help="Comma-separated ports to scan (default: 22,80,443,8080)")
    args = parser.parse_args()
    
    try:
        network = ipaddress.ip_network(args.target, strict=False)
    except ValueError:
        print(f"Error: Invalid IP address or network range: {args.target}")
        sys.exit(1)
    
    try:
        ports = [int(p) for p in args.ports.split(",")]
    except ValueError:
        print("Error: Ports must be numbers separated by commas")
        sys.exit(1)
    
    print(f"Starting scan of {args.target} for ports {args.ports}")
    print("Identifying live hosts...")
    
    # First find live hosts
    live_hosts = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(ping, network)
        for ip, is_up in results:
            if is_up:
                live_hosts.append(ip)
                print(f"Host discovered: {ip}")
    
    if not live_hosts:
        print("No live hosts found.")
        sys.exit(0)
    
    print(f"\nFound {len(live_hosts)} live hosts. Starting port scan...")
    
    # Then scan ports on live hosts
    for host in live_hosts:
        ip, open_ports = scan_host(host, ports)
        print_results(ip, open_ports)
    
    print("\nScan complete!")

if __name__ == "__main__":
    main()
