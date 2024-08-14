from fastapi import APIRouter

courses_router = APIRouter(prefix="/courses", tags=["courses"])


@courses_router.get("/all")
async def get_courses() -> dict:
    return {"health": True}


@courses_router.post("/")
async def create_course(course) -> dict:
    return {"health": True}
