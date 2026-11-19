"""Generated from Smithy shape ``com.amazonaws.secretsmanager#DisassociateCrossAccountReplicaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.secret_arn_type
    import capo_secrets_manager.types.secret_id_type


class DisassociateCrossAccountReplicaRequest(TypedDict, closed=True):
    secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The ARN or name of the primary secret in your account.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>"""
    cross_account_replica_arn: (
        "capo_secrets_manager.types.secret_arn_type.SecretARNType"
    )
    """<p>The ARN of the cross-account replica secret to unlink from the primary secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateCrossAccountReplicaRequest) -> dict:
    out: dict = {}
    out["SecretId"] = value["secret_id"]
    out["CrossAccountReplicaARN"] = value["cross_account_replica_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateCrossAccountReplicaRequest:
    out: DisassociateCrossAccountReplicaRequest = {}  # type: ignore[typeddict-item]
    if data.get("SecretId") is not None:
        out["secret_id"] = data["SecretId"]
    else:
        out["secret_id"] = ""
    if data.get("CrossAccountReplicaARN") is not None:
        out["cross_account_replica_arn"] = data["CrossAccountReplicaARN"]
    else:
        out["cross_account_replica_arn"] = ""
    return out
