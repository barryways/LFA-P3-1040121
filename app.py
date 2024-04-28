### Carlos Daniel Barrientos CAstillo -1040121, le presento mi codigo ing, tal vez no sea el mejor ni el mas eficiente
### ni el mas bonito, ni el mas optimizado, pero es lo que pude hacer, y sin usar chatgpt mas que para el analizador lexico espero que sea de su agrado, y que pueda
### ser tomado en cuenta, para la evaluacion del parcial

from automataPila import AutomataPila
from analizadorLexico import tokenize

def main():
    
    automata = AutomataPila()

    
    input_str = 'struct? MyStruct { int+ var1 = 10, string+ var2 = "hello"}'
    
    tokens = tokenize(input_str)
    contador = 1
    for token in tokens:
        contador += 1
    
    if automata.esAceptada(input_str, contador):
        print(f"Cadena '{input_str}' aceptada por el autómata de pila.")
    else:
        print(f"Cadena '{input_str}' no aceptada por el autómata de pila.")



if __name__ == "__main__":
    main()