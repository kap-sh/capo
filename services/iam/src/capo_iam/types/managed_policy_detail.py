"""Generated from Smithy shape ``com.amazonaws.iam#ManagedPolicyDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.attachment_count_type
    import capo_iam.types.boolean_type
    import capo_iam.types.date_type
    import capo_iam.types.id_type
    import capo_iam.types.policy_description_type
    import capo_iam.types.policy_document_version_list_type
    import capo_iam.types.policy_name_type
    import capo_iam.types.policy_path_type
    import capo_iam.types.policy_version_id_type


class ManagedPolicyDetail(TypedDict, closed=True):
    policy_name: NotRequired["capo_iam.types.policy_name_type.policyNameType"]
    """<p>The friendly name (not ARN) identifying the policy.</p>"""
    policy_id: NotRequired["capo_iam.types.id_type.idType"]
    """<p>The stable and unique string identifying the policy.</p> <p>For more information about IDs, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>.</p>"""
    arn: NotRequired["capo_iam.types.arn_type.arnType"]
    path: NotRequired["capo_iam.types.policy_path_type.policyPathType"]
    """<p>The path to the policy.</p> <p>For more information about paths, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>.</p>"""
    default_version_id: NotRequired[
        "capo_iam.types.policy_version_id_type.policyVersionIdType"
    ]
    """<p>The identifier for the version of the policy that is set as the default (operative) version.</p> <p>For more information about policy versions, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html">Versioning for managed policies</a> in the <i>IAM User Guide</i>. </p>"""
    attachment_count: NotRequired[
        "capo_iam.types.attachment_count_type.attachmentCountType"
    ]
    """<p>The number of principal entities (users, groups, and roles) that the policy is attached to.</p>"""
    permissions_boundary_usage_count: NotRequired[
        "capo_iam.types.attachment_count_type.attachmentCountType"
    ]
    """<p>The number of entities (users and roles) for which the policy is used as the permissions boundary. </p> <p>For more information about permissions boundaries, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html">Permissions boundaries for IAM identities </a> in the <i>IAM User Guide</i>.</p>"""
    is_attachable: "capo_iam.types.boolean_type.booleanType"
    """<p>Specifies whether the policy can be attached to an IAM user, group, or role.</p>"""
    description: NotRequired[
        "capo_iam.types.policy_description_type.policyDescriptionType"
    ]
    """<p>A friendly description of the policy.</p>"""
    create_date: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when the policy was created.</p>"""
    update_date: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when the policy was last updated.</p> <p>When a policy has only one version, this field contains the date and time when the policy was created. When a policy has more than one version, this field contains the date and time when the most recent policy version was created.</p>"""
    policy_version_list: NotRequired[
        "capo_iam.types.policy_document_version_list_type.policyDocumentVersionListType"
    ]
    """<p>A list containing information about the versions of the policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ManagedPolicyDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "policy_name" in value:
        pairs.append((f"{key_prefix}PolicyName", str(value["policy_name"])))
    if "policy_id" in value:
        pairs.append((f"{key_prefix}PolicyId", str(value["policy_id"])))
    if "arn" in value:
        pairs.append((f"{key_prefix}Arn", str(value["arn"])))
    if "path" in value:
        pairs.append((f"{key_prefix}Path", str(value["path"])))
    if "default_version_id" in value:
        pairs.append(
            (f"{key_prefix}DefaultVersionId", str(value["default_version_id"]))
        )
    if "attachment_count" in value:
        pairs.append((f"{key_prefix}AttachmentCount", str(value["attachment_count"])))
    if "permissions_boundary_usage_count" in value:
        pairs.append(
            (
                f"{key_prefix}PermissionsBoundaryUsageCount",
                str(value["permissions_boundary_usage_count"]),
            )
        )
    pairs.append(
        (
            f"{key_prefix}IsAttachable",
            "true" if value.get("is_attachable", False) else "false",
        )
    )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "create_date" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["create_date"], pairs, f"{key_prefix}CreateDate"
        )
    if "update_date" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["update_date"], pairs, f"{key_prefix}UpdateDate"
        )
    if "policy_version_list" in value:
        import capo_iam.types.policy_document_version_list_type

        capo_iam.types.policy_document_version_list_type.serialize_query(
            value["policy_version_list"], pairs, f"{key_prefix}PolicyVersionList"
        )


def deserialize_query(el: Element) -> ManagedPolicyDetail:
    out: ManagedPolicyDetail = {}  # type: ignore[typeddict-item]
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    child_policy_id = el.find("PolicyId")
    if child_policy_id is not None:
        out["policy_id"] = str(child_policy_id.text or "")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    child_default_version_id = el.find("DefaultVersionId")
    if child_default_version_id is not None:
        out["default_version_id"] = str(child_default_version_id.text or "")
    child_attachment_count = el.find("AttachmentCount")
    if child_attachment_count is not None:
        out["attachment_count"] = int(child_attachment_count.text or "")
    child_permissions_boundary_usage_count = el.find("PermissionsBoundaryUsageCount")
    if child_permissions_boundary_usage_count is not None:
        out["permissions_boundary_usage_count"] = int(
            child_permissions_boundary_usage_count.text or ""
        )
    child_is_attachable = el.find("IsAttachable")
    if child_is_attachable is not None:
        out["is_attachable"] = (child_is_attachable.text or "").lower() == "true"
    else:
        out["is_attachable"] = False
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import capo_iam.types.date_type

        out["create_date"] = capo_iam.types.date_type.deserialize_query(
            child_create_date
        )
    child_update_date = el.find("UpdateDate")
    if child_update_date is not None:
        import capo_iam.types.date_type

        out["update_date"] = capo_iam.types.date_type.deserialize_query(
            child_update_date
        )
    child_policy_version_list = el.find("PolicyVersionList")
    if child_policy_version_list is not None:
        import capo_iam.types.policy_document_version_list_type

        out["policy_version_list"] = (
            capo_iam.types.policy_document_version_list_type.deserialize_query(
                child_policy_version_list
            )
        )
    return out
