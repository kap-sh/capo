"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UpdateSecurityPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.policy_description
    import capo_opensearchserverless.types.policy_document
    import capo_opensearchserverless.types.policy_name
    import capo_opensearchserverless.types.policy_version
    import capo_opensearchserverless.types.security_policy_type


class UpdateSecurityPolicyRequest(TypedDict, closed=True):
    type: "capo_opensearchserverless.types.security_policy_type.SecurityPolicyType"
    """<p>The type of access policy.</p>"""
    name: "capo_opensearchserverless.types.policy_name.PolicyName"
    """<p>The name of the policy.</p>"""
    policy_version: "capo_opensearchserverless.types.policy_version.PolicyVersion"
    """<p>The version of the policy being updated.</p>"""
    description: NotRequired[
        "capo_opensearchserverless.types.policy_description.PolicyDescription"
    ]
    """<p>A description of the policy. Typically used to store information about the permissions defined in the policy.</p>"""
    policy: NotRequired[
        "capo_opensearchserverless.types.policy_document.PolicyDocument"
    ]
    """<p>The JSON policy document to use as the content for the new policy.</p>"""
    client_token: NotRequired[
        "capo_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateSecurityPolicyRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["name"] = value["name"]
    out["policyVersion"] = value["policy_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "policy" in value:
        out["policy"] = value["policy"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateSecurityPolicyRequest:
    out: UpdateSecurityPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("policyVersion") is not None:
        out["policy_version"] = data["policyVersion"]
    else:
        out["policy_version"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
