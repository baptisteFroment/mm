import ssl
import socket
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography import x509

def get_ssl_info(host, port=443):
    context = ssl.create_default_context()

    # Création d'une connexion SSL sécurisée
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            # Obtenir les informations de la suite de chiffrement
            cipher = ssock.cipher()
            version = ssock.version()
            certification = ssock.getpeercert(binary_form=True)

            print(f"Version de la suite de chiffrement: {version}")
            print(f"Nom de la suite de chiffrement: {cipher[0]}")

            # Afficher la clé publique RSA
            cert = x509.load_der_x509_certificate(certification, default_backend())
            rsa_key_info = cert.public_key().public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
            print(f"Clé publique RSA (en format PEM): {rsa_key_info.decode('utf-8')}")

# Exemple d'utilisation avec le site de l'université
get_ssl_info("webetud.iut-blagnac.fr")
