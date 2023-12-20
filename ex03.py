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

class Horista(EmpDomestica):
    def __init__(self, nome, telefone, horasTrabalhadas, valorHora):
        super().__init__(nome, telefone)
        self.__horasTrabalhadas = horasTrabalhadas
        self.__valorHora = valorHora

    @property
    def horasTrabalhadas(self):
        return self.__horasTrabalhadas
    
    @property
    def valorHora(self):
        return self.__valorHora
    
    @horasTrabalhadas.setter
    def horasThabalhadas(self, horasTrabalhadas):
        self.horasTrabalhadas = horasTrabalhadas

    @valorHora.setter
    def valorHora(self, valorHora):
        self.__valorHora = valorHora

    def calculaSalario(self):
        salMensal = self.__horasTrabalhadas * self.__valorHora
        return salMensal
    
class Diarista(EmpDomestica):
    def __init__(self, nome, telefone, diasTrabalhados, valorDia):
        super().__init__(nome, telefone)
        self.__diasTrabalhados = diasTrabalhados
        self.__valorDia = valorDia

    @property
    def diasTrabalhados(self):
        return self.__diasTrabalhados
    
    @property
    def valorDia(self):
        return self.__valorDia
    
    @diasTrabalhados.setter
    def diasTrabalhados(self, diasTrabalhados):
        self.diasTrabalhados = diasTrabalhados

    @valorDia.setter
    def valorDia(self, valorDia):
        self.valorDia = valorDia

    def calculaSalario(self):
        salMensal = self.__diasTrabalhados * self.__valorDia
        return salMensal
    
class Mensalista(EmpDomestica):
    def __init__(self, nome, telefone, salario):
        super().__init__(nome, telefone)
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        self.salario = salario

    def calculaSalario(self):
        return self.salario

def empMenorSalario(empregadas):
    menor_salario = float('inf') #variávem inicializada com valor infinito
    emp_menor_salario = None

    for emp in empregadas: #emp representa cada empregada da lista empregadas
        salario = emp.calculaSalario() #chamado para calcular o salário da empregada atual (emp)
        if salario < menor_salario:
            menor_salario = salario
            emp_menor_salario = emp

    return emp_menor_salario

if __name__=="__main__":
    emp1 = Horista('Maria', 995623547, 160, 12)
    emp2 = Diarista('Joana', 997458263, 20, 65)
    emp3 = Mensalista('Márcia', 995412587, 1200)
    empregadas = [emp1, emp2, emp3]
    for emp in empregadas:
        print(f'Nome: {emp.nome} - Telefone: {emp.telefone} - Salário Mensal: {emp.calculaSalario()}')

    print('Opção mais barata para a república:')
    emp_menor_salario = empMenorSalario(empregadas)#chama a função que retorna a de menor salário
    print(f'Nome: {emp_menor_salario.nome} - Telefone: {emp_menor_salario.telefone} - Salário: {emp_menor_salario.calculaSalario()}')
  
