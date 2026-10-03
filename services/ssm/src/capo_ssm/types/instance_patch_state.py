"""Generated from Smithy shape ``com.amazonaws.ssm#InstancePatchState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.baseline_id
    import capo_ssm.types.date_time
    import capo_ssm.types.install_override_list
    import capo_ssm.types.instance_id
    import capo_ssm.types.owner_information
    import capo_ssm.types.patch_available_security_update_count
    import capo_ssm.types.patch_critical_non_compliant_count
    import capo_ssm.types.patch_failed_count
    import capo_ssm.types.patch_group
    import capo_ssm.types.patch_installed_count
    import capo_ssm.types.patch_installed_other_count
    import capo_ssm.types.patch_installed_pending_reboot_count
    import capo_ssm.types.patch_installed_rejected_count
    import capo_ssm.types.patch_missing_count
    import capo_ssm.types.patch_not_applicable_count
    import capo_ssm.types.patch_operation_type
    import capo_ssm.types.patch_other_non_compliant_count
    import capo_ssm.types.patch_security_non_compliant_count
    import capo_ssm.types.patch_unreported_not_applicable_count
    import capo_ssm.types.reboot_option
    import capo_ssm.types.snapshot_id


class InstancePatchState(TypedDict, closed=True):
    instance_id: "capo_ssm.types.instance_id.InstanceId"
    """<p>The ID of the managed node the high-level patch compliance information was collected for.</p>"""
    patch_group: "capo_ssm.types.patch_group.PatchGroup"
    """<p>The name of the patch group the managed node belongs to.</p>"""
    baseline_id: "capo_ssm.types.baseline_id.BaselineId"
    """<p>The ID of the patch baseline used to patch the managed node.</p>"""
    snapshot_id: NotRequired["capo_ssm.types.snapshot_id.SnapshotId"]
    """<p>The ID of the patch baseline snapshot used during the patching operation when this compliance data was collected.</p>"""
    install_override_list: NotRequired[
        "capo_ssm.types.install_override_list.InstallOverrideList"
    ]
    """<p>An https URL or an Amazon Simple Storage Service (Amazon S3) path-style URL to a list of patches to be installed. This patch installation list, which you maintain in an S3 bucket in YAML format and specify in the SSM document <code>AWS-RunPatchBaseline</code>, overrides the patches specified by the default patch baseline.</p> <p>For more information about the <code>InstallOverrideList</code> parameter, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-about-aws-runpatchbaseline.html">SSM Command document for patching: <code>AWS-RunPatchBaseline</code> </a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    owner_information: NotRequired["capo_ssm.types.owner_information.OwnerInformation"]
    """<p>Placeholder information. This field will always be empty in the current release of the service.</p>"""
    installed_count: "capo_ssm.types.patch_installed_count.PatchInstalledCount"
    """<p>The number of patches from the patch baseline that are installed on the managed node.</p>"""
    installed_other_count: (
        "capo_ssm.types.patch_installed_other_count.PatchInstalledOtherCount"
    )
    """<p>The number of patches not specified in the patch baseline that are installed on the managed node.</p>"""
    installed_pending_reboot_count: NotRequired[
        "capo_ssm.types.patch_installed_pending_reboot_count.PatchInstalledPendingRebootCount"
    ]
    """<p>The number of patches installed by Patch Manager since the last time the managed node was rebooted.</p>"""
    installed_rejected_count: NotRequired[
        "capo_ssm.types.patch_installed_rejected_count.PatchInstalledRejectedCount"
    ]
    """<p>The number of patches installed on a managed node that are specified in a <code>RejectedPatches</code> list. Patches with a status of <code>InstalledRejected</code> were typically installed before they were added to a <code>RejectedPatches</code> list.</p> <note> <p>If <code>ALLOW_AS_DEPENDENCY</code> is the specified option for <code>RejectedPatchesAction</code>, the value of <code>InstalledRejectedCount</code> will always be <code>0</code> (zero).</p> </note>"""
    missing_count: "capo_ssm.types.patch_missing_count.PatchMissingCount"
    """<p>The number of patches from the patch baseline that are applicable for the managed node but aren't currently installed.</p>"""
    failed_count: "capo_ssm.types.patch_failed_count.PatchFailedCount"
    """<p>The number of patches from the patch baseline that were attempted to be installed during the last patching operation, but failed to install.</p>"""
    unreported_not_applicable_count: NotRequired[
        "capo_ssm.types.patch_unreported_not_applicable_count.PatchUnreportedNotApplicableCount"
    ]
    """<p>The number of patches beyond the supported limit of <code>NotApplicableCount</code> that aren't reported by name to Inventory. Inventory is a tool in Amazon Web Services Systems Manager.</p>"""
    not_applicable_count: (
        "capo_ssm.types.patch_not_applicable_count.PatchNotApplicableCount"
    )
    """<p>The number of patches from the patch baseline that aren't applicable for the managed node and therefore aren't installed on the node. This number may be truncated if the list of patch names is very large. The number of patches beyond this limit are reported in <code>UnreportedNotApplicableCount</code>.</p>"""
    available_security_update_count: NotRequired[
        "capo_ssm.types.patch_available_security_update_count.PatchAvailableSecurityUpdateCount"
    ]
    """<p>The number of security-related patches that are available but not approved because they didn't meet the patch baseline requirements. For example, an updated version of a patch might have been released before the specified auto-approval period was over.</p> <p>Applies to Windows Server managed nodes only.</p>"""
    operation_start_time: "capo_ssm.types.date_time.DateTime"
    """<p>The time the most recent patching operation was started on the managed node.</p>"""
    operation_end_time: "capo_ssm.types.date_time.DateTime"
    """<p>The time the most recent patching operation completed on the managed node.</p>"""
    operation: "capo_ssm.types.patch_operation_type.PatchOperationType"
    """<p>The type of patching operation that was performed: or </p> <ul> <li> <p> <code>SCAN</code> assesses the patch compliance state.</p> </li> <li> <p> <code>INSTALL</code> installs missing patches.</p> </li> </ul>"""
    last_no_reboot_install_operation_time: NotRequired[
        "capo_ssm.types.date_time.DateTime"
    ]
    """<p>The time of the last attempt to patch the managed node with <code>NoReboot</code> specified as the reboot option.</p>"""
    reboot_option: NotRequired["capo_ssm.types.reboot_option.RebootOption"]
    """<p>Indicates the reboot option specified in the patch baseline.</p> <note> <p>Reboot options apply to <code>Install</code> operations only. Reboots aren't attempted for Patch Manager <code>Scan</code> operations.</p> </note> <ul> <li> <p> <code>RebootIfNeeded</code>: Patch Manager tries to reboot the managed node if it installed any patches, or if any patches are detected with a status of <code>InstalledPendingReboot</code>.</p> </li> <li> <p> <code>NoReboot</code>: Patch Manager attempts to install missing packages without trying to reboot the system. Patches installed with this option are assigned a status of <code>InstalledPendingReboot</code>. These patches might not be in effect until a reboot is performed.</p> </li> </ul>"""
    critical_non_compliant_count: NotRequired[
        "capo_ssm.types.patch_critical_non_compliant_count.PatchCriticalNonCompliantCount"
    ]
    """<p>The number of patches per node that are specified as <code>Critical</code> for compliance reporting in the patch baseline aren't installed. These patches might be missing, have failed installation, were rejected, or were installed but awaiting a required managed node reboot. The status of these managed nodes is <code>NON_COMPLIANT</code>.</p>"""
    security_non_compliant_count: NotRequired[
        "capo_ssm.types.patch_security_non_compliant_count.PatchSecurityNonCompliantCount"
    ]
    """<p>The number of patches per node that are specified as <code>Security</code> in a patch advisory aren't installed. These patches might be missing, have failed installation, were rejected, or were installed but awaiting a required managed node reboot. The status of these managed nodes is <code>NON_COMPLIANT</code>.</p>"""
    other_non_compliant_count: NotRequired[
        "capo_ssm.types.patch_other_non_compliant_count.PatchOtherNonCompliantCount"
    ]
    """<p>The number of patches per node that are specified as other than <code>Critical</code> or <code>Security</code> but aren't compliant with the patch baseline. The status of these managed nodes is <code>NON_COMPLIANT</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePatchState) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["PatchGroup"] = value["patch_group"]
    out["BaselineId"] = value["baseline_id"]
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    if "install_override_list" in value:
        out["InstallOverrideList"] = value["install_override_list"]
    if "owner_information" in value:
        out["OwnerInformation"] = value["owner_information"]
    out["InstalledCount"] = value.get("installed_count", 0)
    out["InstalledOtherCount"] = value.get("installed_other_count", 0)
    if "installed_pending_reboot_count" in value:
        out["InstalledPendingRebootCount"] = value["installed_pending_reboot_count"]
    if "installed_rejected_count" in value:
        out["InstalledRejectedCount"] = value["installed_rejected_count"]
    out["MissingCount"] = value.get("missing_count", 0)
    out["FailedCount"] = value.get("failed_count", 0)
    if "unreported_not_applicable_count" in value:
        out["UnreportedNotApplicableCount"] = value["unreported_not_applicable_count"]
    out["NotApplicableCount"] = value.get("not_applicable_count", 0)
    if "available_security_update_count" in value:
        out["AvailableSecurityUpdateCount"] = value["available_security_update_count"]
    import capo_ssm.types.date_time

    out["OperationStartTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
        value["operation_start_time"]
    )
    import capo_ssm.types.date_time

    out["OperationEndTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
        value["operation_end_time"]
    )
    import capo_ssm.types.patch_operation_type

    out["Operation"] = capo_ssm.types.patch_operation_type.serialize_aws_json_1_1(
        value["operation"]
    )
    if "last_no_reboot_install_operation_time" in value:
        import capo_ssm.types.date_time

        out["LastNoRebootInstallOperationTime"] = (
            capo_ssm.types.date_time.serialize_aws_json_1_1(
                value["last_no_reboot_install_operation_time"]
            )
        )
    if "reboot_option" in value:
        import capo_ssm.types.reboot_option

        out["RebootOption"] = capo_ssm.types.reboot_option.serialize_aws_json_1_1(
            value["reboot_option"]
        )
    if "critical_non_compliant_count" in value:
        out["CriticalNonCompliantCount"] = value["critical_non_compliant_count"]
    if "security_non_compliant_count" in value:
        out["SecurityNonCompliantCount"] = value["security_non_compliant_count"]
    if "other_non_compliant_count" in value:
        out["OtherNonCompliantCount"] = value["other_non_compliant_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstancePatchState:
    out: InstancePatchState = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("InstancePatchState.instance_id required")
    if data.get("PatchGroup") is not None:
        out["patch_group"] = data["PatchGroup"]
    else:
        raise DeserializationError("InstancePatchState.patch_group required")
    if data.get("BaselineId") is not None:
        out["baseline_id"] = data["BaselineId"]
    else:
        raise DeserializationError("InstancePatchState.baseline_id required")
    if data.get("SnapshotId") is not None:
        out["snapshot_id"] = data["SnapshotId"]
    if data.get("InstallOverrideList") is not None:
        out["install_override_list"] = data["InstallOverrideList"]
    if data.get("OwnerInformation") is not None:
        out["owner_information"] = data["OwnerInformation"]
    if data.get("InstalledCount") is not None:
        out["installed_count"] = data["InstalledCount"]
    else:
        out["installed_count"] = 0
    if data.get("InstalledOtherCount") is not None:
        out["installed_other_count"] = data["InstalledOtherCount"]
    else:
        out["installed_other_count"] = 0
    if data.get("InstalledPendingRebootCount") is not None:
        out["installed_pending_reboot_count"] = data["InstalledPendingRebootCount"]
    if data.get("InstalledRejectedCount") is not None:
        out["installed_rejected_count"] = data["InstalledRejectedCount"]
    if data.get("MissingCount") is not None:
        out["missing_count"] = data["MissingCount"]
    else:
        out["missing_count"] = 0
    if data.get("FailedCount") is not None:
        out["failed_count"] = data["FailedCount"]
    else:
        out["failed_count"] = 0
    if data.get("UnreportedNotApplicableCount") is not None:
        out["unreported_not_applicable_count"] = data["UnreportedNotApplicableCount"]
    if data.get("NotApplicableCount") is not None:
        out["not_applicable_count"] = data["NotApplicableCount"]
    else:
        out["not_applicable_count"] = 0
    if data.get("AvailableSecurityUpdateCount") is not None:
        out["available_security_update_count"] = data["AvailableSecurityUpdateCount"]
    if data.get("OperationStartTime") is not None:
        import capo_ssm.types.date_time

        out["operation_start_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["OperationStartTime"]
        )
    else:
        raise DeserializationError("InstancePatchState.operation_start_time required")
    if data.get("OperationEndTime") is not None:
        import capo_ssm.types.date_time

        out["operation_end_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["OperationEndTime"]
        )
    else:
        raise DeserializationError("InstancePatchState.operation_end_time required")
    if data.get("Operation") is not None:
        import capo_ssm.types.patch_operation_type

        out["operation"] = capo_ssm.types.patch_operation_type.deserialize_aws_json_1_1(
            data["Operation"]
        )
    else:
        raise DeserializationError("InstancePatchState.operation required")
    if data.get("LastNoRebootInstallOperationTime") is not None:
        import capo_ssm.types.date_time

        out["last_no_reboot_install_operation_time"] = (
            capo_ssm.types.date_time.deserialize_aws_json_1_1(
                data["LastNoRebootInstallOperationTime"]
            )
        )
    if data.get("RebootOption") is not None:
        import capo_ssm.types.reboot_option

        out["reboot_option"] = capo_ssm.types.reboot_option.deserialize_aws_json_1_1(
            data["RebootOption"]
        )
    if data.get("CriticalNonCompliantCount") is not None:
        out["critical_non_compliant_count"] = data["CriticalNonCompliantCount"]
    if data.get("SecurityNonCompliantCount") is not None:
        out["security_non_compliant_count"] = data["SecurityNonCompliantCount"]
    if data.get("OtherNonCompliantCount") is not None:
        out["other_non_compliant_count"] = data["OtherNonCompliantCount"]
    return out
