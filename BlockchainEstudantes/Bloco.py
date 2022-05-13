import hashlib
import transacao

class Bloco:
    def __init__(self):
        self.blocoAnterior = None
        self.hash = ""
        self.transacoes = []

    def getHash(self):
        return self.hash

    def setHash(self, novaHash):
        self.hash = novaHash

    def getBlocoAnterior(self):
        return self.blocoAnterior

    def setBlocoAnterior(self, bloco):
        self.blocoAnterior = bloco

    def getTransacoes(self):
        return self.transacoes

    def getTransacoesEmString(self):
        transacoesString = ""
        for t in self.getTransacoes():
            transacoesString = transacoesString + t.toString()
        return transacoesString

    def addTransacao (self, _transacao):
        self.transacoes.append(_transacao)

    def calculaHash(self, hashAnterior):
        calcHash = hashlib.sha256()
        calcHash.update((str(hashAnterior)+self.getTransacoesEmString().__str__()).encode('utf-8'))
        return calcHash.hexdigest()

    def minerar(self, hashAnterior):
        self.setHash(self.calculaHash(hashAnterior))
        print("  Bloco minerado: "+self.getHash())
