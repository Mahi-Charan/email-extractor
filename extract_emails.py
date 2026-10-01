import re
import sys

INPUT_FILE = "source.txt"

EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,24}")

# JS/HTML source often contains retina-asset names like "logo@2x.png" or
# "icon@3x.svg" that match the email pattern - these aren't real emails.
NON_EMAIL_EXTENSIONS = {
    "png", "jpg", "jpeg", "gif", "svg", "webp", "ico", "bmp",
    "css", "js", "map", "json", "html", "htm", "xml", "txt",
    "pdf", "woff", "woff2", "ttf", "eot", "otf",
    "mp4", "mp3", "zip", "gz",
}


def extract_emails(text):
    found = {}
    for match in EMAIL_PATTERN.findall(text):
        tld = match.rsplit(".", 1)[-1].lower()
        if tld in NON_EMAIL_EXTENSIONS:
            continue
        key = match.lower()
        if key not in found:
            found[key] = match
    return sorted(found.values(), key=str.lower)


def main():
    try:
        with open(INPUT_FILE, encoding="utf-8", errors="ignore") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: '{INPUT_FILE}' not found. Paste your JS/HTML content into that file first.")
        sys.exit(1)

    emails = extract_emails(text)

    if not emails:
        print("No email addresses found.")
        return

    print(f"Found {len(emails)} email address(es):\n")
    for email in emails:
        print(email)


if __name__ == "__main__":
    main()
