import json 
download = open("ejemplo.json",'r')
download = json.loads(file.read())
print(f"son {len(download)} personas")
print('*'*5)
for dato in download:
    print('vname', dato['nombre'])
    print('vlastname', dato['Apellido'])
    print('vage', dato['Edad'])
    print('v', dato['Pais']) 
