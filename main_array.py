from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4 as uuid # Libreria para generar IDs unicos
from typing import Text, Optional

app = FastAPI()

posts = []

# Modelo de post
class Post(BaseModel):
    id: str
    title: str
    content: Text
    author: str
    created_at: datetime = datetime.now()
    published_at: Optional[datetime] 
    published: bool = False

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[Text] = None
    author: Optional[str] = None
    

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API!"}

@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts/crear')
def create_post(post: Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return {"message": "Post creado correctamente"}

@app.get('/posts/{post_id}')
def get_post_by_id(post_id: str):
    for post in posts:
        if post['id'] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post no encontrado")

@app.delete('/posts/delete/{post_id}')
def delete_post(post_id: str):
    for index, post in enumerate(posts):
        if post['id'] == post_id:
            posts.pop(index)
            return {"message": "Post eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Post no encontrado")

@app.put('/posts/update/{post_id}')
def update_post(post_id: str, updatePost: PostUpdate):
    for post in posts:
        if post['id'] == post_id:
            post.update(updatePost.dict())
            return {"message": "Post actualizado correctamente"}
    raise HTTPException(status_code=404, detail="Post no encontrado")
