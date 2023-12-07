Sommaire

1. Introduction - contexte	1
2. Fonctionnement TLS	1
resumé de la page wikipedia:	2
Les suites de chiffrements tls	4
Le Handshake :	5
3. Diffie-Hellman	6
4. Suivi des tram HTTP vs HTTPS	7
Conclusion - ouverture thème sécurité	7
Brouillon	7
Les algos de chiffrement dans le protocole https	7

Introduction - contexte


Fonctionnement TLS


Le protocole Transport Layer Security (TLS), sécurise les communications en utilisant une infrastructure à clé publique asymétrique, qui est une combinaison d’une clé publique et d’une clé privée.
Lorsqu’un utilisateur se connecte à une page Web, la page envoie à l’utilisateur son certificat Secure Sockets Layer (SSL). Ce qui implique la présence de la clé publique nécessaire pour démarrer une session sécurisée.





Voici trois couches de protection clés que Transport Layer Security (TLS) et Secure Sockets Layer (SSL)  offrent aux utilisateurs :
Le chiffrement
Authentification
Intégrités des données
source : https://www.twaino.com/definition/h/https/
Le certificat TLS est le successeur de SSL 3.0 depuis 1999 avec l’apparition de TLS 1.0

resumé de la page wikipedia: 
La Transport Layer Security (TLS), anciennement connue sous le nom de Secure Sockets Layer (SSL), est un ensemble de protocoles de sécurité utilisés pour sécuriser les communications sur les réseaux informatiques, en particulier sur Internet. Le protocole SSL a été initialement développé par Netscape Communications Corporation pour sécuriser les communications via son navigateur web. Plus tard, l'Internet Engineering Task Force (IETF) a repris le développement du protocole en le renommant TLS. Les termes SSL et TLS sont souvent utilisés de manière interchangeable.

La TLS (ou SSL) fonctionne en mode client-serveur et vise à assurer les objectifs de sécurité suivants :
1. Authentification du serveur.
2. Confidentialité des données échangées grâce à la création d'une session chiffrée.
3. Intégrité des données échangées.
4. Éventuellement, l'authentification du client, bien que celle-ci soit généralement gérée au niveau de la couche applicative.

TLS est largement utilisé, notamment pour sécuriser des protocoles de la couche application tels que le HTTP, qui donne naissance au protocole HTTPS. Au fil du temps, TLS a connu plusieurs versions, notamment TLS v1.0 (1999), TLS v1.1 (2006), TLS v1.2 (2008), et TLS v1.3 (2018).

L'utilisation de TLS a considérablement renforcé la sécurité des transactions en ligne, telles que les paiements par carte bancaire, en empêchant les tiers d'intercepter des données sensibles transitant sur le réseau. Bien que le système de chiffrement ne soit pas infaillible, son adoption répandue par de nombreuses banques et sites de commerce électronique témoigne de son efficacité dans la protection des transactions des utilisateurs.

TLS est couramment reconnaissable par l'ajout du préfixe "https://" dans l'URL du site web, ainsi que par l'affichage d'un cadenas ou d'une icône de sécurité dans le navigateur web.

En plus de son utilisation dans le commerce électronique, TLS est également largement utilisé dans les réseaux industriels modernes pour sécuriser les communications.

TLS fonctionne en utilisant un mélange de chiffrement asymétrique, comme le chiffrement RSA, pour établir un secret partagé, et de chiffrement symétrique, comme l'AES, pour chiffrer les données échangées. La sécurité est renforcée par l'utilisation de fonctions de hachage, telles que SHA-1, pour garantir l'intégrité et l'authenticité des données.




Parler de "certificat SSL" de nos jours est un abus de langage. Bien que le terme "SSL" ait été largement utilisé par le passé pour désigner les certificats de sécurité numérique utilisés pour activer la couche de chiffrement dans les protocoles de sécurité sur Internet, en réalité, ces certificats sont désormais principalement associés à TLS (Transport Layer Security).

La confusion entre SSL et TLS est courante, mais il est important de noter que SSL est une technologie obsolète et a été remplacé par TLS. Les certificats SSL sont en réalité des certificats TLS, car TLS est la norme de sécurité actuelle pour les communications sur Internet. Par conséquent, il est plus précis de se référer à ces certificats comme des "certificats TLS" pour refléter la technologie de sécurité actuellement en vigueur.

Cependant, en pratique, de nombreuses personnes et entreprises utilisent encore le terme "SSL" de manière informelle pour désigner ces certificats de sécurité, même si techniquement, ils se réfèrent à TLS. Cela est principalement dû à la familiarité avec le terme "SSL" et à l'histoire de cette technologie. Il est important de comprendre que, même si l'usage informel de "SSL" persiste, la technologie sous-jacente est basée sur TLS.



Les suites de chiffrements tls

Le TLS (Transport Layer Security) est un protocole de sécurité essentiel pour garantir la confidentialité et la sécurité des données lors des communications sur Internet. Il est principalement utilisé pour chiffrer les échanges entre les applications web et les serveurs, notamment les navigateurs chargent des sites web. Il peut également être employé pour sécuriser d'autres types de communications, comme les e-mails, la messagerie et la voix sur IP (VoIP), mais cet article se concentre sur son rôle dans la sécurité des applications web.

Le protocole TLS a été proposé par l'Internet Engineering Task Force (IETF) et existe depuis 1999, avec la version la plus récente, TLS 1.3, publiée en 2018.

Il est important de noter que le TLS est l'évolution du précédent protocole SSL (Secure Socket Layer) développé par Netscape, et bien que les termes TLS et SSL soient parfois utilisés de manière interchangeable en raison de leur passé commun, le TLS est la version plus récente et améliorée.

Le HTTPS, quant à lui, est une implémentation du chiffrement TLS en surcouche du protocole HTTP utilisé par les sites web. Ainsi, tout site web utilisant le HTTPS repose sur le chiffrement TLS pour sécuriser les données en transit.

Les entreprises et les applications web ont de bonnes raisons d'utiliser le protocole TLS, car il contribue à protéger contre les violations de données et d'autres attaques. Les sites web utilisant le HTTPS, qui est protégé par TLS, sont devenus la norme, et les navigateurs modernes avertissent les utilisateurs des sites non HTTPS, ce qui renforce la confiance des internautes.

Le TLS fonctionne en se basant sur trois principaux composants : le chiffrement pour masquer les données, l'authentification pour vérifier l'identité des parties en communication, et l'intégrité pour s'assurer que les données ne sont pas altérées.

Pour utiliser le TLS, un certificat TLS, également appelé certificat SSL en raison de la confusion des dénominations, doit être installé sur le serveur d'origine d'un site web ou d'une application. Ces certificats sont délivrés par des autorités de certification et contiennent des informations cruciales sur l'entité propriétaire du domaine et la clé publique du serveur pour valider son identité.

Le TLS agit en initiants des négociations TLS, ou "handshake TLS", lorsqu'un utilisateur accède à un site web protégé par ce protocole. Au cours de cette négociation, les appareils client et serveur définissent des paramètres tels que la version de TLS, les suites de chiffrement, et ils authentifient le serveur grâce à son certificat TLS. Ensuite, ils génèrent des clés de session pour chiffrer les données de manière sécurisée.

Les performances des applications web ne sont généralement pas affectées par les dernières versions du TLS. Bien que la négociation TLS puisse nécessiter un certain temps de chargement et de la puissance de calcul en raison de sa complexité, des technologies comme le TLS False Start et la TLS Session Resumption ont été développées pour réduire la latence et rendre le protocole plus rapide. En fin de compte, le TLS est devenu un protocole rapide et efficace, et les coûts de calcul associés sont généralement négligeables par rapport aux normes actuelles. La version TLS 1.3, en particulier, a rendu le processus encore plus rapide en réduisant le nombre d'allers-retours nécessaires lors de la négociation.





Le Handshake : 
Client Hello
Server Hello
Certificats envoyé par le serveur
Echange de clés 
méthode Diffie-Hellman


1 - Client Hello 

Qu’est ce que la négociation (handshake ) ?

Le handshake désigne le processus qui amorce une session de communication en utilisant le chiffrement TLS. Durant cette négociation, les deux parties s’échangent des messages d’authentification et de vérification. Elles établissent également les algorithmes de chiffrement qu’elles utiliseront. De plus, les deux parties se mettent d’accord sur les clés de session.

La négociation intervient chaque fois qu’un utilisateur accède à un site web via HTTPS, le navigateur interroge le serveur d’origine du site web.
Il intervient aussi sur d’autre communication comme les appels api et les requêtes DNS sur HTTPS.

Au cours d’une négociation, le client et le serveur effectuent ensemble les opérations suivantes : 

Préciser la version TLS, décider de la suite de chiffrement, authentifier l’identité du serveur à l’aide de la clé publique et de la signature numérique du certificat.

Enfin, les clés de session afin d’utiliser le chiffrement symétrique une fois la négociation terminée.



Client Hello :

Le client envoie un message Client Hello avec la version du protocole, le client random et une liste de suites de chiffrement. 

Serveur Hello : 

Le serveur répond avec sont certificat, sa suite de chiffrement sélectionnée et le server random. Le serveur calcule une signature numérique de tous les messages jusqu’à ce point.

Authentification : le client vérifie le certificat SSL du serveur auprès de l'autorité de certification qui l'a émis. Cette opération confirme que le serveur est bien celui qu'il prétend être et que le client interagit avec le véritable propriétaire du domaine.

Secret pré-maître : le client envoie une autre chaîne d'octets aléatoire, le « premaster secret », ou secret pré-maître. Le secret pré-maître est chiffré à l'aide de la clé publique et ne peut être déchiffré par le serveur qu'avec la clé privée. (Le client obtient la clé publique dans le certificat SSL du serveur.)

Utilisation de la clé privée : le serveur déchiffre le secret pré-maître.

Création des clés de session : le client et le serveur génèrent des clés de session à partir du client random, du server random et du secret pré-maître. Ils doivent aboutir aux mêmes résultats.

Client prêt : le client envoie un message « Client Finished » chiffré à l'aide d'une clé de session.

Serveur prêt : le serveur envoie un message « Server Finished » chiffré à l'aide d'une clé de session.
Chiffrement symétrique sécurisé effectué : la négociation est terminée et la communication se poursuit à l'aide des clés de session.


Diffie-Hellman


Avec la clé secrète obtenu par l’échange de clé (asymétrique), plus une suite cryptographique (authentification, chiffrement par bloc, code d’authentification de message (MAC)), on peut échanger de manière sécurisée en chiffrant et déchiffrant les messages envoyés.
Autre source : hartleybrody

Suivi des tram HTTP vs HTTPS

liens utiles: https://www.youtube.com/watch?v=WIMKeyJ60Rw

détail TLS 

google évolution du trafic chiffré


Prendre le fonctionnement https sur un site web pour expliquer concrètement

passe par rsa asymétrique pour créer un canal de communication => créer une certification SSL
puis échange en AES (symétrique) 
détaillé les communications que la machine peut avoir avec le serveur

Mettre en place une démo



Comment il calcule sa key ?



Serveur web tout simple HTTP puis HTTPS
intercepté le trafic avec wireShark
reproduire le site : https://tls12.xargs.org/#server-encryption-keys-calculation

Conclusion - ouverture thème sécurité



Brouillon

Les algos de chiffrement dans le protocole https



 vérifier la source : RSA est un des algorithmes de chiffrement qui peuvent être utilisés par SSL.
TLS est le successeur de SSL, il corrige les vulnérabilités de SSL.

wiki TLS


Résumé page cloudflare


