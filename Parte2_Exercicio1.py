#=============================
# Exercício 1 — Enquete curta com validação e funções
#=============================
OPCAO4 = "AlmaLinux"

def mostrar_menu():
    print("=" * 40)
    print("  ENQUETE — SISTEMAS DE SERVIDOR")
    print("=" * 40)
    print("  1 - Windows Server 2022")
    print("  2 - Ubuntu Server")
    print("  3 - Red Hat Enterprise Linux (RHEL)")
    print(f"  4 - {OPCAO4}")
    print("  0 - Encerrar votação")
    print("=" * 40)


def voto_valido(voto):
    if voto >= 0 and voto <= 4:
        return True
    else:
        return False
    
votos_1 = 0
votos_2 = 0
votos_3 = 0
votos_4 = 0
total_votos = 0

print("\nBem-vindo ao sistema de enquete de servidores!")
print("Vote no sistema operacional de sua preferência.\n")


continuar = True
while continuar:
    mostrar_menu()
    try:
        voto = int(input("\nDigite o número da sua escolha: "))
    except ValueError:
        print("Entrada inválida! Digite um número.")
        continue

    if not voto_valido(voto):
        print("Opção fora do intervalo! Tente novamente.")
    elif voto == 0:
        continuar = False
    elif voto == 1:
        votos_1 = votos_1 + 1
        total_votos = total_votos + 1
        print("Voto registrado: Windows Server 2022")
    elif voto == 2:
        votos_2 = votos_2 + 1
        total_votos = total_votos + 1
        print("Voto registrado: Ubuntu Server")
    elif voto == 3:
        votos_3 = votos_3 + 1
        total_votos = total_votos + 1
        print("Voto registrado: Red Hat Enterprise Linux (RHEL)")
    else:
        votos_4 = votos_4 + 1
        total_votos = total_votos + 1
        print(f"Voto registrado: {OPCAO4}")

print("\n" + "=" * 40)
print("  RESULTADO FINAL")
print("=" * 40)
print(f"  Windows Server 2022 : {votos_1} voto(s)")
print(f"  Ubuntu Server       : {votos_2} voto(s)")
print(f"  RHEL                : {votos_3} voto(s)")
print(f"  {OPCAO4}            : {votos_4} voto(s)")
print(f"  Total geral         : {total_votos} voto(s)")
print("=" * 40)


