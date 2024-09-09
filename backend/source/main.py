from fastapi import FastAPI
from sqlmodel import SQLModel
from starlette_admin.contrib.sqlmodel import Admin, ModelView

from source.database.core import engine
from source.database.models import User
from source.routers.auth import auth_router
from source.routers.courses import courses_router
from source.routers.service import service_router
from source.routers.users import users_router


def create_app() -> FastAPI:
    app_ = FastAPI(root_path="/api")

    # add routers
    app_.include_router(service_router)
    app_.include_router(courses_router)
    app_.include_router(users_router)
    app_.include_router(auth_router)

    admin = Admin(engine, title="Example: SQLAlchemy")

    # Add view
    admin.add_view(ModelView(User))

    # Mount admin to your app
    admin.mount_to(app_)

    return app_


app = create_app()
