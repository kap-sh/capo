"""Generated from Smithy shape ``com.amazonaws.secretsmanager#CrossAccountReplicaListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_secrets_manager.types.cross_account_replica_entry

CrossAccountReplicaListType: TypeAlias = list[
    "capo_secrets_manager.types.cross_account_replica_entry.CrossAccountReplicaEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrossAccountReplicaListType) -> list:
    import capo_secrets_manager.types.cross_account_replica_entry

    out: list = []
    for item in value:
        out.append(
            capo_secrets_manager.types.cross_account_replica_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CrossAccountReplicaListType:
    import capo_secrets_manager.types.cross_account_replica_entry

    out: CrossAccountReplicaListType = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_secrets_manager.types.cross_account_replica_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
