from PIL import Image
import pandas as pd

def img_to_RGB(path, name):
    # Abre la imagen
    img = Image.open(path)
    rgb_img = img.convert('RGB')
    width, height = rgb_img.size

    # Extrae los valores RGB de cada pixel
    pixel_in_RGB = []
    for i in range(width):
        for j in range(height):
            pixel_in_RGB.append(list(img.load()[i, j]))

    # Guarda los valores en un dataframe
    pixels = pd.DataFrame(data={'RGB': pixel_in_RGB})
    pixels['R'] = pixels['RGB'].apply(lambda R: R[0])
    pixels['G'] = pixels['RGB'].apply(lambda G: G[1])
    pixels['B'] = pixels['RGB'].apply(lambda B: B[2])
    pixels.drop(columns=['RGB'], inplace=True)
    pixels.to_csv(f'{name}.csv', index=False)

img_to_RGB('./img/arbolito.png', 'name')