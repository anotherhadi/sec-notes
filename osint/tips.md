---
title: "Tips"
description: "A cheatsheet of practical tips and unconventional methods for Open Source Intelligence (OSINT), focusing on advanced data visualization, information leakage detection, and utilizing web archives for historical data."
tags: ["osint"]
publishDate: 2026-05-03
---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Visualisation](#visualisation)
- [Forgotten passwords](#forgotten-passwords)
- [Archive Search](#archive-search)
- [Google Cache](#google-cache)
- [Domain History](#domain-history)
- [Bookmarklets](#bookmarklets)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Visualisation

Use [OSINTracker](https://app.osintracker.com/) to visualise your findings.
It allows you to create a graph of your findings, which can help you see connections and relationships between different pieces of information.

## Forgotten passwords

To find email addresses and phone numbers associated with an account, you can click on "Forgot password?" on the login page of a website. Be careful, though, this creates notifications and can be detected by the target, and often gives your information away.

## Archive Search

- [Wayback Machine](https://web.archive.org) stores over 618 billion web captures
- [Archive.ph](https://archive.ph) creates on-demand snapshots, including for JS-heavy sites, with both a functional page and screenshot version

## Google Cache

Google keeps a cached version of most indexed pages. Access it with the `cache:` operator:

```
cache:example.com
cache:example.com/page
```

If the page has been taken down or modified, the cached version may still show the original content.

## Domain History

[VirusTotal](https://www.virustotal.com) shows the historical DNS records, subdomains, and associated IPs for any domaint useful when a site has moved or been taken down.

[ViewDNS.info](https://viewdns.info) covers WHOIS history, reverse IP, reverse MX, and port scans from a single interface.

## Bookmarklets

- [K2SOsint/Bookmarklets](https://github.com/K2SOsint/Bookmarklets)
- [tools.myosint.training](https://tools.myosint.training/)
