# Projeto 2 - Tecnologias Web - Backend - Insper - 2022.2
Feito por: Vinícius Matheus Morales

Professora: [Barbara Tieko Agena](http://lattes.cnpq.br/3888793516541327 "Lattes CV Barbara Tieko Agena")
___

## 1. Sobre o projeto
Esse projeto tem como objetivo criar uma página com frontend feito em React e backend feito com Django + uma API de escolha própria.

Nesse será utilizada a [RAWG API](https://rawg.io/apidocs), uma API para ter acesso a dados de jogos de videogame diversos.

O nome do projeto será *Expand*.

## 2. Rodando o backend

1. Baixe esse repositório, crie e inicie um ambiente virtual e então instale as dependências:

#### Linux/Mac OS
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

#### Windows cmd
```bash
python -m venv env
env\Scripts\activate.bat
pip install -r requirements.txt
```

#### Windows Power Shell
```bash
python -m venv env
env\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Crie o banco de dados com o seguinte comando:
```bash
python manage.py migrate
```

3. Rode com:
```bash
python manage.py runserver
```
___

Pronto, basta rodar o backend e depois o frontend para ver a aplicação em total funcionamento!