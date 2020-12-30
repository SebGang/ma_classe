from sanic.response import json
from sanic_restful_api import reqparse, Resource, fields, marshal_with

from maclasse.tables import eleves

parser = reqparse.RequestParser()
parser.add_argument("id", dest="id")
parser.add_argument("nom", dest="nom")
parser.add_argument("prenom", dest="prenom")
parser.add_argument("date_naissance", dest="date_naissance")
parser.add_argument("note_trim_1", dest="note_trim_1")
parser.add_argument("note_trim_2", dest="note_trim_2")
parser.add_argument("note_trim_3", dest="note_trim_3")

student_fields = {
    "id": fields.Integer,
    "nom": fields.String,
    "prenom": fields.String,
    "date_naissance": fields.DateTime,
    "note_trim_1": fields.Float,
    "note_trim_2": fields.Float,
    "note_trim_3": fields.Float,
}


class AjoutEleve(Resource):
    async def get(self, request):
        query = eleves.select().order_by("nom")
        rows = await request.app.db.fetch_all(query=query)
        return json(
            {
                "eleves": [
                    {
                        "identifiant": row["id"],
                        "nom": row["nom"],
                        "prenom": row["prenom"],
                        "date de naissance": row["date_naissance"].isoformat(),
                        "note premier trimestre": row["note_trim_1"],
                        "note deuxieme trimestre": row["note_trim_2"],
                        "note troisieme trimestre": row["note_trim_3"],
                    }
                    for row in rows
                ]
            }
        )

    @marshal_with(student_fields)
    async def post(self, request):
        query = eleves.insert()
        args = parser.parse_args(request)
        values = {
            "id": args.id,
            "nom": args.nom,
            "prenom": args.prenom,
            "date_naissance": args.date_naissance,
            "note_trim_1": args.note_trim_1,
            "note_trim_2": args.note_trim_2,
            "note_trim_3": args.note_trim_3,
        }
        await request.app.db.execute(query=query, values=values)
        return 201


# def setup_routes(app):
#     @app.route("/")
#     async def liste_eleves(request):
#         query = eleves.select().order_by("nom")
#         rows = await request.app.db.fetch_all(query=query)
#         return json(
#             {
#                 "eleves": [
#                     {
#                         'nom': row["nom"],
#                         'prenom': row["prenom"],
#                         'date de naissance': row["date_naissance"].isoformat(),
#                         'note premier trimestre': row["note_trim_1"],
#                         'note deuxieme trimestre': row["note_trim_2"],
#                         'note troisieme trimestre': row["note_trim_3"]
#                     }
#                     for row in rows
#                 ]
#             }
#         )
