import sqlalchemy

metadata = sqlalchemy.MetaData()

eleves = sqlalchemy.Table(
    "eleves_cm1",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("nom", sqlalchemy.String(length=50), nullable=False),
    sqlalchemy.Column("prenom", sqlalchemy.String(length=50), nullable=False),
    sqlalchemy.Column("date_naissance", sqlalchemy.DateTime, nullable=False),
    sqlalchemy.Column("note_trim_1", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("note_trim_2", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("note_trim_3", sqlalchemy.Float, nullable=False),
)

