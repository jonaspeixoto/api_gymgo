# GymGo - API de Academia


## Preparação do Ambiente

### 1. Instalação do Python

Certifique-se de ter o Python instalado em sua máquina. Você pode baixar a versão mais recente do Python em [python.org](https://www.python.org/).

### 2. Configuração de um Ambiente Virtual

Recomendamos o uso de ambientes virtuais para isolar as dependências do projeto. Abra o terminal na raiz do projeto e execute os seguintes comandos:


# Instale a ferramenta virtualenv (caso ainda não tenha)
```
pip install virtualenv

```

# Crie um ambiente virtual
```
python -m venv venv

```

# Ative o ambiente virtual (comando pode variar dependendo do sistema operacional):
# No Windows
```
venv\Scripts\activate
```
# No Linux/Mac
```
source venv/bin/activate
```

# 3. Instalação de Dependências
Com o ambiente virtual ativado, instale as dependências do projeto a partir do arquivo requirements.txt:
```
pip install -r requirements.txt
```

# 4 Executando o Projeto
Após a preparação do ambiente, você pode iniciar o servidor da API. Certifique-se de estar com o ambiente virtual ativado e execute:
```
python manage.py runsever
```
