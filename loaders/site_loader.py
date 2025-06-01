from langchain_community.document_loaders import WebBaseLoader

def carrega_site(url):
  if not url:
    print ('ERRO: Nenhuma URL encontrada.')
    return None
  
  try:
    print(f'Carregando conteúdo do site: {url}')
    loader = WebBaseLoader(url)
    lista_documentos = loader.load()

    documento_completo = ''
    for doc in lista_documentos:
      documento_completo += doc.page_content + '\n'

    if not documento_completo.strip():
      print ('Nenhum conteúdo extraído da página.')
      return ''
    
    print('Conteúdo do site carregado com sucesso.')
    return documento_completo.strip()
  
  except Exception as e:
    print (f'Erro ao tentar carregar o site: {e}.')
    return None