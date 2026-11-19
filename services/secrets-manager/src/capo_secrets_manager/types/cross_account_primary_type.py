"""Generated from Smithy shape ``com.amazonaws.secretsmanager#CrossAccountPrimaryType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.secret_arn_type
    import capo_secrets_manager.types.status_message_type
    import capo_secrets_manager.types.status_type


class CrossAccountPrimaryType(TypedDict, closed=True):
    primary_secret_arn: NotRequired[
        "capo_secrets_manager.types.secret_arn_type.SecretARNType"
    ]
    """<p>The ARN of the primary secret replicating into this replica secret.</p>"""
    replication_status: NotRequired["capo_secrets_manager.types.status_type.StatusType"]
    """<p>The status of replication from the primary secret to this replica. The status can be:</p> <ul> <li> <p> <code>InSync</code>: Replication to the replica secret is complete.</p> </li> <li> <p> <code>Failed</code>: Replication to the replica secret was unable to be completed.</p> </li> <li> <p> <code>InProgress</code>: Replication to the replica secret has started but is not complete.</p> </li> <li> <p> <code>Pending</code>: Replication has not yet started for the replica secret.</p> </li> <li> <p> <code>Detached</code>: Replication to the replica secret was stopped by the primary.</p> </li> </ul>"""
    status_message: NotRequired[
        "capo_secrets_manager.types.status_message_type.StatusMessageType"
    ]
    """<p>A message that describes the replication status, if Secrets Manager has more information to provide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrossAccountPrimaryType) -> dict:
    out: dict = {}
    if "primary_secret_arn" in value:
        out["PrimarySecretARN"] = value["primary_secret_arn"]
    if "replication_status" in value:
        import capo_secrets_manager.types.status_type

        out["ReplicationStatus"] = (
            capo_secrets_manager.types.status_type.serialize_aws_json_1_1(
                value["replication_status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CrossAccountPrimaryType:
    out: CrossAccountPrimaryType = {}  # type: ignore[typeddict-item]
    if data.get("PrimarySecretARN") is not None:
        out["primary_secret_arn"] = data["PrimarySecretARN"]
    if data.get("ReplicationStatus") is not None:
        import capo_secrets_manager.types.status_type

        out["replication_status"] = (
            capo_secrets_manager.types.status_type.deserialize_aws_json_1_1(
                data["ReplicationStatus"]
            )
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out
