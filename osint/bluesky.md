---
title: "Bluesky"
description: "Enumeration, search operators, API endpoints and tools for investigating Bluesky accounts."
tags: ["osint", "bluesky", "social-media", "enumeration"]
publishDate: 2026-04-29
---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Key Concepts](#key-concepts)
- [Account Enumeration](#account-enumeration)
  - [Resolve handle → DID](#resolve-handle-%E2%86%92-did)
  - [Resolve DID → history (all past handles, keys, creation date)](#resolve-did-%E2%86%92-history-all-past-handles-keys-creation-date)
  - [Get profile metadata](#get-profile-metadata)
  - [Followers / following](#followers--following)
- [Search Operators](#search-operators)
    - [API equivalent](#api-equivalent)
- [Google Dorks](#google-dorks)
- [Tools](#tools)
  - [BlueSkyNet](#blueskynet)
  - [ClearSky](#clearsky)
  - [plc.directory](#plcdirectory)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Key Concepts

Bluesky is built on the **AT Protocol**. Every account has two identifiers:

- **Handle**: `user.bsky.social` or a custom domain (can change)
- **DID**: `did:plc:ewvi7nxzyoun6zhxrhs64oiz` (permanent, survives handle changes)

All public content is accessible **without an account**. Follower/following lists are also public by default.

## Account Enumeration

### Resolve handle → DID

```
https://bsky.social/xrpc/com.atproto.identity.resolveHandle?handle=$HANDLE
```

### Resolve DID → history (all past handles, keys, creation date)

```
https://plc.directory/$DID
```

### Get profile metadata

```
https://public.api.bsky.app/xrpc/app.bsky.actor.getProfile?actor=$HANDLE
```

Returns: DID, display name, description, follower/following count, creation date, avatar URL.

### Followers / following

```
https://public.api.bsky.app/xrpc/app.bsky.graph.getFollowers?actor=$HANDLE&limit=100
https://public.api.bsky.app/xrpc/app.bsky.graph.getFollows?actor=$HANDLE&limit=100
```

Paginate with the `cursor` field from the response.

## Search Operators

Bluesky's full-text search supports these operators (combinable):

| Operator    | Example                       | Effect                        |
| ----------- | ----------------------------- | ----------------------------- |
| `"..."`     | `"exact phrase"`              | Exact match                   |
| `from:`     | `from:handle.bsky.social`     | Posts by user                 |
| `mentions:` | `mentions:handle.bsky.social` | Posts mentioning user         |
| `since:`    | `since:2024-01-01`            | After date (UTC, YYYY-MM-DD)  |
| `until:`    | `until:2024-06-30`            | Before date (UTC, YYYY-MM-DD) |
| `lang:`     | `lang:fr`                     | Language (ISO 639-1)          |
| `domain:`   | `domain:github.com`           | Posts linking to domain       |
| `#tag`      | `#osint`                      | Hashtag                       |

#### API equivalent

```
https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts?q={QUERY}&author={HANDLE}&since=2024-01-01&until=2024-12-31&lang=en&limit=25
```

## Google Dorks

Bluesky is heavily indexed by Google. Useful for finding profiles and posts without touching the platform:

```
site:bsky.app "$TARGET_NAME"
site:bsky.app "$TARGET_NAME" inurl:profile
site:bsky.app "$KEYWORD" since:2024-01-01
```

## Tools

### BlueSkyNet

Web app for searching and exporting Bluesky data to CSV. Wraps the public API with a UI for advanced search filters.

- [github.com/jakecreps/blueskynet](https://github.com/jakecreps/blueskynet)

### ClearSky

Shows block lists, blocking history, and who blocked a given account. Useful for mapping relationships and adversarial clusters.

- [clearsky.app](https://clearsky.app)

### plc.directory

Official DID PLC directory. Lookup a DID to get full account history: creation date, all past handles, key rotations.

- [plc.directory](https://plc.directory)
