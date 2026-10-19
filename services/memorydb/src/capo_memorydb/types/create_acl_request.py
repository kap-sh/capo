"""Generated from Smithy shape ``com.amazonaws.memorydb#CreateACLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.string
    import capo_memorydb.types.tag_list
    import capo_memorydb.types.user_name_list_input


class CreateACLRequest(TypedDict, closed=True):
    acl_name: "capo_memorydb.types.string.String"
    """<p>The name of the Access Control List.</p>"""
    user_names: NotRequired[
        "capo_memorydb.types.user_name_list_input.UserNameListInput"
    ]
    """<p>The list of users that belong to the Access Control List.</p>"""
    tags: NotRequired["capo_memorydb.types.tag_list.TagList"]
    """<p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateACLRequest) -> dict:
    out: dict = {}
    out["ACLName"] = value["acl_name"]
    if "user_names" in value:
        import capo_memorydb.types.user_name_list_input

        out["UserNames"] = (
            capo_memorydb.types.user_name_list_input.serialize_aws_json_1_1(
                value["user_names"]
            )
        )
    if "tags" in value:
        import capo_memorydb.types.tag_list

        out["Tags"] = capo_memorydb.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateACLRequest:
    out: CreateACLRequest = {}  # type: ignore[typeddict-item]
    if data.get("ACLName") is not None:
        out["acl_name"] = data["ACLName"]
    else:
        out["acl_name"] = ""
    if data.get("UserNames") is not None:
        import capo_memorydb.types.user_name_list_input

        out["user_names"] = (
            capo_memorydb.types.user_name_list_input.deserialize_aws_json_1_1(
                data["UserNames"]
            )
        )
    if data.get("Tags") is not None:
        import capo_memorydb.types.tag_list

        out["tags"] = capo_memorydb.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
