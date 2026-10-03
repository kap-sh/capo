"""Generated from Smithy shape ``com.amazonaws.iam#RoleDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.attached_permissions_boundary
    import capo_iam.types.attached_policies_list_type
    import capo_iam.types.date_type
    import capo_iam.types.id_type
    import capo_iam.types.instance_profile_list_type
    import capo_iam.types.path_type
    import capo_iam.types.policy_detail_list_type
    import capo_iam.types.policy_document_type
    import capo_iam.types.role_last_used
    import capo_iam.types.role_name_type
    import capo_iam.types.tag_list_type


class RoleDetail(TypedDict, closed=True):
    path: NotRequired["capo_iam.types.path_type.pathType"]
    """<p>The path to the role. For more information about paths, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>.</p>"""
    role_name: NotRequired["capo_iam.types.role_name_type.roleNameType"]
    """<p>The friendly name that identifies the role.</p>"""
    role_id: NotRequired["capo_iam.types.id_type.idType"]
    """<p>The stable and unique string identifying the role. For more information about IDs, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>.</p>"""
    arn: NotRequired["capo_iam.types.arn_type.arnType"]
    create_date: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when the role was created.</p>"""
    assume_role_policy_document: NotRequired[
        "capo_iam.types.policy_document_type.policyDocumentType"
    ]
    """<p>The trust policy that grants permission to assume the role.</p>"""
    instance_profile_list: NotRequired[
        "capo_iam.types.instance_profile_list_type.instanceProfileListType"
    ]
    """<p>A list of instance profiles that contain this role.</p>"""
    role_policy_list: NotRequired[
        "capo_iam.types.policy_detail_list_type.policyDetailListType"
    ]
    """<p>A list of inline policies embedded in the role. These policies are the role's access (permissions) policies.</p>"""
    attached_managed_policies: NotRequired[
        "capo_iam.types.attached_policies_list_type.attachedPoliciesListType"
    ]
    """<p>A list of managed policies attached to the role. These policies are the role's access (permissions) policies.</p>"""
    permissions_boundary: NotRequired[
        "capo_iam.types.attached_permissions_boundary.AttachedPermissionsBoundary"
    ]
    """<p>The ARN of the policy used to set the permissions boundary for the role.</p> <p>For more information about permissions boundaries, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html">Permissions boundaries for IAM identities </a> in the <i>IAM User Guide</i>.</p>"""
    tags: NotRequired["capo_iam.types.tag_list_type.tagListType"]
    """<p>A list of tags that are attached to the role. For more information about tagging, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html">Tagging IAM resources</a> in the <i>IAM User Guide</i>.</p>"""
    role_last_used: NotRequired["capo_iam.types.role_last_used.RoleLastUsed"]
    """<p>Contains information about the last time that an IAM role was used. This includes the date and time and the Region in which the role was last used. Activity is only reported for the trailing 400 days. This period can be shorter if your Region began supporting these features within the last year. The role might have been used more than 400 days ago. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period">Regions where data is tracked</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RoleDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "path" in value:
        pairs.append((f"{key_prefix}Path", str(value["path"])))
    if "role_name" in value:
        pairs.append((f"{key_prefix}RoleName", str(value["role_name"])))
    if "role_id" in value:
        pairs.append((f"{key_prefix}RoleId", str(value["role_id"])))
    if "arn" in value:
        pairs.append((f"{key_prefix}Arn", str(value["arn"])))
    if "create_date" in value:
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
    if "instance_profile_list" in value:
        import capo_iam.types.instance_profile_list_type

        capo_iam.types.instance_profile_list_type.serialize_query(
            value["instance_profile_list"], pairs, f"{key_prefix}InstanceProfileList"
        )
    if "role_policy_list" in value:
        import capo_iam.types.policy_detail_list_type

        capo_iam.types.policy_detail_list_type.serialize_query(
            value["role_policy_list"], pairs, f"{key_prefix}RolePolicyList"
        )
    if "attached_managed_policies" in value:
        import capo_iam.types.attached_policies_list_type

        capo_iam.types.attached_policies_list_type.serialize_query(
            value["attached_managed_policies"],
            pairs,
            f"{key_prefix}AttachedManagedPolicies",
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


def deserialize_query(el: Element) -> RoleDetail:
    out: RoleDetail = {}  # type: ignore[typeddict-item]
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    child_role_name = el.find("RoleName")
    if child_role_name is not None:
        out["role_name"] = str(child_role_name.text or "")
    child_role_id = el.find("RoleId")
    if child_role_id is not None:
        out["role_id"] = str(child_role_id.text or "")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import capo_iam.types.date_type

        out["create_date"] = capo_iam.types.date_type.deserialize_query(
            child_create_date
        )
    child_assume_role_policy_document = el.find("AssumeRolePolicyDocument")
    if child_assume_role_policy_document is not None:
        out["assume_role_policy_document"] = str(
            child_assume_role_policy_document.text or ""
        )
    child_instance_profile_list = el.find("InstanceProfileList")
    if child_instance_profile_list is not None:
        import capo_iam.types.instance_profile_list_type

        out["instance_profile_list"] = (
            capo_iam.types.instance_profile_list_type.deserialize_query(
                child_instance_profile_list
            )
        )
    child_role_policy_list = el.find("RolePolicyList")
    if child_role_policy_list is not None:
        import capo_iam.types.policy_detail_list_type

        out["role_policy_list"] = (
            capo_iam.types.policy_detail_list_type.deserialize_query(
                child_role_policy_list
            )
        )
    child_attached_managed_policies = el.find("AttachedManagedPolicies")
    if child_attached_managed_policies is not None:
        import capo_iam.types.attached_policies_list_type

        out["attached_managed_policies"] = (
            capo_iam.types.attached_policies_list_type.deserialize_query(
                child_attached_managed_policies
            )
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
    child_role_last_used = el.find("RoleLastUsed")
    if child_role_last_used is not None:
        import capo_iam.types.role_last_used

        out["role_last_used"] = capo_iam.types.role_last_used.deserialize_query(
            child_role_last_used
        )
    return out
