---
title: "Subdomains Discovery"
description: "Methods and tools for enumerating subdomains of a target domain."
tags: ["web", "enumeration", "discovery", "subdomain"]
publishDate: 2026-06-01
---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [FFUF](#ffuf)
- [Google Dorking](#google-dorking)
- [Certificate Transparency](#certificate-transparency)
- [Passive DNS](#passive-dns)
- [DMARC](#dmarc)
- [ASN & IP Ranges](#asn--ip-ranges)
- [Favicon Hash](#favicon-hash)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## FFUF

See also [FFUF](/notes/web/ffuf) for fuzzing-based subdomain discovery.

## Google Dorking

Google dorks can surface subdomains indexed by Google without any active scanning.

```
site:*.$domain
site:*.$domain -www
site:*.$domain inurl:admin
site:*.$domain ext:php | ext:json | ext:xml
```

## Certificate Transparency

CT logs record every TLS certificate ever issued for a domain. Querying them is
passive and reliable.

```bash
curl -s "https://crt.sh/?q=%25.$domain&output=json" | jq '.[].name_value' | sort -u
```

Tools that aggregate CT logs:

- [crt.sh](https://crt.sh)
- [censys.io](https://search.censys.io)

## Passive DNS

Passive DNS databases store historical DNS resolutions collected from resolvers
worldwide; useful for finding subdomains that no longer resolve but once did.

```bash
# Amass (passive mode, no active scanning)
amass enum -passive -d $domain

# subfinder (uses many passive sources)
subfinder -d $domain -silent
```

## DMARC

DMARC can reveal more domains associated with a target.

Go to `dmarc.live/info/$domain`, it allows you to find domains using the
same DMARC record.

## ASN & IP Ranges

Finding the ASN of a target exposes its entire IP range, which may contain
undiscovered subdomains or related infrastructure.

```bash
# Get ASN from an IP
whois $ip | grep -i "asn\|orgname\|origin"

# Get IP ranges from ASN
whois -h whois.radb.net -- '-i origin AS12345' | grep route
```

## Favicon Hash

A unique favicon can be fingerprinted to find other domains hosted by the same
organisation, including subdomains on non-standard ports.

```bash
# Compute the MMH3 hash of the favicon
python3 -c "
import requests, mmh3, base64
r = requests.get('https://$domain/favicon.ico')
h = mmh3.hash(base64.encodebytes(r.content))
print(h)
"
```

Then search the hash on [Shodan](https://shodan.io): `http.favicon.hash:<hash>`
