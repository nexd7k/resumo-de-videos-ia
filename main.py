from agno.agent import Agent
from agno.tools.youtube import YouTubeTools
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

#Carregar a chave API do arquivo .env
load_dotenv()

#Enviar a URL do vídeo que precisa do resumo
url = input("Cole aqui a URL do vídeo que precisa do resumo: ")

#Criando o agente de IA 
agent = Agent(
    name = "YoutubeTranscriber",
    role = "Resumir videos do youtube",
    #Passando as instruções sobre o que o agente precisará fazer
    instructions =[
        "Receba a URL do vídeo",
        "Identifique os pontos principais, timestamps e os momentos em que os usuários mais assistiram",
        "Não invente informações. Apenas faça um resumo pegando os pontos principais do vídeo enviado como base"
    ],
    #O agente irá usar o modelo gpt 4o mini, um modelo basico porém funcional e barato
    model = OpenAIChat(id="gpt-4o-mini"),
    tools = [YouTubeTools()]
)

#O resumo do vídeo irá ser feito a partir daqui
agent.print_response(f"Resumindo o vídeo {url}", markdown=True)