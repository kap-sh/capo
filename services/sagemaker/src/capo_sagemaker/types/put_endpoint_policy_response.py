"""Generated from Smithy shape ``com.amazonaws.sagemaker#PutEndpointPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_arn


class PutEndpointPolicyResponse(TypedDict, closed=True):
    endpoint_arn: NotRequired["capo_sagemaker.types.endpoint_arn.EndpointArn"]
    """<p>The Amazon Resource Name (ARN) of the endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutEndpointPolicyResponse) -> dict:
    out: dict = {}
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutEndpointPolicyResponse:
    out: PutEndpointPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("EndpointArn") is not None:
        out["endpoint_arn"] = data["EndpointArn"]
    return out
