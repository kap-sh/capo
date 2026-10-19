"""Generated from Smithy shape ``com.amazonaws.machinelearning#DeleteRealtimeEndpointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id


class DeleteRealtimeEndpointInput(TypedDict, closed=True):
    ml_model_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>The ID assigned to the <code>MLModel</code> during creation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRealtimeEndpointInput) -> dict:
    out: dict = {}
    out["MLModelId"] = value["ml_model_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRealtimeEndpointInput:
    out: DeleteRealtimeEndpointInput = {}  # type: ignore[typeddict-item]
    if data.get("MLModelId") is not None:
        out["ml_model_id"] = data["MLModelId"]
    else:
        out["ml_model_id"] = ""
    return out
