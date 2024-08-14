from fastapi import FastAPI

from source.routers.courses import courses_router
from source.routers.service import service_router
from source.routers.users import users_router


def create_app() -> FastAPI:
    app_ = FastAPI()

    # add routers
    app_.include_router(service_router)
    app_.include_router(courses_router)
    app_.include_router(users_router)

    return app_


app = create_app()
