from selenium import webdriver
import requests

browser=webdriver.Chrome('/home/ggpedro/bl/chromedriver')
browser.get("http://www.mercadolivre.com.br") 

# para todas as paginas
numpags=['1','2','3','4','5','6','7','8','9','10','11','12']
for numpag in range(1,13):
    # acessa cada pagina
    browser.get(f'https://www.mercadolivre.com.br/anuncios/lista/?page={numpag}')
    
    # e coleta as informacoes de cada produto
    for numproduto in range(1,51):
        id_produto=browser.find_element_by_xpath(f'//div[1]/div[3]/div[2]/div[{numproduto}]/div/div[3]/div/p[1]')
        print(id_produto.text)
        //*[@id="app-root-wrapper"]/div/div/div[1]/div[3]/div[2]/div[22]/div/div[2]/div/p[1]