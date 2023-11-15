import requests
from bs4 import BeautifulSoup
import feedparser
from lxml import etree

def parse_html_with_lxml(content):
    # Usando lxml como parser do BeautifulSoup para HTML
    soup = BeautifulSoup(content, 'lxml')
    # Adicione o código para extrair as informações do 'soup'
    # ...

def parse_rss_with_lxml(url):
    response = requests.get(url)
    tree = etree.fromstring(response.content)
    # Adicione o código para extrair as informações do feed RSS
    # Exemplo: iterar pelos elementos do feed
    for item in tree.findall('channel/item'):
        title = item.find('title').text
        link = item.find('link').text
        description = item.find('description').text
        print(title, link, description)

def main():
    # Lista de URLs de páginas HTML
    html_urls = ["https://uol.com.br",
                 "https://terra.com.br/"
                ]
    
    # Loop para processar cada URL HTML
    for url in html_urls:
        response = requests.get(url)
        parse_html_with_lxml(response.content)

    # URL do feed RSS
    rss_url = "https://www.tabnews.com.br/recentes/rss"
    parse_rss_with_lxml(rss_url)

if __name__ == "__main__":
    main()
