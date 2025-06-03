import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, render_template, request, redirect, url_for, flash
from chatbot.botinho import resposta_do_bot
from loaders.pdf_loader import carrega_pdf
from loaders.site_loader import carrega_site
from loaders.youtube_loader import carrega_youtube

app = Flask(__name__)
app.secret_key = 'botinho_secret_keey'

mensagens = []
documento = 'documento pendente'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pergunta = request.form.get('pergunta')
        if pergunta:     #  Verifica se pergunta não está vazia
            mensagens.append(('user', pergunta))
            resposta = resposta_do_bot(mensagens, documento)
            mensagens.append(('assistant', resposta))
    return render_template('index.html', historico=mensagens)


@app.route('/carregar_documento', methods=['POST'])
def carregar_doc():
    global documento

    source_type = request.form.get('source_type')  #Armazena o tipo de documento que o user vai enviar
    document_url = request.form.get('document_url')
    
    print(f"--- Debug: Início de carregar_doc ---")
    print(f"request.form: {request.form}")
    print(f"request.files: {request.files}")

    pdf_file = request.files.get('pdf_file')

    print(f"Objeto pdf_file recuperado de request.files.get('pdf_file'): {pdf_file}")
    if pdf_file:
        print(f"Nome do arquivo em pdf_file.filename: '{pdf_file.filename}'")
        print(f"pdf_file.filename é uma string não vazia? {bool(pdf_file.filename and pdf_file.filename != '')}")
    else:
        print(f"pdf_file é None ou Falsy.")
    print(f"------------------------------------")

    
    print('Iniciando carregamento de documento')
    print(f'Tipo de fonte recebido: {source_type}')

    if source_type == 'pdf':
        if pdf_file and pdf_file.filename:
            filename = pdf_file.filename
            conteudo_pdf = carrega_pdf(pdf_file)

            if conteudo_pdf is not None:
                if conteudo_pdf == '':
                    print ('PDF processado mas não contém texto.')
                    documento = f"O PDF '{filename}' foi processado com sucesso, mas não foi encontrado texto extraível nele."
                    flash('O PDF foi lido mas não foi extraída informação.', 'warning')
                else:
                    print (f'PDF: {filename} extraído e enviado')
                    documento = conteudo_pdf
                    flash('PDF lido com sucesso!', 'success')
            else:
                documento = 'Falha ao processar o pdf, verifique o arquivo e os logs do servidor.'
                print ('Falha ao carregar pdf.')
                flash('Falha ao carregar PDF.', 'error')
        else:
            print ('ERRO: PDF selecionado, mas nenhum arquivo enviado.')
            flash('Nenhum arquivo enviado.', 'error')
            if not pdf_file:
                print("Causa: pdf_file é None (request.files.get('pdf_file') não encontrou o arquivo ou o campo).")
            elif not pdf_file.filename: # Catches empty string or None for filename
                print(f"Causa: pdf_file.filename está vazio ou é None. Objeto pdf_file '{pdf_file}'")
            documento = f'Nenhum arquivo foi enviado.'

    elif source_type == 'site':
        if document_url:
            print (f'URL do site recebida: {document_url}')
            conteudo_site = carrega_site(document_url)
            if conteudo_site is not None:
                if conteudo_site == '':
                    print ('Conteúdo acessado, mas página vazia.')
                    documento = f"O site '{document_url}' foi acessado, mas não foi encontrado conteúdo de texto extraível."
                    flash('O link foi lido mas não foi extraída informação.', 'warning')
                else:
                    documento = conteudo_site
                    print ('Conteúdo carregado.')
                    flash('Conteúdo carregado!', 'success')
            else:
                print ('Falha ao carregar conteúdo do site.')
                documento = 'Falha ao carregar conteúdo do site'
                flash('Falha ao carregar conteúdo do site.', 'error')
        else:
            print ('ERRO: Tipo Site selcionado, mas nenhuma URL fornecida.')
            documento = f"Nenhum arquivo enviado."
            flash('Nenhum arquivo enviado.', 'error')

    elif source_type == 'youtube':
        if document_url:
            print (f'URL do YouTube recebida: {document_url}')
            transcricao_video = carrega_youtube(document_url)
            if transcricao_video is not None:
                if transcricao_video == '':
                    print ('Vídeo processado, mas sem transcrição.')
                    documento = f"O vídeo do YouTube '{document_url}' foi processado, mas não foi gerada uma transcrição (pode ser apenas música ou silêncio)."
                    flash('Vídeo enviado, mas não foi gerada transcrição.', 'warning')
                else:
                    print ('Transcrição do vídeo concluída.')
                    documento = transcricao_video
                    flash('Vídeo recebido!', 'success')
            else:
                print ('Falha ao processar o vídeo.')
                documento = 'Falha ao processar o vídeo'
                flash('Falha ao processar o vídeo.', 'error')      
        else:
            print ('Tipo YouTube selecionado, mas nenhuma URL enviado.')
            documento = 'ERRO: Nenhum arquivo enviado.'
            flash('Nenhum arquivo enviado.', 'error')
    else:
        print (f'ERRO: Tipo de fonte inválido ou não selecionado: {source_type}.')
        documento = 'ERRO: Documento ou link inválido ou não selecionado.'
        flash('Tipo de fonte não selecionado!', 'error')

    print (f'Váriavel documento atualizada para: {documento}')

    return redirect (url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)