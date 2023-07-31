# Previsão de vendas das lojas Rossmann

## Contexto

A Rossmann é uma rede de farmácias presente em vários países da Europa. Durante uma reunião com os gerentes, o CFO pediu uma previsão de vendas para as seis semanas seguintas de cada uma das lojas.

### Problema de negócio:
- A rede Rossmann pretende fazer reformas em todas as suas lojas e, para isto, precisa determinar qual será o orçamento disponível em função da previsão de vendas dos próximos seis meses.

### Dificuldade:
- As predições atuais apresentam muita divergência pois se baseiam no conhecimento empírico dos gerentes. O método é pouco técnico.
- Todas as previsões são feitas manualmente, ou seja, não utilizam ferramentas padronizadas para facilitar uma entrega síncrona de resultados.
- A visualização dos resultados não fica centralizada, dificultando a tomada de decisões por parte do CFO.

### Solução:
- Implementar um modelo de Machine Learning para realizar a previsão de vendas de uma forma mais técnica/científica.
- Disponibilizar um sistema capaz de fornecer a previsão de vendas de qualquer loja através de um smartphone.


## Premissas

1. Dados públicos foram utilizados para o estudo. Disponíveis em https://www.kaggle.com/competitions/rossmann-store-sales/data


## Estratégia de solução

1. Coleta dos dados
2. Descrição dos dados em termos de volume e tipo
3. Tratamento dos dados faltantes
4. Formulação das hipóteses que descrevem o fenômeno
5. Criação/derivação de novas características (features) independentes que podem descrever o fenômeno
6. Definição de quais características são as mais relevantes e quais podem ser desconsideradas
7. Comparação entre alguns algorítmos de Machine Learning
8. Ajustar os hiperparâmetros


## Resultado

- Utilizando o algorítmo XGBoost houve um ganho, aproximado, de 40% em performance quando comparado com um modelo de regressão linear.
- Desenvolvimento um bot no Telegram que envia uma requisição ao modelo hospedado em uma cloud e retorna a previsão de vendas de qualquer loja cadastrada para os próximos seis meses. Acesse https://youtube.com/shorts/2abtTxgfy5I para um exemplo de uso.
