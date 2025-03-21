# Personal Security Checklist

This is my personal cybersecurity checklist that I use for both personal and professional projects. 
Feel free to adapt it to your own needs.

## 1. Authentication & Access Control

- [ ] Use strong, unique passwords for each service (min 12 chars, mixed case, numbers, symbols)
- [ ] Implement 2FA/MFA wherever possible (prefer app-based over SMS)
- [ ] Use a password manager (Bitwarden, 1Password, KeePass)
- [ ] Implement least privilege access control
- [ ] Regular access review and pruning of unused accounts
- [ ] Set up account lockout after multiple failed attempts
- [ ] Enforce session timeouts for sensitive applications

## 2. Network Security

- [ ] Use a VPN when on public WiFi
- [ ] Configure firewall (both software and hardware)
- [ ] Disable unnecessary network services
- [ ] Segment networks where possible
- [ ] Keep router firmware updated
- [ ] Change default router credentials
- [ ] Use WPA3 for WiFi encryption when available
- [ ] Disable remote management on routers/devices
- [ ] Use encrypted DNS (DoH or DoT)

## 3. Software Security

- [ ] Keep all software updated (OS, applications, plugins)
- [ ] Enable automatic updates where appropriate
- [ ] Use antivirus/anti-malware software
- [ ] Review application permissions regularly
- [ ] Remove/uninstall unused software
- [ ] Only download software from trusted sources
- [ ] Verify software signatures/checksums
- [ ] Use sandboxed applications for untrusted software

## 4. Data Protection

- [ ] Encrypt sensitive data at rest
- [ ] Use full-disk encryption
- [ ] Implement secure backup strategy (3-2-1 rule)
- [ ] Securely erase data before device disposal
- [ ] Use HTTPS for all web services
- [ ] Implement proper key management
- [ ] Regular data classification and review
- [ ] Define data retention periods

## 5. Development Security

- [ ] Use secure coding practices
- [ ] Input validation and sanitization
- [ ] Parameterized queries (prevent SQL injection)
- [ ] Output encoding to prevent XSS
- [ ] Implement CSRF protection
- [ ] Set secure cookie flags (Secure, HttpOnly, SameSite)
- [ ] Proper error handling (no sensitive data in errors)
- [ ] Regular security testing (SAST, DAST, penetration testing)
- [ ] Dependency scanning for vulnerabilities
- [ ] Secure APIs with rate limiting and proper authentication

## 6. Physical Security

- [ ] Lock screens when away from devices
- [ ] Secure physical access to servers/network equipment
- [ ] Use privacy screens in public locations
- [ ] Track company assets and equipment
- [ ] Implement clean desk policy
- [ ] Secure disposal of physical documents (shredding)
- [ ] Lock up portable devices when not in use

## 7. Monitoring & Incident Response

- [ ] Enable logging for security events
- [ ] Regular log review
- [ ] Set up alerts for suspicious activities
- [ ] Have an incident response plan
- [ ] Document security incidents and lessons learned
- [ ] Test recovery procedures
- [ ] Know who to contact in case of a security incident

## 8. Awareness & Training

- [ ] Stay informed about current threats
- [ ] Subscribe to security advisories
- [ ] Recognize phishing attempts
- [ ] Verify requests for sensitive information
- [ ] Understand social engineering techniques
- [ ] Regular security training and updates

## 9. Mobile Device Security

- [ ] Use screen lock (PIN/password/biometric)
- [ ] Enable remote wipe capability
- [ ] Keep apps updated
- [ ] Only install apps from official stores
- [ ] Review app permissions
- [ ] Disable unnecessary features (Bluetooth, NFC when not in use)
- [ ] Use encrypted backups

## 10. Cloud Security

- [ ] Use strong authentication for cloud services
- [ ] Review cloud storage permissions regularly
- [ ] Understand shared responsibility model
- [ ] Enable encryption for cloud storage
- [ ] Use private repositories for code
- [ ] Review cloud security settings periodically
- [ ] Implement proper IAM policies

_Note: This is a growing document that I update as I learn more about security best practices._
