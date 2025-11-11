"""
Una app que lee binario y lo convierte a texto.

"""

class LectorTexto:
    def leer_texto(self) -> str:
        raise NotImplementedError
    
# Servicio
class LectorBinario:
    def get_bytes(self) -> bytes:
        return b"Lectura de texto binario"
    
# Adaptador: traducir bytes a texto (str)
class AdaptadorBinarioATexto(LectorTexto):
    def __init__(self, servicio: LectorBinario):
        self.servicio = servicio

    def leer_texto(self) -> str:
        datos = self.servicio.get_bytes() # llama la interfaz
        return datos.decode("utf-8") # adapta el formato

# Uso por parte del cliente
def mostrar(lector: LectorTexto):
    print(lector.leer_texto())

mostrar(AdaptadorBinarioATexto(LectorBinario()))