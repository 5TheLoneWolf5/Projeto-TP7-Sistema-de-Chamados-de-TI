from insertData import *

# Joining Tables.

# Both IDs on the JOIN functions need to be converted into INT types (the IDs are coming directly from the CSV files, not the arrays).

# print(dataSO[0]["ID"])

def read_csv(file):

  with open(file, mode="r", newline="") as csvfile:

    read_csv = csv.DictReader(csvfile)

    data = list(read_csv)

  return data

def joinSOToInventario(id):

  for so in read_csv("so.csv"):
    if int(so["ID"]) == int(id):
      return so["SO"]
  return "SO não encontrado."

def joinInventarioToUsuarios(id):

  for sistema in read_csv("inventario.csv"):
    if int(sistema["ID"]) == int(id):
      return sistema["Computador"], joinSOToInventario(sistema["SO"])
  return "Sistema não encontrado."

def joinDepartamentoToUsuarios(id):

  for departamento in read_csv("departamentos.csv"):
    if int(departamento["ID"]) == int(id):
      return departamento["Departamento"]
  return "Departamento não encontrado."

def joinUsuariosToChamados(id):

  for usuario in read_csv("usuarios.csv"):
    if int(usuario["ID"]) == int(id):
      # usuario.update({"Departamento": save})
      return usuario["Nome"], joinInventarioToUsuarios(
          usuario["Computador"]), joinDepartamentoToUsuarios(
              usuario["Departamento"])
  return "Sistema não encontrado."