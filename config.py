# ============================================================
# config.py — Befra Workshop: Datos No Estructurados
# Edita este archivo para adaptar el demo a tu entorno.
# ============================================================

# --- Unity Catalog -------------------------------------------
CATALOG = "jgworkspaceclassic_catalog"
SCHEMA  = "befra_demo"

# --- Rutas de datos ------------------------------------------
VOLUME_PATH      = f"/Volumes/{CATALOG}/{SCHEMA}/datos_no_estructurados/MUDO/"
PARSED_TABLE     = f"{CATALOG}.{SCHEMA}.parsed_befra_docs"
CHUNKS_TABLE     = f"{CATALOG}.{SCHEMA}.befra_chunks"
EMBEDDINGS_TABLE = f"{CATALOG}.{SCHEMA}.befra_embeddings"

# --- Lakebase pgvector ---------------------------------------
PROJECT_ID  = "demo-befra"
BRANCH_ID   = "production"
ENDPOINT_ID = "primary"
DB_NAME     = "databricks_postgres"

# --- Modelos Foundation Model APIs ---------------------------
# Embeddings (1024 dims). Alternativa: databricks-bge-large-en
EMBEDDING_MODEL = "databricks-gte-large-en"
# LLM para generación de respuestas (RAG)
LLM_MODEL       = "databricks-meta-llama-3-3-70b-instruct"

# --- Parámetros del pipeline ---------------------------------
VECTOR_DIM   = 1024   # debe coincidir con el modelo de embeddings
BATCH_SIZE   = 50     # chunks por llamada a la API de embeddings
BATCH_INSERT = 100    # filas por batch al insertar en pgvector
TOP_K        = 5      # resultados en la búsqueda semántica

# --- AI Search (Vector Search) — alternativa a Lakebase ------
# Nombre del endpoint (se crea automáticamente si no existe)
VS_ENDPOINT_NAME = "befra-vs-endpoint"
# Nombre del índice en Unity Catalog (derivado del schema)
VS_INDEX_NAME    = f"{CATALOG}.{SCHEMA}.befra_vs_index"

# --- Video AI Search (Vector Search) -------------------------
# Endpoint reutilizado del pipeline de documentos
VIDEO_VS_ENDPOINT_NAME = VS_ENDPOINT_NAME          # "befra-vs-endpoint"
# Índice específico para transcripciones de video
VIDEO_VS_INDEX_NAME    = f"{CATALOG}.{SCHEMA}.video_transcription_vs_index"
# Tabla Delta fuente del índice (con CDF + PRIMARY KEY)
VIDEO_VS_SOURCE_TABLE  = f"{CATALOG}.{SCHEMA}.video_transcription_vs_source"

# ============================================================
# SECCIÓN 2 — Pipeline de Video (transcripción + embeddings)
# ============================================================

# --- Video fuente ----------------------------------------
VIDEO_NAME   = "Lanzamiento Cat 3 - 2026-001.mp4"
VIDEO_PATH   = f"/Volumes/{CATALOG}/{SCHEMA}/datos_no_estructurados/MUDO/Betterware/Videos/{VIDEO_NAME}"
AUDIO_TMP    = "/tmp/audio_befra.wav"          # archivo temporal para Whisper

# --- Tabla de destino en Lakebase ------------------------
VIDEO_TABLE_NAME = "video_transcription_embeddings"

# --- Lakebase (comparte PROJECT_ID/BRANCH_ID/ENDPOINT_ID) --
LAKEBASE_ENDPOINT = f"projects/{PROJECT_ID}/branches/{BRANCH_ID}/endpoints/{ENDPOINT_ID}"
LAKEBASE_HOST     = "ep-square-term-d2nsxvwg.database.us-east-1.cloud.databricks.com"
LAKEBASE_DB       = DB_NAME                   # alias para mantener compatibilidad

# --- Extracción de frames del video ---------------------
# 1 frame cada N segundos (1 = máximo detalle, 5-10 = más ligero)
FRAME_INTERVAL_S   = 5
# Tabla Delta donde se almacena el resultado de ai_parse_document por frame
VIDEO_FRAMES_TABLE = f"{CATALOG}.{SCHEMA}.video_frames_parsed"

# --- Whisper (transcripción de audio) --------------------
# Opciones: 'tiny' | 'base' | 'small' | 'medium' | 'large'
# 'small' = buen balance velocidad/precisión en español
# 'medium' o 'large' = mayor precisión (requiere GPU)
WHISPER_MODEL = "small"

# --- Modelo de embeddings multilingüe (768 dims) ----------
# Compatible con español e inglés
VIDEO_EMBEDDING_MODEL = "paraphrase-multilingual-mpnet-base-v2"
VIDEO_EMBEDDING_DIM   = 768
