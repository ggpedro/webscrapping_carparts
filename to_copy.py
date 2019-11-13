import os
import shutil

# Script que serve para copiar múltiplos arquivos para um diretório (pode ser separado com aspas simples: 'nome.jpg')

list_imgs=["AB_00548A.jpg","AB_00494A.jpg","AB_00478A.jpg","AB_00298A.jpg","AB_00467A.jpg","AB_00503A.jpg","AB_00534A.jpg","AB_00554A.jpg","AB_00070A.jpg",
"AB_00578A.jpg","AB_00104A.jpg","AB_00176A.jpg","AB_00183A.jpg","AB_00524A.jpg","AB_00081A.jpg","AB_00220A.jpg","AB_00339A.jpg","AB_00344A.jpg",
"AB_00364A.jpg","AB_00530A.jpg","AB_00581A.jpg","AB_00382A.jpg","AB_00374A.jpg","AB_00344A.jpg","AB_00243A.jpg","AB_00374A.jpg","AB_00220A.jpg",
"AB_00374A.jpg","AB_00200A.jpg","AB_00374A.jpg","AB_00104A.jpg","AB_00010A.jpg","AB_00592A.jpg","AB_00220A.jpg","AB_00010A.jpg","AB_00344A.jpg",
"AB_00075A.jpg","AB_00095A.jpg","AB_00081A.jpg","AB_00182A.jpg","AB_00292A.jpg","AB_00392A.jpg","AB_00024A.jpg","AB_00222A.jpg","AB_00199A.jpg",
"AB_00248A.jpg","AB_00248A.jpg","AB_00406A.jpg","AB_00182A.jpg","AB_00220A.jpg","AB_00183A.jpg","AB_00183A.jpg","AB_00222A.jpg","AB_00182A.jpg",
"AB_00372A.jpg","AB_00183A.jpg","AB_00220A.jpg","AB_00182A.jpg","AB_00220A.jpg","AB_00158A.jpg","AB_00183A.jpg","AB_00265A.jpg","AB_00182A.jpg",
"AB_00451A.jpg","AB_00220A.jpg","AB_00040A.jpg","AB_00264A.jpg","AB_00283A.jpg","AB_00344A.jpg","AB_00286A.jpg","AB_00130A.jpg","AB_00273A.jpg",
"AB_00087A.jpg","AB_00415A.jpg","AB_00354A.jpg","AB_00147A.jpg","AB_00130A.jpg","AB_00130A.jpg","AB_00116A.jpg","AB_00203A.jpg","AB_00451A.jpg",
"AB_00047A.jpg","AB_00163A.jpg","AB_00313A.jpg","AB_00042A.jpg","AB_00336A.jpg"]

for img in list_imgs:
    shutil.copy(img,"obsoletos_prontos")
