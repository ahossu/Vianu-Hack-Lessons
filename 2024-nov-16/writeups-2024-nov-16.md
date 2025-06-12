# Challenge Write-ups
> **Author:** Alexandru Hossu  
> **Role:** Cyber Club Co-Founder & Mentor  
> **Website:** [ahossu.ro](https://ahossu.ro)

## 📑 Table of Contents

> * Robots  
> * Summer Vibes
> * Beautiful Places 
> * QR Fun

---

## Robots

**Challenge URL:**  
🔗 https://vianuhack.club/challenges#Robots-1

### 🛠 Tools & What They Do

- **`curl`**  
  A command-line tool for transferring data with URLs.

### 🧩 Solution Hints

1. **Fetch the `robots.txt` file**  
   ```bash
   curl -s https://vianuhack.club/robots.txt
    ```
2. **Access hidden directories**
> **Key Takeaway**
> * The robots.txt file often reveals endpoints the maintainers don’t want indexed—but aren’t hiding from you.

---

## Summer Vibes

**Challenge URL:**  
🔗 https://vianuhack.club/challenges#Summer%20Vibes-2

### 🛠 Tools & What They Do

- **`file`**  
  Examines a file’s header and content to identify its type (text, executable, archive, etc.).

- **`strings`**  
  Extracts sequences of printable characters from binary files—useful for spotting hidden messages.

- **`grep`**  
  Filters input by a regular expression.

### 🧩 Solution Hints

1. **Identify the file type**  
   ```bash
   file chall
    ```
2. **Extract printable strings**  
   ```bash
   strings chall
    ```
3. **Extract printable strings**  
   ```bash
   strings chall | grep "CTF"
    ```
> **Tool Insight**
> * file tells you how to approach a file (text vs. binary).
> * strings pulls out all text-like fragments from binaries.
> * grep hones in on the exact pattern you need.

---

## Beautiful Places

**Challenge URL:**  
🔗 https://vianuhack.club/challenges#Beautiful%20Places-3

### 🛠 Tools & What They Do

- **`exiftool`**  
  Reads and writes metadata (EXIF, IPTC, XMP, etc.) embedded in image, audio, and document files. Metadata can include camera model, GPS coordinates, user comments, and more.

### 🧩 Solution Hints

1. **Extract all metadata**  
   ```bash
   exiftool chall.jpg
    ```
> **Tool Insight**
> * Metadata isn’t just “boring camera info”—it can hide secret data.

---

## QR Fun

**Challenge URL:**  
🔗 https://vianuhack.club/challenges#QR%20Fun-4

### 🛠 Tools & What They Do

- **`zbarimg`**  
  Scans image files for barcodes and QR codes, outputting the embedded data.
- **`base64 -d`**  
  Decodes Base64-encoded text back into its original binary or ASCII form.

### 🧩 Solution Hints

1. **Scan the QR code**  
   ```bash
   zbarimg qr.png --quiet --raw > qr.txt
    ```
2. **Decode Base64**  
   ```bash
   cat qr.txt | base64 -d > decoded.txt
    ```
3. **Apply ROT13**
   ```bash
   cat decoded.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
    ```
> **Process Insight**
> * Layered encodings are common—tackle one layer (QR) at a time, then the next (Base64), and finally simple ciphers (ROT).
