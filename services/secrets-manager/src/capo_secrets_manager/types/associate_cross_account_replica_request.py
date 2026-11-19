"""Generated from Smithy shape ``com.amazonaws.secretsmanager#AssociateCrossAccountReplicaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.replica_restriction_type
    import capo_secrets_manager.types.role_arn_type
    import capo_secrets_manager.types.secret_arn_type
    import capo_secrets_manager.types.secret_id_type


class AssociateCrossAccountReplicaRequest(TypedDict, closed=True):
    secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The ARN or name of the primary secret in your account to replicate.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>"""
    cross_account_replica_arn: (
        "capo_secrets_manager.types.secret_arn_type.SecretARNType"
    )
    """<p>The ARN of the replica secret in the other Amazon Web Services account. The replica secret must be in the same Region and partition as the primary secret. Additionally, the replica account owner must have created the replica secret as a cross-account replica of the primary secret. For more information see <a>CreateSecret</a>.</p>"""
    replica_restriction: NotRequired[
        "capo_secrets_manager.types.replica_restriction_type.ReplicaRestrictionType"
    ]
    """<p>Whether the replica account must belong to the same Amazon Web Services organization as the primary account:</p> <ul> <li> <p> <code>SameOrg</code>, which requires the replica account to be in the same organization as the primary account. This is the default.</p> </li> <li> <p> <code>NoRestriction</code>, which allows the replica account to be in any organization.</p> </li> </ul>"""
    replication_role_arn: NotRequired[
        "capo_secrets_manager.types.role_arn_type.RoleARNType"
    ]
    """<p>The ARN of an IAM role in the primary account that Secrets Manager assumes to perform replication. If you don't include this field, Secrets Manager replicates using the credentials of caller who updates the primary secret. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/cross-account-replicate-permissions.html"> Cross-account replication permissions</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateCrossAccountReplicaRequest) -> dict:
    out: dict = {}
    out["SecretId"] = value["secret_id"]
    out["CrossAccountReplicaARN"] = value["cross_account_replica_arn"]
    if "replica_restriction" in value:
        import capo_secrets_manager.types.replica_restriction_type

        out["ReplicaRestriction"] = (
            capo_secrets_manager.types.replica_restriction_type.serialize_aws_json_1_1(
                value["replica_restriction"]
            )
        )
    if "replication_role_arn" in value:
        out["ReplicationRoleARN"] = value["replication_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateCrossAccountReplicaRequest:
    out: AssociateCrossAccountReplicaRequest = {}  # type: ignore[typeddict-item]
    if data.get("SecretId") is not None:
        out["secret_id"] = data["SecretId"]
    else:
        out["secret_id"] = ""
    if data.get("CrossAccountReplicaARN") is not None:
        out["cross_account_replica_arn"] = data["CrossAccountReplicaARN"]
    else:
        out["cross_account_replica_arn"] = ""
    if data.get("ReplicaRestriction") is not None:
        import capo_secrets_manager.types.replica_restriction_type

        out["replica_restriction"] = (
            capo_secrets_manager.types.replica_restriction_type.deserialize_aws_json_1_1(
                data["ReplicaRestriction"]
            )
        )
    if data.get("ReplicationRoleARN") is not None:
        out["replication_role_arn"] = data["ReplicationRoleARN"]
    return out
