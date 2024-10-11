#Por Padrão o módulo em Python é Singleton
# Modo de Recarregar o Modulo 
import importlib
import singletonTesteM as stm

print(stm.variavel)

for i in range(11):
    importlib.reload(stm)
    print(i)
print("Fim")
