"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteInferenceRouterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_router_name


class DeleteInferenceRouterInput(TypedDict, closed=True):
    inference_router_name: NotRequired[
        "capo_sagemaker.types.inference_router_name.InferenceRouterName"
    ]
    """<p>The name of the inference router to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteInferenceRouterInput) -> dict:
    out: dict = {}
    if "inference_router_name" in value:
        out["InferenceRouterName"] = value["inference_router_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteInferenceRouterInput:
    out: DeleteInferenceRouterInput = {}  # type: ignore[typeddict-item]
    if data.get("InferenceRouterName") is not None:
        out["inference_router_name"] = data["InferenceRouterName"]
    return out
