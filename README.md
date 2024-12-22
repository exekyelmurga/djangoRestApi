# 🚗 EGO-Challenge API  

¡Bienvenido a **EGO-Challenge**! 🎉  
Esta es una API REST creada con Django y Django REST Framework que te permite gestionar un catálogo de autos 🏎️. Podrás:  
- **Crear autos** con detalles como modelo, año de fabricación, precio y características.  
- **Clasificar** los autos en categorías como SUV, sedán, etc.  

¡Perfecta para aficionados de los autos o proyectos de gestión vehicular! 😎  

---

## 🌟 Funcionalidades  
- 🔍 **CRUD completo**: Gestión total de autos.  
- 🗂️ **Base de datos**:  
  - Local: SQLite3.  
  - Producción: PostgreSQL.  
- 🛠️ **Listo para despliegue**: Incluye un script (`build.sh`) para producción.  

---

## 🛠️ Requisitos Previos  
Antes de comenzar, asegúrate de tener lo siguiente instalado:  
- **Python 3.10+** 🐍  
- **pip** (gestor de paquetes de Python)  
- Recomendado: un entorno virtual como `venv`.  

---

## 🚀 Instalación  

1. **Clona este repositorio**:  
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   
2. **Crea y activa un entorno virtual**:
   
   En Unix/macOS:
     ```bash
       python3 -m venv venv  
       source venv/bin/activate
     ```
     En Windows:
   ```bash
   python -m venv venv  
   venv\Scripts\activate
   ```
3. Instala las dependencias:
  ```bash
  pip install -r requirements.txt  
  ```
4. Aplica las migraciones:

  ```bash
  python manage.py migrate  
  ```
5. Inicia el servidor local:
  ```bash

  python manage.py runserver  

  ```
