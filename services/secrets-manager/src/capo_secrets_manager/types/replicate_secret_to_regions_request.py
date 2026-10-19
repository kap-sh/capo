"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ReplicateSecretToRegionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_secrets_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_secrets_manager.types.add_replica_region_list_type
    import capo_secrets_manager.types.boolean_type
    import capo_secrets_manager.types.secret_id_type


class ReplicateSecretToRegionsRequest(TypedDict, closed=True):
    secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The ARN or name of the secret to replicate.</p>"""
    add_replica_regions: "capo_secrets_manager.types.add_replica_region_list_type.AddReplicaRegionListType"
    """<p>A list of Regions in which to replicate the secret.</p>"""
    force_overwrite_replica_secret: NotRequired[
        "capo_secrets_manager.types.boolean_type.BooleanType"
    ]
    """<p>Specifies whether to overwrite a secret with the same name in the destination Region. By default, secrets aren't overwritten.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicateSecretToRegionsRequest) -> dict:
    out: dict = {}
    out["SecretId"] = value["secret_id"]
    import capo_secrets_manager.types.add_replica_region_list_type

    out["AddReplicaRegions"] = (
        capo_secrets_manager.types.add_replica_region_list_type.serialize_aws_json_1_1(
            value["add_replica_regions"]
        )
    )
    if "force_overwrite_replica_secret" in value:
        out["ForceOverwriteReplicaSecret"] = value["force_overwrite_replica_secret"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicateSecretToRegionsRequest:
    out: ReplicateSecretToRegionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("SecretId") is not None:
        out["secret_id"] = data["SecretId"]
    else:
        raise DeserializationError("ReplicateSecretToRegionsRequest.secret_id required")
    if data.get("AddReplicaRegions") is not None:
        import capo_secrets_manager.types.add_replica_region_list_type

        out["add_replica_regions"] = (
            capo_secrets_manager.types.add_replica_region_list_type.deserialize_aws_json_1_1(
                data["AddReplicaRegions"]
            )
        )
    else:
        raise DeserializationError(
            "ReplicateSecretToRegionsRequest.add_replica_regions required"
        )
    if data.get("ForceOverwriteReplicaSecret") is not None:
        out["force_overwrite_replica_secret"] = data["ForceOverwriteReplicaSecret"]
    return out
