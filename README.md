# 🖼️ Ubuntu Image Fetcher  

> **"I am because we are." – Ubuntu Philosophy**  
> This project embodies the spirit of community and sharing by respectfully fetching images from the internet and organizing them for later appreciation.  

---

## 🌍 About  
The **Ubuntu Image Fetcher** is a Python tool that:  
- Prompts the user for one or more image URLs  
- Creates a directory called `Fetched_Images` if it doesn’t exist  
- Downloads the images and saves them locally  
- Handles errors gracefully, ensuring respect for community resources  

This script demonstrates the Ubuntu principles of **community, respect, sharing, and practicality**.  

---

## ✨ Features  
- ✅ Fetch images from the web using the `requests` library  
- ✅ Handles multiple URLs at once (comma-separated input)  
- ✅ Skips non-image content types  
- ✅ Prevents downloads larger than 10MB  
- ✅ Skips duplicates (won’t overwrite existing files)  
- ✅ Saves images in a neatly organized folder (`Fetched_Images`)  

---

## 📦 Requirements  
- Python 3.7+  
- [`requests`](https://pypi.org/project/requests/) library  

Install dependencies:  
```bash
pip install requests
```
Usage

Clone the repository:

```bash
git clone https://github.com/Mechantchulo/Ubuntu_Requests

cd Ubuntu_Requests

```

Run the script:

```bash
python ubuntu_fetcher.py
```
Enter one or more image URLs when prompted (separate multiple with commas):

Please enter image URL(s) (separate multiple with commas): 
```bash
https://www.python.org/static/community_logos/python-logo.png, https://upload.wikimedia.org/wikipedia/commons/3/38/Ubuntu_logo1.png
```

Output example:

```bash
✓ Successfully fetched: python-logo.png
✓ Image saved to Fetched_Images/python-logo.png
✓ Successfully fetched: Ubuntu_logo1.png
✓ Image saved to Fetched_Images/Ubuntu_logo1.png

Connection strengthened. Community enriched.
```

⚠️ Precautions

When fetching from unknown sources, this program:

Ensures the file is actually an image (Content-Type check)

Prevents downloading overly large files (limit: 10 MB)

Skips duplicates to avoid overwriting existing images



🛠️ Future Improvements

Auto-rename duplicate filenames (e.g., image(1).jpg, image(2).jpg)

Support for downloading from text files containing lists of URLs

Optional caching with ETag / Last-Modified headers



💡 Ubuntu Principles in Action

Community: Connects to the wider web to gather resources

Respect: Handles errors gracefully without crashing

Sharing: Organizes images in a structured folder for later use

Practicality: Provides a real-world utility in a simple form



MIT License

Copyright (c) 2025 Erick Mutua

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

