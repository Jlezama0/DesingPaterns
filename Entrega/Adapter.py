from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET # Para simular el parseo

# 1. El Adaptee (El sistema viejo e incompatible)

class LegacyApiXML:
    """
    Esta es la API vieja. Funciona perfectamente, pero devuelve
    un string XML que nuestro sistema moderno no entiende.
    """
    def obtener_datos_xml(self) -> str:
        # Simulamos una respuesta XML
        return "<data><item>Manzana</item><price>1.5</price></data>"


# 2. El Target (La interfaz que nuestro cliente SÍ espera)
class InterfazDatosModernos(ABC):
    """
    Nuestro código cliente solo sabe llamar a este método 
    y espera recibir un diccionario.
    """
    @abstractmethod
    def obtener_datos_dict(self) -> dict:
        pass

# ------------------------------------------------
# 3. El Adapter (El traductor)
# ------------------------------------------------
class AdaptadorApi(InterfazDatosModernos):
    """
    Este es el adaptador Cumple con la interfaz moderna, 
    pero por dentro envuelve a la API vieja.
    """
    def __init__(self, api_vieja: LegacyApiXML):
        self._api_vieja = api_vieja

    def obtener_datos_dict(self) -> dict:
        # ¡AQUÍ ESTÁ LA MAGIA!
        # 1. Llama al método viejo
        xml_data = self._api_vieja.obtener_datos_xml()
        
        # 2. Traduce la respuesta
        print("Adapter: (Traduciendo de XML a Diccionario...)")
        # (Simulación de un parseo real)
        datos_dict = {"producto": "Manzana", "precio": 1.5}
        
        # 3. Devuelve los datos en el formato esperado
        return datos_dict

# ------------------------------------------------
# 4. El Cliente
# ------------------------------------------------
def cliente_codigo(sistema_datos: InterfazDatosModernos):
    """
    Este código cliente funciona mientras reciba algo que
    cumpla con la InterfazDatosModernos. No sabe nada de XML.
    """
    print("\nCliente: Pidiendo datos (no sé de dónde vienen)...")
    datos = sistema_datos.obtener_datos_dict()
    print(f"Cliente: ¡Datos recibidos! {datos}")

# ------------------------------------------------
# Código de ejecución
# ------------------------------------------------

print("--- Ejecutando código con el Adaptador ---")
# 1. Creamos la instancia del sistema viejo
api_vieja = LegacyApiXML()

# 2. Lo envolvemos en el adaptador
adaptador = AdaptadorApi(api_vieja)

# 3. Se lo pasamos al cliente. 
cliente_codigo(adaptador)