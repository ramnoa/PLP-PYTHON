import requests
import os
import time
import hashlib
from urllib.parse import urlparse

# Directory for saving images
SAVE_DIR = "Fetched_Images"

# Maximum file size (10MB precaution)
MAX_FILE_SIZE = 10 * 1024 * 1024  

# Store hashes of downloaded files to prevent duplicates
downloaded_hashes = set()

def get_file_hash(content):
    """Generate a SHA256 hash for the file content."""
    return hashlib.sha256(content).hexdigest()

def fetch_image(url):
    try:
        os.makedirs(SAVE_DIR, exist_ok=True)

        # Fetch with timeout
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # ---- Precautions ----
        # 1. Ensure content type is image
        content_type = response.headers.get("Content-Type", "")
        if "image" not in content_type.lower():
            print(f"✗ Skipping {url} (Not an image: {content_type})")
            return

        # 2. Ensure file size reasonable
        content_length = response.headers.get("Content-Length")
        if content_length and int(content_length) > MAX_FILE_SIZE:
            print(f"✗ Skipping {url} (File too large: {int(content_length)/1024/1024:.2f} MB)")
            return

        # 3. Prevent duplicates using hash
        file_hash = get_file_hash(response.content)
        if file_hash in downloaded_hashes:
            print(f"✗ Skipping {url} (Duplicate image detected)")
            return
        downloaded_hashes.add(file_hash)

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path) or f"downloaded_{int(time.time())}.jpg"
        filepath = os.path.join(SAVE_DIR, filename)

        # Avoid overwriting existing files
        base, ext = os.path.splitext(filename)
        counter = 1
        while os.path.exists(filepath):
            filename = f"{base}_{counter}{ext}"
            filepath = os.path.join(SAVE_DIR, filename)
            counter += 1

        # Save file
        with open(filepath, "wb") as f:
            f.write(response.content)

        size_kb = len(response.content) / 1024
        print(f"✓ Saved {filename} ({size_kb:.2f} KB) from {url}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Network error while fetching {url}: {e}")
    except Exception as e:
        print(f"✗ Unexpected error with {url}: {e}")

def main():
    print("🌍 Ubuntu Image Fetcher")
    print("A mindful tool for collecting images respectfully.\n")
    print("Remember: 'A person is a person through other persons.'\n")

    while True:
        urls = input("Enter image URLs separated by spaces (or 'q' to quit): ")
        if urls.lower() == "q":
            print("\nGoodbye! Connection strengthened. Community enriched.")
            break

        for url in urls.split():
            fetch_image(url)

if __name__ == "__main__":
    main()
