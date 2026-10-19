"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#StopRetrainingSchedulerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.model_name


class StopRetrainingSchedulerRequest(TypedDict, closed=True):
    model_name: "capo_lookoutequipment.types.model_name.ModelName"
    """<p>The name of the model whose retraining scheduler you want to stop.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StopRetrainingSchedulerRequest) -> dict:
    out: dict = {}
    out["ModelName"] = value["model_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StopRetrainingSchedulerRequest:
    out: StopRetrainingSchedulerRequest = {}  # type: ignore[typeddict-item]
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    else:
        out["model_name"] = ""
    return out
