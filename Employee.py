class Employee:
    def __init__(self, id:int , first_name:str , last_name:str , salary:int ):
        self.id = id
        self.salary = salary
        self.first_name = first_name
        self.last_name =last_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_annual_salary(self):
        total_salary = 12 * self.salary
        return total_salary
    
    def raise_salary(self,amount):
        self.salary = self.salary + amount
        return self.salary
