#=============================
#Exercício 2 — Resultado da enquete e análise do vencedor
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


def calcular_percentual(votos, total):
    if total == 0:
        return 0.0
    return (votos / total) * 100


def mostrar_resultado(nome, votos, total):
    percentual = calcular_percentual(votos, total)
    print(f"  {nome}: {votos} voto(s) ({percentual:.1f}%)")


def analisar_vencedor(v1, v2, v3, v4):
    total = v1 + v2 + v3 + v4

    if total == 0:
        print("Classificação: SEM VOTOS")
        return

    maior = v1
    if v2 > maior:
        maior = v2
    if v3 > maior:
        maior = v3
    if v4 > maior:
        maior = v4

    qtd_vencedores = 0
    if v1 == maior:
        qtd_vencedores = qtd_vencedores + 1
    if v2 == maior:
        qtd_vencedores = qtd_vencedores + 1
    if v3 == maior:
        qtd_vencedores = qtd_vencedores + 1
    if v4 == maior:
        qtd_vencedores = qtd_vencedores + 1

    if qtd_vencedores > 1:
        print(f"\nEmpate com {maior} voto(s) entre:")
        if v1 == maior:
            print("  • Windows Server 2022")
        if v2 == maior:
            print("  • Ubuntu Server")
        if v3 == maior:
            print("  • Red Hat Enterprise Linux (RHEL)")
        if v4 == maior:
            print(f"  • {OPCAO4}")
        print("Classificação: DISPUTA EQUILIBRADA")
        return

    if v1 == maior:
        nome_vencedor = "Windows Server 2022"
        segundo = v2
        if v3 > segundo:
            segundo = v3
        if v4 > segundo:
            segundo = v4
    elif v2 == maior:
        nome_vencedor = "Ubuntu Server"
        segundo = v1
        if v3 > segundo:
            segundo = v3
        if v4 > segundo:
            segundo = v4
    elif v3 == maior:
        nome_vencedor = "Red Hat Enterprise Linux (RHEL)"
        segundo = v1
        if v2 > segundo:
            segundo = v2
        if v4 > segundo:
            segundo = v4
    else:
        nome_vencedor = OPCAO4
        segundo = v1
        if v2 > segundo:
            segundo = v2
        if v3 > segundo:
            segundo = v3

    print(f"\nSistema mais votado: {nome_vencedor} com {maior} voto(s).")

    diferenca = maior - segundo
    dez_porcento = total * 0.10

    if diferenca < dez_porcento:
        print("Classificação: DISPUTA EQUILIBRADA")
    else:
        print("Classificação: VANTAGEM CLARA")


# ── Programa principal ──

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
print("  RESULTADO FINAL DA ENQUETE")
print("=" * 40)
mostrar_resultado("Windows Server 2022", votos_1, total_votos)
mostrar_resultado("Ubuntu Server", votos_2, total_votos)
mostrar_resultado("RHEL", votos_3, total_votos)
mostrar_resultado(OPCAO4, votos_4, total_votos)
print(f"  Total geral: {total_votos} voto(s)")
analisar_vencedor(votos_1, votos_2, votos_3, votos_4)
print("=" * 40)
