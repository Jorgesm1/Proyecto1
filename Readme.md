# 🖐️ Sistema Interactivo de Drag & Drop con Seguimiento de Manos

Este proyecto implementa un sistema interactivo de "arrastrar y soltar" (drag & drop) utilizando visión por computadora. 
El usuario puede mover un objeto virtual en pantalla con gestos naturales de la mano, capturados en tiempo real mediante la cámara web. 

---

## 🎯 Objetivo

Desarrollar una interfaz interactiva basada en gestos de la mano que permita:

- Detectar la mano del usuario usando la cámara.
- Reconocer el gesto de "agarre" juntando los dedos índice y pulgar.
- Permitir el movimiento de un objeto virtual cuando se realiza el gesto de agarre estando cerca del objeto.
- Soltar el objeto separando los dedos.

---

## 🧰 Tecnologías Utilizadas

- **Python 3.x**
- [OpenCV](https://opencv.org/) – Captura de video y procesamiento de imagen.
- [MediaPipe](https://google.github.io/mediapipe/) – Detección y seguimiento de manos.
- Visual Studio Code como entorno de desarrollo.
- Git + GitHub para control de versiones.

---



2.- (Opcional) Crea un entorno virtual:

python -m venv venv
.\venv\Scripts\activate  # En Windows
# o
source venv/bin/activate  # En Linux/Mac


📷 Funcionamiento del Sistema
Se activa la cámara web y se detecta la mano del usuario.

Se visualizan los dedos índice (punto 8) y pulgar (punto 4).

Si el usuario junta estos dedos cerca del objeto virtual, el sistema interpreta que se quiere "agarrar" el objeto.

Mientras los dedos se mantengan juntos, el objeto se mueve siguiendo el dedo índice.

Al separar los dedos, el objeto se "suelta" en la nueva posición.

