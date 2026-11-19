"""Generated from Smithy shape ``com.amazonaws.secretsmanager#DisassociateCrossAccountReplicaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.secret_arn_type


class DisassociateCrossAccountReplicaResponse(TypedDict, closed=True):
    arn: NotRequired["capo_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the primary secret.</p>"""
    cross_account_replica_arn: NotRequired[
        "capo_secrets_manager.types.secret_arn_type.SecretARNType"
    ]
    """<p>The ARN of the replica secret that was unlinked from the primary secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateCrossAccountReplicaResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "cross_account_replica_arn" in value:
        out["CrossAccountReplicaARN"] = value["cross_account_replica_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateCrossAccountReplicaResponse:
    out: DisassociateCrossAccountReplicaResponse = {}  # type: ignore[typeddict-item]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    if data.get("CrossAccountReplicaARN") is not None:
        out["cross_account_replica_arn"] = data["CrossAccountReplicaARN"]
    return out
