import csv
from insertData import *
from joinLib import *

# Functions.

def userAlphabeticalOrder():

  users = read_csv("usuarios.csv")
  # Order of sorting.
  users = sorted(users, key=lambda user: user["Nome"])
  users = sorted(
      users,
      key=lambda dptmnt: joinDepartamentoToUsuarios(dptmnt["Departamento"]))

  print("ID | Usuário | Computador | Departamento")
  for i in users:
    # if "Nome" in i:
    print(
        f"{i['ID']}, {i['Nome']}, {joinInventarioToUsuarios(i['Computador'])[0]}, {joinDepartamentoToUsuarios(i['Departamento'])}"
    )

def priorityOrder():

  requests = read_csv("chamados.csv")

  print("ID | Usuário | Problema | Prioridade")

  reorderedList = [request for request in requests if request["Prioridade"] == "Baixa"]
  reorderedList += [request for request in requests if request["Prioridade"] == "Normal"]
  reorderedList += [request for request in requests if request["Prioridade"] == "Alta"]

  for i in reorderedList:
    print(f"{i['ID']}, {joinUsuariosToChamados(i['Usuario'])[0]}, {i['Problema']}, {i['Prioridade']}")

def userMostRequests():

  requests = read_csv("chamados.csv")
  listUsers = []

  for chamadosData in requests:

    user, _, _ = joinUsuariosToChamados(chamadosData["Usuario"])
    listUsers.append(user)

  count = 0
  mostFrequent = listUsers[0]

  for user in listUsers:
    currentAmount = listUsers.count(user)
    if currentAmount > count:
      count = currentAmount
      mostFrequent = user

  print(mostFrequent + ".")

def amountRequestsPerDptm():

  counterCompras = 0
  counterFaturamento = 0
  counterProducao = 0
  counterRH = 0
  counterTI = 0

  for chamadosData in read_csv("chamados.csv"):

    nome, computador, departamento = joinUsuariosToChamados(
        chamadosData['Usuario'])
    # print(nome, computador, departamento)

    if departamento == "Compras":
      counterCompras += 1
    elif departamento == "Faturamento":
      counterFaturamento += 1
    elif departamento == "Produção":
      counterProducao += 1
    elif departamento == "RH":
      counterRH += 1
    elif departamento == "TI":
      counterTI += 1

  print(
      f"Compras: {counterCompras}, Faturamento: {counterFaturamento}, Produção: {counterProducao}, RH: {counterRH}, TI: {counterTI}."
  )

# Executing

def main():
  print("- Relação de todos os usuários por departamento em ordem alfabética.")
  print()
  userAlphabeticalOrder()
  print()
  
  print(
      "- Relação de todos os chamados por grau de prioridade de atendimento (baixa, normal ou alta)."
  )
  print()
  priorityOrder()
  print()
  
  print("- Quem foi o usuário que abriu mais chamados e em que quantidade?")
  print()
  userMostRequests()
  print()
  
  print("- Quantidade de chamados por departamento.")
  print()
  amountRequestsPerDptm()

# Testing

# for i in read_csv("inventario.csv"):
#   if "SO" in i:
#     print(joinSOToInventario(i["SO"]))

# print()

#for i in read_csv("chamados.csv"):
#    if "Usuario" in i:
#      print(f"{i['ID']}, {joinUsuariosToChamados(i['Usuario'])}, {i['Problema']}, {i['Prioridade']}")

if __name__ == "__main__":
  main()
else:
  print("Running from import.")