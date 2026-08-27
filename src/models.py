from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

db = SQLAlchemy()


class Usuario(db.Model):
    __tablename__ = "usuario"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    apellido: Mapped[str] = mapped_column(String(50), nullable=False)
    fecha_suscripcion: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )

    favoritos: Mapped[list["Favorito"]] = relationship(
        back_populates="usuario",
        cascade="all, delete-orphan"
    )


class Planeta(db.Model):
    __tablename__ = "planeta"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    clima: Mapped[str] = mapped_column(String(100))
    terreno: Mapped[str] = mapped_column(String(100))
    poblacion: Mapped[str] = mapped_column(String(100))

    favoritos: Mapped[list["Favorito"]] = relationship(
        back_populates="planeta"
    )


class Personaje(db.Model):
    __tablename__ = "personaje"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    altura: Mapped[str] = mapped_column(String(50))
    peso: Mapped[str] = mapped_column(String(50))
    genero: Mapped[str] = mapped_column(String(50))
    especie: Mapped[str] = mapped_column(String(100))

    favoritos: Mapped[list["Favorito"]] = relationship(
        back_populates="personaje"
    )


class Favorito(db.Model):
    __tablename__ = "favorito"

    id: Mapped[int] = mapped_column(primary_key=True)

    usuario_id: Mapped[int] = mapped_column(
        ForeignKey("usuario.id"),
        nullable=False
    )

    planeta_id: Mapped[int] = mapped_column(
        ForeignKey("planeta.id"),
        nullable=True
    )

    personaje_id: Mapped[int] = mapped_column(
        ForeignKey("personaje.id"),
        nullable=True
    )

    usuario: Mapped["Usuario"] = relationship(
        back_populates="favoritos"
    )

    planeta: Mapped["Planeta"] = relationship(
        back_populates="favoritos"
    )

    personaje: Mapped["Personaje"] = relationship(
        back_populates="favoritos"
    )gi
