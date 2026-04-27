import os
import sys

def path_recurso(relative_path):
    """ Retorna o caminho real, seja rodando no Python ou no .exe """
    try:
        # O PyInstaller cria uma pasta temporária e armazena o caminho em _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# IMPORTANTE: Use essa função sempre que carregar um arquivo!
# Exemplo:
# som_vitoria = pygame.mixer.Sound(path_recurso("assets/vitoria.wav"))
# imagem_jogador = pygame.image.load(path_recurso("assets/player.png"))

import pygame
import random
import os

# 1. Configurações iniciais
pygame.init()
pygame.mixer.init()
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Encontro 2D - Edição Sprites")

# Cores
ROSA = (255, 182, 193)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Função de Carregamento
def carregar_imagem(nome, tamanho, cor_reserva, pasta='assets'):
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(diretorio_script, pasta, nome)
    try:
        imagem = pygame.image.load(caminho).convert_alpha()
        return pygame.transform.scale(imagem, tamanho)
    except Exception:
        print(f"Aviso: Não encontrei '{nome}'. Usando reserva.")
        reserva = pygame.Surface(tamanho, pygame.SRCALPHA)
        if nome == 'coracao.png':
            pygame.draw.ellipse(reserva, (220, 20, 60), [0, 0, tamanho[0], tamanho[1]])
        else:
            reserva.fill(cor_reserva)
        return reserva

# --- CARREGAMENTO DE ATIVOS ---
imagem_jogador = carregar_imagem('caixa.png', (60, 60), (139, 69, 19))
imagem_coracao = carregar_imagem('coracao.png', (30, 30), (220, 20, 60))

# Música com tratamento de erro
diretorio_script = os.path.dirname(os.path.abspath(__file__))
caminho_musica = os.path.join(diretorio_script, "assets", "musica_fundo.mp3")
try:
    pygame.mixer.music.load(caminho_musica)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
except pygame.error:
    print("Aviso: Música não encontrada.")

# 2. Variáveis do Jogo
jogador_pos = [largura // 2 - 25, altura - 70] 
item_pos = [random.randint(0, largura - 30), 0]
pontos_amor = 0
venceu = False # NOVO: Inicializa o estado de vitória
velocidade_jogador = 8
velocidade_item = 1.5   
velocidade_maxima = 5.5 
aceleracao = 0.004      

fonte = pygame.font.SysFont("Arial", 28, bold=True)
clock = pygame.time.Clock()
rodando = True

# 3. Loop Principal
while rodando:
    tela.fill(ROSA)
    if pontos_amor >= 50:
        venceu = True
        rodando = False
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Dificuldade
    if velocidade_item < velocidade_maxima:
        velocidade_item += aceleracao

    # Movimentação
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jogador_pos[0] > 0:
        jogador_pos[0] -= velocidade_jogador
    if teclas[pygame.K_RIGHT] and jogador_pos[0] < largura - 60:
        jogador_pos[0] += velocidade_jogador

    # Lógica do Item
    item_pos[1] += velocidade_item

    if item_pos[1] > altura:
        pontos_amor -= 1
        item_pos = [random.randint(0, largura - 30), 0]

    # Colisão
    rect_jogador = imagem_jogador.get_rect(topleft=(jogador_pos[0], jogador_pos[1]))
    rect_item = imagem_coracao.get_rect(topleft=(item_pos[0], item_pos[1]))

    if rect_jogador.colliderect(rect_item):
        pontos_amor += 1
        item_pos = [random.randint(0, largura - 30), 0]

    # --- CONDIÇÕES DE FIM DE JOGO ---
    if pontos_amor >= 50: # VITÓRIA
        venceu = True
        rodando = False
    
    if pontos_amor < 0: # DERROTA
        venceu = False
        rodando = False

    # Desenhar
    tela.blit(imagem_jogador, jogador_pos)
    tela.blit(imagem_coracao, item_pos)
    texto_pontos = fonte.render(f"Pontos de Afeição: {pontos_amor}", True, PRETO)
    tela.blit(texto_pontos, (20, 20))

    pygame.display.update()
    clock.tick(60)

# ... (todo o seu código inicial de carregamento e loop principal permanece igual)

# --- 4. TRANSIÇÃO DE ÁUDIO E LÓGICA DA TELA FINAL ---

# REMOVEMOS o fadeout genérico daqui para decidir o que fazer com a música:
if venceu:
    # Mantém a música e aumenta o volume para comemorar
    pygame.mixer.music.set_volume(0.9) 
else:
    # Se perdeu, a música para com um efeito suave de 1.5 segundos
    pygame.mixer.music.fadeout(1500)

esperando_sair = True

while esperando_sair:
    tela.fill(PRETO)
    fonte_grande = pygame.font.SysFont("Arial", 50, bold=True)
    
    if venceu:
        msg = fonte_grande.render("PARABÉNS!", True, ROSA)
        sub_msg = fonte.render("Você conquistou meu coração!", True, BRANCO)
    else:
        msg = fonte_grande.render("O CLIMA ESFRIOU...", True, (255, 0, 0))
        sub_msg = fonte.render("Tente novamente!", True, BRANCO)

    # Desenha as mensagens centralizadas
    tela.blit(msg, (largura // 2 - msg.get_width() // 2, altura // 2 - 60))
    tela.blit(sub_msg, (largura // 2 - sub_msg.get_width() // 2, altura // 2 + 10))
    
    instrucao = fonte.render("Pressione ESC para fechar", True, (150, 150, 150))
    tela.blit(instrucao, (largura // 2 - instrucao.get_width() // 2, altura - 50))

    pygame.display.update()
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
            esperando_sair = False

pygame.quit()