from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib, urllib.request, os, time, requests
import pandas as pd

# Abre o Cromedriver e o site
browser=webdriver.Chrome('/home/ggpedro/bl/chromedriver')
browser.get("https://loja.sonnervig.com.br/Index.aspx")

# Lista de Part Numbers
#f_pn = pd.read_csv('partnumbers.csv', encoding="UTF-8", sep=",", header=0)

partnumbers=['HS7Z17D957CBPTM','D2BZ17906BC','D2BZ16612B','G2BZ5427840A','AE8Z5840110A','G2BZ5824631A','DB392120125BC','C1BB13W030CH','DG9Z2C026C','DB392120124BC','BM51A40410AE','BM5113W029GF','BM5113W030GF','BE5Z16612A','AB3917C831DBW','BM51F17906AGXWA','D2BC18K001FD','D2BZ17757AB','AE8Z54211A10A','AE8Z54211A11A','EB3B13W030PM','F1EB8B041AB','JR3Z16612A','D2BZ17B968BA','D2BZ5440110A','AB3916610CB','DS7Z13008B','HS7Z17K835VEPTM','AB3917K824CC','AB3917K825CC','ES7Z17D957EPTM','2S65A24630AE','DS7Z13008A','CN15A03100DF','D3BBA20122AACTR','E4BZ10346E','2N15N40010AV','D3BT14B321CF','AB3912B565CA','AE8Z17D957AAPTM','HS7Z17D957BBPTM','BM5113404BL','9E5Z13008B','CE8Z16138C','9E5Z13008A','F1EB13W030CD','F1EB13405BE','XS6DK61635BAUY9','D2BZ13008M','D2BZ13008K','D2BZ13404B','E3B119D629BB','F1EB13W029CD','7S55B404K24AACTR','HS7Z8200AA','8M51F17906BCXWA','EB3B16E060AD','AB311125AC','9L558200C','DG9Z17906A','DS7Z8475A','EB3B17C831CC','BM5113405AK','BM5Z16006A','E3B513W030BM','8M5117757BDXWA','8N15N16612AA','DS7Z5424630A','F1EB13404BE','EB3B13W029NM','JA6B17757ACXWA','AE8Z7Z369F','BM51A17A894AB','C1B18C607AG','AE5Z8200C','AE8Z17K835AAPTM','BM5113405BL','HP5Z8A284B','7S5516612AACTR','98WT7K491BA','AE5Z17D957BAPTM','2S65A16015AH','AE5Z17K835AAPTM','J7BZ5827847B','BV619600CH','F1EB17B635AB','D3BBA20123AACTR','F1EB13W030TD','EB3B13W030NM','D2BZ8349B','BH2T16450BACRO','H1BG8005CC','2S653B438BA','HS7Z13404J','D2BZ5440320A','8M518B041CC']

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