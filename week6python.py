import requests
import os
from urllib.parse import urlparse

def fetch_images(urls):
    os.makedirs("Fetched_Images", exist_ok=True)

    for url in urls:
        try:
            response = requests.get(url, timeout=10, stream=True)
            response.raise_for_status()
            
            # Check content type
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print(f"✗ Skipping {url} (not an image).")
                continue
            
            # Limit size to 10MB
            content_length = int(response.headers.get("Content-Length", 0))
            if content_length > 10_000_000:  # 10 MB
                print(f"✗ Skipping {url} (file too large).")
                continue

            # Extract filename
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"
            filepath = os.path.join("Fetched_Images", filename)

            # Prevent duplicates
            if os.path.exists(filepath):
                print(f"⚠ Skipped {filename} (already exists).")
                continue

            # Save image in chunks (efficient for large files)
            with open(filepath, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")
        
        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for {url}: {e}")
        except Exception as e:
            print(f"✗ Error processing {url}: {e}")

    print("\nConnection strengthened. Community enriched.")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    urls = input("Please enter image URL(s) (separate multiple with commas): ").split(",")
    urls = [u.strip() for u in urls if u.strip()]
    
    fetch_images(urls)

if __name__ == "__main__":
    main()
