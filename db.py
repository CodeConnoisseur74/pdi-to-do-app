from __future__ import annotations

from datetime import date

from sqlmodel import create_engine
from sqlmodel import Field
from sqlmodel import Session
from sqlmodel import SQLModel

# Set up the SQLite database engine.
engine = create_engine("sqlite:///database.db")


def create_tables():
    SQLModel.metadata.create_all(engine)


class Todo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    completed: bool
    due_date: date


def add_task(title: str, completed: bool = False, due_date: date = None):
    with Session(engine) as session:
        task = Todo(title=title, completed=completed, due_date=due_date)
        session.add(task)
        session.commit()


def view_tasks():
    with Session(engine) as session:
        tasks = session.query(Todo).all()
        return tasks


def mark_task_complete(task_id: int):
    with Session(engine) as session:
        task = session.get(Todo, task_id)
        if task:
            task.completed = True
            session.commit()


def delete_task(task_id: int):
    with Session(engine) as session:
        task = session.get(Todo, task_id)
        if task:
            session.delete(task)
            session.commit()


def quit_program():
    print("Thank you for using the To-Do List!")
    exit()
