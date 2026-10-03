"""Generated from Smithy shape ``com.amazonaws.iam#CreateRoleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.path_type
    import capo_iam.types.policy_document_type
    import capo_iam.types.role_description_type
    import capo_iam.types.role_max_session_duration_type
    import capo_iam.types.role_name_type
    import capo_iam.types.tag_list_type


class CreateRoleRequest(TypedDict, closed=True):
    path: NotRequired["capo_iam.types.path_type.pathType"]
    r"""<p> The path to the role. For more information about paths, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM Identifiers</a> in the <i>IAM User Guide</i>.</p> <p>This parameter is optional. If it is not included, it defaults to a slash (/).</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (<code>\u0021</code>) through the DEL character (<code>\u007F</code>), including most punctuation characters, digits, and upper and lowercased letters.</p>"""
    role_name: "capo_iam.types.role_name_type.roleNameType"
    """<p>The name of the role to create.</p> <p>IAM user, group, role, and policy names must be unique within the account. Names are not distinguished by case. For example, you cannot create resources named both "MyResource" and "myresource".</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    assume_role_policy_document: (
        "capo_iam.types.policy_document_type.policyDocumentType"
    )
    r"""<p>The trust relationship policy document that grants an entity permission to assume the role.</p> <p>In IAM, you must provide a JSON policy that has been converted to a string. However, for CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> used to validate this parameter is a string of characters consisting of the following:</p> <ul> <li> <p>Any printable ASCII character ranging from the space character (<code>\u0020</code>) through the end of the ASCII character range</p> </li> <li> <p>The printable characters in the Basic Latin and Latin-1 Supplement character set (through <code>\u00FF</code>)</p> </li> <li> <p>The special characters tab (<code>\u0009</code>), line feed (<code>\u000A</code>), and carriage return (<code>\u000D</code>)</p> </li> </ul> <p> Upon success, the response includes the same trust policy in JSON format.</p>"""
    description: NotRequired["capo_iam.types.role_description_type.roleDescriptionType"]
    """<p>A description of the role.</p>"""
    max_session_duration: NotRequired[
        "capo_iam.types.role_max_session_duration_type.roleMaxSessionDurationType"
    ]
    """<p>The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default value of one hour is applied. This setting can have a value from 1 hour to 12 hours.</p> <p>Anyone who assumes the role from the CLI or API can use the <code>DurationSeconds</code> API parameter or the <code>duration-seconds</code> CLI parameter to request a longer session. The <code>MaxSessionDuration</code> setting determines the maximum duration that can be requested using the <code>DurationSeconds</code> parameter. If users don't specify a value for the <code>DurationSeconds</code> parameter, their security credentials are valid for one hour by default. This applies when you use the <code>AssumeRole*</code> API operations or the <code>assume-role*</code> CLI operations but does not apply when you use those operations to create a console URL. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html">Using IAM roles</a> in the <i>IAM User Guide</i>.</p>"""
    permissions_boundary: NotRequired["capo_iam.types.arn_type.arnType"]
    """<p>The ARN of the managed policy that is used to set the permissions boundary for the role.</p> <p>A permissions boundary policy defines the maximum permissions that identity-based policies can grant to an entity, but does not grant permissions. Permissions boundaries do not define the maximum permissions that a resource-based policy can grant to an entity. To learn more, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html">Permissions boundaries for IAM entities</a> in the <i>IAM User Guide</i>.</p> <p>For more information about policy types, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policy-types">Policy types </a> in the <i>IAM User Guide</i>.</p>"""
    tags: NotRequired["capo_iam.types.tag_list_type.tagListType"]
    """<p>A list of tags that you want to attach to the new role. Each tag consists of a key name and an associated value. For more information about tagging, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html">Tagging IAM resources</a> in the <i>IAM User Guide</i>.</p> <note> <p>If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateRoleRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "path" in value:
        pairs.append((f"{key_prefix}Path", str(value["path"])))
    pairs.append((f"{key_prefix}RoleName", str(value["role_name"])))
    pairs.append(
        (
            f"{key_prefix}AssumeRolePolicyDocument",
            str(value["assume_role_policy_document"]),
        )
    )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "max_session_duration" in value:
        pairs.append(
            (f"{key_prefix}MaxSessionDuration", str(value["max_session_duration"]))
        )
    if "permissions_boundary" in value:
        pairs.append(
            (f"{key_prefix}PermissionsBoundary", str(value["permissions_boundary"]))
        )
    if "tags" in value:
        import capo_iam.types.tag_list_type

        capo_iam.types.tag_list_type.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateRoleRequest:
    out: CreateRoleRequest = {}  # type: ignore[typeddict-item]
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    child_role_name = el.find("RoleName")
    if child_role_name is not None:
        out["role_name"] = str(child_role_name.text or "")
    else:
        raise DeserializationError("CreateRoleRequest.role_name required")
    child_assume_role_policy_document = el.find("AssumeRolePolicyDocument")
    if child_assume_role_policy_document is not None:
        out["assume_role_policy_document"] = str(
            child_assume_role_policy_document.text or ""
        )
    else:
        raise DeserializationError(
            "CreateRoleRequest.assume_role_policy_document required"
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_max_session_duration = el.find("MaxSessionDuration")
    if child_max_session_duration is not None:
        out["max_session_duration"] = int(child_max_session_duration.text or "")
    child_permissions_boundary = el.find("PermissionsBoundary")
    if child_permissions_boundary is not None:
        out["permissions_boundary"] = str(child_permissions_boundary.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_iam.types.tag_list_type

        out["tags"] = capo_iam.types.tag_list_type.deserialize_query(child_tags)
    return out
