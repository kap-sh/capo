"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#DeleteSecurityPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.policy_name
    import capo_opensearchserverless.types.security_policy_type


class DeleteSecurityPolicyRequest(TypedDict, closed=True):
    type: "capo_opensearchserverless.types.security_policy_type.SecurityPolicyType"
    """<p>The type of policy.</p>"""
    name: "capo_opensearchserverless.types.policy_name.PolicyName"
    """<p>The name of the policy to delete.</p>"""
    client_token: NotRequired[
        "capo_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteSecurityPolicyRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["name"] = value["name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteSecurityPolicyRequest:
    out: DeleteSecurityPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
