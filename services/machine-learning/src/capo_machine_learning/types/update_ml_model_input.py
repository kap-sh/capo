"""Generated from Smithy shape ``com.amazonaws.machinelearning#UpdateMLModelInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id
    import capo_machine_learning.types.entity_name
    import capo_machine_learning.types.score_threshold


class UpdateMLModelInput(TypedDict, closed=True):
    ml_model_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>The ID assigned to the <code>MLModel</code> during creation.</p>"""
    ml_model_name: NotRequired["capo_machine_learning.types.entity_name.EntityName"]
    """<p>A user-supplied name or description of the <code>MLModel</code>.</p>"""
    score_threshold: NotRequired[
        "capo_machine_learning.types.score_threshold.ScoreThreshold"
    ]
    """<p>The <code>ScoreThreshold</code> used in binary classification <code>MLModel</code> that marks the boundary between a positive prediction and a negative prediction.</p> <p>Output values greater than or equal to the <code>ScoreThreshold</code> receive a positive result from the <code>MLModel</code>, such as <code>true</code>. Output values less than the <code>ScoreThreshold</code> receive a negative response from the <code>MLModel</code>, such as <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMLModelInput) -> dict:
    out: dict = {}
    out["MLModelId"] = value["ml_model_id"]
    if "ml_model_name" in value:
        out["MLModelName"] = value["ml_model_name"]
    if "score_threshold" in value:
        out["ScoreThreshold"] = (
            "NaN"
            if value["score_threshold"] != value["score_threshold"]
            else "Infinity"
            if value["score_threshold"] == float("inf")
            else "-Infinity"
            if value["score_threshold"] == float("-inf")
            else value["score_threshold"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMLModelInput:
    out: UpdateMLModelInput = {}  # type: ignore[typeddict-item]
    if data.get("MLModelId") is not None:
        out["ml_model_id"] = data["MLModelId"]
    else:
        out["ml_model_id"] = ""
    if data.get("MLModelName") is not None:
        out["ml_model_name"] = data["MLModelName"]
    if data.get("ScoreThreshold") is not None:
        out["score_threshold"] = float(data["ScoreThreshold"])
    return out
