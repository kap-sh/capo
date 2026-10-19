"""Generated from Smithy shape ``com.amazonaws.memorydb#CreateParameterGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.string
    import capo_memorydb.types.tag_list


class CreateParameterGroupRequest(TypedDict, closed=True):
    parameter_group_name: "capo_memorydb.types.string.String"
    """<p>The name of the parameter group.</p>"""
    family: "capo_memorydb.types.string.String"
    """<p>The name of the parameter group family that the parameter group can be used with.</p>"""
    description: NotRequired["capo_memorydb.types.string.String"]
    """<p>An optional description of the parameter group.</p>"""
    tags: NotRequired["capo_memorydb.types.tag_list.TagList"]
    """<p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateParameterGroupRequest) -> dict:
    out: dict = {}
    out["ParameterGroupName"] = value["parameter_group_name"]
    out["Family"] = value["family"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_memorydb.types.tag_list

        out["Tags"] = capo_memorydb.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateParameterGroupRequest:
    out: CreateParameterGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("ParameterGroupName") is not None:
        out["parameter_group_name"] = data["ParameterGroupName"]
    else:
        out["parameter_group_name"] = ""
    if data.get("Family") is not None:
        out["family"] = data["Family"]
    else:
        out["family"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_memorydb.types.tag_list

        out["tags"] = capo_memorydb.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
