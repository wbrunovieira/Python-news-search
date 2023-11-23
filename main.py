import requests
from bs4 import BeautifulSoup
import feedparser
from lxml import etree

def format_news(title, link, description):
    return f"Título: {title}\nLink: {link}\nDescrição: {description}\n"

def parse_html_with_lxml(url, content):
    soup = BeautifulSoup(content, 'lxml')

    found_news = False
    for news_item in soup.find_all(['h1', 'h2', 'h3']):
        link = news_item.find('a')
        if link and link.get('href'):
            title = news_item.get_text(strip=True)
            news_link = link.get('href')

            # Verifica se o link é relativo ou absoluto
            if not news_link.startswith('http'):
                news_link = url + news_link

            print(f"Título: {title}\nLink: {news_link}\n")
            found_news = True

    if not found_news:
        print(f"Nenhuma notícia encontrada em {url}")
def parse_rss_with_lxml(url):
    response = requests.get(url)
    tree = etree.fromstring(response.content)
    for item in tree.findall('channel/item'):
        title = item.find('title').text
        link = item.find('link').text
        description = item.find('description').text
        print(format_news(title, link, description))

def main():
    # Lista de URLs de páginas HTML
    html_urls = ["https://uol.com.br",
                 "https://terra.com.br/",
                 "https://www.bbc.com/portuguese",
                 "https://www.jn.pt/",
                 "https://sicnoticias.pt/",
                 "https://cnnportugal.iol.pt/",
                 "https://www.dn.pt/",
                 "https://www.sapo.pt/"
                ]
    
    # Loop para processar cada URL HTML
    for url in html_urls:
          try:
            response = requests.get(url, timeout=5)
            print(f"Notícias de {url}:\n")
            parse_html_with_lxml(url, response.content)
          except Exception as e:
            print(f"Erro ao processar {url}: {e}")
        

    # URL do feed RSS
    rss_url = "https://www.tabnews.com.br/recentes/rss"
    try:
        print(f"Notícias do RSS {rss_url}:\n")
        parse_rss_with_lxml(rss_url)
    except Exception as e:
        print(f"Erro ao processar RSS {rss_url}: {e}")

if __name__ == "__main__":
    main()
