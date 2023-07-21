from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from project.database import database as connection
from project.database import User, Movie, UserReview
from .routers import user_router, review_router
from fastapi.security import OAuth2PasswordRequestForm

# Creating app
app = FastAPI(title='Proyecto para reseñar peliculas',
              description='En este proyecto seremos capaces de reseñar peliculas',
              version='1.0')

api_v1 = APIRouter(prefix='/api/v1')

api_v1.include_router(user_router)
api_v1.include_router(review_router)


@api_v1.post('/auth')
async def auth(data: OAuth2PasswordRequestForm = Depends()):
    user = User.authenticate(data.username, data.password)
    if user:
        return {
            'username': data.username,
            'password': data.password
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password',
            headers={'WWW-Authenticate': 'Bearer'}
        )

app.include_router(api_v1)


@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()  # La conexión se va a establecer antes de que el servidor inicie

    # Creando las tablas en la base de datos
    connection.create_tables([User, Movie, UserReview])
    # Si las tablas ya se encuentran en la base de datos, no se van a volver a crear


@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()  # La conexión se va a cerrar cuando el servidor se detenga
        print('Closing...')
