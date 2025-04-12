import cv2
import mediapipe as mp
import math

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Inicializar cámara
cap = cv2.VideoCapture(0)

# Posición inicial del objeto (círculo)
object_pos = [300, 300]
dragging = False

# Calcular distancia entre dos puntos
def distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Voltear horizontalmente
    h, w, _ = frame.shape

    # Convertir imagen a RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Obtener coordenadas del dedo índice (punto 8) y pulgar (punto 4)
            index_finger = hand_landmarks.landmark[8]
            thumb_finger = hand_landmarks.landmark[4]

            # Convertir a coordenadas de píxeles
            ix, iy = int(index_finger.x * w), int(index_finger.y * h)
            tx, ty = int(thumb_finger.x * w), int(thumb_finger.y * h)

            # Dibujar la mano
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Dibujar los dedos índice y pulgar
            cv2.circle(frame, (ix, iy), 8, (0, 255, 0), -1)
            cv2.circle(frame, (tx, ty), 8, (0, 255, 0), -1)

            # Detectar gesto de "agarre": dedos índice y pulgar juntos
            pinch_distance = distance((ix, iy), (tx, ty))

            # Si están juntos (menos de 40 píxeles) y cerca del objeto: activar dragging
            if pinch_distance < 40 and distance((ix, iy), object_pos) < 40:
                dragging = True

            # Si se sueltan los dedos, terminar dragging
            elif pinch_distance > 60:
                dragging = False

            # Si estamos arrastrando, mover el objeto
            if dragging:
                object_pos = [ix, iy]

    # Dibujar objeto virtual (círculo)
    cv2.circle(frame, tuple(object_pos), 25, (255, 0, 0), -1)

    # Mostrar ventana
    cv2.imshow("Drag & Drop con la Mano", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Presiona ESC para salir
        break

cap.release()
cv2.destroyAllWindows()