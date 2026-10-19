"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateOpsMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.metadata_keys_to_delete_list
    import capo_ssm.types.metadata_map
    import capo_ssm.types.ops_metadata_arn


class UpdateOpsMetadataRequest(TypedDict, closed=True):
    ops_metadata_arn: "capo_ssm.types.ops_metadata_arn.OpsMetadataArn"
    """<p>The Amazon Resource Name (ARN) of the OpsMetadata Object to update.</p>"""
    metadata_to_update: NotRequired["capo_ssm.types.metadata_map.MetadataMap"]
    """<p>Metadata to add to an OpsMetadata object.</p>"""
    keys_to_delete: NotRequired[
        "capo_ssm.types.metadata_keys_to_delete_list.MetadataKeysToDeleteList"
    ]
    """<p>The metadata keys to delete from the OpsMetadata object. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateOpsMetadataRequest) -> dict:
    out: dict = {}
    out["OpsMetadataArn"] = value["ops_metadata_arn"]
    if "metadata_to_update" in value:
        import capo_ssm.types.metadata_map

        out["MetadataToUpdate"] = capo_ssm.types.metadata_map.serialize_aws_json_1_1(
            value["metadata_to_update"]
        )
    if "keys_to_delete" in value:
        import capo_ssm.types.metadata_keys_to_delete_list

        out["KeysToDelete"] = (
            capo_ssm.types.metadata_keys_to_delete_list.serialize_aws_json_1_1(
                value["keys_to_delete"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateOpsMetadataRequest:
    out: UpdateOpsMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("OpsMetadataArn") is not None:
        out["ops_metadata_arn"] = data["OpsMetadataArn"]
    else:
        out["ops_metadata_arn"] = ""
    if data.get("MetadataToUpdate") is not None:
        import capo_ssm.types.metadata_map

        out["metadata_to_update"] = (
            capo_ssm.types.metadata_map.deserialize_aws_json_1_1(
                data["MetadataToUpdate"]
            )
        )
    if data.get("KeysToDelete") is not None:
        import capo_ssm.types.metadata_keys_to_delete_list

        out["keys_to_delete"] = (
            capo_ssm.types.metadata_keys_to_delete_list.deserialize_aws_json_1_1(
                data["KeysToDelete"]
            )
        )
    return out
