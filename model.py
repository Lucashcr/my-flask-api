from datetime import date
from peewee import *


db = SqliteDatabase('people.db')

class Person(Model):
    id = IntegerField(primary_key=True)
    name = CharField(unique=True, null=False)
    birthday = DateField(null=False)
    
    class Meta:
        database = db
    
    # def __init__(self, name, birthday) -> None:
    #     self.name = name
    #     self.birthday = birthday
        
    def to_json(self):
        return dict(name=self.name, birthday=self.birthday)
    
    @property
    def age(self):
        return dict(name=self.name, age=(date.today()-self.birthday).days//365.25)
    
    # def __eq__(self, other) -> bool:
    #     return type(self) is type(other) and self.id == other.id
    
    # def __ne__(self, other) -> bool:
    #     return not self.__eq__(other)
    
    # def __repr__(self) -> str:
    #     return f'{self.name}: {self.birthday}'
    
    
if __name__ == '__main__':
    connection = db.connect()
    
    if connection: 
    #     db.create_tables([Person])
    
        teste = Person(name='Lucas', birthday=date(1997, 10, 17))
        teste.save()
        
        db.close()