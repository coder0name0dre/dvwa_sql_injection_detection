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

This script detects that behaviour by comparing responses.

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
username: admin
password: password
```

Then:

1. Go to DVWA Security
2. Set security level to **Low**
3. Save
4. Navigate to **SQL Injection** page

---

## Getting You Session Cookie

DVWA requires you to be logged in.

1. Log in to DVWA in your browser
2. Open browser Developer Tools
3. Go to **Application / Storage**, then to **Cookies**
4. Copy the value of `PHPSESSID`
5. Paste it into the script where indicated (`PASTE_YOURS_HERE`)

---

## Script Behaviour (What It Does)

The script performs three main steps:

1. Sends a normal request (expected behavious)
2. Sends a SQL injection request (`1 OR 1=1`)
3. Compares the size of the responses

If the injection response is much larger, it suggests that:

- More database records were returned
- The site is vulnerable to SQL injection

---

## Running The Script

Install dependencies:

```
pip install requests
```

Run the script:

```
python3 dvwa_sql_injection_detection.py
```

Example Output

```
Normal request length: 3200
Injection request length: 9400
Possible SQL injection detected!
```

---

## Ethical & Legal Notice

Do **not** run this script against:

- Real websites
- Systems you do not own
- Systems without explicit permission

This project focuses on understanding behaviour, not exploiting systems.

---

## License

This project is licensed under the [MIT License](https://github.com/coder0name0dre/dvwa_sql_injection_detection/blob/main/LICENSE).
