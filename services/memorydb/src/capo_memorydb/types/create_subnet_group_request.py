"""Generated from Smithy shape ``com.amazonaws.memorydb#CreateSubnetGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.string
    import capo_memorydb.types.subnet_identifier_list
    import capo_memorydb.types.tag_list


class CreateSubnetGroupRequest(TypedDict, closed=True):
    subnet_group_name: "capo_memorydb.types.string.String"
    """<p>The name of the subnet group.</p>"""
    description: NotRequired["capo_memorydb.types.string.String"]
    """<p>A description for the subnet group.</p>"""
    subnet_ids: "capo_memorydb.types.subnet_identifier_list.SubnetIdentifierList"
    """<p>A list of VPC subnet IDs for the subnet group.</p>"""
    tags: NotRequired["capo_memorydb.types.tag_list.TagList"]
    """<p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSubnetGroupRequest) -> dict:
    out: dict = {}
    out["SubnetGroupName"] = value["subnet_group_name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_memorydb.types.subnet_identifier_list

    out["SubnetIds"] = (
        capo_memorydb.types.subnet_identifier_list.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    )
    if "tags" in value:
        import capo_memorydb.types.tag_list

        out["Tags"] = capo_memorydb.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSubnetGroupRequest:
    out: CreateSubnetGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("SubnetGroupName") is not None:
        out["subnet_group_name"] = data["SubnetGroupName"]
    else:
        out["subnet_group_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("SubnetIds") is not None:
        import capo_memorydb.types.subnet_identifier_list

        out["subnet_ids"] = (
            capo_memorydb.types.subnet_identifier_list.deserialize_aws_json_1_1(
                data["SubnetIds"]
            )
        )
    else:
        out["subnet_ids"] = []
    if data.get("Tags") is not None:
        import capo_memorydb.types.tag_list

        out["tags"] = capo_memorydb.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
