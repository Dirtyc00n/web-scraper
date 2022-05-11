import urllib.request
import xml.etree.ElementTree as xml
url="https://example.com"
info=urllib.request.urlopen(url).read()
resume =xml.fromstring(info.decode())
q = resume.findall("food")
print('cantidad de registros: ', len(q))
for line in query:
    print('Nombre: ', line.find('name').text)
    print('Precio: ', line.find('price').text)
    print('Descripcion: ', line.find('description').text)
    print('Calorias: ', line.find('calories').text)
    print('-'*20)
