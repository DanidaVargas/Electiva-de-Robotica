import cv2
import numpy as np
import matplotlib.pyplot as plt

logo_chevrolet = cv2.imread('chevrolet_logo.png', cv2.IMREAD_GRAYSCALE)
logo_hyundai = cv2.imread('hyundai_logo.png', cv2.IMREAD_GRAYSCALE)

_,thres_chevrolet = cv2.threshold(logo_chevrolet, 240, 255, cv2.THRESH_BINARY)
_,thres_hyundai = cv2.threshold(logo_hyundai, 240, 255, cv2.THRESH_BINARY)

contornos_chevrolet,_ = cv2.findContours(thres_chevrolet, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contornos_hyundai,_ = cv2.findContours(thres_hyundai, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

coord_x_chevrolet = []
coord_y_chevrolet = []
for contorno in contornos_chevrolet:
    for punto in contorno:
        x, y = punto[0]
        coord_x_chevrolet.append(x)
        coord_y_chevrolet.append(y)

coord_x_hyundai = []
coord_y_hyundai = []
for contorno in contornos_hyundai:
    for punto in contorno:
        x, y = punto[0]
        coord_x_hyundai.append(x)
        coord_y_hyundai.append(y)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(coord_x_chevrolet, coord_y_chevrolet, s=1, color='purple')
plt.title('Contorno del logo de Chevrolet')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')

plt.subplot(1, 2, 2)
plt.scatter(coord_x_hyundai, coord_y_hyundai, s=1, color='blue')
plt.title('Contorno del logo de Hyundai')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')

plt.tight_layout()
plt.show()