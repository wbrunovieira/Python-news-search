
from selenium import webdriver
from string import Template

# Configurar o WebDriver
driver = webdriver.Chrome()

# Visitar o site
driver.get('https://www.sapo.pt/noticias/tecnologia') 


driver.quit()

#  template HTML
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
