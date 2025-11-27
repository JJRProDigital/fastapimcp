from pydantic import BaseModel

class TagBase(BaseModel):
    name: str

class Tag(TagBase):
    id: int
    #posts: list[Post] = []

    class Config:
        from_attributes = True

class TagCreate(TagBase):
    pass


