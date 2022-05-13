import Bloco
import Cadeia
import transacao
from random import randint

b1 = Bloco.Bloco()
b2 = Bloco.Bloco()
b3 = Bloco.Bloco()
b4 = Bloco.Bloco()
b5 = Bloco.Bloco()

blocos = [b1, b2, b3, b4, b5]
pessoas = ['Ramão', 'Mateus', 'Eduardo', 'Analice', 'Diego']
valores = [50, 100, 300, 500, 750, 1000]
transacoes = []

for i in range(0, 20):
    nome1 = pessoas[randint(0, len(pessoas)-1)]
    pessoas.remove(nome1)
    nome2 = pessoas[randint(0, len(pessoas)-1)]
    pessoas.append(nome1)
    transacoes.append(transacao.Transacao(nome1, nome2, valores[randint(0, len(valores)-1)]))
    blocos[randint(0, len(blocos)-1)].addTransacao(transacoes[-1])

blockchain = Cadeia.Cadeia()

for i in range(0, 5):
    blockchain.adicionarBloco(blocos[i])

print("___________________________________________________________")
print("Bloco 1:", blocos[0].getTransacoesEmString())
print()
print("Bloco 2:", blocos[1].getTransacoesEmString())
print()
print("Bloco 3:", blocos[2].getTransacoesEmString())
print()
print("Bloco 4:", blocos[3].getTransacoesEmString())
print()
print("Bloco 5:", blocos[4].getTransacoesEmString())
print("___________________________________________________________")

for indice in range(1,blockchain.getTotal()+1):
    blocoX = blockchain.getBloco(indice)
    if indice < 2:
        print("Bloco", indice, "hash:", blocoX.getHash(), "| Hash anterior:")
    else:
        print("Bloco", indice, "hash:", blocoX.getHash(), "| Hash anterior:"+blocoX.getBlocoAnterior().getHash())

print("___________________________________________________________")

print("\n*****Validação antes de modificar:")
blockchain.verificaCadeia(blockchain)

print("\n*****Modificação por um ataque!")
blockchain.getBloco(3).getTransacoes()[0].valor = "10000"

print("\n*****Validação depois de modificar:")
blockchain.verificaCadeia(blockchain)
