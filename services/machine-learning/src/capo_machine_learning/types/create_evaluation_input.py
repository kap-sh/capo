"""Generated from Smithy shape ``com.amazonaws.machinelearning#CreateEvaluationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id
    import capo_machine_learning.types.entity_name


class CreateEvaluationInput(TypedDict, closed=True):
    evaluation_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>A user-supplied ID that uniquely identifies the <code>Evaluation</code>.</p>"""
    evaluation_name: NotRequired["capo_machine_learning.types.entity_name.EntityName"]
    """<p>A user-supplied name or description of the <code>Evaluation</code>.</p>"""
    ml_model_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>The ID of the <code>MLModel</code> to evaluate.</p> <p>The schema used in creating the <code>MLModel</code> must match the schema of the <code>DataSource</code> used in the <code>Evaluation</code>.</p>"""
    evaluation_data_source_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>The ID of the <code>DataSource</code> for the evaluation. The schema of the <code>DataSource</code> must match the schema used to create the <code>MLModel</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEvaluationInput) -> dict:
    out: dict = {}
    out["EvaluationId"] = value["evaluation_id"]
    if "evaluation_name" in value:
        out["EvaluationName"] = value["evaluation_name"]
    out["MLModelId"] = value["ml_model_id"]
    out["EvaluationDataSourceId"] = value["evaluation_data_source_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEvaluationInput:
    out: CreateEvaluationInput = {}  # type: ignore[typeddict-item]
    if data.get("EvaluationId") is not None:
        out["evaluation_id"] = data["EvaluationId"]
    else:
        out["evaluation_id"] = ""
    if data.get("EvaluationName") is not None:
        out["evaluation_name"] = data["EvaluationName"]
    if data.get("MLModelId") is not None:
        out["ml_model_id"] = data["MLModelId"]
    else:
        out["ml_model_id"] = ""
    if data.get("EvaluationDataSourceId") is not None:
        out["evaluation_data_source_id"] = data["EvaluationDataSourceId"]
    else:
        out["evaluation_data_source_id"] = ""
    return out
