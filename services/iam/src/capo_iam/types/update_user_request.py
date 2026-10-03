"""Generated from Smithy shape ``com.amazonaws.iam#UpdateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.existing_user_name_type
    import capo_iam.types.path_type
    import capo_iam.types.user_name_type


class UpdateUserRequest(TypedDict, closed=True):
    user_name: "capo_iam.types.existing_user_name_type.existingUserNameType"
    """<p>Name of the user to update. If you're changing the name of the user, this is the original user name.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    new_path: NotRequired["capo_iam.types.path_type.pathType"]
    r"""<p>New path for the IAM user. Include this parameter only if you're changing the user's path.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (<code>\u0021</code>) through the DEL character (<code>\u007F</code>), including most punctuation characters, digits, and upper and lowercased letters.</p>"""
    new_user_name: NotRequired["capo_iam.types.user_name_type.userNameType"]
    """<p>New name for the user. Include this parameter only if you're changing the user's name.</p> <p>IAM user, group, role, and policy names must be unique within the account. Names are not distinguished by case. For example, you cannot create resources named both "MyResource" and "myresource".</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateUserRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    if "new_path" in value:
        pairs.append((f"{key_prefix}NewPath", str(value["new_path"])))
    if "new_user_name" in value:
        pairs.append((f"{key_prefix}NewUserName", str(value["new_user_name"])))


def deserialize_query(el: Element) -> UpdateUserRequest:
    out: UpdateUserRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError("UpdateUserRequest.user_name required")
    child_new_path = el.find("NewPath")
    if child_new_path is not None:
        out["new_path"] = str(child_new_path.text or "")
    child_new_user_name = el.find("NewUserName")
    if child_new_user_name is not None:
        out["new_user_name"] = str(child_new_user_name.text or "")
    return out
