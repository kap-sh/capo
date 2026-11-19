"""Generated from Smithy shape ``com.amazonaws.comprehend#CreateEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_endpoint_arn
    import capo_comprehend.types.comprehend_model_arn


class CreateEndpointResponse(TypedDict, closed=True):
    endpoint_arn: NotRequired[
        "capo_comprehend.types.comprehend_endpoint_arn.ComprehendEndpointArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the endpoint being created.</p>"""
    model_arn: NotRequired[
        "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the model to which the endpoint is attached.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEndpointResponse) -> dict:
    out: dict = {}
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEndpointResponse:
    out: CreateEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("EndpointArn") is not None:
        out["endpoint_arn"] = data["EndpointArn"]
    if data.get("ModelArn") is not None:
        out["model_arn"] = data["ModelArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateEndpointResponse) -> dict:
    out: dict = {}
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    return out


def deserialize_cbor(data: dict) -> CreateEndpointResponse:
    out: CreateEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("EndpointArn") is not None:
        out["endpoint_arn"] = data["EndpointArn"]
    if data.get("ModelArn") is not None:
        out["model_arn"] = data["ModelArn"]
    return out
