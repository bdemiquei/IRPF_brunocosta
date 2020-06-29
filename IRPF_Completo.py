class Simples:
    def _init_(self,n,cpf,c,r):
        self.n = n
        self.cpf = cpf
        self.c = c
        self.r = r
        
    def setn (self, n):
        self.n = n
        
    def setCPF (self, cpf):
        self.cpf = cpf
        
    def setc (self, c):
        self.c = c
    
    def setr (self, r):
        self.r = r
    
    def getn (self):
        return self.n
    
    def getCPF (self):
        return self.cpf
    
    def getc (self):
        return self.c
    
    def getr (self):
        return self.r

class Completo (Simples):
    
    def _init_(self,n,cpf,i,d,c,r):
        super()._init_(n,cpf,c,r)
        self.i = i
        self.d = d
        
    def setI (self,i):
        self.i = i
            
    def setD (self,d):
        self.d = d
        
    def getI (self):
        return self.i
        
    def getD (self):
        return self.d


Registro = []

continuar = 1
while continuar != 0:
    
    print ("S para cadastro simples e C para cadastro completo")

    x = input()
    
    if x.upper() == 'S':
        
        pessoa = Simples()
        pessoa.n = input("Digite seu nome: ")
        print ("")
        while 1:
                pessoa.cpf = (input("Digite seu CPF: "))
                if pessoa.cpf.isdigit() and len(pessoa.cpf) == 11 : 
                    break
                print ("CPF inválido!")
        print ("")
        
        while 1:
            try:
                pessoa.c = float(input("Digite sua contribuicao: "))
                break
            except ValueError:
                print ("contribuicao invalida!")
        print ("")
        
        while 1:
            try:
                pessoa.r = float(input("Digite sua renda: "))
                break
            except ValueError:
                print ("renda invalida!")
        print ("")
    
        Registro.append(pessoa)
    
        Base = (pessoa.r - pessoa.c) - ((pessoa.r - pessoa.c)*0.05)
    
        if Base <= 12000 :
            print ('Isento de imposto de renda')
    
        elif Base > 12000 :
            Imposto = (Base - 12000)*0.15
            if Base >= 24000 :
                Imposto = Imposto + (Base - 24000) * 0.275
        
            print ('Cálculo Imposto de renda: R$',round(Imposto,2))

    if x.upper() == 'C':
    
        pessoa = Completo()
        pessoa.n = input("Digite seu nome: ")
        print ("")
        while 1:
                pessoa.cpf = (input("Digite seu CPF: "))
                if pessoa.cpf.isdigit() and len(pessoa.cpf) == 11 : 
                    break
                print ("CPF inválido!")
        print ("")
        
        while 1:
            try:
                pessoa.c = float(input("Digite sua contribuicao: "))
                break
            except ValueError:
                print ("constribuicao invalida!")
        print ("")
        
        while 1:
            try:
                pessoa.r = float(input("Digite sua renda: "))
                break
            except ValueError:
                print ("renda invalida!")
        
        print ("")
        while 1:
            try:
                pessoa.i = int(input("Digite sua idade: "))
                break
            except ValueError:
                print ("Idade inválida!")

        print ("")
        
        while 1:
            try:
                pessoa.d = int(input("Digite numero de dependentes: "))
                break
            except ValueError:
                print ("Numero de dependentes inválido!")

        print ("")
    
        Registro.append(pessoa)
    
        Base = (pessoa.r - pessoa.c)

        if pessoa.i < 65 :
            if pessoa.d <= 2 :
                Base = Base - (Base * 0.02)
            elif pessoa.d >= 3 and pessoa.d <=5 :
                Base = Base - (Base * 0.035)
            elif pessoa.d > 5 :
                Base = Base - (Base * 0.05)
        elif pessoa.i >= 65 :
            if pessoa.d <=2 :
                Base = Base - (Base * 0.03)
            elif pessoa.d >= 3 and pessoa.d <=5 :
                Base = Base - (Base * 0.045)
            elif pessoa.d > 5 :
                Base = Base - (Base * 0.06)
    
        if Base <= 12000 :
            print ('Isento de imposto de renda')
    
        elif Base > 12000 :
            Imposto = (Base - 12000)*0.15
            if Base >= 24000 :
                Imposto = Imposto + (Base - 24000) * 0.275
            
            print ('Cálculo Imposto de renda: R$',"%.2f" % Imposto)
    
    print ("Continuar?")
    print ("  0 --> ENCERRAR")
    print ("  1 --> CONTINUAR CADASTRAMENTO")
    continuar = int(input ())