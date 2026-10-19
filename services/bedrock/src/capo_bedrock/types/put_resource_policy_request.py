"""Generated from Smithy shape ``com.amazonaws.bedrock#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.resource_policy_document
    import capo_bedrock.types.resource_policy_resource_arn


class PutResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_bedrock.types.resource_policy_resource_arn.ResourcePolicyResourceArn"
    )
    """<p>The ARN of the Bedrock resource to which this resource policy applies.</p>"""
    resource_policy: (
        "capo_bedrock.types.resource_policy_document.ResourcePolicyDocument"
    )
    """<p>The JSON string representing the Bedrock resource policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["resourcePolicy"] = value["resource_policy"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("resourcePolicy") is not None:
        out["resource_policy"] = data["resourcePolicy"]
    else:
        out["resource_policy"] = ""
    return out
