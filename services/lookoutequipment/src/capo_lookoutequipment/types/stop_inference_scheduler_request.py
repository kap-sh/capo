"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#StopInferenceSchedulerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.inference_scheduler_identifier


class StopInferenceSchedulerRequest(TypedDict, closed=True):
    inference_scheduler_name: "capo_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier"
    """<p>The name of the inference scheduler to be stopped. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StopInferenceSchedulerRequest) -> dict:
    out: dict = {}
    out["InferenceSchedulerName"] = value["inference_scheduler_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StopInferenceSchedulerRequest:
    out: StopInferenceSchedulerRequest = {}  # type: ignore[typeddict-item]
    if data.get("InferenceSchedulerName") is not None:
        out["inference_scheduler_name"] = data["InferenceSchedulerName"]
    else:
        out["inference_scheduler_name"] = ""
    return out
