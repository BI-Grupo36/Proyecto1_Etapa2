from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Resena(Base):
    __tablename__ = "resenas"
    id = Column(Integer, primary_key=True, index=True)
    contenido = Column(Text, nullable=False)
    calificacion = Column(Integer)

app = FastAPI()


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/resenas/")
def crear_resena(contenido: str, calificacion: int, db: Session = Depends(get_db)):
    nueva_resena = Resena(contenido=contenido, calificacion=calificacion)
    db.add(nueva_resena)
    db.commit()
    return {"message": "Reseña creada exitosamente"}

@app.get("/resenas/")
def obtener_resenas(db: Session = Depends(get_db)):
    resenas = db.query(Resena).all()
    return resenas

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
