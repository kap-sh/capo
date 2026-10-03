"""Generated from Smithy shape ``com.amazonaws.iam#User``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.attached_permissions_boundary
    import capo_iam.types.date_type
    import capo_iam.types.id_type
    import capo_iam.types.path_type
    import capo_iam.types.tag_list_type
    import capo_iam.types.user_name_type


class User(TypedDict, closed=True):
    path: "capo_iam.types.path_type.pathType"
    """<p>The path to the user. For more information about paths, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>.</p> <p>The ARN of the policy used to set the permissions boundary for the user.</p>"""
    user_name: "capo_iam.types.user_name_type.userNameType"
    """<p>The friendly name identifying the user.</p>"""
    user_id: "capo_iam.types.id_type.idType"
    """<p>The stable and unique string identifying the user. For more information about IDs, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>.</p>"""
    arn: "capo_iam.types.arn_type.arnType"
    """<p>The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM Identifiers</a> in the <i>IAM User Guide</i>. </p>"""
    create_date: "capo_iam.types.date_type.dateType"
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when the user was created.</p>"""
    password_last_used: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when the user's password was last used to sign in to an Amazon Web Services website. For a list of Amazon Web Services websites that capture a user's last sign-in time, see the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html">Credential reports</a> topic in the <i>IAM User Guide</i>. If a password is used more than once in a five-minute span, only the first use is returned in this field. If the field is null (no value), then it indicates that they never signed in with a password. This can be because:</p> <ul> <li> <p>The user never had a password.</p> </li> <li> <p>A password exists but has not been used since IAM started tracking this information on October 20, 2014.</p> </li> </ul> <p>A null value does not mean that the user <i>never</i> had a password. Also, if the user does not currently have a password but had one in the past, then this field contains the date and time the most recent password was used.</p> <p>This value is returned only in the <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetUser.html">GetUser</a> and <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListUsers.html">ListUsers</a> operations. </p>"""
    permissions_boundary: NotRequired[
        "capo_iam.types.attached_permissions_boundary.AttachedPermissionsBoundary"
    ]
    """<p>For more information about permissions boundaries, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html">Permissions boundaries for IAM identities </a> in the <i>IAM User Guide</i>.</p>"""
    tags: NotRequired["capo_iam.types.tag_list_type.tagListType"]
    """<p>A list of tags that are associated with the user. For more information about tagging, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html">Tagging IAM resources</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: User, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Path", str(value["path"])))
    pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    pairs.append((f"{key_prefix}UserId", str(value["user_id"])))
    pairs.append((f"{key_prefix}Arn", str(value["arn"])))
    import capo_iam.types.date_type

    capo_iam.types.date_type.serialize_query(
        value["create_date"], pairs, f"{key_prefix}CreateDate"
    )
    if "password_last_used" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["password_last_used"], pairs, f"{key_prefix}PasswordLastUsed"
        )
    if "permissions_boundary" in value:
        import capo_iam.types.attached_permissions_boundary

        capo_iam.types.attached_permissions_boundary.serialize_query(
            value["permissions_boundary"], pairs, f"{key_prefix}PermissionsBoundary"
        )
    if "tags" in value:
        import capo_iam.types.tag_list_type

        capo_iam.types.tag_list_type.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> User:
    out: User = {}  # type: ignore[typeddict-item]
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    else:
        raise DeserializationError("User.path required")
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError("User.user_name required")
    child_user_id = el.find("UserId")
    if child_user_id is not None:
        out["user_id"] = str(child_user_id.text or "")
    else:
        raise DeserializationError("User.user_id required")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        raise DeserializationError("User.arn required")
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import capo_iam.types.date_type

        out["create_date"] = capo_iam.types.date_type.deserialize_query(
            child_create_date
        )
    else:
        raise DeserializationError("User.create_date required")
    child_password_last_used = el.find("PasswordLastUsed")
    if child_password_last_used is not None:
        import capo_iam.types.date_type

        out["password_last_used"] = capo_iam.types.date_type.deserialize_query(
            child_password_last_used
        )
    child_permissions_boundary = el.find("PermissionsBoundary")
    if child_permissions_boundary is not None:
        import capo_iam.types.attached_permissions_boundary

        out["permissions_boundary"] = (
            capo_iam.types.attached_permissions_boundary.deserialize_query(
                child_permissions_boundary
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_iam.types.tag_list_type

        out["tags"] = capo_iam.types.tag_list_type.deserialize_query(child_tags)
    return out
