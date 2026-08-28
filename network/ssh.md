---
title: "SSH"
description: "Enumeration, exploitation and post-exploitation techniques for SSH servers."
tags: ["ssh", "network", "service"]
publishDate: 2026-05-04
---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Enumeration](#enumeration)
  - [Banner grabbing](#banner-grabbing)
  - [Nmap](#nmap)
- [Connect](#connect)
- [Brute Force](#brute-force)
- [Key-Based Auth](#key-based-auth)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

SSH runs on **port 22** and provides an encrypted remote shell.
Common implementations: OpenSSH, Dropbear, Bitvise.

## Enumeration

### Banner grabbing

```bash
nc -nv $IP 22
ssh $IP
```

The banner reveals the software and version (e.g. `OpenSSH_9.2`).

### Nmap

```bash
nmap -sV -p 22 $IP
nmap -p 22 --script ssh-* $IP
```

Key scripts:

- `ssh-hostkey`: retrieves the server's public key
- `ssh-auth-methods`: lists accepted authentication methods
- `ssh-brute`: brute-force credentials

## Connect

```bash
ssh $user@$IP
ssh -p 2222 $user@$IP
ssh -i id_rsa $user@$IP
```

## Brute Force

```bash
hydra -l $user -P ~/wordlists/rockyou.txt ssh://$IP
medusa -h $IP -u $user -P ~/wordlists/rockyou.txt -M ssh
```

Only viable if password auth is enabled. Check with:

```bash
ssh -v $user@$IP
```

Look for `publickey,password` in the output.

## Key-Based Auth

If you find a private key (`id_rsa`), set permissions and connect:

```bash
chmod 600 id_rsa
ssh -i id_rsa $user@$IP
```

If the key is encrypted, crack the passphrase:

```bash
ssh2john id_rsa > hash.txt
john hash.txt --wordlist=~/wordlists/rockyou.txt
hashcat -m 22921 hash.txt ~/wordlists/rockyou.txt
```
