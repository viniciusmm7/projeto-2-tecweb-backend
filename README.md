# Projeto 2 - Tecnologias Web - Backend - Insper - 2022.2
Feito por: Vinícius Matheus Morales

Professora: [Barbara Tieko Agena](http://lattes.cnpq.br/3888793516541327 "Lattes CV Barbara Tieko Agena")
___

## 1. Sobre o projeto
Esse projeto tem como objetivo criar uma página com frontend feito em React e backend feito com Django + uma API de escolha própria.

Nesse será utilizada a [RAWG API](https://rawg.io/apidocs), uma API para ter acesso a dados de jogos de videogame diversos.

## 2. Testando a API

### 2.1 Solicitando uma key da RAWG API
1. Acessar o link: [https://rawg.io/login?forward=developer].
2. Fazer login ou criar uma conta.
3. Ler os [Termos de Uso](https://api.rawg.io/docs/ "Termos de Uso RAWG API") - se resumem a não usar a API para fazer um clone, o uso ser gratuito até 100.000 usuários ativos por mês ou 500.000 visualizações de página por mês e atribuir um hyperlink para cada página onde os dados forem utilizados.
4. Preencher o formulário de forma adequada.
5. Copiar a key e salvar num arquivo Python chamado "api_keys.py" com o nome da variável "RAWG_API_KEY".

### 2.2 Solicitando uma key da RAPID API
1. Acessar o link: [https://rapidapi.com/accujazz/api/rawg-video-games-database].
2. Fazer login ou criar uma conta.
3. Ler os [Termos de Serviço](https://website.rapidapi.com/terms/ "Termos de Serviço RAPID API").
4. Copiar a "X-RapidAPI-Key" do teste de endpoint e salvar no mesmo arquivo Python "api_keys.py" com o nome da variável "RAPID_API_KEY".

### 2.3 Rodando o teste
O teste será feito solicitando informações de *Avaliações* do jogo *Grand Theft Auto V*.

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
2. Para de fato testar, rode o arquivo "exemplo.py".
3. Verifique que o output é semelhante ao exemplo comentado no código

## 3