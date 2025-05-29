import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

ALVO_EXTENSOES = [".jpg_", ".jpeg_", ".png_", ".pdf_"]
PASTA = r"C:\users\fabricia.roque\Downloads" 

def gerar_nome_unico(caminho_base, ext):
    contador = 1
    novo_caminho = caminho_base + ext
    while os.path.exists(novo_caminho):
        novo_caminho = f"{caminho_base} ({contador}){ext}"
        contador += 1
    return novo_caminho

def renomear_arquivo(caminho_arquivo):
    raiz, ext = os.path.splitext(caminho_arquivo)
    if ext.lower() in ALVO_EXTENSOES:
        novo_ext = ext[:-1]  # remove o "_"
        caminho_base = raiz
        novo_caminho = gerar_nome_unico(caminho_base, novo_ext)

        try:
            os.rename(caminho_arquivo, novo_caminho)
            print(f"Renomeado: {caminho_arquivo} -> {novo_caminho}")
        except Exception as e:
            print(f"Erro ao renomear {caminho_arquivo}: {e}")

def renomear_existentes():
    for nome in os.listdir(PASTA):
        caminho = os.path.join(PASTA, nome)
        if os.path.isfile(caminho):
            renomear_arquivo(caminho)

class ManipuladorArquivos(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            time.sleep(0.5)
            renomear_arquivo(event.src_path)

    def on_moved(self, event):
        if not event.is_directory:
            renomear_arquivo(event.dest_path)

def iniciar_monitoramento():
    renomear_existentes() 
    observer = Observer()
    handler = ManipuladorArquivos()
    observer.schedule(handler, PASTA, recursive=False)
    observer.start()
    print("Monitoramento iniciado...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    iniciar_monitoramento()
    
    
