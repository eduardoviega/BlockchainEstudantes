import Bloco

class Cadeia:
    def __init__(self):
        self.primeiroBloco = None
        self.ultimoBloco = None
        self.total = 0

    def estaVazia(self):
        return self.primeiroBloco == None and self.ultimoBloco == None

    def adicionarBloco(self, bloco):
        if self.estaVazia():
            bloco.minerar("")
            self.ultimoBloco = bloco
            self.primeiroBloco = bloco
        else:
            bloco.setBlocoAnterior(self.ultimoBloco)
            bloco.minerar(bloco.getBlocoAnterior().getHash())
            self.ultimoBloco = bloco
        self.total += 1

    def getTotal(self):
        return self.total

    def getUltimoBloco(self):
        return self.ultimoBloco

    def getBloco(self, indice):
        bloco = self.getUltimoBloco()
        for i in range(self.getTotal(), indice,-1):
            bloco = bloco.getBlocoAnterior()
        return bloco

    def verificaCadeia(self, blockchain):
        blocoAtual = Bloco.Bloco()
        for i in range(1, blockchain.getTotal()+1):
            blocoAtual = blockchain.getBloco(i)
            if i < 2:
                if blocoAtual.getHash() != blocoAtual.calculaHash(""):
                    print("Hash do bloco ", i, " não é válida!")
                    return False
                else:
                    print("Hash do bloco ", i, " é válida!")
            else:
                if blocoAtual.getHash() != blocoAtual.calculaHash(blocoAtual.getBlocoAnterior().getHash()):
                    print("Hash do bloco ", i, " não é válida!")
                    return False
                else:
                    print("Hash do bloco ", i, " é válida!")
        return True
