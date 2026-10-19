"""Generated from Smithy shape ``com.amazonaws.secretsmanager#RemoveRegionsFromReplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.remove_replica_region_list_type
    import capo_secrets_manager.types.secret_id_type


class RemoveRegionsFromReplicationRequest(TypedDict, closed=True):
    secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The ARN or name of the secret.</p>"""
    remove_replica_regions: "capo_secrets_manager.types.remove_replica_region_list_type.RemoveReplicaRegionListType"
    """<p>The Regions of the replicas to remove.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveRegionsFromReplicationRequest) -> dict:
    out: dict = {}
    out["SecretId"] = value["secret_id"]
    import capo_secrets_manager.types.remove_replica_region_list_type

    out["RemoveReplicaRegions"] = (
        capo_secrets_manager.types.remove_replica_region_list_type.serialize_aws_json_1_1(
            value["remove_replica_regions"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveRegionsFromReplicationRequest:
    out: RemoveRegionsFromReplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("SecretId") is not None:
        out["secret_id"] = data["SecretId"]
    else:
        out["secret_id"] = ""
    if data.get("RemoveReplicaRegions") is not None:
        import capo_secrets_manager.types.remove_replica_region_list_type

        out["remove_replica_regions"] = (
            capo_secrets_manager.types.remove_replica_region_list_type.deserialize_aws_json_1_1(
                data["RemoveReplicaRegions"]
            )
        )
    else:
        out["remove_replica_regions"] = []
    return out
