# ❌⭕ Tic-Tac-Toe (Jogo da Velha)

Uma implementação clássica do Jogo da Velha desenvolvida em **Python**, focada na aplicação de Orientação a Objetos (OOP) e lógica de matrizes.

O projeto apresenta um desafio "Humano vs Computador", onde o jogador enfrenta uma IA que realiza jogadas aleatórias, com gerenciamento completo de turnos e validação de vitórias.

## 🎮 Funcionalidades

- **Oponente Automático (PvE):** Jogue contra o computador (que escolhe posições aleatórias disponíveis).
- **Sistema de Coordenadas:** Seleção de posições baseada em linhas e colunas (Matriz 3x3).
- **Validação Robusta:** O jogo impede jogadas em espaços ocupados ou coordenadas inválidas (tratamento de erros `try/except`).
- **Verificação de Vitória:** Algoritmo que checa horizontal, vertical e diagonal a cada turno.
- **Loop de Replay:** Permite jogar múltiplas partidas consecutivas sem reiniciar o script.

## 🛠️ Tecnologias Utilizadas

- **Biblioteca Standard:** Uso apenas de bibliotecas nativas (`random`, `os`), sem necessidade de instalações externas.

## 🚀 Como Rodar o Jogo

### Pré-requisitos
Certifique-se de ter o [Python](https://www.python.org/) instalado.

### Passo a Passo

1. **Clone o repositório e acesse a pasta:**
   `https://github.com/lucas-abreu56/tic_tac_toe`
2. **Execute o jogo:** Nota: Este projeto não requer instalação de dependências externas via pip.
   `python tic_tac_toe.py`

## 🕹️ Como Jogar

1. **Inicie o jogo** no seu terminal.
2. O tabuleiro é uma matriz 3x3. As posições possíveis vão de `0` a `2`.
3. Quando solicitado, digite o número da **Linha** (`0`, `1` ou `2`) e pressione `Enter`.
4. Em seguida, digite o número da **Coluna** (`0`, `1` ou `2`) e pressione `Enter`.
   > *Exemplo: Linha `0`, Coluna `0` marca o canto superior esquerdo.*
5. Você joga com **X** e o computador joga com **O**.
6. **Objetivo:** Alinhar 3 símbolos iguais (horizontal, vertical ou diagonal) antes do computador.
