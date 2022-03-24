import sys
sys.path.append("")
import requests
from bs4 import BeautifulSoup
from utils import Parser



def html2md(url, md_file, with_title=False):
    response = requests.get(url,headers = header)
    soup = BeautifulSoup(response.content, 'html.parser', from_encoding="utf-8")
    html = ""
    for child in soup.find_all('svg'):
        child.extract()
    if with_title:
        for c in soup.find_all('div', {'class': 'article-title-box'}):
            html += str(c)
    for c in soup.find_all('div', {'id': 'content_views'}):
        html += str(c)

    parser = Parser(html,markdown_dir)
    with open(md_file, 'w',encoding="utf-8") as f:
        f.write('{}\n'.format(''.join(parser.outputs)))
        
def download_csdn_single_page(article_url, md_dir, with_title=True, pdf_dir='pdf', to_pdf=False):
    response = requests.get(article_url,headers = header)
    soup = BeautifulSoup(response.content, 'html.parser', from_encoding="utf-8")
    title = soup.find_all('h1', {'class': 'title-article'})[0].string  ## 使用 html 的 title 作为 md 文件名
    title = title.replace('*', '').strip().split()
    md_file = md_dir+'/'+title[0] + '.md'
    print('Export Markdown File To {}'.format(md_file))
    html2md(article_url, md_file, with_title=with_title)

header = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,und;q=0.7",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
        }

article_url = 'https://blog.csdn.net/weixin_43979260/article/details/114012818' #csdn博客链接
markdown_dir = 'D:\\develop-source\\csdn_to_markdown\\temp' #保存文件夹
download_csdn_single_page(article_url,markdown_dir)
