"""Generated from Smithy shape ``com.amazonaws.connect#ActivateEvaluationFormResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.resource_id
    import capo_connect.types.version_number


class ActivateEvaluationFormResponse(TypedDict, closed=True):
    evaluation_form_id: "capo_connect.types.resource_id.ResourceId"
    """<p>The unique identifier for the evaluation form.</p>"""
    evaluation_form_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the evaluation form resource.</p>"""
    evaluation_form_version: "capo_connect.types.version_number.VersionNumber"
    """<p>A version of the evaluation form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActivateEvaluationFormResponse) -> dict:
    out: dict = {}
    out["EvaluationFormId"] = value["evaluation_form_id"]
    out["EvaluationFormArn"] = value["evaluation_form_arn"]
    out["EvaluationFormVersion"] = value.get("evaluation_form_version", 0)
    return out


def deserialize_json(data: dict) -> ActivateEvaluationFormResponse:
    out: ActivateEvaluationFormResponse = {}  # type: ignore[typeddict-item]
    if data.get("EvaluationFormId") is not None:
        out["evaluation_form_id"] = data["EvaluationFormId"]
    else:
        out["evaluation_form_id"] = ""
    if data.get("EvaluationFormArn") is not None:
        out["evaluation_form_arn"] = data["EvaluationFormArn"]
    else:
        out["evaluation_form_arn"] = ""
    if data.get("EvaluationFormVersion") is not None:
        out["evaluation_form_version"] = data["EvaluationFormVersion"]
    else:
        out["evaluation_form_version"] = 0
    return out
