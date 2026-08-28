---
title: "Directory Discovery"
description: "Techniques and tools for discovering hidden directories and files on web servers."
tags: ["web", "enumeration", "discovery", "directory"]
publishDate: 2026-06-01
---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [FFUF](#ffuf)
- [Robots.txt](#robotstxt)
- [Sitemap.xml](#sitemapxml)
- [Dirb](#dirb)
- [Spider - Katana](#spider---katana)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## FFUF

See also [FFUF](/notes/web/ffuf) for fuzzing-based directory discovery.

## Robots.txt

```bash
curl -s $url/robots.txt
```

## Sitemap.xml

```bash
curl -s $url/sitemap.xml
```

## Dirb

```bash
dirb $url
```

## Spider - Katana

A spider is a tool that crawls a website and collects information about its
structure and content. It can be used to find hidden directories, files, and
parameters.

```bash
katana -c 15 -p 15 -u $url > output
```
