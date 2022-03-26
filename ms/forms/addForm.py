from flaskFormRequest import FormRequest
from flaskFormRequest.validators import (
    Email,
    Exists,
    Max,
    Min,
    Required,
    Unique,
    In,
    Integer,
)
from ms.models import Poll

class AddForm(FormRequest):
    def rules(self):
        return {
            "email": [
                Required(),
                Max(255),
                Email(),
                Unique(Poll)
            ],
            "range_age": [
                Required(),
                In([
                    "18-25",
                    "26-33",
                    "34-40",
                    "40+"
                ])
            ],
            "gender": [
                Required(),
                In(["M", "F"])
            ],
            "favsn": [
                Required(),
                In([
                    "Facebook",
                    "Whatsapp",
                    "Twitter",
                    "Instagram",
                    "TikTok"
                ])
            ],
            "tfb": [
                # Required(),
                Integer(),
            ],
            "twa": [
                # Required(),
                Integer(),
            ],
            "ttw": [
                # Required(),
                Integer(),
            ],
            "tins": [
                # Required(),
                Integer(),
            ],
            "ttik": [
                # Required(),
                Integer(),
            ],
        }
