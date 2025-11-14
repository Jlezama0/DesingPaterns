from abc import ABC, abstractmethod

# ------------------------------------------------
# 1. Producto: El objeto complejo
# ------------------------------------------------
class Computador:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.gpu = None
        self.almacenamiento = None

    def __str__(self):
        return f"PC Specs: [CPU: {self.cpu}, RAM: {self.ram}, GPU: {self.gpu}, HDD/SSD: {self.almacenamiento}]"

# ------------------------------------------------
# 2. Builder (Interfaz)
# ------------------------------------------------
class ComputadorBuilder(ABC):
    
    @property
    @abstractmethod
    def producto(self) -> Computador:
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def instalar_cpu(self):
        pass

    @abstractmethod
    def instalar_ram(self):
        pass

    @abstractmethod
    def instalar_gpu(self):
        pass

    @abstractmethod
    def instalar_almacenamiento(self):
        pass

# ------------------------------------------------
# 3. Concrete Builder (Constructor Específico)
# ------------------------------------------------
class PCGamerBuilder(ComputadorBuilder):
    
    def __init__(self):
        self.reset()

    def reset(self):
        self._computador = Computador()

    @property
    def producto(self) -> Computador:
        computador_terminado = self._computador
        self.reset() 
        return computador_terminado

    def instalar_cpu(self):
        self._computador.cpu = "Intel Core i9"

    def instalar_ram(self):
        self._computador.ram = "32GB DDR5"

    def instalar_gpu(self):
        self._computador.gpu = "NVIDIA RTX 4090"

    def instalar_almacenamiento(self):
        self._computador.almacenamiento = "2TB NVMe SSD"

# ------------------------------------------------
# 4. Director (El jefe de obra)
# ------------------------------------------------
class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> ComputadorBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: ComputadorBuilder):
        self._builder = builder

    def construir_pc_high_end(self):
        self.builder.instalar_cpu()
        self.builder.instalar_ram()
        self.builder.instalar_almacenamiento()
        self.builder.instalar_gpu()

    def construir_pc_basico(self):
        # Un PC básico quizás no tiene GPU dedicada
        self.builder.instalar_cpu()
        self.builder.instalar_ram()
        self.builder.instalar_almacenamiento()

# ------------------------------------------------
# Código Cliente
# ------------------------------------------------

director = Director()
builder_gamer = PCGamerBuilder()

print("Cliente: Quiero un PC Gamer tope de gama.")
director.builder = builder_gamer 
director.construir_pc_high_end() 
pc_gamer = builder_gamer.producto 
print(pc_gamer)

print("\nCliente: Quiero un PC personalizado (sin Director).")
builder_gamer.instalar_cpu()
builder_gamer.instalar_ram()
print(builder_gamer.producto)