#!/bin/bash
echo "
DDDDDDDDDDDDD          jjjj
D::::::::::::DDD      j::::j
D:::::::::::::::DD     jjjj
DDD:::::DDDDD:::::D
  D:::::D    D:::::D jjjjjjj  aaaaaaaaaaaaa  nnnn  nnnnnnnn       ggggggggg   ggggg   ooooooooooo
  D:::::D     D:::::Dj:::::j  a::::::::::::a n:::nn::::::::nn    g:::::::::ggg::::g oo:::::::::::oo
  D:::::D     D:::::D j::::j  aaaaaaaaa:::::an::::::::::::::nn  g:::::::::::::::::go:::::::::::::::o
  D:::::D     D:::::D j::::j           a::::ann:::::::::::::::ng::::::ggggg::::::ggo:::::ooooo:::::o
  D:::::D     D:::::D j::::j    aaaaaaa:::::a  n:::::nnnn:::::ng:::::g     g:::::g o::::o     o::::o
  D:::::D     D:::::D j::::j  aa::::::::::::a  n::::n    n::::ng:::::g     g:::::g o::::o     o::::o
  D:::::D     D:::::D j::::j a::::aaaa::::::a  n::::n    n::::ng:::::g     g:::::g o::::o     o::::o
  D:::::D    D:::::D  j::::ja::::a    a:::::a  n::::n    n::::ng::::::g    g:::::g o::::o     o::::o
DDD:::::DDDDD:::::D   j::::ja::::a    a:::::a  n::::n    n::::ng:::::::ggggg:::::g o:::::ooooo:::::o
D:::::::::::::::DD    j::::ja:::::aaaa::::::a  n::::n    n::::n g::::::::::::::::g o:::::::::::::::o
D::::::::::::DDD      j::::j a::::::::::aa:::a n::::n    n::::n  gg::::::::::::::g  oo:::::::::::oo
DDDDDDDDDDDDD         j::::j  aaaaaaaaaa  aaaa nnnnnn    nnnnnn    gggggggg::::::g    ooooooooooo
                      j::::j                                               g:::::g
            jjjj      j::::j                                   gggggg      g:::::g
           j::::jj   j:::::j                                   g:::::gg   gg:::::g
           j::::::jjj::::::j                                    g::::::ggg:::::::g
            jj::::::::::::j                                      gg:::::::::::::g
              jjj::::::jjj                                         ggg::::::ggg
                 jjjjjj                                               gggggg

"
echo "----------------------"
echo "Instalando python y virtualenv"
sudo apt install python3 python3-dev
sudo apt-get install wget ca-certificates
echo "----------------------"
echo "Instalando postgresql"
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
echo "----------------------"
echo "Instalando git"
sudo apt install git
echo "----------------------"
echo "Instalando vim"
sudo apt install vim
echo "----------------------"
echo "Clonando repositoro"
echo "respositorio:"
read repo
git clone repo
cd repo
echo "----------------------"
echo "Creando virtualenv"
virtualenv -p python3 venv
echo "----------------------"
echo "Instalando requeriemiento, opciones posibles son"
find ./ -name requirements
echo "ruta:"
read ruta
pip install -r ruta
