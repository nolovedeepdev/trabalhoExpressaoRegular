import re

def validar_nome(nome_completo):
    """
    Valida um nome completo de acordo com as seguintes regras:
    - Deve receber o nome e o sobrenome, ambos não vazios, separados por um espaço.
    - Não deve aceitar caracteres especiais ou numéricos.
    - O primeiro símbolo do nome e do sobrenome deve ser do alfabeto Γ (maiúsculas).
    - Os outros símbolos devem ser do alfabeto Σ (minúsculas).

    Args:
        nome_completo (str): A string contendo o nome a ser validado.

    Returns:
        bool: True se o nome for válido, False caso contrário.
    """
    # Σ = {a, b, c, …, z}, Γ = {A, B, C, …, Z}
    # Padrão: Uma letra maiúscula seguida por uma ou mais letras minúsculas (para o nome),
    # um espaço, e então uma letra maiúscula seguida por uma ou mais letras minúsculas (para o sobrenome).
    # O início (^) e o fim ($) da string são importantes para garantir que não haja caracteres extras.
    padrao_nome = r"^[A-Z][a-z]+ [A-Z][a-z]+$"
    
    if re.fullmatch(padrao_nome, nome_completo):
        return True
    else:
        return False

# Exemplos de teste (conforme o documento)
if __name__ == "__main__":
    nomes_aceitos = ["Alan Turing", "Noam Chomsky", "Ada Lovelace"]
    nomes_rejeitados = ["1Alan", "Alan", "A1an", "alan Turing", "Alan turing", "Alan Turing ", " Alan Turing"]

    print("Testando nomes aceitos:")
    for nome in nomes_aceitos:
        print(f'"{nome}": {"Aceito" if validar_nome(nome) else "Rejeitado"}')

    print("\nTestando nomes rejeitados:")
    for nome in nomes_rejeitados:
        print(f'"{nome}": {"Aceito" if validar_nome(nome) else "Rejeitado"}')

    # Testes adicionais
    print("\nTestes adicionais:")
    testes_extras = {
        "Correto": "Carlos Drummond",
        "Apenas Nome": "Carlos",
        "Nome com numero": "Carlos1 Drummond",
        "Nome com especial": "Carlos@ Drummond",
        "Sobrenome com numero": "Carlos Drumm0nd",
        "Minuscula no inicio nome": "carlos Drummond",
        "Minuscula no inicio sobrenome": "Carlos drummond",
        "Espaco extra inicio": " Carlos Drummond",
        "Espaco extra fim": "Carlos Drummond ",
        "Multiplos espacos": "Carlos  Drummond",
        "Nome composto (nao suportado pela regra atual)": "Pedro Alvares Cabral", # Rejeitado pela regra de apenas um nome e um sobrenome
        "Nome com acento (nao suportado pela regra atual)": "João Silva" # Rejeitado pois [a-z] não inclui acentos
    }
    for descricao, nome_teste in testes_extras.items():
        print(f'"{nome_teste}" ({descricao}): {"Aceito" if validar_nome(nome_teste) else "Rejeitado"}')

