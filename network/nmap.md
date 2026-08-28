---
title: "Nmap"
description: "Host discovery, port scanning, service detection and NSE scripting"
tags: ["nmap", "network", "enumeration"]
publishDate: 2026-05-18
---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Host Discovery](#host-discovery)
- [Port Scanning](#port-scanning)
- [Service & Version Detection](#service--version-detection)
- [OS Detection](#os-detection)
- [Aggressive Scan](#aggressive-scan)
- [Timing Templates](#timing-templates)
- [NSE Scripts](#nse-scripts)
- [Output Formats](#output-formats)
- [Common Profiles](#common-profiles)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

Nmap is a network scanner used for host discovery, port scanning, service/version detection, OS fingerprinting, and vulnerability scripting via NSE.

## Host Discovery

```bash
nmap -sn 192.168.1.0/24          # ping sweep, no port scan
nmap -sn -PR 192.168.1.0/24      # ARP ping (local network)
nmap -Pn $IP                      # skip host discovery, treat as up
```

## Port Scanning

```bash
nmap $IP                          # top 1000 ports (SYN scan if root)
nmap -p 80,443,8080 $IP           # specific ports
nmap -p 1-65535 $IP               # all ports
nmap -p- $IP                      # shorthand for all ports
nmap -sU $IP                      # UDP scan
nmap -sU -sS $IP                  # UDP + SYN together
```

Scan types:

- `-sS`: SYN scan (stealth, requires root)
- `-sT`: TCP connect scan (no root needed)
- `-sU`: UDP scan
- `-sA`: ACK scan (firewall rule mapping)
- `-sN/sF/sX`: Null, FIN, Xmas (evasion, unreliable on Windows)

## Service & Version Detection

```bash
nmap -sV $IP
nmap -sV --version-intensity 9 $IP   # more aggressive probing
```

## OS Detection

```bash
nmap -O $IP
nmap -O --osscan-guess $IP           # guess if not confident
```

## Aggressive Scan

```bash
nmap -A $IP     # -sV -O --script=default --traceroute
```

## Timing Templates

```bash
nmap -T0 $IP    # paranoid (IDS evasion, very slow)
nmap -T1 $IP    # sneaky
nmap -T3 $IP    # normal (default)
nmap -T4 $IP    # aggressive (faster, good for CTFs)
nmap -T5 $IP    # insane (may miss results)
```

## NSE Scripts

```bash
nmap --script default $IP
nmap --script vuln $IP
nmap --script "ftp-*" $IP
nmap --script safe $IP
nmap --script $script --script-args user=$user,pass=$password $IP
```

Common script categories: `auth`, `brute`, `default`, `discovery`, `dos`, `exploit`, `intrusive`, `safe`, `version`, `vuln`.

Scripts are located in `/usr/share/nmap/scripts/`.

## Output Formats

```bash
nmap -oN output.txt $IP      # normal
nmap -oX output.xml $IP      # XML
nmap -oG output.gnmap $IP    # grepable
nmap -oA output $IP          # all three at once
```

## Common Profiles

Quick full scan:

```bash
nmap -p- -T4 --min-rate 5000 -sV -sC -oA full $IP
```

CTF/lab initial recon:

```bash
nmap -sV -sC -p- --open $IP
```

UDP top ports:

```bash
nmap -sU --top-ports 100 $IP
```
