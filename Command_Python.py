import sys
import site

# Confefir a versão do Python
python --version

# Locais onde ele procura
print(f'Seus diretórios são: {sys.path}\n')

# Local onde está instalado os pacotes
print(f'Local de armazenamento dos pacotes: {site.getsitepackages()}')

#Criar o ambiente virtual - Para dar nome o ambiente virtual > python -m venv <nome do ambiente>
python -m venv venv

#Ativação via Prompt Comando
.\venv\Scripts\Activate.bat

#Ativação via PowerShel
'.\venv\Scripts\Activate.ps1'

#Desativar o ambiente virtual
deactivate

# Listar pacotes instalados no Ambiente Virtual
pip list

#Instalar Pacotes (Packege)
pip install numpy