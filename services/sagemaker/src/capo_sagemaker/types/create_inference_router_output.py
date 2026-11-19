"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateInferenceRouterOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_router_arn


class CreateInferenceRouterOutput(TypedDict, closed=True):
    inference_router_arn: NotRequired[
        "capo_sagemaker.types.inference_router_arn.InferenceRouterArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the inference router.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateInferenceRouterOutput) -> dict:
    out: dict = {}
    if "inference_router_arn" in value:
        out["InferenceRouterArn"] = value["inference_router_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateInferenceRouterOutput:
    out: CreateInferenceRouterOutput = {}  # type: ignore[typeddict-item]
    if data.get("InferenceRouterArn") is not None:
        out["inference_router_arn"] = data["InferenceRouterArn"]
    return out
