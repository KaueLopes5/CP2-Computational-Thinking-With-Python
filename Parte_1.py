#================================
# PARTE 1
#================================



def fazer_pergunta(numero):

    if numero == 1:
        pergunta = "você telefonou para a vítima?"
    elif numero == 2:
        pergunta = "você esteve no local do crime?"
    elif numero == 3:
        pergunta = "você mora perto da vítima?"
    elif numero == 4:
        pergunta = "você tinha dívidas com a vítima?"
    else:
        pergunta = "você já trabalhou com a vítima?"

    print(f"Pergunta {numero}: {pergunta}")

    resposta = ""                                    
    while resposta != "s" and resposta != "n":       
        resposta = input("Responda com s ou n: ").strip().lower()
        if resposta != "s" and resposta != "n":
            print("Resposta inválida! Digite apenas s ou n.")

    if resposta == "s":
        return 1
    else:
        return 0         

def classificar_investigado(total_sim):
    if total_sim == 0 or total_sim == 1:
        return "Inocente"
    elif total_sim == 2:
        return "Suspeita"
    elif total_sim == 3 or total_sim == 4:
        return "Cúmplice"
    else:
        return "Assassino"
    
nome_investigado = "Roberto Carlos"

print("=" * 60)
print("DELEGACIA DE HOMICÍDIOS — INTERROGATÓRIO OFICIAL")
print("=" * 60)
print(f"""
  Bom dia. O senhor {nome_investigado} está sendo interrogado
  em relação ao assassinato ocorrido na última quinta-feira.
  Por favor, responda com honestidade a cada pergunta.
  Suas respostas serão registradas e analisadas pelo sistema.
""")
print("=" * 60)

total_positivas = 0
numero_pergunta = 1

while numero_pergunta <= 5:
    resultado = fazer_pergunta(numero_pergunta)
    total_positivas = total_positivas + resultado
    numero_pergunta = numero_pergunta + 1

classificacao = classificar_investigado (total_positivas)

print("\n" + "=" * 60)
print("RESULTADO DA ANÁLISE")
print(f"\n  Investigado : {nome_investigado}")
print(f"  Respostas positivas: {total_positivas} de 5")
print(f"\n  Após analisar cuidadosamente as respostas fornecidas,")
print(f"  o investigado {nome_investigado} recebeu a seguinte")
print(f"  classificação: {classificacao}.")
print("\n" + "=" * 60)
