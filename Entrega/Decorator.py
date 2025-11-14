from abc import ABC, abstractmethod

# 1. Componente (Interfaz común)

class Bebida(ABC):
    @abstractmethod
    def costo(self) -> float:
        pass

    @abstractmethod
    def descripcion(self) -> str:
        pass

# 2. Componente Concreto (El objeto base)

class CafeBase(Bebida):
    def costo(self) -> float:
        return 5.0  # El café solo cuesta 5 dólares
    
    def descripcion(self) -> str:
        return "Café base"

# 3. Decorador Base

class DecoradorBebida(Bebida):
    def __init__(self, bebida_envuelta: Bebida):
        self._bebida = bebida_envuelta

    def costo(self) -> float:
        return self._bebida.costo()

    def descripcion(self) -> str:
        return self._bebida.descripcion()

# 4. Decoradores Concretos (Los ingredientes)


class Leche(DecoradorBebida):
    def costo(self) -> float:
        # Sumamos el costo de la bebida original + el costo de la leche
        return self._bebida.costo() + 2.0
    
    def descripcion(self) -> str:
        return f"{self._bebida.descripcion()}, con Leche"

class Chocolate(DecoradorBebida):
    def costo(self) -> float:
        return self._bebida.costo() + 3.5
    
    def descripcion(self) -> str:
        return f"{self._bebida.descripcion()}, con Chocolate"

class CremaBatida(DecoradorBebida):
    def costo(self) -> float:
        return self._bebida.costo() + 1.0
    
    def descripcion(self) -> str:
        return f"{self._bebida.descripcion()}, con Crema Batida"

# Código Cliente


mi_cafe = CafeBase()
print(f"Producto: {mi_cafe.descripcion()} | Total: ${mi_cafe.costo()}")

mi_cafe = Leche(mi_cafe)
print(f"Producto: {mi_cafe.descripcion()} | Total: ${mi_cafe.costo()}")

mi_cafe = Chocolate(mi_cafe)
print(f"Producto: {mi_cafe.descripcion()} | Total: ${mi_cafe.costo()}")

mi_cafe = CremaBatida(mi_cafe)
print(f"Producto final: {mi_cafe.descripcion()} | Total: ${mi_cafe.costo()}")