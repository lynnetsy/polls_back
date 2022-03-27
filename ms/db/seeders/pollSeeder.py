import random
from faker import Faker
from flask_seeder import Seeder
from ms.models import Poll

class PollSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 1

    def run(self):
        faker = Faker()
        ranges = ["18-25", "26-33", "34-40", "40+"]
        genders = ["M", "F"]
        sn = ["Facebook", "Whatsapp", "Twitter", "Instagram", "TikTok"]
        for _ in range(10):
            poll = Poll({
                "email": faker.email(),
                "range_age": random.choice(ranges),
                "gender": random.choice(genders),
                "favsn": random.choice(sn),
                "tfb": random.randint(1, 10),
                "tins": random.randint(1, 10),
                "ttik": random.randint(1, 10),
                "ttw": random.randint(1, 10),
                "twa": random.randint(1, 10),
            })
            self.db.session.add(poll)
