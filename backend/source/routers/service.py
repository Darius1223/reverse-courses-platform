from fastapi import APIRouter

service_router = APIRouter(prefix="/service", tags=["service"])


@service_router.get("/health")
async def health() -> dict:
    return {"health": True}
