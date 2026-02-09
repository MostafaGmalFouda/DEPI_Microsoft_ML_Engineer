from Person import Person

class Staff(Person):
    """
    Class representing a staff member, inheriting from Person.
    
    :name: staff member's name
    :type name: str
    :age: staff member's age
    :type age: int
    :position: staff member's position
    :type position: str
    """
    def __init__(self, name: str, age: int, position: str):
        """ 
            Initialize a Staff member.
            :name: staff member's name
            :age: staff member's age
            :position: staff member's position
        """
        super().__init__(name, age)
        self.position = position

    def view_info(self) -> str:
        """
        Docstring for view_info
        
        :param self: Description
        :return: Description
        :rtype: str
        """
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}"
