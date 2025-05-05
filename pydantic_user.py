from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True


user_data = {
    "id": 1,
    "username": "Zara",
    "email": "zara.bond@gmail.com"
}

user = User(**user_data)
print(user)
print(user.is_active)

invalid_user_data = {
    "id": "own",
    "username": "Zara",
    "email": "zara.bond@gmail.com"
}


try:
    invalid_user_data = User(**invalid_user_data)

except Exception as error:
    print("Ошибка валидации:", error)