from asyncio.log import logger
from app.schemas.usuarios import EditarPass
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import logging
from sqlalchemy import text


def update_url_pdf(db: Session, cod: int, url: str) -> bool:
    try:
        
        query = text(f"""UPDATE programas_formacion SET url_pdf = :url_pdf
                        WHERE cod_programa = :codigo""")
        db.execute(query, {"url_pdf": url, "codigo": cod})
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error al subir pdf: {e}")
        raise Exception("Error de base de datos al subir pdf")
    
    
def get_programa_by_codigo(db: Session, cod: int):
    try:
        query = text(f"""SELECT * FROM programas_formacion
                        WHERE cod_programa = :codigo""")
        result = db.execute(query, {"codigo": cod}).mappings()
        return result
    except SQLAlchemyError as e:
        logger.error(f"Error al consultar programa por código: {e}")
        raise Exception("Error de base de datos al consultar programa por código")
    