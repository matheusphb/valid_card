def identificar_bandeira(numero_cartao):
    """
    Identifica a bandeira de um cartão de crédito com base no número do cartão.

    Args:
        numero_cartao (str): Número do cartão de crédito.

    Returns:
        str: Nome da bandeira do cartão ou 'Desconhecida' se não for possível identificar.
    """
    if numero_cartao.startswith("4"):
        return "Visa"
    elif numero_cartao.startswith(("51", "52", "53", "54", "55")):
        return "MasterCard"
    elif numero_cartao.startswith("34") or numero_cartao.startswith("37"):
        return "American Express"
    elif numero_cartao.startswith("6011") or numero_cartao.startswith("65"):
        return "Discover"
    else:
        return "Desconhecida"

# Exemplo de uso
if __name__ == "__main__":
    numero = input("Digite o número do cartão de crédito: ")
    bandeira = identificar_bandeira(numero)
    print(f"A bandeira do cartão é: {bandeira}")