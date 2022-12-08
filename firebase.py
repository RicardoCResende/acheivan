import firebase_admin
from firebase_admin import credentials, firestore


cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "acheivan",
  "private_key_id": "6d2110e5a315867af5e8cc15986572183177be0a",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDRnCaBNwu5V5R6\n4Bubqbj5xj0m16naAku7zHk6LXFmN2k/UYnt+l4c7UaVNwcY2RRpQeAAf8U3P72o\nWy32B7z7z/cn/RaohkC4oXH3NnRr6lJr0YRus9eD3a3Q+WMT1uMllwcng0QtJsCg\nYJlZe6q66ry5Xzf3cYUmztAoYMD50OaP5ETkBurBSc++B3quPkzJtvJgl1z72wM9\nonP3R8T1jJNPu/eMW5fN7bo97+YV9HQAjNAOETQ6n4H5Mpz5jcpOJke9AuTQF7E8\n4vV1y0z1f7cDL8IIJlBO8IjrHmPbMMGOpXCmJMY0osvr3NANHDM6zCyLxbnzXzUG\n5eEz/U85AgMBAAECggEABjGPf7TxLz5TwFe76RsYQKUnbGzl82+q7jcqA9qQ5bzQ\natMNeM8zlbY7JjCUkJrlfAC6zjj4SlwjTgS3tHPhFS29d1yGnV8uLWZz2CKvSPsJ\nCW+M8rp0rUxRFQIxd8YbOyKdzwCVdKIXAgYosdiyIEjMX8vc+v5LOWzWAMNvIFKK\nqv7Azt4cCIWd2yxi8tURYbDY9QcEKlB9DPBJoyt2lPj5SYmhWojgNgf+1DaakRHE\nfCHAqNZGGzTEBLnVs9xJ9djAZhSI1fiH4qL/gmQ3OPfvjHQAiRAO/Nw3a+UdVA3t\nvNXNbCxFiTpkTrbKI+NZowBEA++QIDtjNQibepuGewKBgQD5zNOd/o2Uey88NjK+\nshDdPuAQ+cfF5qYvE1cHJVfVBckGbPeVbWzQHt+Xbxj2xr6kdMqbVfWKmd7ruSPH\njpgbuMR0R+7KVSe8UrE2J1lhovYyRHfsOJ38YqURvOuNhuzYfU5AwaXoWfLyo3gO\n6qKcoH/g/BHnjEljlbcPgDSjRwKBgQDWz/b3MLSCJV179g0qmvG4ajjzh3eWYM2I\n0ol7TSG+CmTtyO73FdjNg0VH3JjUx+2ftC35arciU6HSRNYhZ8nABADTrYkb7wYv\nUuj0EVcRb90yd4Xup7qOXW27xq7w4OOh2DnfDqQNcf8HvHMu5qgvPn/7bFRNG9z7\nOhTGTg65fwKBgQDebN6lGQsSAhnOIGhQ2pcfmaPEGdUjRzwEQNFGIJ8zpCIaYZ6W\n5Ed2jXcEDT2KRu9r2j6p0AGB937CIClWwIZ6cKwk6gQbD3YBPxRiJul0gbl8ivDJ\nWqR6HY/j2ndXnqN4JSMvj/5dhPJJ0PrPNWez1UnomCqNJaIXVTEaUUsNcwKBgQCI\nQU2jqc81pkHP+ViMp8+fbDFHt6vRRQHaQcFW5qv6gVlXwtZhAAiPAy8U0AZZIZ/G\nZ2GqDViwe1/voh44/j5of6GOo0qO32SK7Ao7liwmMVCbTFk18kpRN039h587x0pc\nRG0g4YaJyL89xvlAzKntnbVMY4BtkLjw2fyHdMe+PQKBgAda/j9GI8/bfi7unz+1\nsg8iNmocEQLW5ajg+mEaD+Fk3kqz7IhIhoip3U5DJ55wKo4lBhU41PO3lq772/Fb\nkWTFBvk1uTVoI7qYYj+kd7srq+g50udViWE+SQsXUWMt3qgqzdTQLUnuR659tTYH\nA7oqtSThkIiszRivQ+P/82iw\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-6gtv0@acheivan.iam.gserviceaccount.com",
  "client_id": "110097814124321170695",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-6gtv0%40acheivan.iam.gserviceaccount.com"
}
)
firebase_admin.initialize_app(cred)

db = firestore.client()

def estados(): #retorna uma lista dos estados cadastrados
    estados = db.collection('Estados').get()
    lista_estados = []
    for c in estados:
        lista_estados.append(c.id)
    return lista_estados


def cidades(id): #retorna uma lista com as cidades do estado selecionado
    cidades = db.collection('Estados').document(id).get().to_dict()
    lista_cidades = []
    for c in cidades:
        lista_cidades.append(c)
    return lista_cidades
    

def escolas(id, cidade): #retorna uma lista com as escolas da cidade selecionada
    escolas = db.collection('Estados').document(id).get().to_dict()
    lista_escolas = []
    for c in escolas[cidade]:
        lista_escolas.append(c)
    return lista_escolas

print(estados())
print(cidades('São Paulo'))
print(escolas('São Paulo', 'Sumaré'))