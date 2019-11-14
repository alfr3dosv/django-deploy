import subprocess
import os

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

def instalar():
    print("----------------------")
    print("Instalando python y virtualenv")
    subprocess.run("sudo apt install python3 python3-devsudo apt-get", shell=True)
    subprocess.run("install wget ca-certificates", shell=True)
    print("----------------------")
    print("Instalando postgresql")
    subprocess.call("wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add", shell=True)
    subprocess.run('echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list', shell=True)
    subprocess.run('sudo apt-get update', shell=True)
    subprocess.run('sudo apt-get install postgresql postgresql-contrib', shell=True)
    print("----------------------")
    print("Instalando git")
    subprocess.run("sudo apt install git", shell=True)
    print( "----------------------")
    print("Instalando vim")
    subprocess.run("sudo apt install vim", shell=True)
    print("----------------------")
    print("Clonando repositoro (acepta formatos https://github.com/usuario/repo.git)")
    repositorio = input("respositorio:")
    repositorio_sin_punto_git = repositorio.replace(".git", "")
    repositorio_nombre = repositorio_sin_punto_git.split("/")[-1]
    print(repositorio_nombre)
    subprocess.run("git clone {}".format(repositorio), shell=True)
    os.chdir(repositorio_nombre)

    print("Buscando requirements.txt")
    encontrados = find_all('requirements.txt', './')
    n = 0
    for i, ruta in enumerate(encontrados):
        print("{}) {}".format(i, ruta))
        n = i
    n += 1
    print("{}) {}".format(n, "omitir"))
    opcion = -1
    while (opcion < 0 or opcion > n):
        try:
            opcion = int(input("ruta: "))
        except Exception as e:
            opcion = -1
    if opcion == n:
        print("no usando requirements")
    else:
        print("creando virtualenv")
        subprocess.run("virtualenv -p python3 venv", shell=True)
        subprocess.run(". venv/bin/activate", shell=True)
        subprocess.run("venv/bin/pip3 install -r {}".format(encontrados[opcion]), shell=True)






print("""
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

""")

opcion = input("""
Opciones
1) Instalar
2) Actualizar paquetes
4) Realizar migraciones
5) Verificar instalacion
3) Salir
opcion: 
""")
if opcion == "1":
    instalar()