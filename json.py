aluno=[
  {
      "nome":"Igor",
      "idade":20,
      "prontuario":"sp12345",
      "notas":{
      "portugues":6,
      "matematica":8,
      "ciencias":10,
      "media": (10+6+8)/3,
      }
  },

  {
      "nome":"Ana",
      "idade":19,
      "prontuario":"sp45678",
      "notas":{
      "portugues":10,
      "matematica":3,
      "ciencias":9,
      "media": (10+3+9)/3,
      }
  }
]

def adicionar(aluno):
  nome = input("Digite o nome do aluno: ")
  idade = int(input("Digite a idade do aluno: "))
  prontuario = input("Digite o prontuário do aluno: ")
  notas = {}
  notas["portugues"] = float(input("Digite a nota de Português: "))
  notas["matematica"] = float(input("Digite a nota de Matemática: "))
  notas["ciencias"] = float(input("Digite a nota de Ciências: "))
  notas["media"] = (notas["portugues"] + notas["matematica"] + notas["ciencias"]) / 3
  novo_aluno = {
      "nome": nome,
      "idade": idade,
      "prontuario": prontuario,
      "notas": notas
  }
  aluno.append(novo_aluno)

adicionar(aluno)
def get_aluno():
    return aluno
print(get_aluno())

