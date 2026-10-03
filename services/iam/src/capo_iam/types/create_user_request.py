"""Generated from Smithy shape ``com.amazonaws.iam#CreateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.path_type
    import capo_iam.types.tag_list_type
    import capo_iam.types.user_name_type


class CreateUserRequest(TypedDict, closed=True):
    path: NotRequired["capo_iam.types.path_type.pathType"]
    r"""<p> The path for the user name. For more information about paths, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>.</p> <p>This parameter is optional. If it is not included, it defaults to a slash (/).</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (<code>\u0021</code>) through the DEL character (<code>\u007F</code>), including most punctuation characters, digits, and upper and lowercased letters.</p>"""
    user_name: "capo_iam.types.user_name_type.userNameType"
    """<p>The name of the user to create.</p> <p>IAM user, group, role, and policy names must be unique within the account. Names are not distinguished by case. For example, you cannot create resources named both "MyResource" and "myresource".</p>"""
    permissions_boundary: NotRequired["capo_iam.types.arn_type.arnType"]
    """<p>The ARN of the managed policy that is used to set the permissions boundary for the user.</p> <p>A permissions boundary policy defines the maximum permissions that identity-based policies can grant to an entity, but does not grant permissions. Permissions boundaries do not define the maximum permissions that a resource-based policy can grant to an entity. To learn more, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html">Permissions boundaries for IAM entities</a> in the <i>IAM User Guide</i>.</p> <p>For more information about policy types, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policy-types">Policy types </a> in the <i>IAM User Guide</i>.</p>"""
    tags: NotRequired["capo_iam.types.tag_list_type.tagListType"]
    """<p>A list of tags that you want to attach to the new user. Each tag consists of a key name and an associated value. For more information about tagging, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html">Tagging IAM resources</a> in the <i>IAM User Guide</i>.</p> <note> <p>If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateUserRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "path" in value:
        pairs.append((f"{key_prefix}Path", str(value["path"])))
    pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    if "permissions_boundary" in value:
        pairs.append(
            (f"{key_prefix}PermissionsBoundary", str(value["permissions_boundary"]))
        )
    if "tags" in value:
        import capo_iam.types.tag_list_type

        capo_iam.types.tag_list_type.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateUserRequest:
    out: CreateUserRequest = {}  # type: ignore[typeddict-item]
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError("CreateUserRequest.user_name required")
    child_permissions_boundary = el.find("PermissionsBoundary")
    if child_permissions_boundary is not None:
        out["permissions_boundary"] = str(child_permissions_boundary.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_iam.types.tag_list_type

        out["tags"] = capo_iam.types.tag_list_type.deserialize_query(child_tags)
    return out
