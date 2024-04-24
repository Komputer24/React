from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

hobbiesList = []

class Item(BaseModel):
    name: str

@app.post('/addHobbies')
async def addHobby(hobby: Item):
    hobbiesList.append(hobby.name)
    return {'message': 'sucess'}

@app.get('/hobbiesList')
async def root():
    return hobbiesList

"""

# A todo list for things to get stored in

todo_list_items = []

# class Item extends BaseModel
class Item(BaseModel):
    name: str
    number: int

    
class Element(BaseModel):
    number: int

@app.get('/items')
#Defining a get route on the app variable
# Runs root() function after making get request

async def root():
#Asynchronous function
    return todo_list_items

@app.post('/add')
async def add_item(item: Item):
    todo_list_items.append((item.name, item.number))
    return {'message': 'sucess'}

@app.delete('/remove')
async def remove_item(element: Element):
    if element.number > len(todo_list_items):
        return "index too large"
    todo_list_items.pop(element.number)
    return {'message': 'success'}
    
"""