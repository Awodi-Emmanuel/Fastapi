from pydantic import BaseModel

class Person(BaseModel):
    first: str
    last: str
    zip_code: str
    
    
    def __str__(self) -> str:
        return "%s %s: %s" % (self.first, self.last, self.zip_code)
    
person_dict = {
    "first": "Bruce",
    "last": "wayne",
    "zip_code": "10021"
}    
    
person = Person(**person_dict)

    
print(person)