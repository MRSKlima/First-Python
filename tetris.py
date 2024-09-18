import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da Tela
LARGURA, ALTURA = 300, 600
TAM_BLOCO = 30
LINHAS, COLUNAS = ALTURA // TAM_BLOCO, LARGURA // TAM_BLOCO
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tetris")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (128, 128, 128)
CORES = [
    (255, 0, 0),   # Vermelho
    (0, 255, 0),   # Verde
    (0, 0, 255),   # Azul
    (255, 255, 0), # Amarelo
    (255, 165, 0), # Laranja
    (0, 255, 255), # Ciano
    (255, 0, 255)  # Magenta
]

# Definições das Peças
PEÇAS = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]   # J
]

def criar_tabuleiro():
    return [[0] * COLUNAS for _ in range(LINHAS)]

def desenhar_tabuleiro(tela, tabuleiro):
    for y in range(LINHAS):
        for x in range(COLUNAS):
            if tabuleiro[y][x] != 0:
                pygame.draw.rect(tela, CORES[tabuleiro[y][x] - 1], (x * TAM_BLOCO, y * TAM_BLOCO, TAM_BLOCO, TAM_BLOCO))
                pygame.draw.rect(tela, PRETO, (x * TAM_BLOCO, y * TAM_BLOCO, TAM_BLOCO, TAM_BLOCO), 1)

def desenhar_peca(tela, peca, pos):
    forma, cor = peca
    for y, linha in enumerate(forma):
        for x, valor in enumerate(linha):
            if valor:
                pygame.draw.rect(tela, CORES[cor - 1], ((pos[0] + x) * TAM_BLOCO, (pos[1] + y) * TAM_BLOCO, TAM_BLOCO, TAM_BLOCO))
                pygame.draw.rect(tela, PRETO, ((pos[0] + x) * TAM_BLOCO, (pos[1] + y) * TAM_BLOCO, TAM_BLOCO, TAM_BLOCO), 1)

def criar_peca():
    forma = random.choice(PEÇAS)
    cor = PEÇAS.index(forma) + 1
    return forma, cor

def verificar_colisao(tabuleiro, peca, pos):
    forma, _ = peca
    for y, linha in enumerate(forma):
        for x, valor in enumerate(linha):
            if valor:
                x_pos, y_pos = pos[0] + x, pos[1] + y
                if x_pos < 0 or x_pos >= COLUNAS or y_pos >= LINHAS or tabuleiro[y_pos][x_pos]:
                    return True
    return False

def remover_linhas_cheias(tabuleiro):
    linhas_cheias = [i for i, linha in enumerate(tabuleiro) if all(celula for celula in linha)]
    for linha in linhas_cheias:
        del tabuleiro[linha]
        tabuleiro.insert(0, [0] * COLUNAS)
    return len(linhas_cheias)

def girar_peca(peca):
    forma, cor = peca
    forma = [list(row) for row in zip(*forma[::-1])]
    return forma, cor

def main():
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    tabuleiro = criar_tabuleiro()

    peca = criar_peca()
    pos = [COLUNAS // 2 - len(peca[0]) // 2, 0]

    clock = pygame.time.Clock()
    delay = 500
    ultima_troca = pygame.time.get_ticks()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return

        agora = pygame.time.get_ticks()
        if agora - ultima_troca > delay:
            pos[1] += 1
            if verificar_colisao(tabuleiro, peca, pos):
                pos[1] -= 1
                forma, cor = peca
                for y, linha in enumerate(forma):
                    for x, valor in enumerate(linha):
                        if valor:
                            tabuleiro[pos[1] + y][pos[0] + x] = cor
                peca = criar_peca()
                pos = [COLUNAS // 2 - len(peca[0]) // 2, 0]
                remover_linhas_cheias(tabuleiro)
            ultima_troca = agora

        # Controle com as teclas A, S, D, W
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_a]:  # Mover para a esquerda
            pos[0] -= 1
            if verificar_colisao(tabuleiro, peca, pos):
                pos[0] += 1
        if teclas[pygame.K_d]:  # Mover para a direita
            pos[0] += 1
            if verificar_colisao(tabuleiro, peca, pos):
                pos[0] -= 1
        if teclas[pygame.K_s]:  # Mover para baixo
            pos[1] += 1
            if verificar_colisao(tabuleiro, peca, pos):
                pos[1] -= 1
        if teclas[pygame.K_w]:  # Girar peça
            peca = girar_peca(peca)
            if verificar_colisao(tabuleiro, peca, pos):
                peca = girar_peca(peca)  # Desfazer a rotação se houver colisão

        tela.fill(PRETO)
        desenhar_tabuleiro(tela, tabuleiro)
        desenhar_peca(tela, peca, pos)
        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()
