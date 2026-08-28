---
title: "FFUF"
description: "Reference and usage examples for ffuf, a fast web fuzzer for directories, endpoints and subdomains."
tags:
  ["web", "enumeration", "discovery", "subdomain", "directory", "bruteforce"]
publishDate: 2026-06-01
---

**Fuff (or ffuf)** is a fast web fuzzer written in Go, mainly used in
cybersecurity to discover hidden directories, files, API endpoints, subdomains,
vhosts and more. Its speed and flexibility make it a must-have for pentesters
and bug bounty hunters.

```bash
# Flags:
# -rate 50 -t 50 # Limit requests to 50 per second with 50 concurrent threads
# -X POST|GET|PUT # Set method
# -e .php,.asp,.bak,.db # Set the extension
# -recursion -recursion-depth 3 # Recursive fuzzing up to 3 levels deep
# -fc 404,500 # Exclude responses with status codes 404 and 500

# Examples:
ffuf -w wordlist.txt -u $url/FUZZ # Basic directory/file fuzzing using a wordlist
ffuf -w subdomains.txt -u https://FUZZ.$url # Subdomain fuzzing
ffuf -w vhosts.txt -u $url -H "Host: https://FUZZ.$url" # Virtual host fuzzing by modifying the Host header
ffuf -w wordlist.txt -u $url/page.php?FUZZ=value # GET parameter fuzzing in the query string
ffuf -w wordlist.txt -u $url/api -X POST -d 'FUZZ=value' # POST body parameter fuzzing
ffuf -w wordlist.txt -u $url/FUZZ -b 'session=abcdef' # Use a session cookie during fuzzing
ffuf -w headers.txt -u $url -H "X-Custom-Header: FUZZ" # HTTP header fuzzing
ffuf -w passwords.txt -X POST -u $url/login -d "username=admin&password=FUZZ" # Password brute-forcing for user "admin"
ffuf -w users.txt:USER -w passwords.txt:PASS -u "$url/login?username=USER&password=PASS" -mode pitchfork # Pitchfork mode: matches each line from both wordlists (USER[i], PASS[i])
ffuf -w users.txt:USER -w passwords.txt:PASS -u "$url/login?username=USER&password=PASS" -mode clusterbomb # Clusterbomb mode: tests every user with every password combination
```
