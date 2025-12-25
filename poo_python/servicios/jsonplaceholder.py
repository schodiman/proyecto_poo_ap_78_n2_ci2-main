import requests 
from prettytable import PrettyTable

def obtener_users_api(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        #print(respuesta.json())
        tabla_usuarios = PrettyTable()
        tabla_usuarios.field_names = ["ID", "Nombre", "Email"]
        usuarios = respuesta.json()
        for usuario in usuarios:
            tabla_usuarios.add_row ([usuario['id'], usuario['name'], usuario['email']])
        print(tabla_usuarios)
    


def crear_user_api(url):
    nombre = input('Ingrese Nombre: ')
    usuario = input('Ingrese Usuario: ')
    email= input('Ingrese Email: ')
    telefono= input('Ingrese Teléfono: ')
    
    
    user = {
        "name": nombre,
        "username": usuario,
        "email": email,
        "phone": telefono
    }
    respuesta = requests.post(url, json=user)
    if respuesta.status_code == 200 or respuesta.status_code == 201:
        print(f'Usuario creado exitosamente:{respuesta.json()}')
        

def actualizar_user_api(url):
    nombre = input('Ingrese Nombre: ')
    usuario = input('Ingrese Usuario: ')
    email= input('Ingrese Email: ')
    telefono= input('Ingrese Teléfono: ')
    id_usuario = input('Ingrese ID de Usuario a Modificar: ')
    url = f'{url}/{id_usuario}'

    user = {
        "name": nombre,
        "username": usuario,
        "email": email,
        "phone": telefono
    }
    respuesta = requests.put(url, json=user)
    if respuesta.status_code == 200:
        print(f'Usuario actualizado exitosamente:{respuesta.json()}')
        
def eliminar_user_api(url):
    id_usuario = input('Ingrese ID de Usuario a Eliminar: ')
    url = f'{url}/{id_usuario}'
    respuesta = requests.delete(url)
    if respuesta.status_code == 200:
        print(f'Usuario con ID {id_usuario} eliminado exitosamente.')
        
        
        
        
               
        
def obtener_photos_api(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        #print(respuesta.json())
        tabla_fotos = PrettyTable()
        tabla_fotos.field_names = ["ID", "Título", "URL"]
        fotos = respuesta.json()
        for foto in fotos:
            tabla_fotos.add_row ([foto['id'], foto['title'], foto['url']])
        print(tabla_fotos)
        
def crear_photo_api(url):
    titulo = input('Ingrese Título: ')
    url_foto = input('Ingrese URL de la Foto: ')
    url_thumbnail= input('Ingrese URL del Thumbnail: ')
    
    
    photo = {
        "title": titulo,
        "url": url_foto,
        "thumbnailUrl": url_thumbnail
    }
    respuesta = requests.post(url, json=photo)
    if respuesta.status_code == 200 or respuesta.status_code == 201:
        print(f'Foto creada exitosamente:{respuesta.json()}')
        
        
def actualizar_photo_api(url):
    titulo = input('Ingrese Título: ')
    url_foto = input('Ingrese URL de la Foto: ')
    url_thumbnail= input('Ingrese URL del Thumbnail: ')
    id_foto = input('Ingrese ID de Foto a Modificar: ')
    url = f'{url}/{id_foto}'

    photo = {
        "title": titulo,
        "url": url_foto,
        "thumbnailUrl": url_thumbnail
    }
    respuesta = requests.put(url, json=photo)
    if respuesta.status_code == 200:
        print(f'Foto actualizada exitosamente:{respuesta.json()}')
        
        
def eliminar_photo_api(url):
    id_foto = input('Ingrese ID de Foto a Eliminar: ')
    url = f'{url}/{id_foto}'
    respuesta = requests.delete(url)
    if respuesta.status_code == 200:
        print(f'Foto con ID {id_foto} eliminada exitosamente.')
        
        
        