Teste ThoughtWorks (Problema 2)
======================


Quickstart
---------------

Versão do python compatível:
```
python 2.7 ou python 3.4
```

Instação do python ::
```
Para executar o programa é necessário que seja feito a instalação do python em seu sistema operacional.
Caso o sistema seja linux ou macOs o python já vem instalado nativamente.
Instalação em windows abaixo:
```
 - http://docs.python-guide.org/en/latest/starting/install/win/


Use virtualenv ::
```
 É aconselhavél que se utilize virtual env, para montagem do ambiente de execução.
```
 - https://virtualenv.pypa.io/en/stable/

Instalação do requirements ::
```
Para instalação do pacote flake8 execute o seguinte comando:
pip install -r requirements.txt
```

Execução dos testes ::
```
Dentro do diretório tw_test execute:
python test.py
```

Executando o programa ::
```
Dentro do diretório tw_test execute:
python3.4 main.py
ou 
python2.7 main.py
```


Explicando o desenvolvido
----------------------------------

Arquivo main.py ::

```
Responsável por receber as entradas de dados e executar o start do processamento dos dados
```

Arquivo talk.py ::

```
Tem como principal função extrair da lista de palestras os minutos do seu título, utilizando regex.
Também responsável por printar a saída de dados após a execução.
```

Arquivo schedule.py ::

```
Responsável por executar o processamento da lista de palestras.
Tem como principal idéia quebrar a lista de palestras em pequenas listas com no máximo 420 minutos cada.
1 lista de 420 minutos pode também ser chamada de track.

Outro papel importante da classe é realocar as palestras do tipo lightning em alguma track que possuir o menor número de horas, ou seja, que está mais distante do total que é de 420 minutos.
```

Arquivo track.py ::

```
Monta e executa a divisão das palestras em manhã e tarde. A divisão é feita da seguinte maneira
manhã <= 180 minutos
tarde <= 240 minutos
Também tem como função inserir o horário de lanche e networking.
Nele também é aplicado o horário para as lightning.

```