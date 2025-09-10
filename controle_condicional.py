# controle_condicional.py
# Objetivo: aplicar controles condicionais (if, elif, else) e operadores lógicos

nota = 85  # exemplo de nota

# Mapear nota para conceitos
if nota >= 90:
    conceito = "A"
elif nota >= 80:
    conceito = "B"
elif nota >= 70:
    conceito = "C"
else:
    conceito = "D"

# Exemplo de operador lógico
aprovado = (nota >= 70) and True

# Exibir resultado
print("Nota:", nota)
print("Conceito:", conceito)
print("Aprovado:", aprovado)
