---
title: "GRUB Boot Bypass"
description: "Physical access techniques to get a root shell by editing GRUB boot parameters."
tags: ["linux", "grub", "physical-access", "privesc"]
publishDate: 2026-05-18
---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Techniques](#techniques)
  - [init=/bin/sh](#initbinsh)
  - [init=/bin/bash](#initbinbash)
  - [rd.break (systemd)](#rdbreak-systemd)
  - [single (single-user mode)](#single-single-user-mode)
  - [systemd.unit=rescue.target](#systemdunitrescuetarget)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

When GRUB is not password-protected, anyone with physical access can edit boot parameters and bypass authentication entirely.

At the GRUB menu, press **`e`** to edit the selected entry. Modify the line starting with `linux`, then press **`F10`** to boot.

## Techniques

### init=/bin/sh

Replaces the init process with a shell; drops directly into a root shell before any login prompt.

```
linux ... init=/bin/sh
```

Filesystem is mounted read-only by default. Remount to make changes:

```bash
mount -o remount,rw /
```

### init=/bin/bash

Same as above but uses bash. Add `rw` on the `linux` line to mount read-write from the start:

```
linux ... rw init=/bin/bash
```

### rd.break (systemd)

Interrupts the boot process in the initramfs, before the real root filesystem is mounted. Useful for resetting the root password.

```
linux ... rd.break
```

From the initramfs shell:

```bash
mount -o remount,rw /sysroot
chroot /sysroot
passwd root
exit
```

### single (single-user mode)

Boots into maintenance mode. On some distros this drops to a root shell without a password prompt (not Debian/Ubuntu).

```
linux ... single
```

### systemd.unit=rescue.target

systemd equivalent of single-user mode: minimal services, root shell.

```
linux ... systemd.unit=rescue.target
```
