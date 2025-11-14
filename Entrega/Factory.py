from abc import ABC, abstractmethod

# --- PRODUCTO ---
class Documento(ABC):
    @abstractmethod
    def abrir(self):
        pass 

class DocumentoPdf(Documento):
    def abrir(self):
        print("Abriendo documento Pdf...")

class DocumentoTexto(Documento):
    def abrir(self):
        print("Abriendo documento de texto plano...")

# --- CREADOR ---
class Aplicacion(ABC):
    @abstractmethod
    def crear_documento(self) -> Documento:
        pass

    def nuevo_documento(self):
        # 1. Obtenemos el objeto (Factory Method)
        documento = self.crear_documento()
        # 2. Usamos el objeto
        documento.abrir() 

# --- CREADORES CONCRETOS ---
class AplicacionPdf(Aplicacion):
    def crear_documento(self) -> Documento:
        return DocumentoPdf()

class AplicacionTexto(Aplicacion):
    def crear_documento(self) -> Documento:
        return DocumentoTexto()

# --- CLIENTE ---
print("Iniciando la aplicación de PDF:")
app_pdf = AplicacionPdf()
app_pdf.nuevo_documento() 

print("\nIniciando la aplicación de Texto:")
app_texto = AplicacionTexto()
app_texto.nuevo_documento()