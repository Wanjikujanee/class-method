
class Student:
      school = "Akirachix"
      def __init__(Self,full_name,age,year_of_birth,country): 
                 Self.full_name = full_name
                 Self.year_of_birth=year_of_birth
                 Self.age = age
                 Self.country = country
     
      def full_name(self):
        return f"Hello {self.f_name} {self.l_name} is your full name"

      def initials(self):
        return f"Your initials are {self.f_name[0]} {self.l_name[0]}"

      def y_o_b(self):
        y_o_b=self.current_year-self.age
        return f" You were born in {y_o_b}"



        
