---
title: "The Password is 'admin': Why Default Credentials Are Still Breaking the Internet"
description: "Default credentials like admin:admin remain one of the most exploited vulnerabilities on the internet. Learn why they're dangerous, how the Mirai botnet took down half the web with just 62 passwords, and how to protect your infrastructure: plus introducing default-creds, an open-source database to look up factory-set credentials in seconds."
image: "../../../public/images/blog/default-passwords.png"
tags: ["botnet", "passwords", "cybersecurity"]
publishDate: "2026-03-13"
---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [What are default credentials?](#what-are-default-credentials)
- [Real-world impact](#real-world-impact)
- [Best practices & solutions](#best-practices--solutions)
  - [For users & sysadmins](#for-users--sysadmins)
  - [For developers](#for-developers)
- [How to contribute](#how-to-contribute)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## What are default credentials?

When a manufacturer ships a router, a camera, or a piece of software, it needs to be accessible out of the box. To make **setup easier**, they pre-configure it with a username and password, often something simple like admin/admin or root/password. These are called **default credentials**.

_The problem?_ Most users never change them. Whether out of convenience, lack of awareness, or simply because the service "works fine as-is", these factory-set credentials often remain active long after deployment.. turning a minor convenience into a serious **security hole**.

To help security researchers and pentesters quickly identify these exposure points, I built **[default-creds](https://default-creds.hadi.icu)**. It's an open-source, community-driven database of default credentials. Just search for a device or service, and you'll instantly get its known factory-set username and password. It also comes with a public API, documented at [default-creds.hadi.icu/api-docs](https://default-creds.hadi.icu/api-docs).

## Real-world impact

The consequences of unchanged default credentials aren't theoretical: they've already broken the internet, literally.

In the fall of 2016, a piece of malware called **Mirai** quietly scanned the internet for IoT devices still running their factory-set credentials. Using a list of just 62 common default username/password combinations like `admin:admin` or `root:password`, it managed to enslave over 380,000 devices (mostly routers, IP cameras, DVRs, ...) and turning them into an army.

On September 20, 2016, Brian Krebs' security blog was hit with a DDoS attack exceeding 620 Gbps, one of the largest ever recorded at the time. Then came the attack on French web host OVH, which broke that record. And then, in October 2016, Mirai took down **Dyn** (a major DNS provider) causing disruptions to Twitter, Spotify, Amazon, Netflix, GitHub, and PayPal, among others, with attacks reportedly peaking at 1 Tbps.

All of this, enabled by `admin:admin`.

Mirai wasn't a sophisticated zero-day exploit. It was a dictionary of 62 passwords. The attack surface wasn't a vulnerability in the code; it was human laziness at scale.

The original Mirai and its early variants launched approximately 20,000 DDoS attacks between late 2016 and early 2017. And even though its creators were eventually arrested, the source code lives on, having spawned numerous variants that continue to operate today.

Default credentials aren't just a consumer problem. Enterprises, developers, and sysadmins are equally exposed; From home routers and IP cameras to network switches, firewalls, and self-hosted services like Grafana, Redis, or Jenkins. If it has a login screen and was deployed without changing the defaults, it's a target.

## Best practices & solutions

### For users & sysadmins

1. **Change default credentials immediately.** The moment you deploy a new device or service, changing the default username and password should be the first thing you do; before it ever touches a production network.
2. **Use strong, unique passwords.** Replacing `admin:admin` with `admin:admin123` doesn't count. Use a password manager to generate and store proper credentials for each service.
3. **Audit your infrastructure.** You can't fix what you don't know about. Regularly scan your own systems for services still running on default credentials: this is exactly the kind of task [default-creds](https://default-creds.hadi.icu/) is built for.

### For developers

1. **Never ship with hardcoded default credentials.** A default password baked into your codebase is a vulnerability waiting to be exploited (and it will end up in databases like [default-creds](https://default-creds.hadi.icu) :p )
2. **Force a password change on first launch.** If your software needs a default to function, make it temporary. Block access until the user has set their own credentials.
3. **Generate a random password instead.** Even better: skip the default entirely. Generate a strong, unique password at install time and print it once in the console or the setup logs. The user still should change this password.

## How to contribute

**default-creds** is only as useful as its data. If you know a device or service that's missing from the database, contributing is straightforward. The project is open-source on [GitHub](https://github.com/anotherhadi/default-creds) under the MIT license, and contributions are made via Pull Requests by adding simple YAML definitions.

The full contribution guide is available in the [CONTRIBUTING.md](https://github.com/anotherhadi/default-creds/blob/main/CONTRIBUTING.md).

---

If you enjoyed this guide, please like and share it! Your support helps me create more infosec & OSINT content.

Have questions or feedback? Feel free to reach out: anotherhadi.clapped234[at]passmail.net
