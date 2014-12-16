**GenHash** est une interface graphique crée avec Python 3 et Gtk3+ (PyGI). Ce logiciel permet de générer des hash des fichiers en se basant sur le module hashlib et zlib de python 3.

#Installation 
Pour lancer le programme, tapez sur vos console : 
 - ~$ python3 hash.py 
Veuillez noter que **GenHash** dépend de python 3 et de PyGI.


#Description 

**GenHash** est en cours d'évolution. Ce programme permet de donner le hashage des fichier à faible volume comme ceux les plus volumineux. Il prend un taille de block de lecture du fichier égal à 65536 octets.
Pour plus d'informations veuillez visiter ce lien sur Wikipédia : http://en.wikipedia.org/wiki/Secure_Hash_Algorithm  

**12/12/2014** 
**Update** - Support des hash suivants :
   * SHA1
   * MD5
   * SHA256
   * SHA384
   * SHA512
   * OpenSSL : ripemd160
   * Open SSL : DSA
   * Open SSL : MD4
   * base64
   * Zlib : adler32
   * Zlib : crc32
  
#TODO :
   - [x]  Ajout des nouveaux algorithmes de hashage
   - [x]  Correction des fonctions de hashage
   - [x]  La GUI ne reste active lors de la génération du hash d'un fichier volumineux
   - [x]  Ajout d'un Spinner pour indiquer que le processus de calcul est encore actif
   - [x]  Hashage d'une entrée par l'utilisateur
   - [x]  Ajouter des liens de documentation des algorithmes listés


#Bugs 
Veuillez notez les bugs sur https://github.com/Chiheb-Nexus/GenHash
![alt tag](http://3.bp.blogspot.com/-lo4qTwpy3So/VJCjx-Z4HfI/AAAAAAAAA8o/7KOqUaaK00Q/s1600/S%C3%A9lection_004.png)

