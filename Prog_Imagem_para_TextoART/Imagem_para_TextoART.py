import pywhatkit as kt

print("Vamos converter a imagem em texto")
source_path = 'flor'
target_path = 'ascii_art.text'
kt.image_to_ascii_art(source_path, target_path)
