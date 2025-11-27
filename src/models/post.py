from sqlalchemy import Column, BigInteger, String, ForeignKey, Boolean, DateTime, Text, Table
from sqlalchemy.orm import relationship
from src.db.base_class import Base
from datetime import datetime
from src.models.associations import post_tag



class Post(Base):
    __tablename__ = "posts"
    id = Column(BigInteger, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    author_id = Column(BigInteger, ForeignKey("authors.id"))
    created_at = Column(DateTime, default=datetime.now)
    published_at = Column(DateTime, nullable=True)
    published = Column(Boolean, default=False)

    #Relaciones
    author = relationship("Author", back_populates="posts") # relacion con el modelo Author
    tags = relationship("Tag", secondary=post_tag, back_populates="posts") # relacion con el modelo Tag