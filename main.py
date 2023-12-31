from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI(
    title='My App'
)

fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "developer", "name": "Denn"},
    {"id": 3, "role": "front_end", "name": "John"},
    {"id": 4, "role": "back_end", "name": "Met"},
    {"id": 5, "role": "full-stack", "name": "Mike"},
    {"id": 6, "role": "java", "name": "Lola"},
]


class User(BaseModel):
    id: int
    role: str
    name: str


class UserUpdateSchema(BaseModel):
    name: Optional[str]
    role: Optional[str]


class UserUpdateResponseSchema(BaseModel):
    name: str
    role: str


# get users for id
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in fake_users:
        if user.get('id') == user_id:
            return user


# get all users
@app.post("/all_users")
def get_all_users(user: User):
    fake_users.extend(user)
    return {"data": fake_users}


@app.delete("/delete/{user_id}")
def delete_user(user_id: int):
    del fake_users[user_id]
    return {f"message, delete user with id {user_id}, data : {fake_users}"}


# create
@app.post("/user_create")
def create_user(user: User):
    return fake_users.extend(user)


# update
@app.put("/update/{user_id}", response_model=UserUpdateResponseSchema)
def update_user(user_id: int, user: UserUpdateSchema):
    return {'name': user.name, 'role': user.role, "id": user_id, 'data': fake_users}
