import os
import wave
import cv2
from PIL import Image
import numpy as np

class Main:
    def __init__(self):
        self.file_types = {
            'png': b'\x49\x45\x4E\x44\xAE\x42\x60\x82',
            'jpeg': b'\xFF\xD9',
            'jpg': b'\xFF\xD9',
            'gif': b'\x00\x3B',
            'zip': b'\x50\x4B\x05\x06',
            'pdf': b'\x25\x25\x45\x4F\x46',
            'wav': b'\x52\x49\x46\x46',
            'bmp': b'\x42\x4D',
            'mp3': None,
            'mp4': b'\x00\x00\x00\x14\x66\x74\x79\x70',
            'txt': None,
            'docx': b'\x50\x4B\x05\x06',
            'xlsx': b'\x50\x4B\x05\x06',
            'pptx': b'\x50\x4B\x05\x06',
            'exe': b'\x4D\x5A',
            'dll': b'\x4D\x5A',
            'rar': b'\x52\x61\x72\x21\x1A\x07\x00',
            'tar': b'\x75\x73\x74\x61\x72\x00\x30\x30',
            'gz': b'\x1F\x8B\x08',
            'iso': b'\x43\x44\x30\x30\x31'
        }

        self.menu()

    def encode_message_eof(self, file_path, message, output_path):
        with open(file_path, 'rb') as file:
            content = file.read()

        message_bytes = message.encode('utf-8')
        encoded_content = content + message_bytes

        with open(output_path, 'wb') as file:
            file.write(encoded_content)
        print(f'Mensaje oculto en {output_path}')

    def decode_message_eof(self, file_path):
        with open(file_path, 'rb') as file:
            content = file.read()

        eof_marker = self.get_eof_marker(file_path)
        eof_index = content.rfind(eof_marker)

        if eof_index == -1:
            print(f"\t\t\t No se encontró un mensaje oculto.")
            return ""

        message_bytes = content[eof_index + len(eof_marker):]
        message = message_bytes.decode('utf-8')
        return message

    def clean_message_eof(self, file_path, output_path):
        with open(file_path, 'rb') as file:
            content = file.read()

        eof_index = content.rfind(eof_marker)

        if eof_index == -1:
            print("No se encontró un mensaje oculto.")
            return False

        cleaned_content = content[:eof_index + len(eof_marker)]

        with open(output_path, 'wb') as file:
            file.write(cleaned_content)
        print(f'Mensaje oculto eliminado en {output_path}')
        return True

    def get_eof_marker(self, file_path):
        file_extension = os.path.splitext(file_path)[1][1:]
        eof_marker = self.file_types.get(file_extension)

        if eof_marker is None:
            if file_extension == 'txt':
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                visible_content = ''.join(lines).rstrip()  # Remove trailing whitespace
                eof_marker = visible_content[-1].encode('utf-8')  # Use the last visible character as the EOF marker
            else:
                with open(file_path, 'rb') as file:
                    content = file.read()
                eof_marker = content[:4]  # Use the first 4 bytes as the EOF marker

        return eof_marker


    def menu(self):
        while True:
            print("\n--- Menú ---")
            print("1. Codificar mensaje en archivo")
            print("2. Decodificar mensaje en archivo")
            print("3. Salir")
            try:
                opcion = input("Elige una opción: ")
            except:
                print("error en introducir la opcion")

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

if __name__ == '__main__':
    Main()
