class CuentaBancaria:
    def __init__(self, titular, numeroCuenta, saldo=0.0, tipoInteres=0.015):
        self.titular = titular
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo
        self.tipoInteres = tipoInteres

    
    def getTitular(self):
        return self.titular

 
    def setTitular(self, titular):
        self.titular = titular


    def getNumeroCuenta(self):
        return self.numeroCuenta


    def setNumeroCuenta(self, numeroCuenta):
        self.numeroCuenta = numeroCuenta

    # Getter para saldo
    def getSaldo(self):
        return self.saldo

   
    def setSaldo(self, saldo):
        self.saldo = saldo

   
    def getTipoInteres(self):
        return self.tipoInteres

  
    def setTipoInteres(self, tipoInteres):
        if 0 <= tipoInteres <= 0.1:
            self.tipoInteres = tipoInteres
        else:
            print("Interés inválido")

 
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
        else:
            print("Cantidad inválida para ingresar.")

 
    def retirar(self, cantidad):
        if cantidad > 0 and self.saldo >= cantidad:
            self.saldo -= cantidad
        else:
            print("Cantidad inválida para retirar o saldo insuficiente.")

  
    def calcularInteres(self):
        if self.saldo >= 0:
            return self.saldo * self.tipoInteres
        else:
            print("Saldo negativo. No se puede calcular el interés.")
            return 0.0
