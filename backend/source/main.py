from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette_admin.contrib.sqlmodel import Admin, ModelView

from source.containers import container
from source.database.core import engine
from source.database.models import User
from source.routers.auth import auth_router
from source.routers.courses import courses_router
from source.routers.service import service_router


def create_app() -> FastAPI:
    app_ = FastAPI(root_path="/api")

    # add routers
    app_.include_router(service_router)
    app_.include_router(courses_router)
    app_.include_router(auth_router)

    # wire
    container.wire(packages=["source"])
    # cors

    origins = [
        "http://localhost.tiangolo.com",
        "https://localhost.tiangolo.com",
        "http://localhost",
        "http://localhost:8081",
    ]

    app_.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    admin = Admin(engine, title="Example: SQLAlchemy")

    # Add view
    admin.add_view(ModelView(User))

    # Mount admin to your app
    admin.mount_to(app_)

    return app_


app = create_app()
