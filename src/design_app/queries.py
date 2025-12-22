from sqlmodel import Session, select
from design_app.database import engine
from design_app.models import *

teacher_name = "John Smith"
course_id =1
student_id = 1
new_domain = "@newschool.com"
"""
# 1. Delete enrollments first
with Session(engine) as session:
    enrollments = session.exec(
        select(Enrollment).join(Teacher).where(Teacher.teacher_name == teacher_name)
    ).all()

    print("Enrollments before delete:", enrollments)

    for e in enrollments:
        session.delete(e)

    session.commit()


# 2. Delete the teacher
with Session(engine) as session:
    teachers = session.exec(
        select(Teacher).where(Teacher.teacher_name == teacher_name)
    ).all()

    print("Teachers before delete:", teachers)

    for t in teachers:
        session.delete(t)

    session.commit()

with Session(engine) as session:
    statement = select(Enrollment).join(Student).join(Course)
    required = statement.where(Student.id == student_id).where(Course.id == course_id)
    enrollments = session.exec(required).all()

    print("Enrollments before delete:", enrollments)

    for e in enrollments:
        session.delete(e)

    session.commit()

# 3. Verify
with Session(engine) as session:
    remaining = session.exec(
        select(Enrollment).join(Teacher).where(Teacher.teacher_name == teacher_name)
    ).all()
    statement = select(Enrollment).join(Student).join(Course)
    required = statement.where(Student.id == student_id).where(Course.id == course_id)
    enrollments = session.exec(required).all()
    

    print("After:", remaining, "\n", enrollments)

with Session(engine) as session:
    statement = select(Course).where(Course.course_code == "MATH101")
    results = session.exec(statement)
    hero = results.one()
    print("before", hero)
    hero.course_code = "MATH102"
    session.add(hero)
    session.commit()
    print("after", hero)
"""
with Session(engine) as session:
    statement = select(Teacher)
    results = session.exec(statement)
    hero = results.first()
    hero.teacher_email = hero.teacher_email.replace("@school.com", new_domain)
    session.add(hero)
    session.commit()
