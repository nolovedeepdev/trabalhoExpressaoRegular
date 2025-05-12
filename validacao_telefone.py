import re

def validar_telefone(telefone):
    """
    Valida um número de telefone de acordo com os formatos:
    - (xx) 9xxxx-xxxx
    - (xx) 9xxxxxxxx
    - xx 9xxxxxxxx
    """
    padroes = [
        r"^\(\d{2}\) 9\d{4}-\d{4}$",  # (xx) 9xxxx-xxxx
        r"^\(\d{2}\) 9\d{8}$",        # (xx) 9xxxxxxxx
        r"^\d{2} 9\d{8}$"             # xx 9xxxxxxxx
    ]

    return any(re.fullmatch(p, telefone) for p in padroes)

if __name__ == "__main__":
    telefones_aceitos = ["(91) 99999-9999", "(91) 999999999", "91 999999999"]
    telefones_rejeitados = {
        "(91) 59999-9999": "Número não inicia com 9",
        "99 99999-9999": "Formato inválido (hífen inesperado ou falta de parênteses)",
        "(94)95555-5555": "Falta espaço após DDD",
        "(91)999999999": "Falta espaço após DDD",
        "91999999999": "Falta espaço após DDD",
        "(91) 99999-999": "Número incompleto (última parte curta)",
        "(91) 9999-99999": "Formato inválido (partes desbalanceadas)",
        "(91) 99999999": "Número curto",
        "(91) 9999999999": "Número longo",
        "91 99999999": "Número curto",
        "91 9999999999": "Número longo",
        "(9a) 99999-9999": "DDD com letra",
        "(91) a9999-9999": "Número com letra",
        "(91) 99999-999X": "Letra no final do número"
    }

    print("Testando telefones aceitos:")
    for telefone in telefones_aceitos:
        resultado = "Aceito" if validar_telefone(telefone) else "Rejeitado"
        print(f'"{telefone}": {resultado} (Esperado: Aceito)')

    print("\nTestando telefones rejeitados:")
    for telefone, motivo in telefones_rejeitados.items():
        resultado = "Aceito" if validar_telefone(telefone) else "Rejeitado"
        print(f'"{telefone}": {resultado} (Esperado: Rejeitado - {motivo})')
