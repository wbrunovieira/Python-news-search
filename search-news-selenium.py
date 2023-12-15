from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from string import Template

# Configurar o WebDriver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.headless = True  # Executar em modo headless (sem abrir janela do navegador)
driver = webdriver.Chrome(service=service, options=options)

# Visitar o site
driver.get('https://www.sapo.pt/noticias/tecnologia') 

# Espera explícita
wait = WebDriverWait(driver, 20)

print("Buscando artigos na página...")
try:
    # Aguarda até que os artigos estejam visíveis na página e os armazena em uma lista
    articles = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'article')))
    print(f'Foram encontrados {len(articles)} artigos.')
except Exception as e:
    print("Erro ao esperar os artigos: ", e)
    driver.quit()
    exit()



noticias_formatadas = ""

print("Processando cada artigo encontrado...")

for article in articles:
    try:
        # Usando '.title > a > span' baseado na estrutura HTML fornecida
        titulo = article.find_element(By.CSS_SELECTOR, '.title > a > span').text
        link = article.find_element(By.CSS_SELECTOR, '.title > a').get_attribute('href')
        noticias_formatadas += f"<div><p>Título da Notícia: {titulo}</p><p>Link: <a href='{link}'>{link}</a></p></div>"
        print(f"Artigo processado: {titulo}")
    except Exception as e:
        print("Erro ao processar um artigo: ", e)

driver.quit()

# Template HTML
template_html = """
<html>
<head><title>Minhas Notícias</title></head>
<body>
    <h1>Notícias do Dia</h1>
    $noticias
</body>
</html>
"""

# Preencha o template com as informações coletadas
template = Template(template_html)
html_final = template.substitute(noticias=noticias_formatadas)

# Salve o resultado em um arquivo HTML
with open('noticias.html', 'w', encoding='utf-8') as file:
    file.write(html_final)