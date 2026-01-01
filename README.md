# DVWA SQL Injection Detection

This project is a Python script that demonstrates how SQL injection vulnerabilities can be detected safely and legally using an intentionally vulnerable test application.

It is designed to be run **only** against DVWA (Damn Vulnerable Web App) running locally on your own machine.

---

## What This Script Demonstrates

This script shows how to:

  - Send input to a website automatically using Python
  - Compare normal input vs unexpected input
  - Detect when a website behaves incorrctly
  - Identify a possible SQL injection vulnerability

**This is not about hacking real websites.**

It is about learning how vulnerabilities happen and how they can be detected.

---

## What Is SQL Injection?

SQL injection happens when:

  - A website takes user input
  - Accidentallty treats that input as instructions, instead of treating it as data

If strange input causes the website to return more data than intended, that is a vulnerability.

This scripot detects that behaviour by comparing responses.

---

## Requirements

- macOS / Linux / Windows
- Python 3
- Docker
- DVWA (Damn Vulnerable Web App) running locally
- Python `requests` library

---

## Setting Up DVWA

Run DVWA using Docker:

```
docker run -d -p 8080:80 vulnerables/web-dvwa
```

Open in your browser:

```
http://localhost:8080
```

Login with:

```
username: admiin
password: password
```

Then:

1. Go to DVWA Security
2. Set security level to **Low**
3. Save
4. Navigate to **SQL Injection** page

---

## Getting You Session Cookie

