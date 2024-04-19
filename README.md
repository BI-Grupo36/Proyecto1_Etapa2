# Proyecto1_Etapa2
---

Integrantes (Sección 1):
- Santiago Martínez Novoa - 202112020
- María Alejandra Estrada García - 202021060
- Marilyn Stephany Joven Fonseca - 202021346

## Instalación de la aplicación

1. Clonar el repositorio

### Ejecución del Backend

2. Acceder a la carpeta del API:

```
cd reviews_back
```

3. Generar un ambiente virtual e instalar las dependencias


Es necesario instalar virtual env para crear el ambiente virtual:

```
pip install virtualenv
```

Una vez instalado, se crea el ambiente virtual con el nombre de `env`:


```
python -m venv env
```
Luego se activa el ambiente virtual:

```
# En powershell
env\Scripts\activate

# En cmd
env\Scripts\activate.bac
```

Finalmente se se instalan las dependencias:

```
pip install -r requirements.txt
```

4. Ejecutar el Backend

```
uvicorn src.main:app --reload
```

La aplicación correrá en el http://127.0.0.1:8000/ y en http://127.0.0.1:8000/docs se puede revisar la documentación del API.


### Ejecución del Frontend

Requisitos:
- Node.js

1. Instalar node. Puedes verificar que node se ha instalado usando el siguiente comando:
   ```node -v```
2. Instalar los node_modules para poder correr la aplicaciòn:
   ```npm install```
3. Ejecutar la aplicación Ejecuta la aplicación usando el siguiente comando:
   ```npm start```
   
La aplicación estará en funcionamiento en http://localhost:3000

Puedes acceder a la aplicación a través de un navegador.

### Nota importante

Para que la aplicación funcione correctamente, debes ejecutar la aplicación del backend, con las instrucciones anteriores.
