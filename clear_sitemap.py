import re

def clean_sitemap(filename):
  """Đọc file sitemap.txt và trích xuất các link"""
  with open(filename, 'r') as file:
    content = file.read()
  links = re.findall(r'https?://(?:www\.)?[\w-]+(?:\.[a-z]{2,})+(?:[\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', content)

  return links

def save_links_to_txt(links, filename):
  """Lưu danh sách các link vào file txt"""
  with open(filename, 'w') as file:
    for link in links:
      file.write(link + '\n')

# Đường dẫn đến file sitemap.txt
filename_sitemap = '/Python/python/Crawl_Glamira/sitemap.txt'

# Đường dẫn đến file txt để lưu kết quả
filename_output = '/Python/python/Crawl_Glamira/links.txt'
links = clean_sitemap(filename_sitemap)
save_links_to_txt(links, filename_output)
print(f"Đã lưu {len(links)} link vào file {filename_output}")