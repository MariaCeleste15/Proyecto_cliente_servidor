import socket

HOST = '127.0.0.1'  # IP del servidor
PORT = 65432        # Puerto del servidor

def ejecutar_cliente():
    print("=== CALCULADORA DE PRODUCCION PROMEDIO ===")
    try:
        unidades = input("Ingrese la cantidad total de unidades producidas: ")
        trabajadores = input("Ingrese el numero de trabajadores participantes: ")

        # Prepara los datos para enviar
        mensaje = f"{unidades},{trabajadores}"

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            cliente.connect((HOST, PORT))
            cliente.sendall(mensaje.encode('utf-8'))

            # Recibe la respuesta del servidor
            respuesta = cliente.recv(1024).decode('utf-8')

        print("\n[RESPUESTA DEL SERVIDOR]:")
        print(respuesta)

    except ConnectionRefusedError:
        print("\n[ERROR]: No se pudo conectar con el servidor. Verifica que servidor.py este ejecutandose.")

if __name__ == '__main__':
    ejecutar_cliente()