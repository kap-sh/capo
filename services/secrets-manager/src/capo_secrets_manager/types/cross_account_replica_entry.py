"""Generated from Smithy shape ``com.amazonaws.secretsmanager#CrossAccountReplicaEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.role_arn_type
    import capo_secrets_manager.types.secret_arn_type
    import capo_secrets_manager.types.status_message_type
    import capo_secrets_manager.types.status_type


class CrossAccountReplicaEntry(TypedDict, closed=True):
    replica_secret_arn: NotRequired[
        "capo_secrets_manager.types.secret_arn_type.SecretARNType"
    ]
    """<p>The ARN of the replica secret.</p>"""
    replication_role_arn: NotRequired[
        "capo_secrets_manager.types.role_arn_type.RoleARNType"
    ]
    """<p>The ARN of the IAM role that Secrets Manager assumes to replicate to this replica, if one was specified when the replica was associated.</p>"""
    replication_status: NotRequired["capo_secrets_manager.types.status_type.StatusType"]
    """<p>The status of replication from this primary secret. The status can be:</p> <ul> <li> <p> <code>InSync</code>: Replication from the primary secret is complete.</p> </li> <li> <p> <code>Failed</code>: Replication from the primary secret was unable to be completed.</p> </li> <li> <p> <code>InProgress</code>: Replication from the primary secret has started but is not complete.</p> </li> <li> <p> <code>Detached</code>: Replication from the primary secret was stopped by the replica.</p> </li> </ul>"""
    status_message: NotRequired[
        "capo_secrets_manager.types.status_message_type.StatusMessageType"
    ]
    """<p>A message that describes the replication status, if Secrets Manager has more information to provide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrossAccountReplicaEntry) -> dict:
    out: dict = {}
    if "replica_secret_arn" in value:
        out["ReplicaSecretARN"] = value["replica_secret_arn"]
    if "replication_role_arn" in value:
        out["ReplicationRoleARN"] = value["replication_role_arn"]
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


def deserialize_aws_json_1_1(data: dict) -> CrossAccountReplicaEntry:
    out: CrossAccountReplicaEntry = {}  # type: ignore[typeddict-item]
    if data.get("ReplicaSecretARN") is not None:
        out["replica_secret_arn"] = data["ReplicaSecretARN"]
    if data.get("ReplicationRoleARN") is not None:
        out["replication_role_arn"] = data["ReplicationRoleARN"]
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
