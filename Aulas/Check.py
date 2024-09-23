# -dir, hasattr e getattr em Python

string = "VICTOR"
metodo = "upper"

if hasattr(string, metodo):
    print(f"Existe {metodo}")
    print(getattr(string, metodo)())
else:
    print("Não existe o método", metodo)
