import subprocess

# Comando para executar os testes no modo "runWithNoTests", "noCache", "watch" e na pasta test
command = "ptw test/"

# Execute o comando no terminal
subprocess.run(command, shell=True, check=True)
