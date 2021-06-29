import json
from Token import Token
class LexAnalizer:
    console = ''
    palabra = ''
    words = []
    def startAnalize(self, code):
        self.code = code
        print(self.code)
        self.findTokens()

    def findTokens(self):
        print('iniciando metodo')
        tokens = json.load(open('tokens.json',encoding="utf8"))
        for i in range(0,len(self.code)): 
            for token in tokens["tokens"]:
                if self.code[i] == token["caracter"]:
                    if token["tipo"] == "operacion":
                        if self.palabra != '':
                            self.words.append(Token(self.palabra,'palabra'))
                        else:
                            self.palabra = token["caracter"]
                            self.words.append(Token(self.palabra,token["tipo"]))
                        self.palabra = ''
                    if token["tipo"] == "llave":
                        self.console += 'Llave encontrada \n'
                    if token["tipo"] == "numero":
                        self.console += 'Numero encontrada \n'
                    if token["tipo"] == "letra":
                        self.palabra += self.code[i]
                elif self.code[i] == ' ':
                    self.words.append(Token(self.palabra,'palabra'))
                    self.palabra = ''
                    
                
                                   

    def getResult(self):
        return str(self.console)