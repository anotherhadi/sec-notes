# Sec Notes

A personal collection of security notes and cheatsheets, covering offensive security and OSINT.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Blog](#blog)
- [Linux](#linux)
- [Network](#network)
- [OSINT](#osint)
- [Web](#web)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Blog

- [The Password is 'admin': Why Default Credentials Are Still Breaking the Internet](./blog/default-passwords.md): Default credentials like admin:admin remain one of the most exploited vulnerabilities on the internet. Learn why they're dangerous, how the Mirai botnet took down half the web with just 62 passwords, and how to protect your infrastructure: plus introducing default-creds, an open-source database to look up factory-set credentials in seconds.
- [Unmasking Github Users: How to Identify the Person Behind Any Github Profile](./blog/github-users-osint.md): Ever wondered who is behind a specific Github username? This guide covers advanced OSINT techniques to deanonymize users, find hidden email addresses, and link Github accounts to real-world identities.

## Linux

- [GRUB Boot Bypass](./linux/grub-bypass.md): Physical access techniques to get a root shell by editing GRUB boot parameters.
- [Linux Privilege Escalation](./linux/privesc.md): Common misconfigurations and weaknesses to check when escalating privileges on Linux.

## Network

- [FTP](./network/ftp.md): Enumeration, exploitation and post-exploitation techniques for FTP servers.
- [NFS](./network/nfs.md): Enumeration, mounting and privilege escalation techniques for NFS shares.
- [Nmap](./network/nmap.md): Host discovery, port scanning, service detection and NSE scripting
- [RDP](./network/rdp.md): Enumeration, exploitation and post-exploitation techniques for RDP servers.
- [SSH](./network/ssh.md): Enumeration, exploitation and post-exploitation techniques for SSH servers.
- [Telnet](./network/telnet.md): Enumeration, exploitation and post-exploitation techniques for Telnet servers.

## OSINT

- [Bluesky](./osint/bluesky.md): Enumeration, search operators, API endpoints and tools for investigating Bluesky accounts.
- [Information Gathering](./osint/information-gathering.md): Essential cybersecurity cheatsheet for Information Gathering and Open Source Intelligence (OSINT). Discover data related to emails, domains, usernames, and images using both command line and online tools.
- [Sock Puppets](./osint/sock-puppets.md): Essential cheatsheet on creating and managing Sock Puppets (fake identities) for ethical security research and Open Source Intelligence (OSINT), focusing on maintaining separation from personal data and bypassing common verification.
- [Tips](./osint/tips.md): A cheatsheet of practical tips and unconventional methods for Open Source Intelligence (OSINT), focusing on advanced data visualization, information leakage detection, and utilizing web archives for historical data.
- [X / Twitter](./osint/twitter-x.md): Enumeration, search operators, deleted content recovery and tools for investigating X accounts.

## Web

- [Directory Discovery](./web/directory-discovery.md): Techniques and tools for discovering hidden directories and files on web servers.
- [FFUF](./web/ffuf.md): Reference and usage examples for ffuf, a fast web fuzzer for directories, endpoints and subdomains.
- [Subdomains Discovery](./web/subdomains-discovery.md): Methods and tools for enumerating subdomains of a target domain.
