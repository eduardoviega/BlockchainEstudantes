class Transacao:
    def __init__(self, _de, _para, _valor):
        self.de = _de
        self.para = _para
        self.valor = _valor

    def toString(self):
        return "De:"+self.de+" Para:"+self.para+" Valor:"+str(self.valor)+";  "