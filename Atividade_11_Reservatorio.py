# Monitoramento do Reservatório de Água

from colorama import Fore, Style

# Lista dos níveis
niveis = [1, 2, 3, 4, 5]

# Funcao 
def monitorar_reservatorio_de_agua(nivel_de_agua): 

    if nivel_de_agua == 1:
        print(f"{Fore.RED}Nivel de agua muito baixo!{Style.RESET_ALL}")

    elif nivel_de_agua == 2:
        print(f"{Fore.YELLOW}Nivel de agua baixo!{Style.RESET_ALL}")

    elif nivel_de_agua == 3:
        print(f"{Fore.GREEN}Nivel de agua adequado!{Style.RESET_ALL}")

    elif nivel_de_agua == 4:
        print(f"{Fore.CYAN}Nivel de agua alto!{Style.RESET_ALL}")

    elif nivel_de_agua == 5:
        print(f"{Fore.BLUE}Nivel de agua muito alto!{Style.RESET_ALL}")
    
# FORA da funcao
nivel = int(input("Qual é o nivel do reservatorio de agua de 1 a 5: "))


# Verificação
if nivel in niveis:
    monitorar_reservatorio_de_agua(nivel)

else:
    print("Nivel de agua invalido! Por favor, insira um valor entre 1 e 5.")