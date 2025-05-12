import re

def validar_email(email):
    """
    Valida um endereço de e-mail de acordo com as seguintes regras:
    - As sentenças possuem símbolos de Σ (a-z) e deve conter exatamente um símbolo "@".
    - Não devem começar com o símbolo "@".
    - Devem terminar com a sequência ".br".
    - Devem ter, pelo menos, um símbolo de Σ entre o símbolo "@" e o ".br".

    Args:
        email (str): A string contendo o e-mail a ser validado.

    Returns:
        bool: True se o e-mail for válido, False caso contrário.
    """
    # Σ = {a, b, c, …, z}
    # Padrão:
    # ^                     -> Início da string
    # [a-z]+                -> Uma ou mais letras minúsculas (parte local antes do @)
    # @                     -> Exatamente um símbolo "@"
    # [a-z]+                -> Pelo menos uma letra minúscula (parte do domínio entre @ e .br)
    # \.br                 -> Literalmente ".br"
    # $                     -> Fim da string
    # A regra "não devem começar com o símbolo '@'" é coberta por [a-z]+ no início.
    # A regra "deve conter exatamente um símbolo '@'" é coberta pelo uso de um único '@' no padrão sem quantificadores.
    padrao_email = r"^[a-z]+@[a-z]+\.br$"

    if re.fullmatch(padrao_email, email):
        return True
    else:
        return False

# Exemplos de teste (conforme o documento)
if __name__ == "__main__":
    emails_aceitos = ["a@a.br", "divulga@ufpa.br"]
    emails_rejeitados = ["@", "a@.br", "T@teste.br", "teste@teste.com", "teste@.br", "@teste.br", "teste@teste.br.com"]

    print("Testando e-mails aceitos:")
    for email_teste in emails_aceitos:
        print(f'"{email_teste}": {"Aceito" if validar_email(email_teste) else "Rejeitado"}	(Esperado: Aceito)')

    print("\nTestando e-mails rejeitados:")
    for email_teste in emails_rejeitados:
        print(f'"{email_teste}": {"Aceito" if validar_email(email_teste) else "Rejeitado"}	(Esperado: Rejeitado)')

    # Testes adicionais
    print("\nTestes adicionais:")
    testes_extras = {
        "Correto simples": "user@domain.br",
        "Correto longo": "longusernameexample@longdomainexample.br",
        "Sem @": "userdomain.br",
        "Comeca com @": "@domain.br",
        "Termina com @": "user@",
        "Sem .br no final": "user@domain.com",
        "Sem nada entre @ e .br": "user@.br",
        "Com maiuscula antes do @": "User@domain.br", # Rejeitado pois Σ é apenas minúsculas
        "Com maiuscula depois do @": "user@Domain.br", # Rejeitado pois Σ é apenas minúsculas
        "Com numero antes do @": "user1@domain.br",
        "Com numero depois do @": "user@domain1.br",
        "Dois @": "user@@domain.br",
        "Ponto antes do @": "user.name@domain.br",
        "Ponto depois do @ (nao .br)": "user@sub.domain.br"
    }
    for descricao, email_teste in testes_extras.items():
        resultado = "Aceito" if validar_email(email_teste) else "Rejeitado"
        print(f'"{email_teste}" ({descricao}): {resultado}')

