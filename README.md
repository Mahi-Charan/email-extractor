# Email Extractor

Pull email addresses out of a web page's source (HTML / JSP / JS).

## Use it online (no install)

Open the GitHub Pages link for this repo, paste the page source, and click **Extract emails**.
Everything runs in your browser — the pasted text is never uploaded anywhere.

To get a page's source: right-click the page → **View Page Source** → `Ctrl+A`, `Ctrl+C`.

## Use it locally (Python)

1. Paste the page source into `source.txt` next to the script.
2. Run:

   ```
   python extract_emails.py
   ```

Image/asset names like `logo@2x.png` are ignored, and duplicates are removed.
