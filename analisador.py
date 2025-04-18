from pytubefix import YouTube
import openai
import ffmpeg
import os

def baixar_video():
    url = input('Digite o URL do vídeo: ')
    yt = YouTube(url)

    print(f"Título: {yt.title}")
    print("Iniciando download do áudio...")

    stream = yt.streams.filter(only_audio=True).first()
    caminho = stream.download(output_path="caminho do arquivo")
    print(f"Download concluído: {caminho}")

    return caminho

def converter_video():
    caminho_do_arquivo = baixar_video()
    nome_sem_extensao = os.path.splitext(caminho_do_arquivo)[0]
    caminho_saida = f"{nome_sem_extensao}.wav"

    print("Convertendo para .wav...")
    ffmpeg.input(caminho_do_arquivo).output(caminho_saida).run()
    print("Conversão concluída.")

    return caminho_saida

def transcrever_video():
    caminho_do_arquivo = converter_video()
    openai.api_key = "sua-chave-aqui"  

    with open(caminho_do_arquivo, "rb") as audio_file:
        response = openai.Audio.transcribe(
            model="whisper-1",
            file=audio_file,
            response_format="text"
        )

    print("📝 Transcrição realizada:")
    print(response)

   
    nome_sem_extensao = os.path.splitext(caminho_do_arquivo)[0]
    with open(f"{nome_sem_extensao}_transcricao.txt", "w", encoding="utf-8") as f:
        f.write(response)
    print(f"Transcrição salva em: {nome_sem_extensao}_transcricao.txt")


transcrever_video()

 
 
   



