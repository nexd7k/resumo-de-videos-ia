# resumo-de-videos-ia
Agente de IA que usa a API da OpenAI para resumir videos enviados do youtube

Por conta do agente usar o YoutubeTools, classe da biblioteca/framework Agno, ele aceita apenas vídeos que tenham alguma legenda ou transcrição e tem alguns problemas se não for em inglês.

O usuário precisará criar um arquivo chamado .env na mesma pasta que o código está localizado. Assim que o arquivo for criado, o usuário precisa digitar (ou colar) na primeira linha: OPENAI_API_KEY=

A sua chave API precisará ser colada após o "=" para o código funcionar.
