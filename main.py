from random import randrange
'''
VARIÁVEIS
'''

profissoes = [
  "APICULTOR", "BARTENDER", "CERIMONIALISTA", "DESPACHANTE",
  "ENDOCRINOLOGISTA", "PERITO", "QUIROPRATA", "ROTEIRIZADOR", "SILVICULTOR",
  "TRADER"
]

animais = [
  'ALBATROZ', 'BACALHAU', 'CHINCHILA', 'ESCARAVELHO', 'HAMSTER', 'LHAMA',
  'MARRECO', 'PELICANO', 'QUATI', 'SURUCUCU'
]

objetos = [
  'ANZOL', 'CANDELABRO', 'ECHARPE', 'FANTOCHE', 'GUIDOM', 'MOUSE', 'NAVALHA',
  'SELIM', 'TECLADO', 'VUVUZELA'
]

frutas = [
  'ABACATE', 'BANANA', 'CIRIGUELA', 'FRAMBOESA', 'GOIABA', 'KIWI', 'LARANJA',
  'MELANCIA', 'TANGERINA', 'UVA'
]

aleatorio = [
  "AZULEJO", "BLITZ", "CATARRO", "DUPLEX", "GIRAR", "HERA", "INTRIGANTE",
  "JAZZ", "MARFIM", "XILOFONE"
]

nomes = [
  "ALINE", "BRENDA", "CLARISSA", "DIOGO", "EVARISTO", "FERNANDO", "GIOVANNA",
  "HELENA", "RODRIGO", "ZUMIRA"
]

validos = [
  "A", "B", "C", "D", "E", "F", "H", "H", "I", "J", "K", "L", "M", "N", "O",
  "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

tema = None
palavra = None
letra = None
acertos = 0
erros = 0
letras = []
global palavra_atual
'''
FUNÇÕES
'''


# Escolhe aleatoriamente a palavra do jogo a partir do tema escolhido pelo usuário
def escolhe_palavra(tema):
  if tema == 1: palavra = profissoes[randrange(10)]
  elif tema == 2: palavra = animais[randrange(10)]
  elif tema == 3: palavra = objetos[randrange(10)]
  elif tema == 4: palavra = frutas[randrange(10)]
  elif tema == 5: palavra = aleatorio[randrange(10)]
  elif tema == 6: palavra = nomes[randrange(10)]

  return palavra


# Mostra a palavra atual ao usuário e verifica se a letra escolhida está certa
def mostra_palavra(palavra, acertos, letras):
  palavra_print = " "
  if acertos == 0:
    for i in range(len(palavra)):
      palavra_print += palavra_atual[i] + ""
    print("A palavra é:", palavra_print)
  else:
    for i in range(len(palavra)):
      if palavra[i] == letras[-1]:
        palavra_atual[i] = letras[-1]
    for i in range(len(palavra)):
      palavra_print += palavra_atual[i] + ""
    print("A palavra é:", palavra_print)


# Verifica se o jogo acabou e diz se o usuário ganhou ou perdeu
def verifica_final(palavra, erros):
  if "_" not in palavra_atual:
    print("\n" * 3 + "PARABÉNS, VOCÊ GANHOU!!")
    print("A palavra era:", palavra)
    print("Fim de jogo.")
    return True
  elif erros >= 6:
    print("\n" * 3 + "Que pena, você perdeu :(")
    print("A palavra era:", palavra)
    print("Fim de jogo.")
    return True

  return False


'''
INÍCIO DO JOGO
'''

# Mostra o cabeçalho do jogo
print("""
<--- BEM VINDO À FORCA.PY --->

OBSERVAÇÕES:
- Qualquer caracter digitado que não seja uma letra maiúscula será considerado inválido.
- Cada tema tem 10 palavras diferentes de onde uma é escolhida aleatoriamente.

Temos vários temas diferentes, escolha um:
1 - Profissões
2 - Animais
3 - Objetos
4 - Frutas
5 - Aleatório
6 - Nomes
""")

# Pede o tema ao usuário
tema = int(input("Digite o número correspondente ao tema escolhido: "))

# Escolhe a palavra
palavra = escolhe_palavra(tema)
palavra_atual = ["_" for i in range(len(palavra))]

# Abre o loop do jogo
while True:
  print("\n" * 3)

  # Imprime a palavra atual
  mostra_palavra(palavra, acertos, letras)

  # Checa se o usuário ganhou ou perdeu
  if verifica_final(palavra, erros):
    break

  # Pede uma letra ao usuário
  letra = input("Digite uma letra: ")

  # Checa se o input é válido, se não pede outro
  if len(letra) != 1 or letra not in validos:
    print("Input inválido, por favor tente novamente.")
    continue

  # Checa se a letra já foi escolhida antes. Se sim, pede outra
  if letra in letras:
    print(f"A letra {letra} já foi escolhida, por favor tente novamente.")
    continue
