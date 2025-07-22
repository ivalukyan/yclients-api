from pydantic import BaseModel


class ParamsRecords(BaseModel):
    id: int
    services: list[int] | None
    staff_id: int
    datetime: int
