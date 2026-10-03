"""Generated from Smithy shape ``com.amazonaws.secretsmanager#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.name_type
    import capo_secrets_manager.types.non_empty_resource_policy_type
    import capo_secrets_manager.types.secret_arn_type


class GetResourcePolicyResponse(TypedDict, closed=True):
    arn: NotRequired["capo_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the secret that the resource-based policy was retrieved for.</p>"""
    name: NotRequired["capo_secrets_manager.types.name_type.NameType"]
    """<p>The name of the secret that the resource-based policy was retrieved for.</p>"""
    resource_policy: NotRequired[
        "capo_secrets_manager.types.non_empty_resource_policy_type.NonEmptyResourcePolicyType"
    ]
    """<p>A JSON-formatted string that contains the permissions policy attached to the secret. For more information about permissions policies, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html">Authentication and access control for Secrets Manager</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcePolicyResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "resource_policy" in value:
        out["ResourcePolicy"] = value["resource_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourcePolicyResponse:
    out: GetResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ResourcePolicy") is not None:
        out["resource_policy"] = data["ResourcePolicy"]
    return out
