class Person:
    """ 
    A class representing a person.
    
    Attributes:
        name (str): The person's name.
        age (int): The person's age.
   
    """
    def __init__(self, name, age):
        """
        Constructor to initialize a new Person instance.

        :param name: The name of the person
        :type name: str
        :param age: The age of the person
        :type age: int

        """
        self.name = name
        self.age = age

    def view_info(self):
        """ 
         this function View basic information about the person
      
         return: A formatted string containing the person's name and age.
         :rtyp:str  
      
        """
        return f"Name: {self.name}, Age: {self.age}"