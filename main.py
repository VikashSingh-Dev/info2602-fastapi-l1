""" from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
def hello_world():
    return 'Hello, World!' """

from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
async def hello_world():
    return 'Hello, World!'

# ### New Function
# @app.get('/students')
# async def get_students():
#     return data
# ### End of new function

# @app.get('/students/{id}')
# async def get_student(id):
#   for student in data: 
#     if student['id'] == id: # Only return the student if the ID matches
#       return student

# @app.get('/students')
# async def get_students(pref=None):
#     if pref:
#         filtered_students = []
#         for student in data:
#             if student['pref'] == pref: # select only the students with a given meal preference
#                 filtered_students.append(student) # add match student to the result
#         return filtered_students
#     return data


# EXERCISE 1
@app.get('/stats')
async def get_stats():
    counts = {
        "count_veg": 0,
        "count_fish": 0,
        "count_chicken": 0,
        "count_csSP": 0,
        "count_csM": 0,
        "count_itSP": 0,
        "count_itM": 0
    }
    
    for student in data:
        if student['pref'] == "Chicken":
            counts["count_chicken"] += 1
        
        elif student['pref'] == "Fish":
            counts["count_fish"] += 1
        
        elif student['pref'] == "Vegetable":
            counts["count_veg"] += 1

        if student['programme'] == "Computer Science (Major)":
            counts["count_csM"] += 1
        
        elif student['programme'] == "Computer Science (Special)":
            counts["count_csSP"] += 1

        elif student['programme'] == "Information Technology (Major)":
            counts["count_itM"] += 1

        elif student['programme'] == "Information Technology (Special)":
            counts["count_itSP"] += 1
        
    return counts


# EXERCISE 2
@app.get('/add/{a}/{b}')
async def add(a: int, b:int):
    return {"result": a + b}

@app.get('/subtract/{a}/{b}')
async def sub(a: int, b: int):
    return {"result": a - b}

@app.get('/multiply/{a}/{b}')
async def mul(a: int, b: int):
    return {"result" : a * b}

@app.get('/divide/{a}/{b}')
async def div(a: int, b:int):
    if b != 0:
        return {"result": a / b}
    return {"error": "cannot divide by zero"}