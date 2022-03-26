from flask_seeder import Seeder, Faker, generator
from ms.models import Role


class RoleSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 10

    def run(self):
        roles = (
            Role({"name": "admin"}),
            Role({"name": "client"}),
            Role({"name": "financial"}),
        )

        for _ in roles:
            role = Role.query.filter_by(name=_.name).first()
            if role is None:
                self.db.session.add(_)
