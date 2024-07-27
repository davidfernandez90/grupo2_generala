def validar_numero(prompt, min_val=None, max_val=None):
    while True:
        try:
            valor = int(input(prompt))
            if (min_val is not None and valor < min_val) or (max_val is not None and valor > max_val):
                print(f"Por favor, ingrese un número entre {min_val} y {max_val}.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")
