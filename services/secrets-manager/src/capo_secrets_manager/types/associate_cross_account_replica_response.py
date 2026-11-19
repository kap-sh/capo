"""Generated from Smithy shape ``com.amazonaws.secretsmanager#AssociateCrossAccountReplicaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.secret_arn_type
    import capo_secrets_manager.types.status_type


class AssociateCrossAccountReplicaResponse(TypedDict, closed=True):
    arn: NotRequired["capo_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the primary secret.</p>"""
    cross_account_replica_arn: NotRequired[
        "capo_secrets_manager.types.secret_arn_type.SecretARNType"
    ]
    """<p>The ARN of the replica secret in the other account.</p>"""
    replication_status: NotRequired["capo_secrets_manager.types.status_type.StatusType"]
    """<p>The status of replication to the replica secret. Possible values:</p> <ul> <li> <p> <code>InSync</code>, which indicates that replication to the replica completed successfully and the replica is up to date.</p> </li> <li> <p> <code>Failed</code>, which indicates that replication to the replica did not succeed.</p> </li> <li> <p> <code>InProgress</code>, which indicates that Secrets Manager is replicating to the replica.</p> </li> <li> <p> <code>Pending</code>, which indicates that replication has not yet started.</p> </li> <li> <p> <code>Detached</code>, which indicates that primary secret is no longer linked to the replica secret.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateCrossAccountReplicaResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "cross_account_replica_arn" in value:
        out["CrossAccountReplicaARN"] = value["cross_account_replica_arn"]
    if "replication_status" in value:
        import capo_secrets_manager.types.status_type

        out["ReplicationStatus"] = (
            capo_secrets_manager.types.status_type.serialize_aws_json_1_1(
                value["replication_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateCrossAccountReplicaResponse:
    out: AssociateCrossAccountReplicaResponse = {}  # type: ignore[typeddict-item]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    if data.get("CrossAccountReplicaARN") is not None:
        out["cross_account_replica_arn"] = data["CrossAccountReplicaARN"]
    if data.get("ReplicationStatus") is not None:
        import capo_secrets_manager.types.status_type

        out["replication_status"] = (
            capo_secrets_manager.types.status_type.deserialize_aws_json_1_1(
                data["ReplicationStatus"]
            )
        )
    return out
