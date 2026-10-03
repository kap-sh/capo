"""Generated from Smithy shape ``com.amazonaws.ssm#UpdatePatchBaselineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.baseline_description
    import capo_ssm.types.baseline_id
    import capo_ssm.types.baseline_name
    import capo_ssm.types.boolean
    import capo_ssm.types.patch_action
    import capo_ssm.types.patch_compliance_level
    import capo_ssm.types.patch_compliance_status
    import capo_ssm.types.patch_filter_group
    import capo_ssm.types.patch_id_list
    import capo_ssm.types.patch_rule_group
    import capo_ssm.types.patch_source_list


class UpdatePatchBaselineRequest(TypedDict, closed=True):
    baseline_id: "capo_ssm.types.baseline_id.BaselineId"
    """<p>The ID of the patch baseline to update.</p>"""
    name: NotRequired["capo_ssm.types.baseline_name.BaselineName"]
    """<p>The name of the patch baseline.</p>"""
    global_filters: NotRequired["capo_ssm.types.patch_filter_group.PatchFilterGroup"]
    """<p>A set of global filters used to include patches in the baseline.</p> <important> <p>The <code>GlobalFilters</code> parameter can be configured only by using the CLI or an Amazon Web Services SDK. It can't be configured from the Patch Manager console, and its value isn't displayed in the console.</p> </important>"""
    approval_rules: NotRequired["capo_ssm.types.patch_rule_group.PatchRuleGroup"]
    """<p>A set of rules used to include patches in the baseline.</p>"""
    approved_patches: NotRequired["capo_ssm.types.patch_id_list.PatchIdList"]
    """<p>A list of explicitly approved patches for the baseline.</p> <p>For information about accepted formats for lists of approved patches and rejected patches, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html">Package name formats for approved and rejected patch lists</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    approved_patches_compliance_level: NotRequired[
        "capo_ssm.types.patch_compliance_level.PatchComplianceLevel"
    ]
    """<p>Assigns a new compliance severity level to an existing patch baseline.</p>"""
    approved_patches_enable_non_security: NotRequired["capo_ssm.types.boolean.Boolean"]
    """<p>Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes. The default value is <code>false</code>. Applies to Linux managed nodes only.</p>"""
    rejected_patches: NotRequired["capo_ssm.types.patch_id_list.PatchIdList"]
    """<p>A list of explicitly rejected patches for the baseline.</p> <p>For information about accepted formats for lists of approved patches and rejected patches, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html">Package name formats for approved and rejected patch lists</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    rejected_patches_action: NotRequired["capo_ssm.types.patch_action.PatchAction"]
    """<p>The action for Patch Manager to take on patches included in the <code>RejectedPackages</code> list.</p> <dl> <dt>ALLOW_AS_DEPENDENCY</dt> <dd> <p> <b>Linux and macOS</b>: A package in the rejected patches list is installed only if it is a dependency of another package. It is considered compliant with the patch baseline, and its status is reported as <code>INSTALLED_OTHER</code>. This is the default action if no option is specified.</p> <p> <b>Windows Server</b>: Windows Server doesn't support the concept of package dependencies. If a package in the rejected patches list and already installed on the node, its status is reported as <code>INSTALLED_OTHER</code>. Any package not already installed on the node is skipped. This is the default action if no option is specified.</p> </dd> <dt>BLOCK</dt> <dd> <p> <b>All OSs</b>: Packages in the rejected patches list, and packages that include them as dependencies, aren't installed by Patch Manager under any circumstances. </p> <p>State value assignment for patch compliance:</p> <ul> <li> <p>If a package was installed before it was added to the rejected patches list, or is installed outside of Patch Manager afterward, it's considered noncompliant with the patch baseline and its status is reported as <code>INSTALLED_REJECTED</code>.</p> </li> <li> <p>If an update attempts to install a dependency package that is now rejected by the baseline, when previous versions of the package were not rejected, the package being updated is reported as <code>MISSING</code> for <code>SCAN</code> operations and as <code>FAILED</code> for <code>INSTALL</code> operations.</p> </li> </ul> </dd> </dl>"""
    description: NotRequired["capo_ssm.types.baseline_description.BaselineDescription"]
    """<p>A description of the patch baseline.</p>"""
    sources: NotRequired["capo_ssm.types.patch_source_list.PatchSourceList"]
    """<p>Information about the patches to use to update the managed nodes, including target operating systems and source repositories. Applies to Linux managed nodes only.</p>"""
    available_security_updates_compliance_status: NotRequired[
        "capo_ssm.types.patch_compliance_status.PatchComplianceStatus"
    ]
    """<p>Indicates the status to be assigned to security patches that are available but not approved because they don't meet the installation criteria specified in the patch baseline.</p> <p>Example scenario: Security patches that you might want installed can be skipped if you have specified a long period to wait after a patch is released before installation. If an update to the patch is released during your specified waiting period, the waiting period for installing the patch starts over. If the waiting period is too long, multiple versions of the patch could be released but never installed.</p> <p>Supported for Windows Server managed nodes only.</p>"""
    replace: NotRequired["capo_ssm.types.boolean.Boolean"]
    """<p>If True, then all fields that are required by the <a>CreatePatchBaseline</a> operation are also required for this API request. Optional fields that aren't specified are set to null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePatchBaselineRequest) -> dict:
    out: dict = {}
    out["BaselineId"] = value["baseline_id"]
    if "name" in value:
        out["Name"] = value["name"]
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
    if "replace" in value:
        out["Replace"] = value["replace"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePatchBaselineRequest:
    out: UpdatePatchBaselineRequest = {}  # type: ignore[typeddict-item]
    if data.get("BaselineId") is not None:
        out["baseline_id"] = data["BaselineId"]
    else:
        raise DeserializationError("UpdatePatchBaselineRequest.baseline_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
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
    if data.get("Replace") is not None:
        out["replace"] = data["Replace"]
    return out
