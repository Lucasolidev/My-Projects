import os
import time

path = 'C:\Scanner'
now = time.time()

for arquivo in os.listdir(path):
    arquivo = os.path.join(path, arquivo)
    if os.stat(arquivo).st_mtime < now - 1 * 86400:
        if os.path.isfile(arquivo):
            os.remove(arquivo)
