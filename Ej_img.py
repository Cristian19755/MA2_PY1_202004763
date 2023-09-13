import numpy as np
import matplotlib.pyplot as plt

# Importamos la imagen (asegúrate de que la ruta de la imagen sea correcta)
image = plt.imread("Proyecto/perrito.jpg") 

# Calculamos la transformada de Fourier 2D de la imagen
F = np.fft.fft2(image)

# Aplicamos un filtro en el dominio de la frecuencia
filtro = 1000000000  # Umbral de frecuencia para eliminar componentes de baja frecuencia
F_filtered = np.copy(F)  # Creamos una copia de la transformada para aplicar el filtro
F_filtered[np.abs(F) < filtro] = 0  # Eliminamos componentes de frecuencia inferiores al umbral

# Calculamos la imagen filtrada aplicando la transformada inversa de Fourier
image_filtered = np.fft.ifft2(F_filtered).real  # Usamos .real para obtener la parte real

# Normalizamos la imagen filtrada para asegurarnos de que esté en el rango [0, 1]
image_filtered = (image_filtered - np.min(image_filtered)) / (np.max(image_filtered) - np.min(image_filtered))

# Visualizamos la imagen original y la imagen filtrada
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Imagen original")

plt.subplot(1, 2, 2)
plt.imshow(image_filtered, cmap='gray')
plt.title("Imagen filtrada")

plt.show()
