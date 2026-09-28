#URN,PY 
#linha 20-Comunicação tava escrito errado
#linha 22-Presidencial-tava escrito em inglês

#VALIDATION.PY
# linha 57-Senha invalida: Voce tem {tentativas}acessar arquivos
#Tava aparecendo duas vezes#

#DESCRYPTOGRAPHY.PY
#linha 15-Comunicação escrito errado

def powerHasher(txtToHash):

    newTxt = "".join([str(((ord(x) * ord(x)) * 2.718281828459045) ** 3.141592653589793) for x in txtToHash])
    print(newTxt)
    return newTxt

newInput = input()

powerHasher(newInput)

