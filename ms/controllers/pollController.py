from flask import jsonify, request, Response
from ms.repositories import PollRepository
from ms.decorators import form_validator
from ms.forms import AddForm

class PollController():
    def __init__(self):
        self.pollRepo = PollRepository()

    @form_validator(AddForm)
    def add(self, form):
        self.pollRepo.add(form.data)
        return jsonify(), 204
