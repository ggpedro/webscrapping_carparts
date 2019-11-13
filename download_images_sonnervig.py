from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib, urllib.request, os, time, requests

# Abre o Cromedriver e o site
browser=webdriver.Chrome('/home/ggpedro/brasal/chromedriver')
browser.get("https://loja.sonnervig.com.br/Index.aspx")

# Lista de Part Numbers
partnumbers=['DG9Z2C026C','EB3B13W030PM','EB3B13W030NM','D2BZ13404B','HS7Z13404J','9E5Z13404A','BM5113405AK','D2BZ13405B','BM5113405BL','BS6513006AG','AB3913405FA','BV619600CH','8M5113101AE','F1EB13405CF','F1EB13404CF','2S6513005BF','2S6513006BE','BM5113404AK','AB3913W030UD','AB3913404FA','91AG13405FD','F1EB13404AD','GN1517682AGA','GN1513B221BD','F1EB13A603AB','AB3916700AG','BM5113A602AD','BM5113A603AD','D2BZ9600A','AB3917683BFAB3913W029TC','C1BZ1007A','AB3913W029VA','F1EZ17682X','CN1Z9424A','E3B17B633AE','AE8Z2001C','AN1513005AA','DG9Z2200N','EB3Z17682ABB','F1EZ15200A','BE8Z5442701A','5M5113A603AA','8N1513005AC','BE8Z5442700A8N1513006AC','5M5113A602AA','E3B513404AJ','EB3Z17683AAY','6G9Z8K556A','GN1513B220AB','E3B513405AJ','8A6117B613AG','7S5513005AH','6E5Z17618A','6E5Z17682B','CN159E857CA','E3B517683AH5JA','8N1515K202AB','8N1515K201ABAB398K218AA','DCP12C299B1B','BE8Z2B121AA','CN1515K273AD','D3BB13405AC','E3BG6600DC','CN15A219A64CE','97KB8K218AG','CN1515500AD','7S5513404AC','CS5513405AA','7L5517C617DA','E4B513A602AG','CN159E857AA','7S5513405ACBE5Z8A080B','CS5513404AA','AB312L361AB','6S6513A602AD','EB3G8K218AC','6S659600AF','J7BZ13405H','J7BZ13404J','J7BZ13405F','J7BZ13405G','D3BB17E714BB','5L5515K201AD','8N1513A602AB','8A399D653AA','CN1515501ADCA6917085AC','D3BBA045H22AA','D2BZ15266DB','CS5513005AC','98FU17C773AHYYD','D3B19E857BA','2N1115201AB','7S453R700AA','BM557A564AB','C1BT13802BB','E3B17A543AA','7S5517682CF','F1EB17683GB','AB3915201AA','J7BZ17080CCN157A543BB','6C357B118AB','8S658K218BA','J7BZ17618D','E3B517618AA','E3BZ18124B','BE8Z8A080A','E3B16P082AD','E3B517K740AB','E3BZ9600G','J7BZ13832C','8M5Z7220C','E3B517K741AB','MB2A1125BA','E3B5A01820AB3JA96FB8K218AG','2S6517683LF','7S5517683AD','CN15A27936AA','MB0A2K021FA','MB2A1125AA','MB8A1125AA','CN1Z13404K','MB8A1125BA','E3B119D710AC','AV1Z18476D']

# Pesquisa de cada Part Number
for pn in partnumbers:
    i=0 #Para incremental de salvar imagem
    temp = browser.find_element_by_id('txtDescricao')
    temp.clear()
    temp.send_keys(pn)
    confirm=browser.find_element_by_id('btnBuscar')
    confirm.click()
    current_page=browser.current_url
    time.sleep(3)

    # Importar o texto do site
    site = requests.get(current_page).text
    soup = BeautifulSoup(site, 'lxml')

    # Lista de IDs das imagens
    images=['img_Foto', 'rptMedia_imgProduto_0','rptMedia_imgProduto_1','rptMedia_imgProduto_2','rptMedia_imgProduto_3',
    'rptMedia_imgProduto_4','rptMedia_imgProduto_5']

    for image in images:
        time.sleep(1)
        try:
            i = i+1
            image_src = soup.find('img',id=image).get('src')
            print(image_src)
            # serao obtidos os links no console, deverão ser removidas duplicatas e baixadas com wget na pasta de destino

        except Exception:
            pass