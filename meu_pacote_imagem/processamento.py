from PIL import Image

def redimensionar_imagem(caminho_imagem, largura, altura):
    imagem = Image.open(caminho_imagem)
    imagem_redimensionada = imagem.resize((largura, altura))
    return imagem_redimensionada

def converter_para_cinza(caminho_imagem):
    imagem = Image.open(caminho_imagem)
    imagem_cinza = imagem.convert('L')
    return imagem_cinza