# Changelog - Proyecto CRUD FastAPI + MCP

## [Unreleased] - 2025-11-27

### Añadido
- **Servidor MCP (`src/mcp/server.py`)**: Implementación inicial de servidor FastMCP.
- **Herramientas MCP**:
  - `listar_tags`: Listado general.
  - `crear_nuevo_tag`: Creación de registros.
  - `buscar_tag_por_nombre`: Búsqueda exacta.
  - `actualizar_tag`: Edición por ID.
  - `eliminar_tag`: Borrado por ID.
- **Compatibilidad n8n**: Se añadieron parámetros opcionales (`sessionId`, `action`, `chatInput`, `tool`, `toolCallId`) a todas las herramientas MCP para evitar errores de validación estricta de Pydantic cuando n8n inyecta contexto.
- **Documentación**: `src/mcp/README.md` con instrucciones y System Prompt.

### Corregido
- **Importación Circular/Faltante**: Se corrigió el import en `src/mcp/server.py` y `src/api/routes/tags.py` para usar el módulo `src.crud.tag` completo en lugar de intentar importar un objeto `tag` inexistente.
- **Configuración Alembic**:
  - Se modificó `alembic/env.py` para manejar URLs de base de datos con caracteres especiales (`%`) escapándolos.
  - Se implementó lógica para reemplazar automáticamente `postgres://` por `postgresql://` en la cadena de conexión.
- **Migraciones**: Se realizó un reset limpio de migraciones (borrado de tablas y carpeta `versions`) para solucionar inconsistencias de claves foráneas (`DependentObjectsStillExist`).
- **Modelo Post**: Se corrigió el nombre de la relación en `src/models/post.py` (de `authors` a `author`) para coincidir con `back_populates` en `src/models/author.py`.

### Infraestructura
- **Git**: Inicialización de repositorio, configuración de `.gitignore` y subida a GitHub.
- **Dependencias**: Actualización de `requirements.txt`.

