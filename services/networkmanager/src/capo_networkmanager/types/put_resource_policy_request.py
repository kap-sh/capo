"""Generated from Smithy shape ``com.amazonaws.networkmanager#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.resource_arn
    import capo_networkmanager.types.synthesized_json_resource_policy_document


class PutResourcePolicyRequest(TypedDict, closed=True):
    policy_document: "capo_networkmanager.types.synthesized_json_resource_policy_document.SynthesizedJsonResourcePolicyDocument"
    """<p>The JSON resource policy document.</p>"""
    resource_arn: "capo_networkmanager.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource policy. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["PolicyDocument"] = value["policy_document"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("PolicyDocument") is not None:
        out["policy_document"] = data["PolicyDocument"]
    else:
        out["policy_document"] = ""
    return out
