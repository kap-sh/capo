"""Generated from Smithy shape ``com.amazonaws.machinelearning#GetMLModelInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id
    import capo_machine_learning.types.verbose


class GetMLModelInput(TypedDict, closed=True):
    ml_model_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>The ID assigned to the <code>MLModel</code> at creation.</p>"""
    verbose: NotRequired["capo_machine_learning.types.verbose.Verbose"]
    """<p>Specifies whether the <code>GetMLModel</code> operation should return <code>Recipe</code>.</p> <p>If true, <code>Recipe</code> is returned.</p> <p>If false, <code>Recipe</code> is not returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMLModelInput) -> dict:
    out: dict = {}
    out["MLModelId"] = value["ml_model_id"]
    if "verbose" in value:
        out["Verbose"] = value["verbose"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMLModelInput:
    out: GetMLModelInput = {}  # type: ignore[typeddict-item]
    if data.get("MLModelId") is not None:
        out["ml_model_id"] = data["MLModelId"]
    else:
        out["ml_model_id"] = ""
    if data.get("Verbose") is not None:
        out["verbose"] = data["Verbose"]
    return out
