# Servidor MCP para FastAPI Blog

Este módulo implementa un servidor **Model Context Protocol (MCP)** utilizando `fastmcp`. Permite que agentes de IA (como n8n, LangChain, Claude Desktop) interactúen directamente con la base de datos del blog para gestionar etiquetas (tags), y extensible a posts y autores.

## Instalación y Ejecución

El servidor está configurado para correr con `fastmcp`.

### Desarrollo
Desde la raíz del proyecto:
```bash
# En Windows (PowerShell)
$env:PYTHONPATH="."; fastmcp dev src/mcp/server.py
```

## Herramientas Disponibles

Las siguientes herramientas están expuestas al agente. Todas aceptan parámetros de contexto opcionales (`sessionId`, `action`, etc.) para compatibilidad con n8n.

| Herramienta | Descripción | Parámetros Clave |
|CR|---|---|
| `listar_tags` | Devuelve una lista de todos los tags (ID y Nombre). | Ninguno |
| `buscar_tag_por_nombre` | Busca un tag específico por su nombre exacto. | `nombre` (str) |
| `crear_nuevo_tag` | Crea un nuevo tag si no existe. | `nombre` (str) |
| `actualizar_tag` | Modifica el nombre de un tag existente. | `tag_id` (int), `nuevo_nombre` (str) |
| `eliminar_tag` | Elimina permanentemente un tag. | `tag_id` (int) |

## Integración con n8n (AI Agent)

Para que tu agente de n8n entienda cómo usar estas herramientas correctamente, utiliza el siguiente **System Prompt** en la configuración del nodo AI Agent.

### System Prompt Recomendado

```markdown
Eres un Agente Técnico de Operaciones de Base de Datos que interactúa con un backend FastAPI a través del Protocolo de Contexto de Modelo (MCP).

### CONTEXTO DEL SISTEMA
Estás conectado a un servidor MCP (`src/mcp/server.py`) que actúa como interfaz para una base de datos PostgreSQL gestionada con SQLAlchemy. Tu responsabilidad es manipular la entidad `Tag` asegurando la integridad de los datos.

### ESPECIFICACIÓN DE HERRAMIENTAS MCP
Debes invocar las herramientas utilizando estrictamente los parámetros definidos. Los parámetros de contexto (sessionId) son automáticos.

#### 1. `listar_tags`
- Firma: `listar_tags()` -> str
- Uso: Validación masiva o exploración.

#### 2. `buscar_tag_por_nombre`
- Firma: `buscar_tag_por_nombre(nombre: str)` -> str
- Uso: Verificar existencia antes de crear o buscar ID para borrar/editar.

#### 3. `crear_nuevo_tag`
- Firma: `crear_nuevo_tag(nombre: str)` -> str
- Restricción: El nombre debe ser único.

#### 4. `actualizar_tag`
- Firma: `actualizar_tag(tag_id: int, nuevo_nombre: str)` -> str
- Nota: Requiere ID numérico.

#### 5. `eliminar_tag`
- Firma: `eliminar_tag(tag_id: int)` -> str
- Nota: Requiere ID numérico.

### PROTOCOLO DE OPERACIÓN
1. **Verificación**: Antes de CREAR, usa `buscar_tag_por_nombre` para evitar duplicados.
2. **Resolución de IDs**: Si el usuario pide borrar/editar por NOMBRE, primero busca el ID con `buscar_tag_por_nombre` y luego ejecuta la acción con el ID obtenido.
3. **Errores**: Si recibes un error, infórmalo textualmente al usuario.
```

