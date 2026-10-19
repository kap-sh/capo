"""Generated from Smithy shape ``com.amazonaws.bedrock#PutUseCaseForModelAccessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.acknowledgement_form_data_body


class PutUseCaseForModelAccessRequest(TypedDict, closed=True):
    form_data: (
        "capo_bedrock.types.acknowledgement_form_data_body.AcknowledgementFormDataBody"
    )
    """<p>Put customer profile Request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutUseCaseForModelAccessRequest) -> dict:
    out: dict = {}
    import capo_bedrock.types.acknowledgement_form_data_body

    out["formData"] = capo_bedrock.types.acknowledgement_form_data_body.serialize_json(
        value["form_data"]
    )
    return out


def deserialize_json(data: dict) -> PutUseCaseForModelAccessRequest:
    out: PutUseCaseForModelAccessRequest = {}  # type: ignore[typeddict-item]
    if data.get("formData") is not None:
        import capo_bedrock.types.acknowledgement_form_data_body

        out["form_data"] = (
            capo_bedrock.types.acknowledgement_form_data_body.deserialize_json(
                data["formData"]
            )
        )
    else:
        out["form_data"] = b""
    return out
