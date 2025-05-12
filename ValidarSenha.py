import re

def validar_senha(senha):
    """
    Valida uma senha de acordo com as seguintes regras:
    - As cadeias podem conter símbolos dos alfabetos Σ (a-z), Γ (A-Z) e N (0-9).
    - Devem, obrigatoriamente, ter pelo menos um símbolo do alfabeto Γ (maiúscula) e um símbolo do alfabeto N (número).
    - Devem ter comprimento igual a 8.

    Args:
        senha (str): A string contendo a senha a ser validada.

    Returns:
        bool: True se a senha for válida, False caso contrário.
    """
    # Σ = {a, b, c, …, z}, Γ = {A, B, C, …, Z}, N = {0, 1, 2, …, 9}
    # Padrão:
    # ^                    -> Início da string
    # (?=.*[A-Z])        -> Lookahead positivo para garantir pelo menos uma letra maiúscula
    # (?=.*[0-9])        -> Lookahead positivo para garantir pelo menos um número
    # [a-zA-Z0-9]{8}     -> Exatamente 8 caracteres, que podem ser letras (maiúsculas ou minúsculas) ou números
    # $                    -> Fim da string
    padrao_senha = r"^(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8}$"

    if re.fullmatch(padrao_senha, senha):
        return True
    else:
        return False

# Exemplos de teste (conforme o documento)
if __name__ == "__main__":
    senhas_aceitas = ["518R2r5e", "F123456A", "1234567T", "ropsSoq0"]
    # "F1234567A" (rejeitada por comprimento 9)
    # "abcdefgH" (rejeitada por faltar número)
    # "1234567HI" (rejeitada por comprimento 9, e não por faltar número como o doc sugere, pois tem '1')
    # O documento diz que "1234567HI" é rejeitada por faltar número, mas ela tem o número '1'. A rejeição correta seria pelo comprimento 9.
    # Vamos usar os exemplos de rejeição e adicionar os motivos corretos.
    senhas_rejeitadas = {
        "F1234567A": "Comprimento 9 (esperado 8)",
        "abcdefgH": "Falta número",
        "1234567HI": "Comprimento 9 (esperado 8)",
        "abcdefgh": "Falta maiúscula e número",
        "ABCDEFGH": "Falta número",
        "12345678": "Falta maiúscula",
        "Abc1234": "Comprimento 7 (esperado 8)",
        "Abc123456": "Comprimento 9 (esperado 8)",
        "Abc!2345": "Contém caractere especial",
    }

    print("Testando senhas aceitas:")
    for senha_teste in senhas_aceitas:
        print(f'"{senha_teste}": {"Aceita" if validar_senha(senha_teste) else "Rejeitada"}	(Esperado: Aceita)')

    print("\nTestando senhas rejeitadas:")
    for senha_teste, motivo in senhas_rejeitadas.items():
        print(f'"{senha_teste}": {"Aceita" if validar_senha(senha_teste) else "Rejeitada"}	(Esperado: Rejeitada - {motivo})')

