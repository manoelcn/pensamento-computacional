p1 = []
p2 = []
p3 = []

while True:
  tarefa = input("Digite a tarefa: ")
  if tarefa == "fim":
    break
  prioridade = input("Digite a prioridade da tarefa: ")
  
  if prioridade == "1":
    p1.append(tarefa)
  elif prioridade == "2":
    p2.append(tarefa)
  elif prioridade == "3":
    p3.append(tarefa)
  else:
    print("Error")

print("Tarefas de prioridade 1: ")
for x in p1:
  print(x)
  
print("Tarefas de prioridade 2: ")
for x in p2:
  print(x)
  
print("Tarefas de prioridade 3: ")
for x in p3:
  print(x)