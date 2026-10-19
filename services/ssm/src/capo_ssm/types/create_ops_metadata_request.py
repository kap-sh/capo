"""Generated from Smithy shape ``com.amazonaws.ssm#CreateOpsMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.metadata_map
    import capo_ssm.types.ops_metadata_resource_id
    import capo_ssm.types.tag_list


class CreateOpsMetadataRequest(TypedDict, closed=True):
    resource_id: "capo_ssm.types.ops_metadata_resource_id.OpsMetadataResourceId"
    """<p>A resource ID for a new Application Manager application.</p>"""
    metadata: NotRequired["capo_ssm.types.metadata_map.MetadataMap"]
    """<p>Metadata for a new Application Manager application. </p>"""
    tags: NotRequired["capo_ssm.types.tag_list.TagList"]
    """<p>Optional metadata that you assign to a resource. You can specify a maximum of five tags for an OpsMetadata object. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag an OpsMetadata object to identify an environment or target Amazon Web Services Region. In this case, you could specify the following key-value pairs:</p> <ul> <li> <p> <code>Key=Environment,Value=Production</code> </p> </li> <li> <p> <code>Key=Region,Value=us-east-2</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateOpsMetadataRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    if "metadata" in value:
        import capo_ssm.types.metadata_map

        out["Metadata"] = capo_ssm.types.metadata_map.serialize_aws_json_1_1(
            value["metadata"]
        )
    if "tags" in value:
        import capo_ssm.types.tag_list

        out["Tags"] = capo_ssm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateOpsMetadataRequest:
    out: CreateOpsMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("Metadata") is not None:
        import capo_ssm.types.metadata_map

        out["metadata"] = capo_ssm.types.metadata_map.deserialize_aws_json_1_1(
            data["Metadata"]
        )
    if data.get("Tags") is not None:
        import capo_ssm.types.tag_list

        out["tags"] = capo_ssm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
