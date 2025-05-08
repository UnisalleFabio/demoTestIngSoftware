
# 📋 **Guía del Proyecto Demo - To-Do App (MVC)**

**Autor:** Fabio Andrés Hernández
**Docente de Ingeniería de Software**

---

## 📝 **Descripción del Proyecto**

El proyecto **To-Do App** es una aplicación de consola que implementa el patrón **Modelo-Vista-Controlador (MVC)**. En este proyecto, aprenderás a estructurar una aplicación en capas y a aplicar diferentes tipos de **pruebas de software** para asegurar su calidad.

---

## 🧱 **Estructura del Proyecto**

```
todo_app/
├── app.py                 # Lógica de negocio
├── models.py              # Modelo de datos
├── views.py               # Interfaz (terminal)
├── tests/
│   ├── test_unit.py       # Pruebas Unitarias
│   ├── test_integration.py# Pruebas de Integración
│   ├── test_system.py     # Pruebas de Sistema
│   └── test_acceptance.py # Pruebas de Aceptación
├── requirements.txt
└── README.md
```

---

## 📐 **Componentes del Proyecto**

* **Modelo (`models.py`)**: Define cómo se estructuran las tareas.
* **Controlador (`app.py`)**: Maneja la lógica de negocio y las operaciones sobre las tareas.
* **Vista (`views.py`)**: Interactúa con el usuario a través de la consola.

---

## 🧪 **Tipos de Pruebas en el Proyecto**

### 1. **Pruebas Unitarias (`tests/test_unit.py`)**

➡️ **Objetivo**: Verificar que **funciones individuales** o **clases** funcionen correctamente.
➡️ **Alcance**: Solo el **modelo** (`Task`).
➡️ **Ejemplos en el código**:

* **Creación de tareas (`test_task_creation`)**: Verifica que los objetos `Task` se creen correctamente.
* **Marcar tareas como completadas (`test_mark_completed`)**: Verifica que `mark_completed()` funcione correctamente.

📝 **Resultado esperado**:

* Las tareas deben tener un título y descripción válidos.
* Las tareas deben marcarse como completadas correctamente.

---

### 2. **Pruebas de Integración (`tests/test_integration.py`)**

➡️ **Objetivo**: Verificar que **múltiples componentes** funcionen correctamente juntos.
➡️ **Alcance**: Interacciones entre `TaskManager` y `Task`.
➡️ **Ejemplos en el código**:

* **Agregar tareas (`test_add_task`)**: Verifica que se puedan agregar tareas al administrador.
* **Completar tareas (`test_complete_task`)**: Verifica que `complete_task()` funcione correctamente al marcar tareas.

📝 **Resultado esperado**:

* Las tareas deben agregarse correctamente a la lista.
* Las tareas deben completarse sin errores.

---

### 3. **Pruebas de Sistema (`tests/test_system.py`)**

➡️ **Objetivo**: Verificar que el **sistema completo** funcione como se espera.
➡️ **Alcance**: Flujo completo de la aplicación.
➡️ **Ejemplos en el código**:

* **Completar y eliminar tareas (`test_complete_and_remove_task`)**: Verifica que se puedan completar y eliminar tareas.
* **Manejo de errores (`test_invalid_task_removal`)**: Verifica que los errores se manejen correctamente.

📝 **Resultado esperado**:

* Las tareas deben poder completarse y eliminarse sin errores.
* Los intentos de eliminar tareas no existentes deben lanzar errores correctamente.

---

### 4. **Pruebas de Aceptación (`tests/test_acceptance.py`)**

➡️ **Objetivo**: Verificar que la aplicación cumpla con los **requisitos del usuario final**.
➡️ **Alcance**: Flujo completo del sistema desde la perspectiva del usuario.
➡️ **Ejemplos en el código**:

* **Flujo completo (`test_full_workflow`)**: Verifica que los usuarios puedan agregar, completar y eliminar tareas en un flujo continuo.

📝 **Resultado esperado**:

* Las tareas deben poder agregarse, completarse y eliminarse en un flujo continuo sin errores.

---

## 🚀 **Ejecución de las Pruebas**

Para ejecutar todas las pruebas, usa el siguiente comando:

```bash
python -m unittest discover tests
```

Esto ejecutará todos los archivos que comienzan con `test_` en la carpeta `tests`.

---

## 📊 **Resumen de los tipos de pruebas:**

| **Tipo de Prueba**         | **Alcance**            | **Resultado Esperado**                                                      |
| -------------------------- | ---------------------- | --------------------------------------------------------------------------- |
| **Pruebas Unitarias**      | `Task` (modelo)        | Los objetos `Task` deben crearse correctamente y marcarse como completados. |
| **Pruebas de Integración** | `TaskManager` y `Task` | Las tareas deben agregarse, listarse y completarse correctamente.           |
| **Pruebas de Sistema**     | Flujo completo         | Las tareas deben completarse y eliminarse sin errores.                      |
| **Pruebas de Aceptación**  | Flujo del usuario      | El usuario debe poder completar un flujo completo de uso sin problemas.     |

---

## 📝 **Reto Adicional**

🔍 **Agrega nuevas funciones a la aplicación, como la edición de tareas o la búsqueda de tareas, e implementa las pruebas correspondientes.**

 