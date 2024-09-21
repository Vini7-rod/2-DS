print("Bem vindo ao gerenciador de tarefas")

Lista_de_tarefas = [
  [],
]

while True:
  tarefa = input(" Digite uma tarefa: ")

  data = input("Deseja adicionar um dia para essa tarefa?\n")
  if data == "sim":
   data  = input("Digite a data de vencimento:\n")
   print(tarefa + " foi marcada para o dia " + data,"\n")
  elif data == "não":
   print(tarefa + " foi adicionada com sucesso")

  prioridade = input("Deseja adicionar um marcador de prioridade?, se sim digite 'prioridade'\n")
  if prioridade == "prioridade":
   print(tarefa + " foi marcada como prioridade\n")
  elif(prioridade == "não"):
    print( tarefa + " foi adicionada com sucesso\n")

  tarefa = [tarefa, data, prioridade ]
  print(f"{tarefa},\n")

  pergunta = input("Deseja adicionar uma nova tarefa?\n")
  if pergunta == "sim":
    print("Nova tarefa criada")

  elif pergunta == "não":
   break