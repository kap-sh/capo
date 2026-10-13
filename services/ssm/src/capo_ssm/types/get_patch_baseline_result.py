"""Generated from Smithy shape ``com.amazonaws.ssm#GetPatchBaselineResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.baseline_description
    import capo_ssm.types.baseline_id
    import capo_ssm.types.baseline_name
    import capo_ssm.types.boolean
    import capo_ssm.types.date_time
    import capo_ssm.types.operating_system
    import capo_ssm.types.patch_action
    import capo_ssm.types.patch_compliance_level
    import capo_ssm.types.patch_compliance_status
    import capo_ssm.types.patch_filter_group
    import capo_ssm.types.patch_group_list
    import capo_ssm.types.patch_id_list
    import capo_ssm.types.patch_rule_group
    import capo_ssm.types.patch_source_list


class GetPatchBaselineResult(TypedDict, closed=True):
    baseline_id: NotRequired["capo_ssm.types.baseline_id.BaselineId"]
    """<p>The ID of the retrieved patch baseline.</p>"""
    name: NotRequired["capo_ssm.types.baseline_name.BaselineName"]
    """<p>The name of the patch baseline.</p>"""
    operating_system: NotRequired["capo_ssm.types.operating_system.OperatingSystem"]
    """<p>Returns the operating system specified for the patch baseline.</p>"""
    global_filters: NotRequired["capo_ssm.types.patch_filter_group.PatchFilterGroup"]
    """<p>A set of global filters used to exclude patches from the baseline.</p>"""
    approval_rules: NotRequired["capo_ssm.types.patch_rule_group.PatchRuleGroup"]
    """<p>A set of rules used to include patches in the baseline.</p>"""
    approved_patches: NotRequired["capo_ssm.types.patch_id_list.PatchIdList"]
    """<p>A list of explicitly approved patches for the baseline.</p>"""
    approved_patches_compliance_level: NotRequired[
        "capo_ssm.types.patch_compliance_level.PatchComplianceLevel"
    ]
    """<p>Returns the specified compliance severity level for approved patches in the patch baseline.</p>"""
    approved_patches_enable_non_security: NotRequired["capo_ssm.types.boolean.Boolean"]
    """<p>Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes. The default value is <code>false</code>. Applies to Linux managed nodes only.</p>"""
    rejected_patches: NotRequired["capo_ssm.types.patch_id_list.PatchIdList"]
    """<p>A list of explicitly rejected patches for the baseline.</p>"""
    rejected_patches_action: NotRequired["capo_ssm.types.patch_action.PatchAction"]
    """<p>The action specified to take on patches included in the <code>RejectedPatches</code> list. A patch can be allowed only if it is a dependency of another package, or blocked entirely along with packages that include it as a dependency.</p>"""
    patch_groups: NotRequired["capo_ssm.types.patch_group_list.PatchGroupList"]
    """<p>Patch groups included in the patch baseline.</p>"""
    created_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date the patch baseline was created.</p>"""
    modified_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date the patch baseline was last modified.</p>"""
    description: NotRequired["capo_ssm.types.baseline_description.BaselineDescription"]
    """<p>A description of the patch baseline.</p>"""
    sources: NotRequired["capo_ssm.types.patch_source_list.PatchSourceList"]
    """<p>Information about the patches to use to update the managed nodes, including target operating systems and source repositories. Applies to Linux managed nodes only.</p>"""
    available_security_updates_compliance_status: NotRequired[
        "capo_ssm.types.patch_compliance_status.PatchComplianceStatus"
    ]
    """<p>Indicates the compliance status of managed nodes for which security-related patches are available but were not approved. This preference is specified when the <code>CreatePatchBaseline</code> or <code>UpdatePatchBaseline</code> commands are run.</p> <p>Applies to Windows Server managed nodes only.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPatchBaselineResult) -> dict:
    out: dict = {}
    if "baseline_id" in value:
        out["BaselineId"] = value["baseline_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "operating_system" in value:
        import capo_ssm.types.operating_system

        out["OperatingSystem"] = capo_ssm.types.operating_system.serialize_aws_json_1_1(
            value["operating_system"]
        )
    if "global_filters" in value:
        import capo_ssm.types.patch_filter_group

        out["GlobalFilters"] = capo_ssm.types.patch_filter_group.serialize_aws_json_1_1(
            value["global_filters"]
        )
    if "approval_rules" in value:
        import capo_ssm.types.patch_rule_group

        out["ApprovalRules"] = capo_ssm.types.patch_rule_group.serialize_aws_json_1_1(
            value["approval_rules"]
        )
    if "approved_patches" in value:
        import capo_ssm.types.patch_id_list

        out["ApprovedPatches"] = capo_ssm.types.patch_id_list.serialize_aws_json_1_1(
            value["approved_patches"]
        )
    if "approved_patches_compliance_level" in value:
        import capo_ssm.types.patch_compliance_level

        out["ApprovedPatchesComplianceLevel"] = (
            capo_ssm.types.patch_compliance_level.serialize_aws_json_1_1(
                value["approved_patches_compliance_level"]
            )
        )
    if "approved_patches_enable_non_security" in value:
        out["ApprovedPatchesEnableNonSecurity"] = value[
            "approved_patches_enable_non_security"
        ]
    if "rejected_patches" in value:
        import capo_ssm.types.patch_id_list

        out["RejectedPatches"] = capo_ssm.types.patch_id_list.serialize_aws_json_1_1(
            value["rejected_patches"]
        )
    if "rejected_patches_action" in value:
        import capo_ssm.types.patch_action

        out["RejectedPatchesAction"] = (
            capo_ssm.types.patch_action.serialize_aws_json_1_1(
                value["rejected_patches_action"]
            )
        )
    if "patch_groups" in value:
        import capo_ssm.types.patch_group_list

        out["PatchGroups"] = capo_ssm.types.patch_group_list.serialize_aws_json_1_1(
            value["patch_groups"]
        )
    if "created_date" in value:
        import capo_ssm.types.date_time

        out["CreatedDate"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["created_date"]
        )
    if "modified_date" in value:
        import capo_ssm.types.date_time

        out["ModifiedDate"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["modified_date"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "sources" in value:
        import capo_ssm.types.patch_source_list

        out["Sources"] = capo_ssm.types.patch_source_list.serialize_aws_json_1_1(
            value["sources"]
        )
    if "available_security_updates_compliance_status" in value:
        import capo_ssm.types.patch_compliance_status

        out["AvailableSecurityUpdatesComplianceStatus"] = (
            capo_ssm.types.patch_compliance_status.serialize_aws_json_1_1(
                value["available_security_updates_compliance_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPatchBaselineResult:
    out: GetPatchBaselineResult = {}  # type: ignore[typeddict-item]
    if data.get("BaselineId") is not None:
        out["baseline_id"] = data["BaselineId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("OperatingSystem") is not None:
        import capo_ssm.types.operating_system

        out["operating_system"] = (
            capo_ssm.types.operating_system.deserialize_aws_json_1_1(
                data["OperatingSystem"]
            )
        )
    if data.get("GlobalFilters") is not None:
        import capo_ssm.types.patch_filter_group

        out["global_filters"] = (
            capo_ssm.types.patch_filter_group.deserialize_aws_json_1_1(
                data["GlobalFilters"]
            )
        )
    if data.get("ApprovalRules") is not None:
        import capo_ssm.types.patch_rule_group

        out["approval_rules"] = (
            capo_ssm.types.patch_rule_group.deserialize_aws_json_1_1(
                data["ApprovalRules"]
            )
        )
    if data.get("ApprovedPatches") is not None:
        import capo_ssm.types.patch_id_list

        out["approved_patches"] = capo_ssm.types.patch_id_list.deserialize_aws_json_1_1(
            data["ApprovedPatches"]
        )
    if data.get("ApprovedPatchesComplianceLevel") is not None:
        import capo_ssm.types.patch_compliance_level

        out["approved_patches_compliance_level"] = (
            capo_ssm.types.patch_compliance_level.deserialize_aws_json_1_1(
                data["ApprovedPatchesComplianceLevel"]
            )
        )
    if data.get("ApprovedPatchesEnableNonSecurity") is not None:
        out["approved_patches_enable_non_security"] = data[
            "ApprovedPatchesEnableNonSecurity"
        ]
    if data.get("RejectedPatches") is not None:
        import capo_ssm.types.patch_id_list

        out["rejected_patches"] = capo_ssm.types.patch_id_list.deserialize_aws_json_1_1(
            data["RejectedPatches"]
        )
    if data.get("RejectedPatchesAction") is not None:
        import capo_ssm.types.patch_action

        out["rejected_patches_action"] = (
            capo_ssm.types.patch_action.deserialize_aws_json_1_1(
                data["RejectedPatchesAction"]
            )
        )
    if data.get("PatchGroups") is not None:
        import capo_ssm.types.patch_group_list

        out["patch_groups"] = capo_ssm.types.patch_group_list.deserialize_aws_json_1_1(
            data["PatchGroups"]
        )
    if data.get("CreatedDate") is not None:
        import capo_ssm.types.date_time

        out["created_date"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["CreatedDate"]
        )
    if data.get("ModifiedDate") is not None:
        import capo_ssm.types.date_time

        out["modified_date"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ModifiedDate"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Sources") is not None:
        import capo_ssm.types.patch_source_list

        out["sources"] = capo_ssm.types.patch_source_list.deserialize_aws_json_1_1(
            data["Sources"]
        )
    if data.get("AvailableSecurityUpdatesComplianceStatus") is not None:
        import capo_ssm.types.patch_compliance_status

        out["available_security_updates_compliance_status"] = (
            capo_ssm.types.patch_compliance_status.deserialize_aws_json_1_1(
                data["AvailableSecurityUpdatesComplianceStatus"]
            )
        )
    return out


def redact_sensitive(value: GetPatchBaselineResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sources" in value:
        import capo_ssm.types.patch_source_list

        out["sources"] = capo_ssm.types.patch_source_list.redact_sensitive(
            value["sources"]
        )
    return out
