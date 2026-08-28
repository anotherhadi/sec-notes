---
title: "FTP"
description: "Enumeration, exploitation and post-exploitation techniques for FTP servers."
tags: ["ftp", "network", "service"]
publishDate: 2026-04-29
---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Enumeration](#enumeration)
  - [Banner grabbing](#banner-grabbing)
  - [Nmap](#nmap)
- [Anonymous Login](#anonymous-login)
- [Brute Force](#brute-force)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

FTP runs on **port 21** (control) and uses a secondary data channel (port 20 for active, ephemeral port for passive).
Common implementations: vsftpd, ProFTPD, Pure-FTPd, FileZilla Server, IIS FTP.

## Enumeration

### Banner grabbing

```bash
nc -nv $IP 21
ftp $IP
```

The banner often reveals the software version: cross-reference with CVE databases.

### Nmap

```bash
nmap -sV -p 21 $IP
nmap -p 21 --script ftp-* $IP
```

Key scripts:

- `ftp-anon`: checks anonymous login
- `ftp-bounce`: tests for FTP bounce attack
- `ftp-brute`: brute-force credentials
- `ftp-syst`: retrieves system info

## Anonymous Login

```bash
ftp $IP
# Username: anonymous
# Password: <empty> or anonymous@
```

If allowed, list and download everything:

```bash
ls -la
mget *
```

Check for writable directories: you may be able to upload a webshell if FTP root overlaps with a web root.

## Brute Force

```bash
hydra -l $user -P ~/wordlists/rockyou.txt ftp://$IP
medusa -h $IP -u $user -P ~/wordlists/rockyou.txt -M ftp
```

Try default credentials first: `admin:admin`, `ftp:ftp`, `user:password`.
