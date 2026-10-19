"""Generated from Smithy shape ``com.amazonaws.machinelearning#GetEvaluationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id


class GetEvaluationInput(TypedDict, closed=True):
    evaluation_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>The ID of the <code>Evaluation</code> to retrieve. The evaluation of each <code>MLModel</code> is recorded and cataloged. The ID provides the means to access the information. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEvaluationInput) -> dict:
    out: dict = {}
    out["EvaluationId"] = value["evaluation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEvaluationInput:
    out: GetEvaluationInput = {}  # type: ignore[typeddict-item]
    if data.get("EvaluationId") is not None:
        out["evaluation_id"] = data["EvaluationId"]
    else:
        out["evaluation_id"] = ""
    return out
