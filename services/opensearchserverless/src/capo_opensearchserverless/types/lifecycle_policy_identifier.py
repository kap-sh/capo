"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#LifecyclePolicyIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.lifecycle_policy_type
    import capo_opensearchserverless.types.policy_name


class LifecyclePolicyIdentifier(TypedDict, closed=True):
    type: "capo_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType"
    """<p>The type of lifecycle policy.</p>"""
    name: "capo_opensearchserverless.types.policy_name.PolicyName"
    """<p>The name of the lifecycle policy.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LifecyclePolicyIdentifier) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LifecyclePolicyIdentifier:
    out: LifecyclePolicyIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
