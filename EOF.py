import os
import sys
import wave
import cv2
from PIL import Image
import numpy as np

class Main:
    def __init__(self):
        self.menu()

    def encode_message_eof(self, file_path, message, output_path):
        with open(file_path, 'rb') as file:
            content = file.read()

        message_bytes = message.encode('utf-8')
        eof_marker = b'EOFEOFEOF'
        encoded_content = content + eof_marker + message_bytes

        with open(output_path, 'wb') as file:
            file.write(encoded_content)
        print(f'Mensaje oculto en {output_path}')

    def decode_message_eof(self, file_path):
        with open(file_path, 'rb') as file:
            content = file.read()

        eof_marker = b'EOFEOFEOF'
        eof_index = content.find(eof_marker)
        if eof_index == -1:
            print("No se encontró un mensaje oculto.")
            return ""

        message_bytes = content[eof_index + len(eof_marker):]
        message = message_bytes.decode('utf-8')
        return message

    def menu(self):
        while True:
            print("\n--- Menú ---")
            print("1. Codificar mensaje en archivo")
            print("2. Decodificar mensaje en archivo")
            print("3. Salir")
            opcion = input("Elige una opción: ")

            if opcion == '1':
                file_path = input("Introduce la ruta del archivo original: ")
                message = input("Introduce el mensaje a ocultar: ")
                output_path = input("Introduce la ruta del archivo de salida: ")
                self.encode_message_eof(file_path, message, output_path)
            elif opcion == '2':
                file_path = input("Introduce la ruta del archivo con el mensaje oculto: ")
                mensaje_oculto = self.decode_message_eof(file_path)
                print(f'Mensaje oculto: {mensaje_oculto}')
            elif opcion == '3':
                print("Saliendo...")
                break
            else:
                print("Opción no válida, por favor intenta de nuevo.")

if __name__ == '__main__':
    Main()
