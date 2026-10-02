
import socket

HOST = '127.0.0.1'
PORT = 65432

def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((HOST, PORT))
        servidor.listen()
        print(f"[*] Servidor escuchando en {HOST}:{PORT}...")

        while True:
            conexion, direccion = servidor.accept()
            with conexion:
                print(f"[+] Cliente conectado desde: {direccion}")
                datos = conexion.recv(1024).decode('utf-8')
                if not datos:
                    break

                try:
                    unidades, trabajadores = map(float, datos.split(','))

                    # VALIDACION OBLIGATORIA
                    if trabajadores <= 0:
                        respuesta = "ERROR: El numero de trabajadores debe ser mayor a cero."
                    else:
                        promedio = unidades / trabajadores
                        respuesta = f"EXITO: La produccion promedio por trabajador es: {promedio:.2f} unidades."

                except ValueError:
                    respuesta = "ERROR: Datos de entrada invalidos."

                conexion.sendall(respuesta.encode('utf-8'))

if __name__ == '__main__':
    iniciar_servidor()