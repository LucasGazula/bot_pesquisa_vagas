from colorama import Fore, Style, init
from datetime import datetime


def log(mensagem, sucesso):
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if sucesso == "SUCESSO":
        mensagem_formatada = f"{Fore.GREEN}[{agora}] {mensagem} - SUCESSO"
    elif sucesso == "FALHA":
        mensagem_formatada = f"{Fore.RED}[{agora}] {mensagem} - FALHA"
    
    print(mensagem_formatada)

    arquivo="log.txt"
    
    if arquivo:
        mensagem_sem_cores = mensagem_formatada.replace(Fore.GREEN, '').replace(Fore.RED, '').replace(Style.RESET_ALL, '')
        with open(arquivo, 'a') as f:
            f.write(mensagem_sem_cores + '\n')
            
    init(autoreset=True)


# log("Iniciando navegador", "SUCESSO")  # Adiciona a mensagem de sucesso ao arquivo "log.txt"
# log("Iniciando navegador", "FALHA") # Adiciona a mensagem de falha ao arquivo "log.txt"
