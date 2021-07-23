from fastapi import FastAPI
import uvicorn
import json
from app.repotory.courses import Course
from app.repotory.facultys import Faculty
from app.repotory.forms import Form
from app.repotory.studentgroups import StudentGroup

app = FastAPI()

"""get requests"""


@app.get("/get_form/courses/{id}")
def get_courses(id: int):
    course = Course(id).get().__dict__
    json_data = json.dumps(course)
    return json_data


@app.get("/get_form/forms/{id}")
def get_forms(id: int):
    form = Form(id).get().__dict__
    json_data = json.dumps(form)
    return json_data


@app.get("/get_form/facultys/{id}")
def get_facultys(id: int):
    faculty = Faculty(id).get().__dict__
    json_data = json.dumps(faculty)
    return json_data


@app.get("/get_form/groups/{id}")
def get_groups(id: int):
    group = StudentGroup(id).get().__dict__
    json_data = json.dumps(group)
    return json_data


"""post requests"""


@app.post("/post_form/courses/{id}")
def post_courses(id, num):
    course = Course(id, num)
    course.save()
    return {"result": "success"}


@app.post("/post_form/forms/{id}")
def post_forms(id, type):
    form = Form(id, type)
    form.save()
    return {"result": "success"}


@app.post("/post_form/facultys/{id}")
def post_facultys(id, name):
    faculty = Faculty(id, name)
    faculty.save()
    return {"result": "success"}


@app.post("/post_form/groups/{id}")
def post_groups(id, name, faculty, course, form):
    group = StudentGroup(id, name, faculty, course, form)
    group.save()
    return {"result": "success"}


"""put requests"""


@app.put("/put_form/courses/{id}")
def put_courses(id, num):
    course = Course(id, num)
    course.update()
    return {"result": "success"}


@app.put("/put_form/forms/{id}")
def put_forms(id, type):
    form = Form(id, type)
    form.update()
    return {"result": "success"}


@app.put("/put_form/facultys/{id}")
def put_facultys(id, name):
    faculty = Faculty(id, name)
    faculty.update()
    return {"result": "success"}


@app.put("/put_form/groups/{id}")
def put_groups(id, name, faculty, course, form):
    group = StudentGroup(id, name, faculty, course, form)
    group.update()
    return {"result": "success"}


"""delete requests"""


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
