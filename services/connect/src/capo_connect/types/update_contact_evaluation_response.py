"""Generated from Smithy shape ``com.amazonaws.connect#UpdateContactEvaluationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.resource_id


class UpdateContactEvaluationResponse(TypedDict, closed=True):
    evaluation_id: "capo_connect.types.resource_id.ResourceId"
    """<p>A unique identifier for the contact evaluation.</p>"""
    evaluation_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the contact evaluation resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactEvaluationResponse) -> dict:
    out: dict = {}
    out["EvaluationId"] = value["evaluation_id"]
    out["EvaluationArn"] = value["evaluation_arn"]
    return out


def deserialize_json(data: dict) -> UpdateContactEvaluationResponse:
    out: UpdateContactEvaluationResponse = {}  # type: ignore[typeddict-item]
    if data.get("EvaluationId") is not None:
        out["evaluation_id"] = data["EvaluationId"]
    else:
        out["evaluation_id"] = ""
    if data.get("EvaluationArn") is not None:
        out["evaluation_arn"] = data["EvaluationArn"]
    else:
        out["evaluation_arn"] = ""
    return out
