from sqlalchemy import Table, Column, BigInteger, ForeignKey
from src.db.base_class import Base

#Tabla intermedia para la relacion many to many entre Post y Tag
post_tag = Table("posts_tag", Base.metadata,
    Column("post_id", BigInteger, ForeignKey("posts.id")),
    Column("tag_id", BigInteger, ForeignKey("tags.id"))
)