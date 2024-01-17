from abc import ABC, abstractmethod

class EmpDomestica(ABC):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def telefone(self):
        return self.__telefone
    
    @abstractmethod
    def calculaSalario(self):
        pass

    @staticmethod
    def menorSal(empregada):
        menorSal = float('inf')
        empMenorSal = None
        for emp in empregada:
            sal = emp.calculaSalario()
            if sal < menorSal:
                menorSal = sal
                empMenorSal = emp
        return empMenorSal

class Horista(EmpDomestica):
    def __init__(self, nome, telefone, horasTrab, valorHora):
        super().__init__(nome, telefone)
        self.__horasTrab = horasTrab
        self.__valorHora = valorHora

    @property
    def horasTrab(self):
        return self.__horasTrab
    
    @property 
    def valorHora(self):
        return self.__valorHora
    
    def calculaSalario(self):
        salMensal = self.__horasTrab * self.__valorHora
        return salMensal
    
class Diarista(EmpDomestica):
    def __init__(self, nome, telefone, diasTrab, valorDia):
        super().__init__(nome, telefone)
        self.__diasTrab = diasTrab
        self.__valorDia = valorDia

    @property
    def diasTrab(self):
        return self.__diasTrab
    
    @property
    def valorDia(self):
        return self.__valorDia
    
    def calculaSalario(self):
        salMensal = self.__diasTrab * self.__valorDia
        return salMensal
    
class Mensalista(EmpDomestica):
    def __init__(self, nome, telefone, valorMensal):
        super().__init__(nome, telefone)
        self.__valorMensal = valorMensal

    @property
    def valorMensal(self):
        return self.__valorMensal
    
    def calculaSalario(self):
        salMensal = self.__valorMensal
        return salMensal
    
if __name__ == "__main__":
    emp1 = Horista("Ana Cláudia", 997582634, 160, 12)
    emp2 = Diarista("Márcia", 995871452, 20, 65)
    emp3 = Mensalista("Lúcia", 987491549, 1200)
    empregada = [emp1, emp2, emp3]
    for emp in empregada:
        print(f'Nome: {emp.nome} - Telefone: {emp.telefone} - Salário Mensal: {emp.calculaSalario()}')
    empMenorSal = EmpDomestica.menorSal(empregada)
    print(f'Menor salário:\nNome: {empMenorSal.nome} - Telefone: {empMenorSal.telefone} - Salário Mensal: {empMenorSal.calculaSalario()}')
  
