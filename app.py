# Códigos de cores ANSI para o terminal 
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
VERDE = "\033[92m"
CIANO = "\033[96m"
AZUL = "\033[94m"
RESET = "\033[0m"

# Lista para armazenar os dados dos níveis do reservatório
niveis_reservatorio = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)"},
    {"nivel": 2, "situacao": "Baixo"},
    {"nivel": 3, "situacao": "Médio"},
    {"nivel": 4, "situacao": "Alto"},
    {"nivel": 5, "situacao": "Muito alto (alerta)"},
]

def definir_cor_nivel(nivel):
    """Função responsável por definir e retornar a cor ANSI conforme o nível informado."""
    if nivel == 1:
        return VERMELHO
    elif nivel == 2:
        return AMARELO
    elif nivel == 3:
        return VERDE
    elif nivel == 4:
        return CIANO
    elif nivel == 5:
        return AZUL
    else:
        return RESET

def simular_monitoramento(dados_niveis):
    """Simula o monitoramento exibindo a situação atual no terminal com as cores correspondentes."""
    print("=" * 45)
    print("       SISTEMA DE CONTROLO DE NÍVEIS DE ÁGUA")
    print("=" * 45)

    for item in dados_niveis:
        nivel = item["nivel"]
        situacao = item["situacao"]

        # Obtém a cor através da função dedicada
        cor_alerta = definir_cor_nivel(nivel)

        # Exibe a mensagem formatada no terminal restaurando a cor no final
        print(f"{cor_alerta}[ESTADO] Nível {nivel}: {situacao.upper()}{RESET}")

    print("=" * 45)

# Execução da simulação
if __name__ == "__main__":
    simular_monitoramento(niveis_reservatorio)