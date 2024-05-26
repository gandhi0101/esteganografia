from PIL import Image
import numpy as np

def encode_message(img_path, message, output_path):
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

# Ejemplo de uso

