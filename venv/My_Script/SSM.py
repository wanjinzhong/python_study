class Student:
    id = 0
    name = ''
    score = 0
    grade = ''

    def __init__(self):
        pass

    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score

    def calc_grade(self):
        if self.score < 0:
            return "CHEAT"
        elif self.score < 60:
            return "D"
        elif self.score < 70:
            return "C"
        elif self.score < 80:
            return "B"
        elif self.score < 90:
            return "A"
        elif self.score <= 100:
            return "A+"
        else:
            return "Wrong"

    def get_table(self):
        return str(self.id) + "\t" + self.name + "\t" + str(self.score) + "\t" + self.calc_grade()


students = [Student(1, 'Neil', 100), Student(2, 'Bill', 100), Student(3, 'Leon', 100)]
grades = ((0, "FAIL"), (50, "D"), (60, "C"), (70, "B"), (80, "A"), (-1, "CHEAT!"))
hint = "=======Student Score Management=======\n"
hint += "  1. Add a new record\n"
hint += "  2. Delete a record\n"
hint += "  3. Query records\n"
hint += "  4. Update record\n"
hint += "  5. Exit\n"
hint += "======================================\n"


def add_record():
    global students
    while True:
        try:
            print("Student Id:")
            id = int(input(">>"))
        except ValueError:
            print("Id must be number")
        else:
            student = query_by_id(id)
            if student is not None:
                print("This student is already exist, cover it?(y/n)")
                cover = input(">>");
                if cover.upper() == 'Y':
                    student = student[0]
                    break
                else:
                    print("Cancel add a new record")
                    return
            else:
                student = Student()
                students.append(student)
            break
    print("Student Name:")
    name = input(">>")
    while True:
        try:
            print("Student Score:")
            score = float(input(">>"))
        except ValueError:
            print("Score must be number")
        else:
            break
    student.id = id
    student.name = name
    student.score = score
    print("Add record success")
    print_table(student)


def print_tables(stus):
    print(get_table_header())
    if stus is None or len(stus) == 0:
        print(" No Data")
    else:
        for s in stus:
            print(s.get_table())
    print(get_table_foot(), end="\n\n")


def print_table(student):
    print(get_table_header())
    if student is None:
        print(" No Data")
    else:
        print(student.get_table())
    print(get_table_foot(), end="\n\n")


def get_table_header():
    str = "Id\tName\tScore\tGrade\n"
    str += "========================="
    return str


def get_table_foot():
    str = "========================="
    return str


def delete_record():
    print("1. Delete by id")
    print("2. Delete by name")
    while True:
        try:
            choose = int(input(">>"))
        except ValueError:
            print("Error: Only accept number")
        else:
            if choose != 1 and choose != 2:
                print("Error: Range: 1-2")
            else:
                break
    if choose == 1:
        print("Id:")
        while True:
            try:
                id = int(input(">>"))
            except ValueError:
                print("Error: Only accept number")
            else:
                break
        stus = query_by_id(id)
        if stus is None:
            print("No record found")
        else:
            print("Bellow record found, sure to delete?(y/n)")
            print_table(stus)
            cover = input(">>");
            if cover.upper() == 'Y':
                delete_records(stus)
                print("Delete records success")
            else:
                print("Cancel delete a record")
    elif choose == 2:
        print("Name:")
        name = input(">>")
        stus = query_by_name(name)
        if stus is None:
            print("No record found")
        else:
            print("Bellow record found, sure to delete?(y/n)")
            print_tables(stus)
            cover = input(">>");
            if cover.upper() == 'Y':
                delete_records(stus)
                print("Delete records success")
            else:
                print("Cancel delete a record")


def delete_records(toDelete):
    for j in toDelete:
        students.remove(j)


def query_record():
    print("1. Query by one")
    print("2. Query by all")
    while True:
        try:
            choose = int(input(">>"))
        except ValueError:
            print("Error: Only accept number")
        else:
            if choose != 1 and choose != 2:
                print("Error: Range: 1-2")
            else:
                break
    if choose == 1:
        query()
    elif choose == 2:
        query_all()


def update_record():
    print("1. Update by id")
    print("2. Update by name")
    while True:
        try:
            choose = int(input(">>"))
        except ValueError:
            print("Error: Only accept number")
        else:
            if choose != 1 and choose != 2:
                print("Error: Range: 1-2")
            else:
                break
    if choose == 1:
        while True:
            print("Id: ")
            try:
                id = int(input(">>"))
            except ValueError:
                print("Error: Only accept number")
            else:
                break
        student = query_by_id(id)
    elif choose == 2:
        print("Name: ")
        name = input(">>")
        student = query_by_name(name)
    if student is None or len(student) == 0:
        print("No record found")
        return
    elif len(student) > 1:
        print("Too much record found, please make your condition more accurate")
        print_tables(student)
        return
    else:
        stu = student[0]
        while True:
            try:
                print("Update Score:")
                score = float(input(">>"))
            except ValueError:
                print("Score must be number")
            else:
                stu.score = score
                print("Update score success")
                print_table(stu)
                break


def query():
    print("1. Query by id")
    print("2. Query by name")
    while True:
        try:
            choose = int(input(">>"))
        except ValueError:
            print("Error: Only accept number")
        else:
            if choose != 1 and choose != 2:
                print("Error: Range: 1-2")
            else:
                break
    if choose == 1:
        while True:
            print("Id: ")
            try:
                id = int(input(">>"))
            except ValueError:
                print("Error: Only accept number")
            else:
                break
        student = query_by_id(id)
        print_table(student)
    elif choose == 2:
        print("Name: ")
        name = input(">>")
        student = query_by_name(name)
        print_tables(student)


def query_by_id(id):
    stus = []
    for s in students:
        if s.id == id:
            stus.append(s)
    return stus


def query_by_name(name):
    stus = []
    for s in students:
        if name.upper() in s.name.upper():
            stus.append(s)
    return stus


def query_all():
    global students
    print_tables(students)


while True:
    print(hint)
    while True:
        try:
            print("Please choose one: ")
            choose = int(input(">>"))
        except ValueError:
            print("Error: Only accept number")
        else:
            if choose < 1 or choose > 5:
                print("Error: Range: 1-5")
            else:
                break
    if choose == 1:
        add_record()
    elif choose == 2:
        delete_record()
    elif choose == 3:
        query_record()
    elif choose == 4:
        update_record()
    elif choose == 5:
        print("Bye")
        break
