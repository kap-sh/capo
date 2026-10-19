"""Generated from Smithy shape ``com.amazonaws.billing#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.policy_document
    import capo_billing.types.resource_arn


class GetResourcePolicyResponse(TypedDict, closed=True):
    resource_arn: "capo_billing.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the billing view resource to which the policy is attached to. </p>"""
    policy: NotRequired["capo_billing.types.policy_document.PolicyDocument"]
    """<p>The resource-based policy document attached to the resource in <code>JSON</code> format. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourcePolicyResponse) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourcePolicyResponse:
    out: GetResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    return out
