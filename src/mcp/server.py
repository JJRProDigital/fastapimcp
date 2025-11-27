from fastmcp import FastMCP
from src.db.session import SessionLocal
# Importamos el modulo CRUD completo ya que usa funciones directas
import src.crud.tag as tag_crud
from src.schemas.tag import TagCreate

# Inicializar el servidor MCP
mcp = FastMCP("FastAPI Blog MCP")

from typing import Optional

# ... imports ...

@mcp.tool()
def listar_tags(
    sessionId: Optional[str] = None, 
    action: Optional[str] = None, 
    chatInput: Optional[str] = None,
    tool: Optional[str] = None,
    toolCallId: Optional[str] = None
) -> str:
    """
    Lista todos los tags existentes en la base de datos del blog.
    Devuelve una cadena formateada con los tags encontrados.
    Los parámetros opcionales son para compatibilidad con n8n.
    """
    db = SessionLocal()
    try:
        tags = tag_crud.get_tags(db)
        if not tags:
            return "No hay tags registrados."
        return ", ".join([f"{t.id}: {t.name}" for t in tags])
    except Exception as e:
        return f"Error al leer tags: {str(e)}"
    finally:
        db.close()

@mcp.tool()
def crear_nuevo_tag(
    nombre: str,
    sessionId: Optional[str] = None, 
    action: Optional[str] = None, 
    chatInput: Optional[str] = None,
    tool: Optional[str] = None,
    toolCallId: Optional[str] = None
) -> str:
    """
    Crea un nuevo tag en la base de datos.
    Args:
        nombre: El nombre del tag a crear.
    """
    db = SessionLocal()

    try:
        tag_in = TagCreate(name=nombre)
        # Nota: Asegúrate de que create_tag maneje excepciones de duplicados
        nuevo_tag = tag_crud.create_tag(db, tag=tag_in)
        return f"Tag creado exitosamente: ID {nuevo_tag.id}, Nombre '{nuevo_tag.name}'"
    except Exception as e:
        return f"Error al crear tag: {str(e)}"
    finally:
        db.close()

@mcp.tool()
def buscar_tag_por_nombre(
    nombre: str,
    sessionId: Optional[str] = None, 
    action: Optional[str] = None, 
    chatInput: Optional[str] = None,
    tool: Optional[str] = None,
    toolCallId: Optional[str] = None
) -> str:
    """
    Busca un tag por su nombre exacto.
    Args:
        nombre: El nombre del tag a buscar.
    """
    db = SessionLocal()
    try:
        tag = tag_crud.get_tag_by_name(db, name=nombre)
        if tag:
            return f"Tag encontrado: ID {tag.id}, Nombre '{tag.name}'"
        return f"No se encontró ningún tag con el nombre '{nombre}'"
    except Exception as e:
        return f"Error al buscar tag: {str(e)}"
    finally:
        db.close()

@mcp.tool()
def actualizar_tag(
    tag_id: int,
    nuevo_nombre: str,
    sessionId: Optional[str] = None, 
    action: Optional[str] = None, 
    chatInput: Optional[str] = None,
    tool: Optional[str] = None,
    toolCallId: Optional[str] = None
) -> str:
    """
    Actualiza el nombre de un tag existente dado su ID.
    Args:
        tag_id: El ID del tag a actualizar.
        nuevo_nombre: El nuevo nombre para el tag.
    """
    db = SessionLocal()
    try:
        # Verificamos primero si existe
        tag_existente = tag_crud.get_tag_by_id(db, tag_id=tag_id)
        if not tag_existente:
            return f"No se encontró el tag con ID {tag_id}"
            
        tag_in = TagCreate(name=nuevo_nombre)
        tag_actualizado = tag_crud.update_tag(db, tag_id=tag_id, tag=tag_in)
        return f"Tag actualizado: ID {tag_actualizado.id}, Nuevo Nombre '{tag_actualizado.name}'"
    except Exception as e:
        return f"Error al actualizar tag: {str(e)}"
    finally:
        db.close()

@mcp.tool()
def eliminar_tag(
    tag_id: int,
    sessionId: Optional[str] = None, 
    action: Optional[str] = None, 
    chatInput: Optional[str] = None,
    tool: Optional[str] = None,
    toolCallId: Optional[str] = None
) -> str:
    """
    Elimina un tag de la base de datos dado su ID.
    Args:
        tag_id: El ID del tag a eliminar.
    """
    db = SessionLocal()
    try:
        # Verificamos primero si existe
        tag_existente = tag_crud.get_tag_by_id(db, tag_id=tag_id)
        if not tag_existente:
            return f"No se encontró el tag con ID {tag_id} para eliminar"

        tag_crud.delete_tag(db, tag_id=tag_id)
        return f"Tag con ID {tag_id} eliminado exitosamente"
    except Exception as e:
        return f"Error al eliminar tag: {str(e)}"
    finally:
        db.close()

if __name__ == "__main__":
    mcp.run()

