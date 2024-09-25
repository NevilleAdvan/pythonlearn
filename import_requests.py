import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()  # 如果请求失败，抛出异常
    return response.text

def parse_image_urls(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    img_tags = soup.find_all('img')
    img_urls = [urljoin(base_url, img['src']) for img in img_tags if 'src' in img.attrs]
    return img_urls

def download_image(url, folder):
    response = requests.get(url, stream=True)
    response.raise_for_status()  # 如果请求失败，抛出异常
    filename = os.path.join(folder, url.split('/')[-1])
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)

def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def main(url, folder='images'):
    create_folder(folder)
    html = fetch_html(url)
    img_urls = parse_image_urls(html, url)
    for img_url in img_urls:
        try:
            download_image(img_url, folder)
            print(f"Downloaded {img_url}")
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")

if __name__ == "__main__":
    url = "http://rxjh.cdcgames.net/"  # 替换为你要爬取的网页URL
    main(url)