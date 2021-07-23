CREATE TABLE Faculty(
    id int PRIMARY KEY ,
    name varchar
);
CREATE TABLE Course(
    id int PRIMARY KEY ,
    num int
);
CREATE TABLE Form(
    id int PRIMARY KEY ,
    type varchar
);
CREATE TABLE StudentGroup(
    id int PRIMARY KEY,
    name varchar,
    faculty varchar,
    course int,
    form varchar,
    FOREIGN KEY (faculty) REFERENCES Faculty(name),
    FOREIGN KEY (course) REFERENCES Course(num),
    FOREIGN KEY (form) REFERENCES Form(type)
);
