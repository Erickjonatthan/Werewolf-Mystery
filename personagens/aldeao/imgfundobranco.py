import os
from rembg import remove
from PIL import Image, ImageOps

caminho = "C:/Users/User/Documents/Estudo/Werewolf-Mystery/personagens/aldeao/output/SemFundo_jump_eixo_x"
formato = ".png"
frames = 110
saida = "SemFundo_jump_eixo_espelhado"

# Create the directory if it doesn't exist
if not os.path.exists(f"{caminho}/{saida}"):
    os.makedirs(f"{caminho}/{saida}")

# for i in range(frames):
#     id = i+1
#     caminhoimagem = f"{caminho}/{id:04d}{formato}"
#     imgemarq = Image.open(caminhoimagem)
#     imagesembg = remove(imgemarq)
#     print(f"Salvando {id:04d}{formato}")
#     imagesembg.save(f"{caminho}/{saida}/{id:04d}{formato}")

for i in range(frames):
    id = i+1
    caminhoimagem = f"{caminho}/{id:04d}{formato}"
    imgemarq = Image.open(caminhoimagem)
    imgemarq = ImageOps.mirror(imgemarq)  # Espelha a imagem
    imagesembg = remove(imgemarq)
    print(f"Salvando {id:04d}{formato}")
    imagesembg.save(f"{caminho}/{saida}/{id:04d}{formato}")