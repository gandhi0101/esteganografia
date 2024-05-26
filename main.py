import os
import sys
from PIL import Image
import numpy as np

class Main:
    URLFile = ''
    File = any
    def __init__ (self):
        self.menu()
        
        
    def menu(self):
        while True:
            print("\n--- Menú ---")
            print("1. Codificar mensaje")
            print("2. Decodificar mensaje")
            print("3. Salir")
            opcion = input("Elige una opción: ")

            if opcion == '1':
                img_path = input("Introduce la ruta de la imagen original: ")
                message = input("Introduce el mensaje a ocultar: ")
                output_path = input("Introduce la ruta de la imagen de salida: ")
                self.encode_message(img_path, message, output_path)
            elif opcion == '2':
                img_path = input("Introduce la ruta de la imagen con el mensaje oculto: ")
                mensaje_oculto = self.decode_message(img_path)
                print(f'Mensaje oculto: {mensaje_oculto}')
            elif opcion == '3':
                print("Saliendo...")
                break
            else:
                print("Opción no válida, por favor intenta de nuevo.")
    
    '''encode_message: Este script carga una imagen y un mensaje, 
    convierte el mensaje a su representación binaria y luego inserta 
    estos bits en los bits menos significativos de los píxeles de 
    la imagen. La imagen resultante se guarda en un nuevo archivo.'''

    def encode_message(self,img_path, message, output_path):
        # Cargar la imagen
        img = Image.open(img_path)
        img_array = np.array(img)

        # Convertir el mensaje a binario
        binary_message = ''.join(format(ord(char), '08b') for char in message)
        binary_message += '1111111111111110'  # Indicador de fin de mensaje

        # Insertar el mensaje en la imagen
        data_index = 0
        for i in range(img_array.shape[0]):
            for j in range(img_array.shape[1]):
                for k in range(img_array.shape[2]):
                    if data_index < len(binary_message):
                        img_array[i, j, k] = int(format(img_array[i, j, k], '08b')[:-1] + binary_message[data_index], 2)
                        data_index += 1

        # Guardar la imagen con el mensaje oculto
        encoded_img = Image.fromarray(img_array)
        encoded_img.save(output_path)
        print(f'Mensaje oculto en {output_path}')


    '''decode_message: Este script carga la imagen con el mensaje 
    oculto, extrae los bits menos significativos de los píxeles, 
    reconstruye el mensaje binario y lo convierte de nuevo a texto.'''

    def decode_message(self,img_path):
        # Cargar la imagen
        self.img = Image.open(img_path)
        self.img_array = np.array(self.img)

        # Extraer los bits menos significativos
        binary_message = ''
        for i in range(self.img_array.shape[0]):
            for j in range(self.img_array.shape[1]):
                for k in range(self.img_array.shape[2]):
                    binary_message += format(self.img_array[i, j, k], '08b')[-1]

        # Convertir el mensaje binario a texto
        message = ''
        for i in range(0, len(binary_message), 8):
            byte = binary_message[i:i+8]
            if byte == '11111110':  # Indicador de fin de mensaje
                break
            message += chr(int(byte, 2))

        return message



if __name__ == '__main__':
    try:
        main = Main()
    except IndexError:
        print(f"Error: En la llamada al main.{IndexError}")