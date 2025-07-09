import random
opcoes = ['pedra', 'papel', 'tesoura']
humano = 0
pc = 0

while True:
  jogada_humano = input('Digite: pedra, papel ou tesoura: ').lower()
  if jogada_humano == 'sair':
    break
  sortear = random.randint(0,2)
  jogada_pc = opcoes[sortear]
  print(f"Pc jogou {jogada_pc}")
  
  if jogada_humano == jogada_pc:
    print("Empate!")
  
  elif jogada_humano == 'pedra' and jogada_pc == 'tesoura':
    print('Humano ganhou!')
    humano = humano + 1
    print(f'Vitórias do humano {humano}')
    print(f'Vitórias do pc {pc}')
  
  elif jogada_humano == 'papel' and jogada_pc == 'pedra':
    print('Humano ganhou!')
    humano = humano + 1
    print(f'Vitórias do humano {humano}')
    print(f'Vitórias do pc {pc}')
    
  elif jogada_humano == 'tesoura' and jogada_pc == 'papel':
    print('Humano ganhou!')
    humano = humano + 1
    print(f'Vitórias do humano {humano}')
    print(f'Vitórias do pc {pc}')
    
  else:
    print('Pc ganhou!')
    pc = pc + 1
    print(f'Vitórias do humano {humano}')
    print(f'Vitórias do pc {pc}')