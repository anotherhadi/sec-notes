---
title: "Unmasking Github Users: How to Identify the Person Behind Any Github Profile"
description: "Ever wondered who is behind a specific Github username? This guide covers advanced OSINT techniques to deanonymize users, find hidden email addresses, and link Github accounts to real-world identities."
image: "../../../public/images/blog/github-osint-users.png"
tags: ["osint", "github", "cybersecurity"]
publishDate: "2026-01-01"
---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Level 1: The Low-Hanging Fruit](#level-1-the-low-hanging-fruit)
- [Level 2: Digging into Commits](#level-2-digging-into-commits)
  - [The `.patch` Method](#the-patch-method)
  - [The API Events Method](#the-api-events-method)
- [The Verification Loop: Linking Email to Account](#the-verification-loop-linking-email-to-account)
  - [The Email Spoofing Method](#the-email-spoofing-method)
  - [The Search Index: Finding Hidden Contributions](#the-search-index-finding-hidden-contributions)
- [Level 3: Technical Metadata](#level-3-technical-metadata)
  - [SSH Keys](#ssh-keys)
  - [GPG Keys](#gpg-keys)
- [Level 4: Connecting the Dots](#level-4-connecting-the-dots)
- [Automating the Hunt: Github-Recon](#automating-the-hunt-github-recon)
- [Conclusion and Protection: How to Stay Anonymous](#conclusion-and-protection-how-to-stay-anonymous)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

In the world of Open-Source Intelligence (OSINT), we often focus on social media platforms like Twitter or LinkedIn. However, developers frequently leave behind much more detailed personal information on **Github**.

Whether you are a recruiter, a security researcher, or a digital investigator, Github is a goldmine. Why? Because while a user might choose a cryptic handle like `anotherhadi`, their Git configuration often reveals their real name and email address.

## Level 1: The Low-Hanging Fruit

Before diving into technical exploits, start with the obvious. Many users forget how much they have shared in their profile settings.

- **The Bio & Location**: Even a vague location like "Montpellier, France," combined with a niche tech stack (e.g., "COBOL expert"), significantly narrows down the search.
- **External Links**: Check the personal website or blog link. Run a WHOIS lookup on that domain to find registration details. Use other OSINT tools and techniques on those websites to pivot further.
- **The Profile Picture**: Right-click the avatar and use Google Reverse Image Search, Yandex, or other reverse image engines. Developers often use the same professional headshot on Github as they do on LinkedIn.

## Level 2: Digging into Commits

This is the **most effective OSINT** method. While Github masks author names and emails in the web view, this information is permanently embedded in the commit metadata.

### The `.patch` Method

Find a repository where the target has contributed. Open any commit they made, and simply add `.patch` to the end of the URL.

- **URL**: `https://github.com/{username}/{repo}/commit/{commit_hash}.patch`
- Look at the `From:` line. It should look like this: `From: John Doe <j.doe@company.com>`

For example, check: [github.com/anotherhadi/nixy/commit/e6873e8caae491073d8ab7daad9d2e50a04490ce.patch](https://github.com/anotherhadi/nixy/commit/e6873e8caae491073d8ab7daad9d2e50a04490ce.patch)

### The API Events Method

If you cannot find a recent commit, check their **public activity** stream via the Github API.

- **Go to**: `https://api.github.com/users/{target_username}/events/public`
- Search (Ctrl+F) for the word `email`. You will often find the **email address** associated with their `PushEvent` headers, even if they have "Keep my email addresses private" enabled in their current settings.

## The Verification Loop: Linking Email to Account

If you have found an email address and want to be 100% sure it belongs to a specific Github profile, you can use Github’s own attribution engine against itself.

### The Email Spoofing Method

While the previous methods help you find an email _from_ a profile, this technique does the opposite: it identifies which Github account is linked to a specific email address.

**How it works:**
Github attributes commits based on the email address found in the Git metadata. If you push a commit using a specific email, Github will automatically link that commit to the account associated with that address as its **primary email**.

**The Process:**

1. **Initialize a local repo:** `git init investigation`
2. **Configure the target email:** `git config user.email "target@example.com"` and `git config user.name "A Username"`
3. **Create a dummy commit:** `echo "test" > probe.txt && git add . && git commit -m "Probe"`
4. **Push to a repo you own:** Create a new empty repository on your Github account and push the code there.
5. **Observe the result:** Go to the commit history on the Github web interface. The avatar and username of the account linked to that email will appear as the author of the commit.

> **Note:** This method only works if the target email is set as the **Primary Email** on the user's account. It is a foolproof way to confirm if an email address you found elsewhere belongs to a specific Github user.

### The Search Index: Finding Hidden Contributions

Even if an email address is not listed on a user's profile, it may still be indexed within Github's global search.
Github allows you to filter search results by the metadata fields of a commit.
This is particularly useful if the target has **contributed to public repositories** using their real email.

You can use these specific qualifiers in the **Github search bar** (select the "Commits" tab):

- `author-email:target@example.com`: Finds commits where the target is the original author.
- `committer-email:target@example.com`: Finds commits where the target was the one who committed the code (sometimes different from the author).

## Level 3: Technical Metadata

If the email is masked or missing, we can look at the **cryptographic keys** the user uses to communicate with Github.

### SSH Keys

Every user’s public **SSH keys are public**.

- **URL**: `https://github.com/{username}.keys`
- **The Pivot**: You can take the key string and search for it on platforms like **Censys** or **Shodan**. If that same key is authorized on a specific server IP, you have successfully located the user’s infrastructure.

### GPG Keys

If a user signs their commits, their **GPG key** is available at:

- **URL**: `https://github.com/{username}.gpg`
- **The Reveal**: Import this key into your local GPG tool (`gpg --import`). It will often reveal the **Verified Identity** and the primary email address linked to the encryption key.

## Level 4: Connecting the Dots

Once you have a **name**, an **email**, or a **unique username**, it’s time to _pivot_.

- **Username Pivoting**: Use tools like [Sherlock](https://github.com/sherlock-project/sherlock) or [Maigret](https://github.com/soxoj/maigret/) to search for the same username across hundreds of other platforms. Developers are creatures of habit; they likely use the same handle on Stack Overflow, Reddit, or even old gaming forums.
- **Email Pivoting**: Use tools like [holehe](https://github.com/megadose/holehe) to find other accounts registered with the email addresses you just uncovered.

## Automating the Hunt: Github-Recon

If you want to move from manual investigation to automated intelligence, check out [Github-Recon](https://github.com/anotherhadi/github-recon).
Written in Go, this powerful CLI tool aggregates public OSINT data by automating the techniques mentioned above and more. Whether you start with a username or a single email address, it can retrieve SSH/GPG keys, enumerate social accounts, and find "close friends" based on interactions.
Its standout features include a **Deep Scan** mode-which clones repositories to perform regex searches and TruffleHog secret detection—and an automated **Email Spoofing** engine that instantly identifies the account linked to any primary email address.

## Conclusion and Protection: How to Stay Anonymous

If you are a developer reading this, you might be feeling exposed.
Understanding what information about you is publicly visible is the **first step to managing your online presence**. This guide and tools like [github-recon](https://github.com/anotherhadi/github-recon) can help you identify your own publicly available data on Github. Here’s how you can take steps to protect your privacy and security:

- **Review your public profile**: Regularly check your Github profile and
  repositories to ensure that you are not unintentionally exposing sensitive
  information.
- **Manage email exposure**: Use Github's settings to control which email
  addresses are visible on your profile and in commit history. You can also **use
  a no-reply email** address for commits, and an
  [alias email](https://proton.me/support/addresses-and-aliases) for your
  account. Delete/modify any sensitive information in your commit history.
- **Be Mindful of Repository Content**: **Avoid including sensitive information** in
  your repositories, such as API keys, passwords, emails or personal data. Use
  `.gitignore` to exclude files that contain sensitive information.

You can also use a tool like [TruffleHog](github.com/trufflesecurity/trufflehog)
to scan your repositories specifically for exposed secrets and tokens.

**Useful links:**

- [Blocking command line pushes that expose your personal email address](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/blocking-command-line-pushes-that-expose-your-personal-email-address)
- [No-reply email address](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address)

In OSINT, the best hidden secrets are the ones we forget we ever shared. Happy hunting!

---

If you enjoyed this guide, please like and share it! Your support helps me create more infosec & OSINT content.

Have questions or feedback? Feel free to reach out: anotherhadi.clapped234[at]passmail.net
