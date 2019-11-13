import os, shutil
from PIL import Image

os.chdir('/home/ggpedro/brasal/fotos')

for img in os.listdir():
    im=Image.open(img)
    width, height=im.size
    print(f'{img}|{width}|{height}')
    
    # copia arquivos de tamanho OK para uma pasta
    '''
    if width>=500 and height >=500:
        shutil.copy(img, 'fotos_ok')
    else:
        pass
    '''