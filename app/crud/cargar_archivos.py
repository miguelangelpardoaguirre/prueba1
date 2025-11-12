
from fastapi import APIRouter, UploadFile, File, Depends
import pandas as pd
from sqlalchemy.orm import Session
from io import BytesIO
from app.crud.cargar_archivos import insertar_datos_en_bd
from core.database import get_db

router = APIRouter()

@router.post("/upload-excel-pe04/")
async def upload_excel(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    contents = await file.read()
    df = pd.read_excel(     #pd es un alias de pandas trayendo todo lo que contiene / pandas contiene la funcion npara leer excel 
        BytesIO(contents),
        engine="openpyxl",
        skiprows=4, # Saltar las primeras 4 filas dl excel / es opcional 
        usecols=["CODIGO_REGIONAL", "NOMBRE_REGIONAL",	"CODIGO_CENTRO", "NOMBRE_CENTRO",	"IDENTIFICADOR_FICHA",	"IDENTIFICADOR_UNICO_FICHA",	"ESTADO_CURSO",	"CODIGO_NIVEL_FORMACION",	"NIVEL_FORMACION",	"CODIGO_JORNADA",	"NOMBRE_JORNADA",	"TIPO_DE_FORMACION",	"FECHA_INICIO_FICHA",	"FECHA_TERMINACION_FICHA",	"ETAPA_FICHA",	"MODALIDAD_FORMACION",	"NOMBRE_RESPONSABLE",	"NUMERO_IDENTIFICACION_EMPRESA",	"TIPO_IDENTIFICACION_EMPRESA",	"NOMBRE_EMPRESA",	"CODIGO_SECTOR_PROGRAMA",	"NOMBRE_SECTOR_PROGRAMA",	"CODIGO_OCUPACION",	"NOMBRE_OCUPACION",	"CODIGO_PROGRAMA",	"VERSION_PROGRAMA",	"NOMBRE_PROGRAMA_FORMACION",	"CODIGO_PAIS_CURSO",	"NOMBRE_PAIS_CURSO",	"CODIGO_DEPARTAMENTO_CURSO",	"NOMBRE_DEPARTAMENTO_CURSO",	"CODIGO_MUNICIPIO_CURSO",	"NOMBRE_MUNICIPIO_CURSO",	"CODIGO_CONVENIO",	"NOMBRE_CONVENIO",	"AMPLIACION_COBERTURA",	"CODIGO_PROGRAMA_ESPECIAL",	"NOMBRE_PROGRAMA_ESPECIAL",	"NUMERO_CURSOS",	"TOTAL_APRENDICES_MASCULINOS",	"TOTAL_APRENDICES_FEMENINOS",	"TOTAL_APRENDICES_NOBINARIO",	"TOTAL_APRENDICES",	"HORAS_PLANTA",	"HORAS_CONTRATISTAS",	"HORAS_CONTRATISTAS_EXTERNOS",	"HORAS_MONITORES",	"HORAS_INST_EMPRESA",	"TOTAL_HORAS",	"TOTAL_APRENDICES_ACTIVOS",	"DURACION_PROGRAMA",	"NOMBRE_NUEVO_SECTOR" ],  # Nombres reales
        dtype=str
    )
    print(df.head())  # paréntesis
    print(df.columns)
    print(df.dtypes)

    # Renombrar columnas
    df = df.rename(columns={
    "CODIGO_REGIONAL": "CODIGO_REGIONAL",
    "NOMBRE_REGIONAL": "NOMBRE_REGIONAL",	
    "CODIGO_CENTRO": "CODIGO_CENTRO", 
    "NOMBRE_CENTRO": "NOMBRE_CENTRO",	
    "IDENTIFICADOR_FICHA": "IDENTIFICADOR_FICHA",	
    "IDENTIFICADOR_UNICO_FICHA": "IDENTIFICADOR_UNICO_FICHA",	
    "ESTADO_CURSO": "ESTADO_CURSO",	
    "CODIGO_NIVEL_FORMACION": "CODIGO_NIVEL_FORMACION",	
    "NIVEL_FORMACION": "NIVEL_FORMACION",	
    "CODIGO_JORNADA": "CODIGO_JORNADA",	
    "NOMBRE_JORNADA": "NOMBRE_JORNADA",	
    "TIPO_DE_FORMACION": "TIPO_DE_FORMACION",	
    "FECHA_INICIO_FICHA": "FECHA_INICIO_FICHA",	
    "FECHA_TERMINACION_FICHA": "FECHA_TERMINACION_FICHA",	
    "ETAPA_FICHA": "ETAPA_FICHA",	
    "FECHA_TERMINACION_FICHA": "FECHA_TERMINACION_FICHA",	
    "NOMBRE_RESPONSABLE":"NOMBRE_RESPONSABLE",	
    "NUMERO_IDENTIFICACION_EMPRESA":"NUMERO_IDENTIFICACION_EMPRESA",	
    "TIPO_IDENTIFICACION_EMPRESA":"TIPO_IDENTIFICACION_EMPRESA",	
    "NOMBRE_EMPRESA":"NOMBRE_EMPRESA",	
    "CODIGO_SECTOR_PROGRAMA"	:"CODIGO_SECTOR_PROGRAMA",	
    "NOMBRE_SECTOR_PROGRAMA"	:"NOMBRE_SECTOR_PROGRAMA",	
    "CODIGO_OCUPACION"	:"CODIGO_OCUPACION"	,
    "NOMBRE_OCUPACION"	:"NOMBRE_OCUPACION"	,
    "CODIGO_PROGRAMA"	:"CODIGO_PROGRAMA"	,
    "VERSION_PROGRAMA"	:"VERSION_PROGRAMA"	,
    "NOMBRE_PROGRAMA_FORMACION"	:"NOMBRE_PROGRAMA_FORMACION",	
    "CODIGO_PAIS_CURSO"	:"CODIGO_PAIS_CURSO",	
    "NOMBRE_PAIS_CURSO"	:"NOMBRE_PAIS_CURSO",	
    "CODIGO_DEPARTAMENTO_CURSO"	:"CODIGO_DEPARTAMENTO_CURSO",	
    "NOMBRE_DEPARTAMENTO_CURSO"	:"NOMBRE_DEPARTAMENTO_CURSO",	
    "CODIGO_MUNICIPIO_CURSO"	:"CODIGO_MUNICIPIO_CURSO",	
    "NOMBRE_MUNICIPIO_CURSO"	:"NOMBRE_MUNICIPIO_CURSO",	
    "CODIGO_CONVENIO"	:"CODIGO_CONVENIO",	
    "NOMBRE_CONVENIO"	:"NOMBRE_CONVENIO",	
    "AMPLIACION_COBERTURA"	:"AMPLIACION_COBERTURA",	
    "CODIGO_PROGRAMA_ESPECIAL"	:"CODIGO_PROGRAMA_ESPECIAL",	
    "NOMBRE_PROGRAMA_ESPECIAL"	:"NOMBRE_PROGRAMA_ESPECIAL",	
    "NUMERO_CURSOS"	:"NUMERO_CURSOS",	
    "TOTAL_APRENDICES_MASCULINOS"	:"TOTAL_APRENDICES_MASCULINOS",	
    "TOTAL_APRENDICES_FEMENINOS"	:"TOTAL_APRENDICES_FEMENINOS",	
    "TOTAL_APRENDICES_NOBINARIO"	:"TOTAL_APRENDICES_NOBINARIO",	
    "TOTAL_APRENDICES"	:"TOTAL_APRENDICES",	
    "HORAS_PLANTA"	:"HORAS_PLANTA",	
    "HORAS_CONTRATISTAS"	:"HORAS_CONTRATISTAS",	
    "HORAS_CONTRATISTAS_EXTERNOS"	:"HORAS_CONTRATISTAS_EXTERNOS",	
    "HORAS_MONITORES"	:"HORAS_MONITORES",	
    "HORAS_INST_EMPRESA"	:"HORAS_INST_EMPRESA",	
    "TOTAL_HORAS"	:"TOTAL_HORAS",	
    "TOTAL_APRENDICES_ACTIVOS"	:"TOTAL_APRENDICES_ACTIVOS",	
    "DURACION_PROGRAMA"	:"DURACION_PROGRAMA",	
    "NOMBRE_NUEVO_SECTOR":"NOMBRE_NUEVO_SECTOR"
    })

    print(df.head())  # paréntesis

    # Eliminar filas con campos obligatorios faltantes
    required_fields = [
        "cod_ficha", "cod_centro", "cod_programa", "la_version", "nombre", 
        "fecha_inicio", "fecha_fin", "etapa", "responsable", "nombre_municipio"
    ]
    df = df.dropna(subset=required_fields)

    # Convertir columnas a tipo numérico
    for col in ["cod_ficha", "cod_programa", "la_version", "cod_centro"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

    print(df.head())  # paréntesis
    print(df.dtypes)

    # Convertir fechas
    df["fecha_inicio"] = pd.to_datetime(df["fecha_inicio"], errors="coerce").dt.date
    df["fecha_fin"] = pd.to_datetime(df["fecha_fin"], errors="coerce").dt.date

    # Asegurar columnas no proporcionadas
    df["hora_inicio"] = "00:00:00"
    df["hora_fin"] = "00:00:00"
    df["aula_actual"] = ""

    # Crear DataFrame de programas únicos
    df_programas = df[["cod_programa", "la_version", "nombre"]].drop_duplicates()
    df_programas["horas_lectivas"] = 0
    df_programas["horas_productivas"] = 0

    print(df_programas.head())

    # Eliminar la columna nombre del df.
    df = df.drop('nombre', axis=1)
    print(df.head())

    resultados = insertar_datos_en_bd(db, df_programas, df)
    return resultados