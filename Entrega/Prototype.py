import copy

# ------------------------------------------------
# La Clase Prototipo
# ------------------------------------------------
class Robot:
    def __init__(self, modelo, color, armas):
        self.modelo = modelo
        self.color = color
        self.armas = armas  

    def __str__(self):
        return f"Robot {self.modelo} | Color: {self.color} | Armas: {self.armas}"

    # Este es el método clave del patrón
    def clonar(self):
        """
        Crea una copia profunda (independiente) de este robot.
        Usamos deepcopy para asegurar que la lista de armas 
        también se clone y no se comparta.
        """
        return copy.deepcopy(self)

# ------------------------------------------------
# Código Cliente
# ------------------------------------------------

print("--- Creando el Prototipo Original ---")
robot_base = Robot(modelo="T-800", color="Plateado", armas=["Rifle", "Cuchillo"])
print(f"Original: {robot_base}")

print("\n--- Clonando Robots ---")

robot_clon_1 = robot_base.clonar()
print(f"Clon 1 (sin cambios): {robot_clon_1}")

robot_clon_2 = robot_base.clonar()
robot_clon_2.color = "Rojo"          
robot_clon_2.armas.append("Lanzallamas") 
print(f"Clon 2 (modificado): {robot_clon_2}")


print("\n--- Verificando Independencia ---")
print(f"Original tras las modificaciones del clon: {robot_base}")
