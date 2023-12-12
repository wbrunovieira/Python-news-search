
from selenium import webdriver
from string import Template

# Configurar o WebDriver
driver = webdriver.Chrome('/caminho/para/chromedriver')  # Substitua pelo caminho correto do seu WebDriver

# Visitar o site
driver.get('https://www.sapo.pt/noticias/tecnologia')  # Substitua pela URL do site de notícias

# Extraia as informações necessárias
# Exemplo: titulo = driver.find_element_by_id('id_do_elemento').text

# Fechar o navegador
driver.quit()

# Crie seu template HTML
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
noticias_formatadas = "<p>Título da Notícia: " + titulo + "</p>"
template = Template(template_html)
html_final = template.substitute(noticias=noticias_formatadas)

# Salve o resultado em um arquivo HTML
with open('noticias.html', 'w') as file:
    file.write(html_final)
