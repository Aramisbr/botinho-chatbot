import os
from langchain_community.document_loaders import PyPDFLoader

TEMP_PDF = 'temp_pdf_upload'
os.makedirs(TEMP_PDF, exist_ok=True)

def carrega_pdf(arquivo_pdf):
  if not arquivo_pdf or not arquivo_pdf.filename:
    print ('ERRO: Nenhum arquivo fornecido ou nome inválido.')
    return None
  
  temp_filename = f'temp_{arquivo_pdf.filename}'
  temp_file_path = os.path.join(TEMP_PDF, temp_filename)

  texto = ''

  try:
    arquivo_pdf.save(temp_file_path)
    loader = PyPDFLoader(temp_file_path)
    pages = loader.load()

    if not pages:
      print ('Arquivo PDF em branco.')
      return ''
    
    for page in pages:
      texto += page.page_content + '\n'

    texto = texto.strip()

    if not texto:
      print('Nenhum texto extraído.')
      return ''
    
    print ('Print extraído com sucesso.')
    return texto
  
  except Exception as e:
    print (f'Erro ao processar o arquivo PDF: {e}')
    return None
  
  finally:
    if os.path.exists(temp_file_path):
      try:
        os.remove(temp_file_path)
      except Exception as ex:
        print (f'Falha ao remover arquivo temporário: {ex}.')

