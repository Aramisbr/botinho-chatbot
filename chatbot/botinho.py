from dotenv import load_dotenv
load_dotenv()
from datetime import datetime
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


llm = ChatOpenAI (model = "gpt-4-turbo")

# Instruções para o bot
def resposta_do_bot(historico_conversa, documento_atual):
  hoje = datetime.now().strftime('%d/%m/%Y')

  prompt_inicial = ChatPromptTemplate.from_template(
    """Você é o Botinho, um assistente direto, inteligente e com linguagem informal.
Hoje é {hoje}. Use as seguintes informações para responder: {documento}.

IMPORTANTE:
- Não fique repetindo coisas como “Como posso te ajudar?”, “Estou aqui para ajudar”, “Se precisar de algo, é só chamar”, ou similares.
- Fale como um amigo que conversa naturalmente, sem se comportar como um assistente formal.
- Se sua resposta for muito grande, formate-a em parágrafos para ficar mais organizada.
""")
  
  system_prompt = prompt_inicial.format(hoje = hoje, documento = documento_atual if documento_atual else 'Nenhum documento carregado, haja normalmente.')
  mensagens = [SystemMessage(content=system_prompt)]

  for autor, msg in historico_conversa:
    if autor == 'user':
      mensagens.append (HumanMessage(content=msg))
    elif autor == 'assistant':
      mensagens.append (AIMessage(content=msg))

  resposta = llm.invoke(mensagens)
  return resposta.content