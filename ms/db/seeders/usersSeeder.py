from faker import Faker
from flask_seeder import Seeder
from ms.models import Role, User


class UsersSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 20

    def run(self):
        adminRole = Role.query.filter_by(name="admin").first()
        clientRole = Role.query.filter_by(name="client").first()
        financialRole = Role.query.filter_by(name="financial").first()

        users = (
            User({
                "phone": "5512312312",
                "email": "admin@example.com",
                "role_id": adminRole.id,
            }),
            User({
                "phone": "5512312313",
                "email": "client@example.com",
                "role_id": clientRole.id,
            }),
            User({
                "phone": "5512312314",
                "email": "financial@example.com",
                "role_id": financialRole.id,
            })
        )

        for _ in users:
            user = User.query.filter_by(email=_.email).first()
            if user is None:
                _.set_password('secret')
                self.db.session.add(_)

        fake = Faker()
        for _ in range(5):
            client = User({
                "phone": fake.msisdn(),
                "email": fake.email(),
                "role_id": clientRole.id,
            })
            client.set_password("secret")
            self.db.session.add(client)
