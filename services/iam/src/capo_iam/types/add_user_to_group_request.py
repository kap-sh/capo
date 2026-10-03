"""Generated from Smithy shape ``com.amazonaws.iam#AddUserToGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.existing_user_name_type
    import capo_iam.types.group_name_type


class AddUserToGroupRequest(TypedDict, closed=True):
    group_name: "capo_iam.types.group_name_type.groupNameType"
    """<p>The name of the group to update.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    user_name: "capo_iam.types.existing_user_name_type.existingUserNameType"
    """<p>The name of the user to add.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AddUserToGroupRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))
    pairs.append((f"{key_prefix}UserName", str(value["user_name"])))


def deserialize_query(el: Element) -> AddUserToGroupRequest:
    out: AddUserToGroupRequest = {}  # type: ignore[typeddict-item]
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    else:
        raise DeserializationError("AddUserToGroupRequest.group_name required")
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError("AddUserToGroupRequest.user_name required")
    return out
