import re

def validar_cpf(cpf):
    """
    Valida um CPF de acordo com as seguintes regras:
    - As cadeias devem ter o formato xxx.xxx.xxx-xx, onde x ∈N (0-9).

    Args:
        cpf (str): A string contendo o CPF a ser validado.

    Returns:
        bool: True se o CPF for válido, False caso contrário.
    """
    # N = {0, 1, 2, …, 9}
    # Padrão:
    # ^                 -> Início da string
    # \d{3}            -> Exatamente três dígitos
    # \.                -> Literalmente um ponto
    # \d{3}            -> Exatamente três dígitos
    # \.                -> Literalmente um ponto
    # \d{3}            -> Exatamente três dígitos
    # -                 -> Literalmente um hífen
    # \d{2}            -> Exatamente dois dígitos
    # $                 -> Fim da string
    padrao_cpf = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"

    if re.fullmatch(padrao_cpf, cpf):
        return True
    else:
        return False

# Exemplos de teste (conforme o documento)
if __name__ == "__main__":
    cpfs_aceitos = ["123.456.789-09", "000.000.000-00"]
    # "123.456.789-0" (rejeitada por ter apenas um dígito verificador)
    # "111.111.11-11" (rejeitada por ter apenas dois dígitos no terceiro grupo)
    cpfs_rejeitados = {
        "123.456.789-0": "Dígito verificador incompleto",
        "111.111.11-11": "Terceiro grupo de números incompleto",
        "12345678909": "Sem formatação",
        "123.456.789.09": "Ponto em vez de hífen",
        "12.345.678-90": "Primeiro grupo incompleto",
        "123.45.678-90": "Segundo grupo incompleto",
        "abc.def.ghi-jk": "Contém letras",
        "123.456.789-001": "Dígito verificador muito longo"
    }

    print("Testando CPFs aceitos:")
    for cpf_teste in cpfs_aceitos:
        print(f'"{cpf_teste}": {"Aceito" if validar_cpf(cpf_teste) else "Rejeitado"}	(Esperado: Aceito)')

    print("\nTestando CPFs rejeitados:")
    for cpf_teste, motivo in cpfs_rejeitados.items():
        print(f'"{cpf_teste}": {"Aceito" if validar_cpf(cpf_teste) else "Rejeitado"}	(Esperado: Rejeitado - {motivo})')
