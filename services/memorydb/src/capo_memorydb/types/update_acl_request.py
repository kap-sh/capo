"""Generated from Smithy shape ``com.amazonaws.memorydb#UpdateACLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.string
    import capo_memorydb.types.user_name_list_input


class UpdateACLRequest(TypedDict, closed=True):
    acl_name: "capo_memorydb.types.string.String"
    """<p>The name of the Access Control List.</p>"""
    user_names_to_add: NotRequired[
        "capo_memorydb.types.user_name_list_input.UserNameListInput"
    ]
    """<p>The list of users to add to the Access Control List.</p>"""
    user_names_to_remove: NotRequired[
        "capo_memorydb.types.user_name_list_input.UserNameListInput"
    ]
    """<p>The list of users to remove from the Access Control List.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateACLRequest) -> dict:
    out: dict = {}
    out["ACLName"] = value["acl_name"]
    if "user_names_to_add" in value:
        import capo_memorydb.types.user_name_list_input

        out["UserNamesToAdd"] = (
            capo_memorydb.types.user_name_list_input.serialize_aws_json_1_1(
                value["user_names_to_add"]
            )
        )
    if "user_names_to_remove" in value:
        import capo_memorydb.types.user_name_list_input

        out["UserNamesToRemove"] = (
            capo_memorydb.types.user_name_list_input.serialize_aws_json_1_1(
                value["user_names_to_remove"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateACLRequest:
    out: UpdateACLRequest = {}  # type: ignore[typeddict-item]
    if data.get("ACLName") is not None:
        out["acl_name"] = data["ACLName"]
    else:
        out["acl_name"] = ""
    if data.get("UserNamesToAdd") is not None:
        import capo_memorydb.types.user_name_list_input

        out["user_names_to_add"] = (
            capo_memorydb.types.user_name_list_input.deserialize_aws_json_1_1(
                data["UserNamesToAdd"]
            )
        )
    if data.get("UserNamesToRemove") is not None:
        import capo_memorydb.types.user_name_list_input

        out["user_names_to_remove"] = (
            capo_memorydb.types.user_name_list_input.deserialize_aws_json_1_1(
                data["UserNamesToRemove"]
            )
        )
    return out
