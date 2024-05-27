# Proyecto de Esteganografía usando EOF

## Descripción

Este proyecto permite ocultar mensajes en diferentes tipos de archivos (imágenes, texto, audio y video) utilizando el marcador de fin de archivo (EOF) para esteganografía.

## Requisitos

- Python 3.12.3

## Instalación de Dependencias

Para instalar las librerías necesarias, ejecuta los siguientes comandos:

``pip install pillow numpy``

``pip install opencv-python``



## Uso

Para ejecutar el código, asegúrate de estar situado dentro del directorio del proyecto y ejecuta el siguiente comando:



```python .\EOF.py```

## Menú del Programa

El programa ofrece un menú interactivo con las siguientes opciones:

1. **Codificar mensaje en archivo**
2. **Decodificar mensaje en archivo**
3. **Salir**

## Funcionalidades

- **Codificación y decodificación de mensajes en imágenes**.
- **Codificación y decodificación de mensajes en archivos de texto**.
- **Codificación y decodificación de mensajes en archivos de audio**.
- **Codificación y decodificación de mensajes en archivos de video**.

## Ejecución del Programa

Al ejecutar el programa, se mostrará un menú en la terminal donde podrás elegir la opción deseada. Dependiendo de la opción seleccionada, deberás proporcionar las rutas de los archivos y el mensaje a ocultar.

---

### Ejemplo de Ejecución



--- Menú ---

Codificar mensaje en archivo
Decodificar mensaje en archivo
Salir
Elige una opción: 1
Introduce la ruta del archivo original: example.txt
Introduce el mensaje a ocultar: Este es un mensaje secreto.
Introduce la ruta del archivo de salida: output.txt
Mensaje oculto en output.txt



---

¡Gracias por usar nuestro proyecto de esteganografía!
