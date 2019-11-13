from bs4 import BeautifulSoup
import requests

site = requests.get('https://loja.sonnervig.com.br/Produto.aspx?CP=66330').text
soup = BeautifulSoup(site,'lxml')

images=['img_Foto', 'rptMedia_imgProduto_0','rptMedia_imgProduto_1','rptMedia_imgProduto_2','rptMedia_imgProduto_3',
    'rptMedia_imgProduto_4','rptMedia_imgProduto_5']

for image in images:
    try:
        image_src = soup.find('img',id=image).get('src')
        print(image_src)
    except Exception:
        pass