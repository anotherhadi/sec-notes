---
title: "X / Twitter"
description: "Enumeration, search operators, deleted content recovery and tools for investigating X accounts."
tags: ["osint", "twitter", "x", "social-media", "enumeration"]
publishDate: 2026-04-29
---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Key Concepts](#key-concepts)
- [Account Enumeration](#account-enumeration)
  - [Handle to User ID](#handle-to-user-id)
  - [Banner last update time](#banner-last-update-time)
  - [Timestamp from ID (Snowflake)](#timestamp-from-id-snowflake)
  - [Direct profile URL by ID](#direct-profile-url-by-id)
- [Search Operators](#search-operators)
    - [Direct search URL](#direct-search-url)
- [Google Dorks](#google-dorks)
- [Deleted and Archived Content](#deleted-and-archived-content)
  - [Wayback Machine](#wayback-machine)
  - [Twayback](#twayback)
  - [Profile history](#profile-history)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Key Concepts

Every account has two identifiers:

- **Handle**: `@username` (can change)
- **User ID**: numeric, permanent (survives handle changes and suspensions)

Unlike [Bluesky](./bluesky.md), X now requires a login to browse most content in the browser. The free API tier (v2) is severely limited. Most open-source scraping tools that bypassed the API (Twint, snscrape, GetOldTweets3) are broken since the 2023 API lockdown.

## Account Enumeration

### Handle to User ID

The user ID stays constant when someone changes their handle or gets suspended. Several web tools resolve it:

- [tweeterid.com](https://tweeterid.com/)
- [commentpicker.com/twitter-id.php](https://commentpicker.com/twitter-id.php)

Or via the profile page source: look for `"id_str"` in the page JSON.

### Banner last update time

The profile banner URL contains a Unix timestamp indicating when the banner was last changed:

```
https://pbs.twimg.com/profile_banners/{user_id}/{unix_timestamp}/600x200
```

Right-click the banner image and copy the URL, or inspect the page source. Convert the timestamp at [unixtimestamp.com](https://www.unixtimestamp.com/).

### Timestamp from ID (Snowflake)

Twitter IDs are Snowflake IDs: the numeric value encodes the exact creation time of a tweet or account. Extract it with:

```python
tweet_id = 1234567890123456789
timestamp_ms = (tweet_id >> 22) + 1288834974657
```

`1288834974657` is Twitter's custom epoch (Nov 4, 2010). Works on both tweet IDs and user IDs: useful to confirm account creation date without needing profile metadata.

Several online converters exist if you don't want to do it manually: search "snowflake id decoder".

### Direct profile URL by ID

Old tweet/profile URLs using numeric IDs still resolve even after handle changes:

```
https://x.com/i/user/$USER_ID
```

## Search Operators

Accessible at `x.com/search`. Operators are combinable.

| Operator          | Example                    | Effect                   |
| ----------------- | -------------------------- | ------------------------ |
| `"..."`           | `"exact phrase"`           | Exact match              |
| `from:`           | `from:handle`              | Posts by user            |
| `to:`             | `to:handle`                | Posts directed at user   |
| `since:`          | `since:2024-01-01`         | After date (YYYY-MM-DD)  |
| `until:`          | `until:2024-06-30`         | Before date (YYYY-MM-DD) |
| `lang:`           | `lang:fr`                  | Language (ISO 639-1)     |
| `near:`           | `near:"Paris" within:10km` | Geo (web only, not API)  |
| `geocode:`        | `geocode:48.85,2.35,5km`   | Geo by coordinates       |
| `filter:images`   |                            | Posts with images        |
| `filter:videos`   |                            | Posts with videos        |
| `filter:links`    |                            | Posts with URLs          |
| `filter:verified` |                            | Verified accounts only   |
| `-filter:replies` |                            | Exclude replies          |
| `min_retweets:`   | `min_retweets:100`         | Engagement threshold     |
| `min_faves:`      | `min_faves:500`            | Engagement threshold     |
| `#tag`            | `#osint`                   | Hashtag                  |
| `-term`           | `-spam`                    | Exclude term             |

Boolean: spaces imply AND, use uppercase `OR` for alternatives, parentheses for grouping.

#### Direct search URL

```
https://x.com/search?q=from%3A$HANDLE+since%3A2024-01-01&f=live
```

`f=live` returns chronological results instead of relevance-ranked.

## Google Dorks

```
site:x.com "$TARGET"
site:twitter.com "$TARGET"
site:x.com/i/status "$KEYWORD"
"twitter.com/$HANDLE" OR "x.com/$HANDLE"
```

Old `twitter.com` URLs are still indexed separately from `x.com`, search both.

## Deleted and Archived Content

### Wayback Machine

```
https://web.archive.org/web/*/twitter.com/$HANDLE/status/*
https://web.archive.org/web/*/x.com/$HANDLE/status/*
```

Manually browse snapshots, or use [waybacktweets](https://github.com/claromes/waybacktweets) to batch-retrieve CDX data:

```bash
pip install waybacktweets
waybacktweets $HANDLE
```

Outputs CSV/JSON with archived tweet URLs. Useful for deleted posts and suspended accounts.

### Twayback

Web tool wrapping the same Wayback CDX API with a UI:

```
https://twayback.space/
```

Note: only works if the tweet was crawled before deletion.

### Profile history

The Wayback Machine also archives profile pages: past bios, display names, profile photos, header images. Check snapshots at:

```
https://web.archive.org/web/*/twitter.com/$HANDLE
```
