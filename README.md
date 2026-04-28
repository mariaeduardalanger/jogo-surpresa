
# 🕹️ Catch The Hearts: Asset Pipeline & Game

Este projeto demonstra um fluxo completo de desenvolvimento: desde a **automação de assets** (preparação de imagens e sons) até a criação de um **jogo funcional** em Pygame. 

O foco principal aqui foi resolver problemas comuns de desenvolvedores, como a padronização de arquivos em massa e a criação de executáveis (.exe) que não quebram ao carregar arquivos.

---

## 🛠️ O que o projeto faz?

### 1. Processador de Mídia (`processor.py`)
Um script de automação que limpa e padroniza arquivos brutos.
* **Imagens:** Redimensiona para **20x20 pixels** com filtro `NEAREST` (preserva a nitidez de Pixel Art).
* **Áudio:** Converte diversos formatos para `.wav` usando **FFmpeg**, garantindo que o som rode sem erros no Pygame.
* **Logs:** O script valida se as ferramentas (FFmpeg) estão instaladas antes de começar.

### 2. Catch The Hearts Game (`game.py`)
Um jogo de captura com mecânicas de progressão.
* **Dificuldade Escalável:** A velocidade dos itens aumenta conforme você pontua.
* **Compatibilidade EXE:** Uso da função `path_recurso` para garantir que o jogo encontre as imagens mesmo após ser compilado pelo PyInstaller.
* **UX Sonora:** Sistema de *fadeout* na trilha sonora em caso de derrota e aumento de volume na vitória.

---

## 🚀 Como testar

### 1. Pré-requisitos
* **Python 3.x**
* **FFmpeg** (necessário para o processamento de áudio)
* Bibliotecas: `pip install pygame Pillow pydub`

### 2. Rodando o projeto
1.  Coloque suas imagens/músicas em `assets_brutos/`.
2.  Execute o `processor.py` para gerar os arquivos na pasta `assets_processados/`.
3.  Mova os arquivos para a pasta `assets/` do jogo.
4.  Inicie o jogo:
    ```bash
    python game.py
    ```

---

## 📁 Estrutura de Pastas
- `/assets`: Arquivos que o jogo utiliza (caixa.png, coracao.png).
- `/assets_brutos`: Onde você coloca seus arquivos originais.
- `processor.py`: O "motor" de automação.
- `game.py`: O código principal do jogo.

---

## 📄 Licença
Este projeto está sob a licença MIT. 

---
**Desenvolvido por Maria**
