"""Generated from Smithy shape ``com.amazonaws.comprehend#UpdateEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_model_arn


class UpdateEndpointResponse(TypedDict, closed=True):
    desired_model_arn: NotRequired[
        "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the new model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEndpointResponse) -> dict:
    out: dict = {}
    if "desired_model_arn" in value:
        out["DesiredModelArn"] = value["desired_model_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEndpointResponse:
    out: UpdateEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("DesiredModelArn") is not None:
        out["desired_model_arn"] = data["DesiredModelArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateEndpointResponse) -> dict:
    out: dict = {}
    if "desired_model_arn" in value:
        out["DesiredModelArn"] = value["desired_model_arn"]
    return out


def deserialize_cbor(data: dict) -> UpdateEndpointResponse:
    out: UpdateEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("DesiredModelArn") is not None:
        out["desired_model_arn"] = data["DesiredModelArn"]
    return out
