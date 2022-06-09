
class Vyraz:

    def Validuj(self,vyraz):
        return True

    def Vypocitej(self,vyraz):
        if self.Validuj(vyraz):
            return eval(vyraz)
        return 0


    