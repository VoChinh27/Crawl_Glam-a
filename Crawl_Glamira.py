import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import zipfile
from google.colab import files

links_file_path = "/python/Crawl_Glamira/links.txt"
image_dir = "images"

# Tạo thư mục images nếu chưa tồn tại
os.makedirs(image_dir, exist_ok=True)

with open(links_file_path, "r") as f:
    links = f.readlines()
for link in links:
    link = link.strip()
    print(f"Đang xử lý link: {link}")

    try:
        response = requests.get(link)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"  Lỗi tải trang: {e}")
        continue
    soup = BeautifulSoup(response.content, "html.parser")
    images = soup.find_all("img")
    for image in images:
        image_url = image.get("src")
        if not image_url:
            continue
        image_url = urljoin(link, image_url)
        try:
            image_data = requests.get(image_url).content
            image_name = image_url.split("/")[-1]
            image_path = os.path.join(image_dir, image_name)
            with open(image_path, "wb") as f:
                f.write(image_data)

            print(f"  Đã tải ảnh: {image_name}")

        except Exception as e:
            print(f"  Lỗi tải ảnh: {e}")
zip_path = "images.zip"
with zipfile.ZipFile(zip_path, 'w') as zipf:
    for root, _, files in os.walk(image_dir):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), image_dir))
files.download(zip_path)
