"""Generated from Smithy shape ``com.amazonaws.secretsmanager#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.resource_policy_name_type
    import capo_secrets_manager.types.secret_id_type


class DeleteResourcePolicyRequest(TypedDict, closed=True):
    secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The ARN or name of the secret to delete the attached resource-based policy for.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>"""
    policy_name: NotRequired[
        "capo_secrets_manager.types.resource_policy_name_type.ResourcePolicyNameType"
    ]
    """<p>The name of the resource policy to delete. If you don't specify this field, Secrets Manager uses <code>default</code>. You can only delete the <code>default</code> policy; if you specify any other name, the operation returns an <code>InvalidParameterException</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    out["SecretId"] = value["secret_id"]
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("SecretId") is not None:
        out["secret_id"] = data["SecretId"]
    else:
        out["secret_id"] = ""
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    return out
