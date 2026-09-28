import os
from datetime import datetime
data_hora_formatada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(data_hora_formatada)

#ARQUIVO 82731642-736
validation = "2231339632391.34861094762020439.08641992496804839.21391239813027020.376964254179866.00481775527371685.90531400694262289.09621094762020439.08641992496804839.21391239813027020.3761775527371685.9053"
#SENHA = "encryption72#"
Key = "90760934835506.66155176116704544.7280042765833238.47194218544003003.47282424774470303.06173777251919546.62216644894613610.62115846591637596.31164255394863536.66155176116704544.721992496804839.21391094762020439.0864116423862490.77095"
Arquivo_valido = []

def powerHasher(txtToHash):

    newTxt = "".join([str(((ord(x) * ord(x)) * 2.718281828459045) ** 3.141592653589793) for x in txtToHash])
    print(newTxt)
    return newTxt

def hashCheck():
    # Diretório onde os arquivos estão localizados
    diretorio = 'file'
    
    # Verificar se o diretório existe
    if not os.path.exists(diretorio):
        print(f"O diretório {diretorio} não existe.")
        return
    arquivos = os.listdir(diretorio)

    # Verificar se há arquivos no diretório
    if not arquivos:
        print("Nenhum arquivo encontrado no diretório.")
        return

    # Escolher um arquivo aleatório
    arquivo_escolhido = input("\nESCOLHA UM ARQUIVO:\n")
    try:
        with open(os.path.join(diretorio, arquivo_escolhido), "r", encoding="utf-8") as arquivo:
            hashfied = (arquivo.readline()).strip()
            hashfied = powerHasher(hashfied)
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")
        return
    
    if  hashfied == validation:
        print("\nArquivo escolhido é válido para apuração!")
        tentativas = 3
        while tentativas > 0:
            print(f"VOCÊ TEM {tentativas} TENTATIVAS PARA ACESSAR O ARQUIVO.")
            senha = input("\nDIGITE A SENHA DE SEGURANÇA:\n")
            if powerHasher(senha) == Key:
                Arquivo_valido.append(arquivo_escolhido)
                print("Senha válida!")
                with open(f"file/"+arquivo_escolhido, 'a') as arquivo:
                    arquivo.write("241209795436649.1290760934835506.66194218544003003.47115846591637596.3196556928224662.19115846591637596.3180042765833238.4770409510219590.77216644894613610.62115846591637596.31164255394863536.66155176116704544.72")
                for arquivo in arquivos:
                    if arquivo != arquivo_escolhido:
                        os.remove(os.path.join(diretorio, arquivo))
                break
                
                        
            else:
                tentativas -= 1
                print("\nSENHA INVALIDA!")
                if tentativas == 0:
                    for arquivo in arquivos:
                        try:
                            os.remove(os.path.join(diretorio, arquivo))
                            print(f"Arquivo removido: {arquivo}")
                        except Exception as e:
                            print(f"Erro ao remover o arquivo {arquivo}: {e}")
                
                             
    else:
        for arquivo in arquivos:
            try:
                os.remove(os.path.join(diretorio, arquivo))
                print(f"Arquivo removido: {arquivo}")
            except Exception as e:
                print(f"Erro ao remover o arquivo {arquivo}: {e}")

hashCheck()
