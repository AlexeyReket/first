CREATE TABLE Faculty(
    id INTEGER PRIMARY KEY ,
    name varchar
);
CREATE TABLE Course(
    id INTEGER PRIMARY KEY ,
    num int
);
CREATE TABLE Form(
    id INTEGER PRIMARY KEY ,
    type varchar
);
CREATE TABLE StudentGroup(
    id INTEGER PRIMARY KEY,
    name varchar,
    faculty_id int,
    course_id int,
    form_id int,
    FOREIGN KEY (faculty_id) REFERENCES Faculty(id),
    FOREIGN KEY (course_id) REFERENCES Course(id),
    FOREIGN KEY (form_id) REFERENCES Form(id)
);
