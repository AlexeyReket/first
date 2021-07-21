CREATE TABLE Faculty(
    f_name varchar
);
CREATE TABLE Course(
    num int PRIMARY KEY
);
CREATE TABLE Form(
  type varchar
);
CREATE TABLE StudentGroup(
    id int PRIMARY KEY,
    g_name varchar,
    faculty_name varchar NOT NULL,
    course_num int NOT NULL,
    form_type varchar,
    FOREIGN KEY (faculty_name) REFERENCES Faculty(f_name),
    FOREIGN KEY (course_num) REFERENCES Course(num),
    FOREIGN KEY (form_type) REFERENCES Form(type)
);
