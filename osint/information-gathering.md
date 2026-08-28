---
title: "Information Gathering"
description: "Essential cybersecurity cheatsheet for Information Gathering and Open Source Intelligence (OSINT). Discover data related to emails, domains, usernames, and images using both command line and online tools."
tags: ["osint", "enumeration", "information-gathering"]
publishDate: 2026-05-03
---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

    - [IKnowYou](#iknowyou)
- [Command line tools](#command-line-tools)
- [Online tools](#online-tools)
- [OSINT Aggregation Tool](#osint-aggregation-tool)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

**Information Gathering**, often referred to as **Open Source Intelligence (OSINT)** in the context of ethical hacking, is the systematic collection and analysis of publicly available data about a target, providing the foundational knowledge necessary to identify potential vulnerabilities and craft targeted security assessments.

## Command line tools

| **From**  | **Use**                                                                                         |
| --------- | ----------------------------------------------------------------------------------------------- |
| Email     | `holehe $email`                                                                                 |
|           | `ghunt email $email` (for google account)                                                       |
|           | `github-recon $email` ([link](http://github.com/anotherhadi/github-recon/), for github account) |
| Domain    | `theHarvester -d $domain -l 100`                                                                |
|           | `theHarvester -d $domain -l 100 -b all` (full)                                                  |
| Username  | `sherlock $username`                                                                            |
| Image     | `exiftool $imagePath`                                                                           |
| Instagram | `instaloader profile $username`                                                                 |
| Github    | `trufflehog github --org=$usernameOrOrg`                                                        |
|           | `github-recon $username` ([link](http://github.com/anotherhadi/github-recon/))                  |

## Online tools

| **For**    | **Use**                                                |
| ---------- | ------------------------------------------------------ |
| Visualiser | [OSINTracker](https://www.osintracker.com/)            |
| IP         | [Shodan](https://www.shodan.io/)                       |
|            | [Censys](https://search.censys.io/)                    |
| Domain     | [Whois](https://www.whois.com/whois/)                  |
|            | [crt.sh](https://crt.sh/) (certificate transparency)   |
| Name       | [Webmii](https://webmii.com/)                          |
|            | [BreachDirectory](https://breachdirectory.org/)        |
|            | [LeakLookup](https://leak-lookup.com/search)           |
|            | [IntelX](https://intelx.io/)                           |
|            | [Genealogic.review](https://genealogic.review/)        |
| SSID       | [Wigle](https://wigle.net/)                            |
| Image      | [PimEyes (faces)](https://pimeyes.com/)                |
|            | [Lenso (faces)](https://lenso.ai)                      |
|            | [TinEye](https://tineye.com)                           |
|            | [Pic2Map (exif geolocation)](https://www.pic2map.com/) |
| Username   | [DeHashed](https://dehashed.com/search)                |
|            | [BreachDirectory](https://breachdirectory.org/)        |
|            | [IntelX](https://intelx.io/)                           |
|            | [LeakLookup](https://leak-lookup.com/search)           |
|            | [Oathnet](https://oathnet.org/)                        |
| Email      | [DeHashed](https://dehashed.com/search)                |
|            | [Hunter](https://hunter.io/)                           |
|            | [HaveIBeenPwned](https://haveibeenpwned.com/)          |
|            | [BreachDirectory](https://breachdirectory.org/)        |
|            | [LeakLookup](https://leak-lookup.com/search)           |
|            | [IntelX](https://intelx.io/)                           |
|            | [Oathnet](https://oathnet.org/)                        |
| Phone      | [Epieos](https://epieos.com/)                          |
| Instagram  | [Dumpor](https://dumpor.io/)                           |
| Misc       | [Goosint](https://goosint.com/)                        |
|            | [OSINT Framework](https://osintframework.com/)         |
|            | [OSINT Dojo](https://osintdojo.com/)                   |

## OSINT Aggregation Tool

<a href="https://iknowyou.hadi.icu" class="link-card not-prose" target="_blank">
  <span>
    <h4>IKnowYou</h4>
    <p>Self-hosted OSINT aggregation platform: Run dozens of open-source intelligence tools against a single target in parallel; all from one clean web interface.</p>
  </span>
</a>
