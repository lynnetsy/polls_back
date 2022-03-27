from flask import jsonify, request, Response
from ms.repositories import PollRepository
from ms.decorators import form_validator
from ms.forms import AddForm

class PollController():
    def __init__(self):
        self.pollRepo = PollRepository()

    def stats(self):
        fav, less_fav = self.pollRepo.favsocialnet()
        return jsonify({
            "total": self.pollRepo.total(),
            "avg_time": self.pollRepo.avgTime(),
            "favorite": {
                "label": fav[0],
                "total": fav[1]
            },
            "less_fav": {
                "label": less_fav[0],
                "total": less_fav[1]
            },
            "per_sn": self.pollRepo.per_sn()
        }), 200

    @form_validator(AddForm)
    def add(self, form):
        self.pollRepo.add(form.data)
        return jsonify(), 204

