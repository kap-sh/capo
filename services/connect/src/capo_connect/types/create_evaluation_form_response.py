"""Generated from Smithy shape ``com.amazonaws.connect#CreateEvaluationFormResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.resource_id


class CreateEvaluationFormResponse(TypedDict, closed=True):
    evaluation_form_id: "capo_connect.types.resource_id.ResourceId"
    """<p>The unique identifier for the evaluation form.</p>"""
    evaluation_form_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the evaluation form resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEvaluationFormResponse) -> dict:
    out: dict = {}
    out["EvaluationFormId"] = value["evaluation_form_id"]
    out["EvaluationFormArn"] = value["evaluation_form_arn"]
    return out


def deserialize_json(data: dict) -> CreateEvaluationFormResponse:
    out: CreateEvaluationFormResponse = {}  # type: ignore[typeddict-item]
    if data.get("EvaluationFormId") is not None:
        out["evaluation_form_id"] = data["EvaluationFormId"]
    else:
        out["evaluation_form_id"] = ""
    if data.get("EvaluationFormArn") is not None:
        out["evaluation_form_arn"] = data["EvaluationFormArn"]
    else:
        out["evaluation_form_arn"] = ""
    return out
