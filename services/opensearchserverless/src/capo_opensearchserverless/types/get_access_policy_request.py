"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#GetAccessPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.access_policy_type
    import capo_opensearchserverless.types.policy_name


class GetAccessPolicyRequest(TypedDict, closed=True):
    type: "capo_opensearchserverless.types.access_policy_type.AccessPolicyType"
    """<p>Tye type of policy. Currently, the only supported value is <code>data</code>.</p>"""
    name: "capo_opensearchserverless.types.policy_name.PolicyName"
    """<p>The name of the access policy.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAccessPolicyRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAccessPolicyRequest:
    out: GetAccessPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
