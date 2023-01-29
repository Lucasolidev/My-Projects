import sys
import site

# Confefir a versão do Python
python --version

# Locais onde ele procura
print(f'Seus diretórios são: {sys.path}\n')

# Local onde está instalado os pacotes
print(f'Local de armazenamento dos pacotes: {site.getsitepackages()}')

#----------------------------venv-----------------------------------------
# Nativo do Python
#Criar o ambiente virtual - Para dar nome o ambiente virtual > python -m venv <nome do ambiente>
python -m venv venv

#Ativação via Prompt Comando
.\venv\Scripts\Activate.bat

# Ativação via PowerShell
'.\venv\Scripts\Activate.ps1'

# Desativar o ambiente virtual
deactivate

# Remover todos pacotes instalados no venv
# pip freeze salva todos os pacotes e dependências no ambiente,
# incluindo aqueles que você não usa em seu projeto atual
pip uninstall -y (pip freeze)

#---------------------------virtualenv-------------------------------------
# Mantido e atualizado pela PyPa (Python Packaging Authority)
# Vantagens do virtualenv
# + E mais rápido
# + Tem um ciclo de lançamento independente do python
# + É extensível
# + Tem um API de código
# Instalação:
pip install virtualenv
# Criar ambiente virtual
virtualenv venv
# Desativar o ambiente
deactivate

#----------------------------requirements.txt------------------------------
# Documentação: https://pip.pypa.io/en/stable/reference/requirements-file-format/
# Listando minhas dependências
# Imagine que você tenha que dizer a algum quais os pacotes necessários?
# O arquivo requirements.txt é 0 lugar onde dizemos isso

# Exemplo:
# requirements.txt

# Pacotes que quero instalar
httpx
pandas
pytest

# pacotes com versões específicas
black == 0.6.1      # igual a 0.6.1
django >= 4.1.1     # maior que 4.1.1
flask != 3.5        # diferente de 3.5
selenium ~= 1.1     # maior ou igual a 1.1, mas menor que 2

# Fixar os requerimentos e criar o arquivo
pip freeze > requirements.txt

# Usando o arquivo requirements_dev.txt ou requirements.txt
pip install -r requirements_dev.txt
pip install -r requirements.txt

# requirements_dev.txt
-r requirements.txt # instala as de produção

# Bibliotecas de desenvolvimento
ipdb    # debugger
ipython # shell interativo
black   # formatador de código

#-----------------------------constraints.txt-----------------------------
# Restringe instalação de versão de pacotes, por motivos de segurança, bugs ou regra da equipe.
#comando criar arquivo no PowerShell
ni constraints.txt

# Instalar requirements com restrição das constraints
pip install -r requirements_dev.txt -c constraints.txt

#------------------------------PIP-----------------------------------------
# Atualizar o PIP
pip install --upgrade pip

# Atualizar o Setuptools
pip install --upgrade setuptools

# Listar pacotes instalados no Ambiente Virtual
pip list

# Instalar Pacotes (Packaging)
pip install numpy

# Desinstalar Pacotes (Packaging)
pip uninstall numpy

# Remove todos pacotes intalados
pip uninstall -y (pip freeze)

#-------------------------pip-autoremove-----------------------------------------
# Remove do ambiente as bibliotecas dependentes
pip install pip-autoremove

# Remover pacotes e suas dependências
pip-autoremove pandas

# Se der erro na execução pip-autoremove copiar o arquivo pip_autoremove.py para C:\Program Files\Python311\Lib ou C:\Users\Username\Documents\venv\Lib

#------------------------pipdeptree---------------------------------------------
# Mostra quais bibliotecas depende de quais
# Instalação:
pip install pipdeptree

# Listando as dependências dos pacotes
pipdeptree

#------------------------pipx---------------------------------------------------
# Instala ferramentas de linha de comando em um ambiente virtual isolado, bom para instalações globais
# Instalação:
pip install pipx

# Consultar pacotes instalados no pipx
pipx list

# Instalação de pacotes:
pipx install 