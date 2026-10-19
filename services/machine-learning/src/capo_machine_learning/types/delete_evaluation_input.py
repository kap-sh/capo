"""Generated from Smithy shape ``com.amazonaws.machinelearning#DeleteEvaluationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id


class DeleteEvaluationInput(TypedDict, closed=True):
    evaluation_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>A user-supplied ID that uniquely identifies the <code>Evaluation</code> to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEvaluationInput) -> dict:
    out: dict = {}
    out["EvaluationId"] = value["evaluation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEvaluationInput:
    out: DeleteEvaluationInput = {}  # type: ignore[typeddict-item]
    if data.get("EvaluationId") is not None:
        out["evaluation_id"] = data["EvaluationId"]
    else:
        out["evaluation_id"] = ""
    return out
