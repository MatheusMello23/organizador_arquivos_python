import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)

#Adicionar as extensões que deseja organiza-los em cada pasta 
locais = {
    "imagens": [".png", ".jpg", "jpeg"],
    "planilhas": [".xlsx"],
    "pdfs": [".pdf"],
    "csv": [".csv"],
    "Arquivos compactados":[".zip", ".7z", ".rar"],
    "Documentos":[".doc"],
    "Bloco de notas":[".txt"],
    "Pastas":[".Pasta de arquivos"],
}

for arquivo in lista_arquivos:
    # 01. ARquivo.pdf
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")