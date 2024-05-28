import os
import sys
import wave
import cv2
from PIL import Image
import numpy as np

class Main:
    def __init__(self):
        self.menu()

    """encode_message_eof
        
        A) Y B)
        """
    def encode_message_eof(self, file_path, message, output_path):
        with open(file_path, 'rb') as file:
            content = file.read()

        message_bytes = message.encode('utf-8')
        eof_marker = b'EOFEOFEOF'
        encoded_content = content + eof_marker + message_bytes

        with open(output_path, 'wb') as file:
            file.write(encoded_content)
        print(f'Mensaje oculto en {output_path}')


        """ decode_message_eof
        B)
        """
        
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
    

    def clean_message_eof(self, file_path, output_path):
            with open(file_path, 'rb') as file:
                content = file.read()  # Abrimos el archivo y cargamos el contenido

            eof_marker = b'EOFEOFEOF'
            eof_index = content.find(eof_marker)
            if eof_index == -1:
                print("No se encontró un mensaje oculto.")  # Si no se encuentra la etiqueta, no hay mensaje oculto
                return False

            cleaned_content = content[:eof_index]  # Eliminar el mensaje y el marcador EOF

            with open(output_path, 'wb') as file:
                file.write(cleaned_content)  # Guardamos el archivo sin el mensaje oculto
            print(f'Mensaje oculto eliminado en {output_path}')
            return True
        
    """menu()
    D)

    """
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

                if mensaje_oculto:
                    eliminar = input("¿Deseas eliminar el mensaje oculto del archivo? (s/n): ")
                    if eliminar.lower() == 's':
                        output_path = input("Introduce la ruta del archivo de salida sin el mensaje oculto: ")
                        self.clean_message_eof(file_path, output_path)

            elif opcion == '3':
                print("Saliendo...")
                break
            else:
                print("Opción no válida, por favor intenta de nuevo.")

""" 
E)

"""
if __name__ == '__main__':
    Main()
