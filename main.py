import requests
import os

print("Bem-vindo ao Verificador de Sites 1.0!")

count = "s"
url=[]

while count == "s" or count == "S":
  print("Insira as URLs dos sites que deseja verificar o status.\n(separadas por vírgula)\n")
  
  url = input().split(",")

  print("\n")
  
  for i in url:
    i = i.strip()
    try:
      if ("http" or "https") not in i:
        r = requests.get("https://" + i) #requests.get() retorna um objeto Response
        if r.status_code in {200, 404, 403}: #r.status_code retorna inteiro /// r.ok retorna boolean
          print("https://" + i, "Site online.")
      else:
        r = requests.get(i)
        if r.status_code in {200, 404, 403}:
          print(i, "Site online.")
    except:
      print(i, "URL inválida")

  count = "z"
  while count not in {'s', 'S', 'n', 'N'}:
    count = input("Precisa verificar mais algum site? (s/n) ")
    if count in {'n', 'N'}:
       print("\nPrograma Encerrado!!!")
    elif count in {'s', 'S'}:
      # Clearing the Screen
      os.system('clear')
    else:
      print("\nOpção inválida!")
