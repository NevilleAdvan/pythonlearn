爬取网络中的图片涉及到以下几个步骤：

1. **发送HTTP请求**：获取网页内容。
2. **解析HTML**：提取图片的URL。
3. **下载图片**：根据提取的URL下载图片并保存到本地。

我们可以使用Python的`requests`库来发送HTTP请求，使用`BeautifulSoup`库来解析HTML，使用`os`库来创建目录和保存图片。

以下是一个示例代码，展示了如何爬取网页中的图片并保存到本地：

### 示例代码

```python
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
    url = "https://example.com"  # 替换为你要爬取的网页URL
    main(url)
```

### 代码解释

1. **fetch_html(url)**：
   - 使用`requests.get`发送HTTP请求获取网页内容。
   - 使用`response.raise_for_status`检查请求是否成功。
   - 返回网页的HTML内容。

2. **parse_image_urls(html, base_url)**：
   - 使用`BeautifulSoup`解析HTML内容。
   - 查找所有`<img>`标签。
   - 提取`src`属性并使用`urljoin`将相对URL转换为绝对URL。
   - 返回图片URL列表。

3. **download_image(url, folder)**：
   - 使用`requests.get`发送HTTP请求下载图片。
   - 使用`response.iter_content`以流的方式下载图片，避免大文件占用过多内存。
   - 将图片保存到指定文件夹中。

4. **create_folder(folder)**：
   - 检查文件夹是否存在，如果不存在则创建文件夹。

5. **main(url, folder)**：
   - 创建保存图片的文件夹。
   - 获取网页HTML内容。
   - 解析图片URL。
   - 下载并保存图片。

### 注意事项

- 确保你遵守目标网站的`robots.txt`文件和使用条款。
- 避免频繁请求同一网站，以免被封禁IP。
- 对于大规模爬取，可以考虑使用多线程或异步IO来提高效率。

### 依赖安装

你需要安装`requests`和`BeautifulSoup`库，可以使用以下命令安装：

```sh
pip install requests beautifulsoup4
```

希望这个示例代码能帮助你爬取网络中的图片。如果你有任何问题或需要进一步的帮助，请随时提问！📸