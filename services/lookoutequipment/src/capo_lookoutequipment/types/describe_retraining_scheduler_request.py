"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeRetrainingSchedulerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.model_name


class DescribeRetrainingSchedulerRequest(TypedDict, closed=True):
    model_name: "capo_lookoutequipment.types.model_name.ModelName"
    """<p>The name of the model that the retraining scheduler is attached to. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRetrainingSchedulerRequest) -> dict:
    out: dict = {}
    out["ModelName"] = value["model_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRetrainingSchedulerRequest:
    out: DescribeRetrainingSchedulerRequest = {}  # type: ignore[typeddict-item]
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    else:
        out["model_name"] = ""
    return out
