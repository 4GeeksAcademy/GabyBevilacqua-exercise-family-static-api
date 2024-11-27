
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [ # lista
            { # diccionario
                "id": self._generateId(),
                "first_name": "Gaby",
                "last_name": last_name,
                "age": 46,
                "lucky_numbers": [46, 14, 63]
            },
             {
                "id": self._generateId(),
                "first_name": "Carlo",
                "last_name": last_name,
                "age": 63,
                "lucky_numbers": [4, 11, 33]
            },
             {
                "id": self._generateId(),
                "first_name": "Sam",
                "last_name": last_name,
                "age": 40,
                "lucky_numbers": [6, 22, 7]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        self._members.append(member) #revisar si es plural o singular memders
        pass

    def delete_member(self, id):
        # fill this method and update the return
        for index, member in enumerate(self._members):  # Buscar por índice y miembro
            if member["id"] == id:
                return self._members.pop(index)  # Eliminar por índice
                return None  # Si no se encuentra el miembro, devolver None
    
    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member ["id"] == id:
                return member
        
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
    
# https://www.python.org/downloads/windows/