# Se tiene una aplicación que maneja datos de clientes en diferentes formatos. 
# Una clase que devuelve el nombre del cliente en formato de diccionario (JSON), y otra clase que necesita
# el nombre en un formato de cadena de texto (String).

# Clase que devuelve al cliente en formato JSON.
class ClienteJSON:
    def obtener_cliente(self):
        return {
            "nombre": "Pancracio Gómez",
            "edad": 30
        }

# Clase que necesita al cliente en formato String
class ClienteString:
    def mostrar_cliente(self, datos):
        print(f"Cliente: {datos}")

# Clase ADAPTER que adapta el formato JSON a String
class ClienteAdapter:
    def __init__(self, cliente_json):
        self.cliente_json = cliente_json

    def obtener_cliente_formato_string(self):
        datos_json = self.cliente_json.obtener_cliente()
        return f"Nombre: {datos_json['nombre']}, Edad: {datos_json['edad']}"

# Se instancian las clases originales en variables
cliente_json = ClienteJSON()
cliente_string = ClienteString()

# Se crea el adaptador
adapter = ClienteAdapter(cliente_json)

# Se obtienen los datos en formato String del adaptador
datos_adaptados = adapter.obtener_cliente_formato_string()

# Se agregan los datos a la Clase ClienteString
cliente_string.mostrar_cliente(datos_adaptados)
