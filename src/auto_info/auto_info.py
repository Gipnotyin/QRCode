from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from auto_info.models import auto
from auto_info.schemas import Auto
from database import get_async_session
from generate.generate_qrcode import GenerateQRcode

router = APIRouter(
    prefix="/auto",
    tags=["auto"]
)


@router.get("/car/{vin}")
async def get_auto_info(vin: str, session: AsyncSession = Depends(get_async_session)):
    query = select(auto).where(auto.c.vin == vin)
    result = await session.execute(query)
    res = []
    for a in result.all():
        res.append(list(a))

    return {
        "data": res
    }


@router.post("/")
async def add_auto(new_auto: Auto, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(auto).values(**new_auto.dict())
    await session.execute(stmt)
    await session.commit()
    GenerateQRcode(new_auto.vin)
    return {"status": "success"}
