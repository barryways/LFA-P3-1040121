from analizadorLexico import tokenize

class AutomataPila:
    def S0(self, stack):
        stack.append("S")
    
    def S1(self, input_str, index, stack):
        tokens = tokenize(input_str)

        for token in tokens:
            lookahead, token_type = token

            if token_type == 'STRUCT':
                top_stack = stack[-1]

                if top_stack == "S":
                    stack.pop()
                    stack.append("CBRACES_CLOSE")
                    stack.append("CBRACES_OPEN")
                    stack.append("VAR_IDENTIFIER")
                    stack.append("STRUCT")
                else:
                    raise Exception("No hay transición válida con " + top_stack + " y " + lookahead)

            elif token_type == 'VAR_IDENTIFIER':
                top_stack = stack[-1]

                if top_stack == "STRUCT" or top_stack == "VAR_IDENTIFIER":
                   
                    index += 1
                    stack.pop()  
                elif top_stack == "VAR_TYPE":
                    index+=1
                    stack.pop()
                    stack.append("VAR_IDENTIFIER")
                
                else:
                    raise Exception("No hay transición válida con " + top_stack + " y " + lookahead)

            elif token_type == 'VAR_TYPE':
                top_stack = stack[-1]

                if top_stack == "VAR_IDENTIFIER":
                    
                    index += 1
                    stack.pop() 
                elif top_stack == "CBRACES_OPEN":
                    index+=1
                    stack.pop()
                    stack.append("VAR_TYPE")
                elif top_stack == "COMMA":
                    index+=1
                    stack.pop()
                    stack.append("VAR_TYPE")
                elif top_stack == "VAR_TYPE":
                    index+=1
                    stack.pop()
                    stack.append("VAR_TYPE")
                else:
                    raise Exception("No hay transición válida con " + top_stack + " y " + lookahead)

            elif token_type == 'EQUALS':
                top_stack = stack[-1]

                if top_stack == "VAR_IDENTIFIER":
                   
                    index+=1
                    stack.pop()  
                    stack.append("EQUALS")  
                    
                else:
                    raise Exception("No hay transición válida con " + top_stack + " y " + lookahead)

            elif token_type == 'NUMBER' or token_type == 'STRING':
                top_stack = stack[-1]

                if top_stack == "EQUALS":
                
                    index += 1
                    stack.pop()  
                    if token_type == 'NUMBER':
                        index+=1
                        stack.append("NUMBER")
                    elif token_type == 'STRING':
                        index+=1
                        stack.append("STRING")
                else:
                    raise Exception("No hay transición válida con " + top_stack + " y " + lookahead)

            elif token_type == 'COMMA':
                top_stack = stack[-1]

                if top_stack == "VAR_IDENTIFIER":
                    
                    index += 1
                    stack.pop() 
                elif top_stack == 'NUMBER' or top_stack =='STRING':
                    index+=1
                    stack.pop()
                    stack.append("VAR_TYPE")
                
                else:
                    raise Exception("No hay transición válida con " + top_stack + " y " + lookahead)

            elif token_type == 'CBRACES_CLOSE':
                top_stack = stack[-1]

                if top_stack == "CBRACES_OPEN":
                   
                    index += 1
                    stack.pop()  
                elif top_stack == "COMMA":
                    stack.pop()
                    index+=1
                    stack.append("VAR_TYPE")
                elif top_stack == "STRING" or top_stack == "NUMBER":
                    index+=1
                    stack.pop()
                else:
                   raise Exception("No hay transición válida con " + top_stack + " y " + lookahead)
            elif token_type == 'CBRACES_OPEN':
                top_stack = stack[-1]

                if top_stack == "VAR_IDENTIFIER":
                   
                    index += 1
                    stack.pop()  
                else:
                   raise Exception("No hay transición válida con " + top_stack + " y " + lookahead + "cbracesopen")
            elif token_type == 'VAR_TYPE':
                top_stack = stack[-1]

                if top_stack == "VAR_IDENTIFIER":
                  
                    index += 1
                    stack.pop() 
                
                else:
                   raise Exception("No hay transición válida con " + top_stack + " y " + lookahead + "el erro va aca")

            else:
                raise Exception("El token: " + lookahead + " no pertenece al alfabeto")


        return index

    
    def S2(self, index, contador):
        
        if index != contador:  
            raise Exception("Símbolos pendientes de consumir cadena no aceptada")
        
    
    def esAceptada(self, input_str, contador):
        cadena_aceptada = False
        index = 0
        stack = []

        try:
            self.S0(stack)
            index = self.S1(input_str, index, stack)
            self.S2( index, contador)
            cadena_aceptada = True
        except Exception as e:
            print(e)

        return cadena_aceptada