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

