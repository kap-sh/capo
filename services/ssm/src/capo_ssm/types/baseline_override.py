"""Generated from Smithy shape ``com.amazonaws.ssm#BaselineOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.boolean
    import capo_ssm.types.operating_system
    import capo_ssm.types.patch_action
    import capo_ssm.types.patch_compliance_level
    import capo_ssm.types.patch_compliance_status
    import capo_ssm.types.patch_filter_group
    import capo_ssm.types.patch_id_list
    import capo_ssm.types.patch_rule_group
    import capo_ssm.types.patch_source_list


class BaselineOverride(TypedDict, closed=True):
    operating_system: NotRequired["capo_ssm.types.operating_system.OperatingSystem"]
    """<p>The operating system rule used by the patch baseline override.</p>"""
    global_filters: NotRequired["capo_ssm.types.patch_filter_group.PatchFilterGroup"]
    approval_rules: NotRequired["capo_ssm.types.patch_rule_group.PatchRuleGroup"]
    approved_patches: NotRequired["capo_ssm.types.patch_id_list.PatchIdList"]
    """<p>A list of explicitly approved patches for the baseline.</p> <p>For information about accepted formats for lists of approved patches and rejected patches, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html">Package name formats for approved and rejected patch lists</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    approved_patches_compliance_level: NotRequired[
        "capo_ssm.types.patch_compliance_level.PatchComplianceLevel"
    ]
    """<p>Defines the compliance level for approved patches. When an approved patch is reported as missing, this value describes the severity of the compliance violation.</p>"""
    rejected_patches: NotRequired["capo_ssm.types.patch_id_list.PatchIdList"]
    """<p>A list of explicitly rejected patches for the baseline.</p> <p>For information about accepted formats for lists of approved patches and rejected patches, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html">Package name formats for approved and rejected patch lists</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    rejected_patches_action: NotRequired["capo_ssm.types.patch_action.PatchAction"]
    """<p>The action for Patch Manager to take on patches included in the <code>RejectedPackages</code> list. A patch can be allowed only if it is a dependency of another package, or blocked entirely along with packages that include it as a dependency.</p>"""
    approved_patches_enable_non_security: "capo_ssm.types.boolean.Boolean"
    """<p>Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes. The default value is <code>false</code>. Applies to Linux managed nodes only.</p>"""
    sources: NotRequired["capo_ssm.types.patch_source_list.PatchSourceList"]
    """<p>Information about the patches to use to update the managed nodes, including target operating systems and source repositories. Applies to Linux managed nodes only.</p>"""
    available_security_updates_compliance_status: NotRequired[
        "capo_ssm.types.patch_compliance_status.PatchComplianceStatus"
    ]
    """<p>Indicates whether managed nodes for which there are available security-related patches that have not been approved by the baseline are being defined as <code>COMPLIANT</code> or <code>NON_COMPLIANT</code>. This option is specified when the <code>CreatePatchBaseline</code> or <code>UpdatePatchBaseline</code> commands are run.</p> <p>Applies to Windows Server managed nodes only.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BaselineOverride) -> dict:
    out: dict = {}
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
    out["ApprovedPatchesEnableNonSecurity"] = value.get(
        "approved_patches_enable_non_security", False
    )
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


def deserialize_aws_json_1_1(data: dict) -> BaselineOverride:
    out: BaselineOverride = {}  # type: ignore[typeddict-item]
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
    if data.get("ApprovedPatchesEnableNonSecurity") is not None:
        out["approved_patches_enable_non_security"] = data[
            "ApprovedPatchesEnableNonSecurity"
        ]
    else:
        out["approved_patches_enable_non_security"] = False
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
