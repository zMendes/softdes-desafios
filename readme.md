## Servidor DesSoft

Servidor que hospeda os desafios para os alunos da matéria de engenharia de Design de Software. Você pode criar desafios e os alunos conseguem mandar suas respostas via interface gráfica e obter feedback em tempo real. Além disso, é possível escolher um prazo para que o desafio seja cumprido pelos alunos. 


## Testes

#### Unitários
Para rodar,  execute:
`cd src && pytest softdes_test.py  `

#### Integração
Instale o driver do chrome de acordo com a versão do seu navegador: https://chromedriver.chromium.org/downloads  

Extraia o arquivo e coloque na pasta src. Em seguida, para rodar os testes execute:
`cd src && python3 integration_test.py`