"""Generated from Smithy shape ``com.amazonaws.secretsmanager#PutResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.name_type
    import capo_secrets_manager.types.resource_policy_name_type
    import capo_secrets_manager.types.secret_arn_type


class PutResourcePolicyResponse(TypedDict, closed=True):
    arn: NotRequired["capo_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the secret.</p>"""
    name: NotRequired["capo_secrets_manager.types.name_type.NameType"]
    """<p>The name of the secret.</p>"""
    policy_name: NotRequired[
        "capo_secrets_manager.types.resource_policy_name_type.ResourcePolicyNameType"
    ]
    """<p>The name of the resource policy. If you didn't specify <code>PolicyName</code> in the request, this is <code>default</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourcePolicyResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourcePolicyResponse:
    out: PutResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    return out
