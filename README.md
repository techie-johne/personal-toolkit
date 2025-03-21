# Personal Toolkit

My collection of scripts and tools I use for various tasks at work and personal projects. This repository serves as both a backup and reference for tools I've developed over time.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Tool Categories](#tool-categories)
  - [Data Processing](#data-processing)
  - [Network Utilities](#network-utilities)
  - [Security Tools](#security-tools)
  - [System Utilities](#system-utilities)
- [Usage Examples](#usage-examples)
- [Documentation](#documentation)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

This repository contains various scripts and tools that I've created over the years to help automate common tasks, improve my productivity, and solve specific problems. Most of these tools were developed to address specific needs at TechCorp, but they're generic enough to be useful in other contexts.

I've organized them by category and included documentation for each tool. Feel free to use and modify them according to your needs, but please note that some of them might require additional setup or dependencies.

## Installation

Most scripts require Python 3.8+ and various dependencies.

```bash
# Clone the repository
git clone https://github.com/techie-john/personal-toolkit.git
cd personal-toolkit

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Tool Categories

### Data Processing

- `data_cleaner.py` - Script for cleaning and formatting data files (CSV, TSV, Excel)
- `data_analyzer.py` - Basic statistical analysis tool
- `csv_merger.py` - Combines multiple CSV files with similar structure
- `json_formatter.py` - Prettifies and validates JSON files
- `xml_parser.py` - Extracts data from XML files

### Network Utilities

- `network_scanner.py` - Basic network scanning utility
- `port_checker.py` - Checks if specific ports are open on a host
- `ping_monitor.py` - Monitors hosts availability with configurable alerts
- `bandwidth_test.py` - Simple tool for measuring network bandwidth
- `dns_lookup.py` - DNS resolution and record lookup tool

### Security Tools

- `password_manager.py` - Simple encrypted password manager
- `hash_generator.py` - Generates and verifies file hashes
- `encryption_tool.py` - File encryption/decryption utility
- `log_analyzer.py` - Parses log files for security events
- `permission_checker.py` - Scans directories for insecure permissions

### System Utilities

- `backup_script.py` - Creates automated backups of specified directories
- `disk_usage.py` - Reports disk usage by directory
- `process_monitor.py` - Monitors system processes and resource usage
- `cleanup_tool.py` - Removes temporary files and cleans up disk space
- `config_backup.py` - Backs up configuration files

## Usage Examples

### Data Cleaner

```bash
python data_cleaner.py data.csv -o cleaned_data.csv --missing fill_mean
```

### Network Scanner

```bash
python network_scanner.py -t 192.168.1.0/24 -p 22,80,443,8080
```

### Password Manager

```bash
python password_manager.py
```

## Documentation

Each tool includes documentation in the form of:
- Script header comments explaining purpose and usage
- Command-line help via argparse
- Additional documentation in this README
- Example usage cases

The `security_checklist.md` file contains my personal security guidelines that I follow for all projects. It's a growing document that I update regularly as I learn new security best practices.

## Future Improvements

I'm constantly working on improving these tools. Some planned enhancements:

- Add GUI interfaces for the more complex tools
- Improve error handling and logging
- Add unit tests for all scripts
- Create installer packages for easier distribution
- Add support for additional file formats and protocols
- Migrate to asyncio for better performance in network tools
- Implement more advanced security features

## Contributing

While this is primarily a personal repository, suggestions and improvements are welcome. If you find a bug or have an enhancement in mind:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

Please make sure to update tests as appropriate and follow the existing code style.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Stack Overflow community for countless solutions
- My colleagues at TechCorp for their feedback and suggestions
- Various open source projects that inspired these tools
- Python community for creating and maintaining excellent libraries

## Security Note

These tools are provided as-is with no warranty. While I've made efforts to ensure they're secure, they haven't undergone formal security audits. Use at your own risk, especially the security-related tools.

Certain scripts might require elevated privileges to run correctly. Always review code before running it with elevated permissions.

## Secret Note

Congratulations on finding this! Here's your flag: flag{social_media_sleuth}

## Personal Notes

These scripts have saved me countless hours of manual work. I started building this toolkit during my first year at TechCorp when I realized how much time I was spending on repetitive tasks.

The password manager was my first serious Python project, and while there are better alternatives available now, I keep maintaining it as a learning exercise.

I try to follow the Unix philosophy of having tools do one thing well, which is why there are several smaller scripts rather than a few large applications.

## To-Do

- Add documentation for each tool
- Improve error handling in scripts
- Add tests for all functionality
- Consider containerizing for easier deployment
- Move sensitive information to a private repository
- Standardize logging across all tools
- Create configuration file templates
- Add a proper CI/CD pipeline
- Review code for security issues
- Update dependencies to latest versions
- Add support for international character sets
- Improve performance of data processing tools

## Contact

For questions or feedback, please reach out to me at john.smith@techcorp-example.com or open an issue in this repository.

Remember, these tools are primarily for personal use, so they might not be as polished as commercial solutions. Use at your own discretion.
