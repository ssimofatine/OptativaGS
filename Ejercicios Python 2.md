# Ejercicios de Python 2

## Funciones

### Ejercicio 1: Calculadora de estadísticas
Crea una función que reciba una lista de números y retorne un diccionario con la media, mediana y moda.

**Ejemplo:**
```python
numeros = [1, 2, 2, 3, 4, 5, 5, 5, 6]
resultado = calcular_estadisticas(numeros)
# {'media': 3.67, 'mediana': 4, 'moda': 5}
```

---

### Ejercicio 2: Validador de contraseñas
Escribe una función que valide si una contraseña cumple los siguientes criterios:
- Al menos 8 caracteres
- Al menos una letra mayúscula
- Al menos una letra minúscula
- Al menos un número
- Al menos un carácter especial (@, #, $, %, etc.)

La función debe retornar `True` si cumple todos los criterios, `False` en caso contrario.

---

### Ejercicio 3: Contador de palabras
Crea una función que reciba un texto y retorne un diccionario con la frecuencia de cada palabra (ignorando mayúsculas/minúsculas y signos de puntuación).

**Ejemplo:**
```python
texto = "Python es genial. Python es poderoso y Python es versátil."
contar_palabras(texto)
# {'python': 3, 'es': 3, 'genial': 1, 'poderoso': 1, 'y': 1, 'versátil': 1}
```

---

## Módulos

### Ejercicio 4: Utilidades de strings
Crea un módulo `string_utils.py` con las siguientes funciones:
- `invertir_texto(texto)`: Invierte el orden de los caracteres
- `contar_vocales(texto)`: Cuenta cuántas vocales hay
- `es_palindromo(texto)`: Verifica si es un palíndromo
- `capitalizar_palabras(texto)`: Capitaliza la primera letra de cada palabra

Importa y usa estas funciones en otro archivo.

---

### Ejercicio 5: Gestor de fechas
Usa el módulo `datetime` para crear una función que:
- Reciba una fecha de cumpleaños (día, mes, año)
- Calcule cuántos días faltan para el próximo cumpleaños
- Si ya pasó este año, calcule para el próximo año

---

## List Comprehension

### Ejercicio 6: Números al cuadrado
Genera una lista con los cuadrados de los números pares del 1 al 50 usando list comprehension.

**Resultado esperado:**
```python
[4, 16, 36, 64, ..., 2500]
```

---

### Ejercicio 7: Filtrar palabras
Dada una lista de palabras, crea una nueva lista solo con las palabras que tengan más de 5 letras usando list comprehension.

**Ejemplo:**
```python
palabras = ["sol", "python", "casa", "programación", "gato", "computadora"]
# Resultado: ['python', 'programación', 'computadora']
```

---

### Ejercicio 8: Diccionario de longitudes
Dada una lista de strings, crea un diccionario usando comprehension donde las claves sean las palabras y los valores su longitud.

**Ejemplo:**
```python
palabras = ["Python", "Java", "JavaScript", "C++"]
# {'Python': 6, 'Java': 4, 'JavaScript': 10, 'C++': 3}
```

---

## Funciones Lambda

### Ejercicio 9: Ordenar por criterio
Usa una función lambda con `sorted()` para ordenar una lista de tuplas `(nombre, edad, altura)` por edad de menor a mayor.

**Ejemplo:**
```python
personas = [("Ana", 25, 165), ("Juan", 30, 175), ("María", 22, 160)]
# Resultado: [("María", 22, 160), ("Ana", 25, 165), ("Juan", 30, 175)]
```

---

### Ejercicio 10: Filtrar números
Usa `filter()` con lambda para obtener solo los números que sean divisibles por 3 Y por 5 (es decir, divisibles por 15) de una lista.

**Ejemplo:**
```python
numeros = [15, 30, 7, 45, 60, 12, 90]
# Resultado: [15, 30, 45, 60, 90]
```

---

### Ejercicio 11: Mapeo de temperaturas
Convierte una lista de temperaturas en Celsius a Fahrenheit usando `map()` y lambda. La fórmula es: F = (C × 9/5) + 32

**Ejemplo:**
```python
celsius = [0, 10, 20, 30, 40]
# Resultado: [32.0, 50.0, 68.0, 86.0, 104.0]
```

---

## Manejo de Excepciones

### Ejercicio 12: División segura
Crea una función `division_segura(a, b)` que divida dos números y maneje las siguientes excepciones:
- `ZeroDivisionError`: Si se intenta dividir por cero
- `ValueError`: Si los valores no son numéricos
- `TypeError`: Si los tipos de datos son incorrectos

La función debe retornar el resultado o un mensaje de error apropiado.

---

### Ejercicio 13: Conversión robusta
Crea una función que:
- Reciba una lista de strings
- Intente convertir cada elemento a entero
- Ignore los valores que no se puedan convertir
- Retorne una lista con los números convertidos y otra con los errores encontrados

**Ejemplo:**
```python
datos = ["10", "20", "abc", "30", "xyz", "40"]
# Resultado: ([10, 20, 30, 40], ["abc no se pudo convertir", "xyz no se pudo convertir"])
```

---

## Empaquetado/Desempaquetado

### Ejercicio 14: Coordenadas geográficas
Crea un programa que trabaje con coordenadas geográficas (latitud, longitud) utilizando desempaquetado de tuplas.  
- Función calcular_distancia_euclidiana(punto1, punto2)
  Recibe dos tuplas con coordenadas (latitud, longitud)
  Usa desempaquetado para extraer lat/lon de cada punto
  Calcula la distancia euclidiana simplificada: √((lat2-lat1)² + (lon2-lon1)²)
  Retorna la distancia

- Función procesar_ruta(*puntos)
  Recibe una cantidad variable de puntos (mínimo 2)
  Separa el punto de origen, el destino, y todos los puntos intermedios
  Calcula la distancia total del recorrido (suma de distancias entre puntos consecutivos)
  Retorna un diccionario con: origen, destino, puntos_intermedios, y distancia_total



Ejemplo de uso:
```python
# Coordenadas de ciudades españolas (aproximadas)

madrid = (40.4168, -3.7038)
barcelona = (41.3851, 2.1734)
valencia = (39.4699, -0.3763)
sevilla = (37.3891, -5.9845)

# Calcular distancia
dist = calcular_distancia_euclidiana(madrid, barcelona)
print(f"Distancia Madrid-Barcelona: {dist:.2f}")

# Procesar ruta completa
ruta = procesar_ruta(madrid, valencia, barcelona, sevilla)
print(f"Origen: {ruta['origen']}")
print(f"Destino: {ruta['destino']}")
print(f"Puntos intermedios: {ruta['puntos_intermedios']}")
print(f"Distancia total: {ruta['distancia_total']:.2f}")
```
