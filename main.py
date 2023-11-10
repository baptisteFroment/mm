import ssl
import socket

def get_ssl_info(host, port=443):
    context = ssl.create_default_context()

    # Création  d'une connexion SSL sécurisée
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            # Obtenir les informations de la suite de chiffrement
            cipher = ssock.cipher()
            version = ssock.version()

            print(f"Version de la suite de chiffrement: {version}")
            print(f"Nom de la suite de chiffrement: {cipher[0]}")
            print(f"Exposant RSA (si utilisé): {ssock.getpeercert().get('rsa_public_key', 'N/A')}")

get_ssl_info("webetud.iut-blagnac.fr")
