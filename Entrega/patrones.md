# Integrantes
**Juan Pablo Lezama**
**Juan David Olivos**

# Resumen de Patrones de Diseño en Python

---

## 1. Factory Method (Método de Fábrica)

* **Ejemplo (Logística):** El código define una `Aplicacion` abstracta. Las clases concretas (`AplicacionPdf`, `AplicacionTexto`) implementan el "método de fábrica" (`crear_documento`) para devolver un `Documento pdf` o un `Documento de texto plano`. El código principal (`nuevo_documento`) funciona con la `Aplicacion` genérica sin saber qué documento específico se está usando.

---

## 2. Builder (Constructor)

* **Ejemplo (PC Gamer):** El código permite ensamblar un `Computador`. El `PCGamerBuilder` sabe *cómo* instalar cada pieza (i9, RTX 4090). El `Director` (opcional) sabe *en qué orden* pedirlas (la receta para un "PC High End"). Esto separa el proceso de ensamblaje (el `Builder`) del resultado final (el `Computador`).

---

## 3. Prototype (Prototipo)


* **Ejemplo (Robots):** El código tiene una clase `Robot` con un método `clonar()`. Este método usa `copy.deepcopy()` para crear un duplicado exacto pero totalmente independiente del robot original. Es más rápido clonar un `robot_base` ya configurado que instanciar uno nuevo y reconfigurar sus armas y color cada vez.

---

## 4. Decorator (Decorador)

* **Ejemplo (Cafetería):** El código empieza con un `CafeBase`. Para añadir extras, se envuelve el objeto: `mi_cafe = Leche(mi_cafe)` y luego `mi_cafe = Chocolate(mi_cafe)`. Cada decorador (`Leche`, `Chocolate`) suma su propio costo y descripción al objeto que envuelve, creando una estructura de "muñeca rusa".

---

## 5. Adapter (Adaptador)

* **Ejemplo (API XML/JSON):** El código cliente (`cliente_codigo`) espera una interfaz que le dé un diccionario (`obtener_datos_dict`). Pero tenemos una `LegacyApiXML` que solo da XML. El `AdaptadorApi` se pone en medio: implementa la interfaz moderna, pero por dentro llama a la API vieja y *traduce* el XML a un diccionario, permitiendo que el cliente la use sin saber que existe XML.