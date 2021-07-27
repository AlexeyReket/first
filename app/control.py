from fastapi import FastAPI, Request
import uvicorn
from app.repotory.courses import Course
from app.repotory.facultys import Faculty
from app.repotory.forms import Form
from app.repotory.studentgroups import StudentGroup

app = FastAPI(title="It's working!", version="0.1.1")

"""get all requests"""


@app.get("/get_form/courses/all")
def get_all_courses():
    temp = []
    ids = Course(0).get_all()
    for id in ids:
        temp.append(Course(id[0]).get())
    return temp


@app.get("/get_form/forms/all")
def get_all_forms():
    temp = []
    ids = Form(0).get_all()
    for id in ids:
        temp.append(Form(id[0]).get())
    return temp


@app.get("/get_form/facultys/all")
def get_all_facultys():
    temp = []
    ids = Faculty(0).get_all()
    for id in ids:
        temp.append(Faculty(id[0]).get())
    return temp


@app.get("/get_form/groups/all")
def get_all_groups():
    temp = []
    ids = StudentGroup(0).get_all()
    for id in ids:
        group = StudentGroup(id[0])
        temp.append(group.get())
    return temp


"""get one requests"""


@app.get("/get_form/courses/{id}")
def get_courses(id: int):
    course = Course(id).get()
    return course


@app.get("/get_form/forms/{id}")
def get_forms(id: int):
    form = Form(id).get()
    return form


@app.get("/get_form/facultys/{id}")
def get_facultys(id: int):
    faculty = Faculty(id).get()
    return faculty


@app.get("/get_form/groups/{id}")
def get_groups(id: int):
    group = StudentGroup(id).get()
    return group


"""post requests"""


@app.post("/post_form/courses")
async def post_courses(request: Request):
    body = await request.json()
    num = body["num"]
    Course(0, num).save()
    return {"result": "success"}


@app.post("/post_form/forms")
async def post_forms(request: Request):
    body = await request.json()
    type = body["type"]
    Form(0, type).save()
    return {"result": "success"}


@app.post("/post_form/facultys")
async def post_facultys(request: Request):
    body = await request.json()
    name = body["name"]
    Faculty(0, name).save()
    return {"result": "success"}


@app.post("/post_form/groups")
async def post_groups(request: Request):
    body = await request.json()
    name = body["name"]
    faculty = body["faculty"]
    course = body["course"]
    form = body["form"]
    StudentGroup(0, name, faculty, course, form).save()
    return {"result": "success"}


"""put requests"""


@app.put("/put_form/courses/{id}")
async def put_courses(id, request: Request):
    body = await request.json()
    num = body["num"]
    Course(id, num).update()
    return {"result": "success"}


@app.put("/put_form/forms/{id}")
async def put_forms(id, request: Request):
    body = await request.json()
    type = body["type"]
    Form(id, type).update()
    return {"result": "success"}


@app.put("/put_form/facultys/{id}")
async def put_facultys(id, request: Request):
    body = await request.json()
    name = body["name"]
    Faculty(id, name).update()
    return {"result": "success"}


@app.put("/put_form/groups/{id}")
async def put_groups(id, request: Request):
    body = await request.json()
    name = body["name"]
    faculty = body["faculty"]
    course = body["course"]
    form = body["form"]
    StudentGroup(id, name, faculty, course, form).update()
    return {"result": "success"}


"""delete all requests"""


@app.delete("/delete_form/courses/all")
def delete_all_courses():
    Course(0).clear()
    return {"result": "success"}


@app.delete("/delete_form/forms/all")
def delete_all_forms():
    Form(0).clear()
    return {"result": "success"}


@app.delete("/delete_form/facultys/all")
def delete_all_facultys():
    Faculty(0).clear()
    return {"result": "success"}


@app.delete("/delete_form/groups/all")
def delete_all_groups():
    StudentGroup(0).clear()
    return {"result": "success"}


"""delete one requests"""


@app.delete("/delete_form/courses/{id}")
def delete_courses(id):
    course = Course(id)
    course.delete()
    return {"result": "success"}


@app.delete("/delete_form/forms/{id}")
def delete_forms(id):
    form = Form(id)
    form.delete()
    return {"result": "success"}


@app.delete("/delete_form/facultys/{id}")
def delete_facultys(id):
    faculty = Faculty(id)
    faculty.delete()
    return {"result": "success"}


@app.delete("/delete_form/groups/{id}")
def delete_groups(id):
    group = StudentGroup(id)
    group.delete()
    return {"result": "success"}


if __name__ == "__main__":
    uvicorn.run(
        "control:app",
        host='localhost',
        port=8000,
        reload=True
    )
