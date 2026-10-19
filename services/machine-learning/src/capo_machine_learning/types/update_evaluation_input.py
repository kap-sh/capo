"""Generated from Smithy shape ``com.amazonaws.machinelearning#UpdateEvaluationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id
    import capo_machine_learning.types.entity_name


class UpdateEvaluationInput(TypedDict, closed=True):
    evaluation_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>The ID assigned to the <code>Evaluation</code> during creation.</p>"""
    evaluation_name: "capo_machine_learning.types.entity_name.EntityName"
    """<p>A new user-supplied name or description of the <code>Evaluation</code> that will replace the current content. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEvaluationInput) -> dict:
    out: dict = {}
    out["EvaluationId"] = value["evaluation_id"]
    out["EvaluationName"] = value["evaluation_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEvaluationInput:
    out: UpdateEvaluationInput = {}  # type: ignore[typeddict-item]
    if data.get("EvaluationId") is not None:
        out["evaluation_id"] = data["EvaluationId"]
    else:
        out["evaluation_id"] = ""
    if data.get("EvaluationName") is not None:
        out["evaluation_name"] = data["EvaluationName"]
    else:
        out["evaluation_name"] = ""
    return out
