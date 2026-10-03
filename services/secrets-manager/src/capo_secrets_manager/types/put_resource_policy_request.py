"""Generated from Smithy shape ``com.amazonaws.secretsmanager#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_secrets_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_secrets_manager.types.boolean_type
    import capo_secrets_manager.types.non_empty_resource_policy_type
    import capo_secrets_manager.types.secret_id_type


class PutResourcePolicyRequest(TypedDict, closed=True):
    secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The ARN or name of the secret to attach the resource-based policy.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>"""
    resource_policy: "capo_secrets_manager.types.non_empty_resource_policy_type.NonEmptyResourcePolicyType"
    """<p>A JSON-formatted string for an Amazon Web Services resource-based policy. For example policies, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html">Permissions policy examples</a>.</p>"""
    block_public_policy: NotRequired[
        "capo_secrets_manager.types.boolean_type.BooleanType"
    ]
    """<p>Specifies whether to block resource-based policies that allow broad access to the secret, for example those that use a wildcard for the principal. By default, public policies aren't blocked.</p> <important> <p>Resource policy validation and the BlockPublicPolicy parameter help protect your resources by preventing public access from being granted through the resource policies that are directly attached to your secrets. In addition to using these features, carefully inspect the following policies to confirm that they do not grant public access:</p> <ul> <li> <p>Identity-based policies attached to associated Amazon Web Services principals (for example, IAM roles)</p> </li> <li> <p>Resource-based policies attached to associated Amazon Web Services resources (for example, Key Management Service (KMS) keys)</p> </li> </ul> <p>To review permissions to your secrets, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/determine-acccess_examine-iam-policies.html">Determine who has permissions to your secrets</a>.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["SecretId"] = value["secret_id"]
    out["ResourcePolicy"] = value["resource_policy"]
    if "block_public_policy" in value:
        out["BlockPublicPolicy"] = value["block_public_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("SecretId") is not None:
        out["secret_id"] = data["SecretId"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.secret_id required")
    if data.get("ResourcePolicy") is not None:
        out["resource_policy"] = data["ResourcePolicy"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.resource_policy required")
    if data.get("BlockPublicPolicy") is not None:
        out["block_public_policy"] = data["BlockPublicPolicy"]
    return out
