import csv

# Add data and Create CSV Files.

dataSO = [{
    "ID": 1,
    "SO": "Windows"
}, {
    "ID": 2,
    "SO": "Linux"
}, {
    "ID": 3,
    "SO": "Xenix"
}, {
    "ID": 4,
    "SO": "MacOS"
}]

dataInventario = [{
    "ID": 1,
    "Computador": "NTRJ001",
    "SO": 1
}, {
    "ID": 2,
    "Computador": "DTRJ002",
    "SO": 2
}, {
    "ID": 3,
    "Computador": "DTRJ003",
    "SO": 1
}, {
    "ID": 4,
    "Computador": "NTRJ004",
    "SO": 1
}, {
    "ID": 5,
    "Computador": "NTSP005",
    "SO": 2
}, {
    "ID": 6,
    "Computador": "NTRJ006",
    "SO": 1
}, {
    "ID": 7,
    "Computador": "DTRJ007",
    "SO": 3
}, {
    "ID": 8,
    "Computador": "DTRJ008",
    "SO": 1
}, {
    "ID": 9,
    "Computador": "NTRJ009",
    "SO": 4
}, {
    "ID": 10,
    "Computador": "NTSP0010",
    "SO": 2
}]

# Required
dataUsuarios = [{
    "ID": 1,
    "Nome": "João",
    "Computador": 1,
    "Departamento": 1
}, {
    "ID": 2,
    "Nome": "Paulo",
    "Computador": 2,
    "Departamento": 2
}, {
    "ID": 3,
    "Nome": "Pedro",
    "Computador": 3,
    "Departamento": 3
}, {
    "ID": 4,
    "Nome": "Maria",
    "Computador": 4,
    "Departamento": 4
}, {
    "ID": 5,
    "Nome": "Flavia",
    "Computador": 5,
    "Departamento": 3
}, {
    "ID": 6,
    "Nome": "Andreia",
    "Computador": 6,
    "Departamento": 2
}, {
    "ID": 7,
    "Nome": "Carmen",
    "Computador": 7,
    "Departamento": 5
}, {
    "ID": 8,
    "Nome": "Judite",
    "Computador": 8,
    "Departamento": 4
}, {
    "ID": 9,
    "Nome": "Gloria",
    "Computador": 9,
    "Departamento": 2
}, {
    "ID": 10,
    "Nome": "Andre",
    "Computador": 10,
    "Departamento": 2
}]

# Required
dataDepartamentos = [{
    "ID": 1,
    "Departamento": "TI"
}, {
    "ID": 2,
    "Departamento": "Compras"
}, {
    "ID": 3,
    "Departamento": "Faturamento"
}, {
    "ID": 4,
    "Departamento": "RH"
}, {
    "ID": 5,
    "Departamento": "Produção"
}]

# Required
dataChamados = [{
    "ID": 1,
    "Usuario": 1,
    "Problema": "Bug",
    "Prioridade": "Baixa"
}, {
    "ID": 2,
    "Usuario": 2,
    "Problema": "Error 404",
    "Prioridade": "Alta"
}, {
    "ID": 3,
    "Usuario": 3,
    "Problema": "Bug",
    "Prioridade": "Baixa"
}, {
    "ID": 4,
    "Usuario": 4,
    "Problema": "Error 134",
    "Prioridade": "Normal"
}, {
    "ID": 5,
    "Usuario": 5,
    "Problema": "Bug",
    "Prioridade": "Normal"
}, {
    "ID": 6,
    "Usuario": 6,
    "Problema": "Error 404",
    "Prioridade": "Alta"
}, {
    "ID": 7,
    "Usuario": 7,
    "Problema": "Bug",
    "Prioridade": "Baixa"
}, {
    "ID": 8,
    "Usuario": 8,
    "Problema": "Error 23",
    "Prioridade": "Baixa"
}, {
    "ID": 9,
    "Usuario": 9,
    "Problema": "Bug",
    "Prioridade": "Normal"
}, {
    "ID": 10,
    "Usuario": 10,
    "Problema": "Error 43",
    "Prioridade": "Alta"
}, {
    "ID": 11,
    "Usuario": 3,
    "Problema": "Error 404",
    "Prioridade": "Alta"
}, {
    "ID": 12,
    "Usuario": 4,
    "Problema": "Bug",
    "Prioridade": "Baixa"
}, {
    "ID": 13,
    "Usuario": 3,
    "Problema": "Bug",
    "Prioridade": "Baixa"
}, {
    "ID": 14,
    "Usuario": 7,
    "Problema": "Error 32",
    "Prioridade": "Normal"
}]



with open("so.csv", mode="w", newline="") as csvfile:

  header = ["ID", "SO"]

  write_csv = csv.DictWriter(csvfile, fieldnames=header)
  write_csv.writeheader()
  write_csv.writerows(dataSO)

with open("inventario.csv", mode="w", newline="") as csvfile:

  header = ["ID", "Computador", "SO"]

  write_csv = csv.DictWriter(csvfile, fieldnames=header)
  write_csv.writeheader()
  write_csv.writerows(dataInventario)

with open("usuarios.csv", mode="w", newline="") as csvfile:

  header = ["ID", "Nome", "Computador", "Departamento"]

  write_csv = csv.DictWriter(csvfile, fieldnames=header)
  write_csv.writeheader()
  write_csv.writerows(dataUsuarios)

with open("departamentos.csv", mode="w", newline="") as csvfile:

  header = ["ID", "Departamento"]

  write_csv = csv.DictWriter(csvfile, fieldnames=header)
  write_csv.writeheader()
  write_csv.writerows(dataDepartamentos)

with open("chamados.csv", mode="w", newline="") as csvfile:

  header = ["ID", "Usuario", "Problema", "Prioridade"]

  write_csv = csv.DictWriter(csvfile, fieldnames=header)
  write_csv.writeheader()
  write_csv.writerows(dataChamados)