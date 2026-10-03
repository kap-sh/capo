"""Generated from Smithy shape ``com.amazonaws.iam#GroupDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.attached_policies_list_type
    import capo_iam.types.date_type
    import capo_iam.types.group_name_type
    import capo_iam.types.id_type
    import capo_iam.types.path_type
    import capo_iam.types.policy_detail_list_type


class GroupDetail(TypedDict, closed=True):
    path: NotRequired["capo_iam.types.path_type.pathType"]
    """<p>The path to the group. For more information about paths, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>.</p>"""
    group_name: NotRequired["capo_iam.types.group_name_type.groupNameType"]
    """<p>The friendly name that identifies the group.</p>"""
    group_id: NotRequired["capo_iam.types.id_type.idType"]
    """<p>The stable and unique string identifying the group. For more information about IDs, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>.</p>"""
    arn: NotRequired["capo_iam.types.arn_type.arnType"]
    create_date: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when the group was created.</p>"""
    group_policy_list: NotRequired[
        "capo_iam.types.policy_detail_list_type.policyDetailListType"
    ]
    """<p>A list of the inline policies embedded in the group.</p>"""
    attached_managed_policies: NotRequired[
        "capo_iam.types.attached_policies_list_type.attachedPoliciesListType"
    ]
    """<p>A list of the managed policies attached to the group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GroupDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "path" in value:
        pairs.append((f"{key_prefix}Path", str(value["path"])))
    if "group_name" in value:
        pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))
    if "group_id" in value:
        pairs.append((f"{key_prefix}GroupId", str(value["group_id"])))
    if "arn" in value:
        pairs.append((f"{key_prefix}Arn", str(value["arn"])))
    if "create_date" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["create_date"], pairs, f"{key_prefix}CreateDate"
        )
    if "group_policy_list" in value:
        import capo_iam.types.policy_detail_list_type

        capo_iam.types.policy_detail_list_type.serialize_query(
            value["group_policy_list"], pairs, f"{key_prefix}GroupPolicyList"
        )
    if "attached_managed_policies" in value:
        import capo_iam.types.attached_policies_list_type

        capo_iam.types.attached_policies_list_type.serialize_query(
            value["attached_managed_policies"],
            pairs,
            f"{key_prefix}AttachedManagedPolicies",
        )


def deserialize_query(el: Element) -> GroupDetail:
    out: GroupDetail = {}  # type: ignore[typeddict-item]
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import capo_iam.types.date_type

        out["create_date"] = capo_iam.types.date_type.deserialize_query(
            child_create_date
        )
    child_group_policy_list = el.find("GroupPolicyList")
    if child_group_policy_list is not None:
        import capo_iam.types.policy_detail_list_type

        out["group_policy_list"] = (
            capo_iam.types.policy_detail_list_type.deserialize_query(
                child_group_policy_list
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
    return out
