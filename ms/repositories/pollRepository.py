from sqlalchemy.sql import func
from ms.db import db
from ms.models import Poll
from .repository import Repository

class PollRepository(Repository):
    def get_model(self):
        return Poll

    def add(self, data):
        poll = self._model(data)
        self.db_save(poll)
        return poll

    def total(self):
        return self._model.query.count()

    def avgTime(self):
        res = db.session.query(
            func.avg(Poll.tfb),
            func.avg(Poll.ttw),
            func.avg(Poll.twa),
            func.avg(Poll.tins),
            func.avg(Poll.ttik)
        ).one()
        return {
            "facebook": round(res[0], 2),
            "twitter": round(res[1], 2),
            "whatsapp": round(res[2], 2),
            "instagram": round(res[3], 2),
            "tiktok:": round(res[4], 2)
        }

    def favsocialnet(self):
        label = func.count(Poll.favsn).label('total')
        fav = db.session.query(
            Poll.favsn,
            label
        )\
            .group_by(Poll.favsn)\
            .order_by(label.desc())\
            .all()

        return fav[0], fav[-1]

    def per_sn(self):
        sn = {
            "facebook": func.sum(Poll.tfb).label('tfb'),
            "whatsapp": func.sum(Poll.twa).label('twa'),
            "twitter": func.sum(Poll.ttw).label('ttw'),
            "instagram": func.sum(Poll.tins).label('tins'),
            "tiktok": func.sum(Poll.ttik).label('ttik'),
        }
        res = []

        for name, label in sn.items():
            range, hours = db.session.query(
                Poll.range_age, label
            )\
                .group_by(Poll.range_age)\
                .order_by(label.desc())\
                .limit(1)\
                .one()
            res.append({
                "label": name,
                "range": range,
                "hours": hours
            })

        return res
