# Como instalar las dependencias

## Creación de entorno virtual
Se recomienda crear un entorno virtual para instalar las dependencias necesarias y evitar conflictos con otros proyectos.

### En windows
1. Crear el entorno virtual:
```bash
$ py -m venv venv
```
2. Activar el entorno virtual:
```bash
$ venv/Scripts/activate
```

### En linux
1. Crear el entorno virtual:
```bash
$ python -m venv venv
```
2. Activar el entorno virtual:
```bash
$ source venv/bin/activate
```

## Instalacion de las dependencias
Con el entorno virtual activado, instala las dependencias(Independientemente del sistema operativo)
```bash
$ pip install -r requirements.txt
```