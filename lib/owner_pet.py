class Pet:
     
     PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
     all =[]

     def __init__ (self,name,pet_type, owner = None):
          self.name = name
          self.pet_type = pet_type
          self.owner = owner
          Pet.all.append(self)
    
    
     @property
     def pet_type(self):
      return self._pet_type
     @pet_type.setter
     def pet_type(self, value):
         if value in Pet.PET_TYPES :
             self._pet_type = value
         else: 
           raise ValueError ("Invalid pet type")
     


class Owner:
    def __init__(self,name):
         self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be an instance of Pet class")
        pet.owner = self

    
    
    def get_sorted_pets(self):
       pets = [pet for pet in Pet.all if pet.owner == self]
       return sorted(pets, key=lambda pet: pet.name)




