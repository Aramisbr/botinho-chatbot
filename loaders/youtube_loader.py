import os
from faster_whisper import WhisperModel
from yt_dlp import YoutubeDL

modelo = WhisperModel('base', compute_type='int8')

def carrega_youtube(url):  # Baixa o vídeo do YouTube, transcreve e depois retorna.
    if not url:
        print ('ERRO: Nenhuma URL fornecida.')
        return None
    pasta_saida = 'audios'
    os.makedirs(pasta_saida, exist_ok=True)

    nome_arquivo = 'audio_youtube'
    caminho_saida = os.path.join(pasta_saida, nome_arquivo)
    caminho_final_wav = f'{caminho_saida}.wav'

    opcoes_ydl = {
        'format': 'bestaudio/best',
        'outtmpl': caminho_saida,
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }],
    }

    if os.path.exists(caminho_final_wav):
        try:
            os.remove(caminho_final_wav)
        except Exception as c:
            print('Não foi possível substituir o arquivo já existente.')

    try:
        with YoutubeDL(opcoes_ydl) as ydl:
            ydl.download([url])

        if not os.path.exists(caminho_final_wav):
            print(f'Erro, arquivo de áudio não encontrado.')
            return None
        
        print (f"Áudio baixado com sucesso, transcrevendo: '{caminho_final_wav}'...")
        segmentos, _ = modelo.transcribe(caminho_final_wav, beam_size=5)
        transcricao_completa = ''

        for segmento in segmentos:
            transcricao_completa += segmento.text + ' '

        if not transcricao_completa:
            print ('Não foi possível gerar transcrição para o vídeo.')
            return ''

        print(f"Transcrição gerada com sucesso para: {url}")
        return transcricao_completa

    except Exception as e:
            print (f'Erro ao processar: {e}')
            return None

    finally:
        if os.path.exists(caminho_final_wav):
            try:
                os.remove(caminho_final_wav)
            except Exception as e_rem:
                pass


    
