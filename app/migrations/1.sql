CREATE TABLE Faculty(
    id int PRIMARY KEY,
    f_name varchar
);
CREATE TABLE Course(
    num int PRIMARY KEY
);
CREATE TABLE StudentGroup(
    id int PRIMARY KEY,
    g_name varchar,
    faculty_id varchar NOT NULL,
    course_num int NOT NULL,
    FOREIGN KEY (faculty_id) REFERENCES Faculty(id),
    FOREIGN KEY (course_num) REFERENCES Course(num)
);
CREATE TABLE Student(
    id int PRIMARY KEY,
    s_name varchar,
    group_id int NOT NULL,
    FOREIGN KEY (group_id) REFERENCES StudentGroup(id)
);
CREATE TABLE GroupTimeTable(
    group_id int NOT NULL,
    FOREIGN KEY (group_id) REFERENCES StudentGroup(id)
);
CREATE TABLE CurWeeks(
    week_date DATE,
    mon
);
CREATE TABLE OneDayItems(
    item_name varchar,
    item_time TIME,
    item_lecturer varchar,
    item_type varchar
);

