"""Generated from Smithy shape ``com.amazonaws.iam#Role``."""

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
    import capo_iam.types.policy_document_type
    import capo_iam.types.role_description_type
    import capo_iam.types.role_last_used
    import capo_iam.types.role_max_session_duration_type
    import capo_iam.types.role_name_type
    import capo_iam.types.source_role_template
    import capo_iam.types.tag_list_type


class Role(TypedDict, closed=True):
    path: "capo_iam.types.path_type.pathType"
    """<p> The path to the role. For more information about paths, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>. </p>"""
    role_name: "capo_iam.types.role_name_type.roleNameType"
    """<p>The friendly name that identifies the role.</p>"""
    role_id: "capo_iam.types.id_type.idType"
    """<p> The stable and unique string identifying the role. For more information about IDs, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>. </p>"""
    arn: "capo_iam.types.arn_type.arnType"
    """<p> The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how to use them in policies, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i> guide. </p>"""
    create_date: "capo_iam.types.date_type.dateType"
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when the role was created.</p>"""
    assume_role_policy_document: NotRequired[
        "capo_iam.types.policy_document_type.policyDocumentType"
    ]
    """<p>The policy that grants an entity permission to assume the role.</p>"""
    description: NotRequired["capo_iam.types.role_description_type.roleDescriptionType"]
    """<p>A description of the role that you provide.</p>"""
    max_session_duration: NotRequired[
        "capo_iam.types.role_max_session_duration_type.roleMaxSessionDurationType"
    ]
    """<p>The maximum session duration (in seconds) for the specified role. Anyone who uses the CLI, or API to assume the role can specify the duration using the optional <code>DurationSeconds</code> API parameter or <code>duration-seconds</code> CLI parameter.</p>"""
    permissions_boundary: NotRequired[
        "capo_iam.types.attached_permissions_boundary.AttachedPermissionsBoundary"
    ]
    """<p>The ARN of the policy used to set the permissions boundary for the role.</p> <p>For more information about permissions boundaries, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html">Permissions boundaries for IAM identities </a> in the <i>IAM User Guide</i>.</p>"""
    tags: NotRequired["capo_iam.types.tag_list_type.tagListType"]
    """<p>A list of tags that are attached to the role. For more information about tagging, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html">Tagging IAM resources</a> in the <i>IAM User Guide</i>.</p>"""
    role_last_used: NotRequired["capo_iam.types.role_last_used.RoleLastUsed"]
    """<p>Contains information about the last time that an IAM role was used. This includes the date and time and the Region in which the role was last used. Activity is only reported for the trailing 400 days. This period can be shorter if your Region began supporting these features within the last year. The role might have been used more than 400 days ago. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period">Regions where data is tracked</a> in the <i>IAM user Guide</i>.</p>"""
    source_role_template: NotRequired[
        "capo_iam.types.source_role_template.SourceRoleTemplate"
    ]
    """<p>Contains information about the role template that this role was created from. This member is present only for roles created with <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_AcquireRole.html">AcquireRole</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Role, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Path", str(value["path"])))
    pairs.append((f"{key_prefix}RoleName", str(value["role_name"])))
    pairs.append((f"{key_prefix}RoleId", str(value["role_id"])))
    pairs.append((f"{key_prefix}Arn", str(value["arn"])))
    import capo_iam.types.date_type

    capo_iam.types.date_type.serialize_query(
        value["create_date"], pairs, f"{key_prefix}CreateDate"
    )
    if "assume_role_policy_document" in value:
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
        import capo_iam.types.attached_permissions_boundary

        capo_iam.types.attached_permissions_boundary.serialize_query(
            value["permissions_boundary"], pairs, f"{key_prefix}PermissionsBoundary"
        )
    if "tags" in value:
        import capo_iam.types.tag_list_type

        capo_iam.types.tag_list_type.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "role_last_used" in value:
        import capo_iam.types.role_last_used

        capo_iam.types.role_last_used.serialize_query(
            value["role_last_used"], pairs, f"{key_prefix}RoleLastUsed"
        )
    if "source_role_template" in value:
        import capo_iam.types.source_role_template

        capo_iam.types.source_role_template.serialize_query(
            value["source_role_template"], pairs, f"{key_prefix}SourceRoleTemplate"
        )


def deserialize_query(el: Element) -> Role:
    out: Role = {}  # type: ignore[typeddict-item]
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    else:
        raise DeserializationError("Role.path required")
    child_role_name = el.find("RoleName")
    if child_role_name is not None:
        out["role_name"] = str(child_role_name.text or "")
    else:
        raise DeserializationError("Role.role_name required")
    child_role_id = el.find("RoleId")
    if child_role_id is not None:
        out["role_id"] = str(child_role_id.text or "")
    else:
        raise DeserializationError("Role.role_id required")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        raise DeserializationError("Role.arn required")
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import capo_iam.types.date_type

        out["create_date"] = capo_iam.types.date_type.deserialize_query(
            child_create_date
        )
    else:
        raise DeserializationError("Role.create_date required")
    child_assume_role_policy_document = el.find("AssumeRolePolicyDocument")
    if child_assume_role_policy_document is not None:
        out["assume_role_policy_document"] = str(
            child_assume_role_policy_document.text or ""
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_max_session_duration = el.find("MaxSessionDuration")
    if child_max_session_duration is not None:
        out["max_session_duration"] = int(child_max_session_duration.text or "")
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
    child_role_last_used = el.find("RoleLastUsed")
    if child_role_last_used is not None:
        import capo_iam.types.role_last_used

        out["role_last_used"] = capo_iam.types.role_last_used.deserialize_query(
            child_role_last_used
        )
    child_source_role_template = el.find("SourceRoleTemplate")
    if child_source_role_template is not None:
        import capo_iam.types.source_role_template

        out["source_role_template"] = (
            capo_iam.types.source_role_template.deserialize_query(
                child_source_role_template
            )
        )
    return out
