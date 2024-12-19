from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"Главная страница"}

@app.get("/user")
async def user_predator(username: str, age: int) -> dict:
    return {"User": username, "Age": age}

@app.get("/user/admin")
async def welcome_admin() -> dict:
    return {"Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def welcome_user(user_id: int) -> dict:
    return {f"Вы вошли как пользователь № {user_id}"}