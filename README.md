# 🏥 Análisis de Datos Médicos - Estructuras de Datos en Python 💉🧠

Bienvenidos a nuestro proyecto de **Análisis y Gestión de Datos Médicos** para la cátedra de **Estructuras de Datos en Python**. Aquí, llevamos el manejo de datos clínicos al siguiente nivel, aplicando desde árboles binarios hasta algoritmos de camino mínimo en un contexto real y desafiante.

**📆 Curso**: II Cuatrimestre 2024

**💼 Integrantes**:
- [Juan Ignacio Diaz](https://github.com/JuanIDiaz00)
- [Lucas Marcelo Contreras](https://github.com/Lure2002)
- [Martin Bahl](https://github.com/BahlMartin)

**🔧 Lenguaje**: Python (_of course! 🐍_)

## 🩺 Descripción del Proyecto

Este proyecto consiste en diseñar y desarrollar un sistema que permita **gestionar y analizar datos médicos** mediante estructuras de datos avanzadas. Imaginá una clínica digital donde podemos almacenar, organizar y optimizar el acceso a la información de los pacientes, gestionando desde su historial clínico hasta la red de hospitales más cercana para un traslado rápido.

## 🛠️ Estructura del Proyecto

Nuestro proyecto se divide en dos partes principales:

### 1. Teoría y Realización Práctica 📚💡

**Objetivo**: Implementar clases y algoritmos eficientes para la organización y consulta de información médica. Las secciones incluyen:

- **Clase `Paciente` y Gestión de Datos**: Crea, edita y elimina información de los pacientes.
- **Árbol Binario de Búsqueda**: Para encontrar pacientes por su ID en un abrir y cerrar de ojos.
- **Árbol General para el Historial Clínico**: Conecta diagnósticos, tratamientos y visitas.
- **Cola de Prioridades**: Los pacientes más graves siempre tienen prioridad.
- **Análisis de Complejidad**: Todo con eficiencia y estilo, siempre optimizando. 💡

### 2. Codificación y Algoritmos 🧑‍💻📈

**Objetivo**: Simular un sistema robusto de hospitales y diagnósticos, utilizando grafos y recorridos de manera estratégica.

- **Grafo de Hospitales**: Modela las conexiones entre centros médicos para una transferencia rápida y segura.
- **DFS y BFS**: Encuentra los caminos más cortos y rápidos en situaciones de emergencia.
- **Ordenamiento Topológico**: Ordena pasos de diagnóstico en secuencia.
- **Camino Mínimo (Dijkstra)**: Calcula la ruta ideal para que una ambulancia llegue a tiempo. 🚑

---

## 🚀 Cómo Empezar

1. **Cloná este Repositorio**:
   ```bash
   git clone https://github.com/usuario/analisis-datos-medicos.git
   cd analisis-datos-medicos
   ```

2. **Instalá las Dependencias**:
   > Este proyecto solo necesita Python 3.8+ y algunos paquetes estándar como `heapq`, que vienen incluidos. Easy-peasy. 🍋

3. **Ejecutá el Código**:
   ```bash
   python main.py
   ```

---

## 📁 Estructura de Archivos

```plaintext
.
├── README.md               # Este archivo fabuloso que estás leyendo
├── main.py                 # Punto de entrada del proyecto
├── clases/                 # Todas las clases necesarias (Paciente, NodoPaciente, etc.)
├── estructuras/            # Estructuras de datos (Árboles, Colas, Grafos)
└── algoritmos/             # Algoritmos (DFS, BFS, Dijkstra)
```

## 🧬 Funcionalidades Principales

- **Gestión Completa de Pacientes**: Agrega, edita y elimina pacientes con toda la info médica.
- **Búsqueda Optimizada**: Búsqueda en tiempo récord gracias a estructuras como árboles binarios y colas de prioridad.
- **Análisis de Complejidad**: Eficiencia garantizada con análisis detallado de cada operación.
- **Simulación de Red de Hospitales**: Rápido acceso y traslado de pacientes en situaciones críticas.

---

## 📈 Ejemplos de Uso

Aquí algunos ejemplos de cómo usar el código:

### Agregar un Paciente

```python
from clases import Paciente

paciente_nuevo = Paciente(id_paciente=1, nombre="Juan Perez", edad=34)
paciente_nuevo.agregar_enfermedad("Hipertensión")
print(paciente_nuevo)
```

### Crear un Árbol de Pacientes por ID

```python
from estructuras import ArbolPacientes

arbol_pacientes = ArbolPacientes()
arbol_pacientes.insertar(paciente_nuevo)
paciente_encontrado = arbol_pacientes.buscar(1)
print(paciente_encontrado)
```

### Usar el Algoritmo de Dijkstra para la Ruta más Corta

```python
from algoritmos import dijkstra
from estructuras import GrafoHospitales

grafo = GrafoHospitales()
grafo.agregar_hospital("Hospital A")
grafo.agregar_hospital("Hospital B")
grafo.agregar_conexion("Hospital A", "Hospital B", 10)

distancias = dijkstra(grafo, "Hospital A")
print("Distancia más corta a cada hospital:", distancias)
```

---

## 📊 Análisis de Complejidad

| Estructura/Algoritmo    | Complejidad Temporal | Complejidad Espacial |
|-------------------------|----------------------|----------------------|
| Árbol Binario de Búsqueda | O(log n)            | O(n)                |
| Cola de Prioridades     | O(log n)              | O(n)                |
| Dijkstra                | O(E log V)           | O(V)                |
| DFS/BFS                 | O(V + E)             | O(V)                |

---

## 🤝 Contribuciones

¿Te gustaría aportar alguna mejora o nueva funcionalidad? ¡Sos más que bienvenido/a! Simplemente hace un fork, creá una branch nueva y enviá un pull request. 🙌

---

## 🧠 Reflexión Final

El uso de estructuras de datos eficientes nos permite optimizar el procesamiento de información médica. En este proyecto, cada decisión de diseño ha sido cuidadosamente pensada para lograr una herramienta robusta y escalable en un área tan crucial como lo es la salud.

--- 

## 🏆 Agradecimientos

Gracias a la cátedra de Estructuras de Datos y a nuestro equipo por la dedicación y esfuerzo en este proyecto. 🙏

**¡Ahora estás listo para explorar nuestro sistema de análisis de datos médicos!**
