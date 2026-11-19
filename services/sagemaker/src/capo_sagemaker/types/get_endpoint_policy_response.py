"""Generated from Smithy shape ``com.amazonaws.sagemaker#GetEndpointPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_arn
    import capo_sagemaker.types.endpoint_name
    import capo_sagemaker.types.endpoint_policy_document


class GetEndpointPolicyResponse(TypedDict, closed=True):
    endpoint_name: NotRequired["capo_sagemaker.types.endpoint_name.EndpointName"]
    """<p>The name of the endpoint.</p>"""
    endpoint_arn: NotRequired["capo_sagemaker.types.endpoint_arn.EndpointArn"]
    """<p>The Amazon Resource Name (ARN) of the endpoint.</p>"""
    resource_policy: NotRequired[
        "capo_sagemaker.types.endpoint_policy_document.EndpointPolicyDocument"
    ]
    """<p>The endpoint policy, as a JSON policy document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEndpointPolicyResponse) -> dict:
    out: dict = {}
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
    if "resource_policy" in value:
        out["ResourcePolicy"] = value["resource_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEndpointPolicyResponse:
    out: GetEndpointPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("EndpointName") is not None:
        out["endpoint_name"] = data["EndpointName"]
    if data.get("EndpointArn") is not None:
        out["endpoint_arn"] = data["EndpointArn"]
    if data.get("ResourcePolicy") is not None:
        out["resource_policy"] = data["ResourcePolicy"]
    return out
