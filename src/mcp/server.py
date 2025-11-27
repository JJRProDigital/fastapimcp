from fastmcp import FastMCP
from src.db.session import SessionLocal
# Importamos el modulo CRUD completo ya que usa funciones directas
import src.crud.tag as tag_crud
from src.schemas.tag import TagCreate

# Inicializar el servidor MCP
mcp = FastMCP("FastAPI Blog MCP")

@mcp.tool()
def listar_tags() -> str:
    """
    Lista todos los tags existentes en la base de datos del blog.
    Devuelve una cadena formateada con los tags encontrados.
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
def crear_nuevo_tag(nombre: str) -> str:
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

if __name__ == "__main__":
    mcp.run()

