import pyfiglet
import subprocess
import sys 


f = pyfiglet.figlet_format("naja docker-auto", font="slant")
print(f)

print(f"Instalando Ansible...")
try:
    subprocess.run('apt-get', 'install', '-y', 'ansible'], check=True)
    print(f"Pacote ansilbe instalado com sucesso.")
except subprocess.CalledProcessError as e:
    print(f"Falha ao instalar ansible: {e}")
    sys.exit(1)


#   python3 -m venv path/to/venv
#    source path/to/venv/bin/activate
#    python3 -m pip install xyz
