"""Generated from Smithy shape ``com.amazonaws.sagemaker#PutEndpointPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_name
    import capo_sagemaker.types.endpoint_policy_document


class PutEndpointPolicyRequest(TypedDict, closed=True):
    endpoint_name: NotRequired["capo_sagemaker.types.endpoint_name.EndpointName"]
    """<p>The name of the endpoint. The endpoint must be in your account and in the current Amazon Web Services Region.</p>"""
    resource_policy: NotRequired[
        "capo_sagemaker.types.endpoint_policy_document.EndpointPolicyDocument"
    ]
    """<p>The endpoint policy, as a JSON policy document. The policy can contain only ASCII characters. For information about the policy rules, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router-cross-account.html">Use destinations in other accounts</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutEndpointPolicyRequest) -> dict:
    out: dict = {}
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "resource_policy" in value:
        out["ResourcePolicy"] = value["resource_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutEndpointPolicyRequest:
    out: PutEndpointPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("EndpointName") is not None:
        out["endpoint_name"] = data["EndpointName"]
    if data.get("ResourcePolicy") is not None:
        out["resource_policy"] = data["ResourcePolicy"]
    return out
