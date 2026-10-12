Sistema de Monitoramento de Controle de Níveis de Água

Um sistema simples desenvolvido em Python para simular o monitoramento do nível de água de um reservatório. O sistema exibe mensagens de alerta diretamente no terminal, utilizando cores dinâmicas via biblioteca Colorama para facilitar a identificação visual da situação de risco.

📌 Funcionalidades Monitoramento em tempo real (simulado): Exibição dos níveis do reservatório de 1 a 5.Alertas Coloridos: Mapeamento visual das situações com cores representativas no terminal.Restauração Automática: Reposição do estilo padrão do terminal após a exibição dos alertas.

🎨 Tabela de Níveis e Cores
Nível Situação Cor no Terminal 
1 Muito baixo (crítico)🔴 Vermelho
2 Baixo🟡 Amarelo
3 Médio🟢 Verde
4 Alto🟦 Ciano
5 Muito alto (alerta)🔵 Azul

🛠️ Tecnologias Utilizadas Python Colorama — Biblioteca para formatação e cores no terminal.🚀 Como Executar o ProjetoPré-requisitosCertifique-se de ter o Python 3 instalado em sua máquina.1. Instalar a biblioteca coloramaNo seu terminal ou prompt de comando, execute:pip install colorama
2. Executar o programaSalve o código Python em um arquivo (por exemplo, main.py) e execute:python main.py
📂 Estrutura do Códigoniveis_reservatorio: Lista contendo os dicionários de cada nível e sua respectiva situação.definir_cor_nivel(nivel): Função que mapeia o número do nível para a cor da biblioteca colorama.simular_monitoramento(dados_niveis): Função responsável por percorrer os dados e exibir as saídas formatadas.