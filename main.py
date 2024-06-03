import pyfiglet
import subprocess
import sys 
import os
import ansible_runner


f = pyfiglet.figlet_format("naja docker-auto", font="slant")
print(f)

def install_packages():
    try:
        os.system('sudo apt update -y')
    except os.error as e:
        print(f'Falha ao atualizar pacotes: {e}')
    
    try:
        os.system('sudo apt install -y software-properties-common')
    except os.error as e:
        print(f'Falha ao instalar dependencias {e}')

    try:
        os.system('sudo add-apt-repository --yes --update ppa:ansible/ansible')
    except os.error as e:
        print(f'Falha ao instalar asdicionar repositório {e}')

    try:
        os.system('sudo apt install ansible -y')
    except os.error as e:
        print(f'Falha ao instalar o ansible {e}')

def run_playbook(playbook_path, inventory_path):
    runner_config = {
        'playbook': playbook_path,
        'inventory': inventory_path,
        'quiet': True
    }
    result = ansible_runner.run(private_data_dir='.', **runner_config)

    for event in result.events:
        print(event['stdout'])

    return result.status

if __name__ == "__main__":
    install_packages()
    playbook_path = './playbook.yml'
    inventory_path = './hosts' 
    status = run_playbook(playbook_path, inventory_path)
    print(f"Playbook status: {status}")



#   python3 -m venv path/to/venv
#    source path/to/venv/bin/activate
#    python3 -m pip install xyz