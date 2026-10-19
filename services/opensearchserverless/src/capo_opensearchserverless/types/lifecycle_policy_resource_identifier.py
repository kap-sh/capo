"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#LifecyclePolicyResourceIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.lifecycle_policy_type
    import capo_opensearchserverless.types.resource_name


class LifecyclePolicyResourceIdentifier(TypedDict, closed=True):
    type: "capo_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType"
    """<p>The type of lifecycle policy.</p>"""
    resource: "capo_opensearchserverless.types.resource_name.ResourceName"
    """<p>The name of the OpenSearch Serverless ilndex resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LifecyclePolicyResourceIdentifier) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["resource"] = value["resource"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LifecyclePolicyResourceIdentifier:
    out: LifecyclePolicyResourceIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("resource") is not None:
        out["resource"] = data["resource"]
    else:
        out["resource"] = ""
    return out
