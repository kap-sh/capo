"""Generated from Smithy shape ``com.amazonaws.ssm#PatchRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.approve_after_days
    import capo_ssm.types.boolean
    import capo_ssm.types.patch_compliance_level
    import capo_ssm.types.patch_filter_group
    import capo_ssm.types.patch_string_date_time


class PatchRule(TypedDict, closed=True):
    patch_filter_group: "capo_ssm.types.patch_filter_group.PatchFilterGroup"
    """<p>The patch filter group that defines the criteria for the rule.</p>"""
    compliance_level: NotRequired[
        "capo_ssm.types.patch_compliance_level.PatchComplianceLevel"
    ]
    """<p>A compliance severity level for all approved patches in a patch baseline.</p>"""
    approve_after_days: NotRequired[
        "capo_ssm.types.approve_after_days.ApproveAfterDays"
    ]
    """<p>The number of days after the release date of each patch matched by the rule that the patch is marked as approved in the patch baseline. For example, a value of <code>7</code> means that patches are approved seven days after they are released.</p> <p>Patch Manager evaluates patch release dates using Coordinated Universal Time (UTC). If a patch is released at <code>2025-11-09T18:00:00Z</code> and <code>ApproveAfterDays</code> is set to <code>7</code>, the patch will be approved after <code>2025-11-16T18:00:00Z</code>.</p> <p>This parameter is marked as <code>Required: No</code>, but your request must include a value for either <code>ApproveAfterDays</code> or <code>ApproveUntilDate</code>.</p> <p>Not supported for Debian Server or Ubuntu Server.</p> <important> <p>Use caution when setting this value for Windows Server patch baselines. Because patch updates that are replaced by later updates are removed, setting too broad a value for this parameter can result in crucial patches not being installed. For more information, see the <b>Windows Server</b> tab in the topic <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-selecting-patches.html">How security patches are selected</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> </important>"""
    approve_until_date: NotRequired[
        "capo_ssm.types.patch_string_date_time.PatchStringDateTime"
    ]
    """<p>The cutoff date for auto approval of released patches. Any patches released on or before this date are installed automatically.</p> <p>Enter dates in the format <code>YYYY-MM-DD</code>. For example, <code>2025-11-16</code>.</p> <p>Patch Manager evaluates patch release dates using Coordinated Universal Time (UTC). If you enter the date <code>2025-11-16</code>, patches released between <code>2025-11-16T00:00:00Z</code> and <code>2025-11-16T23:59:59Z</code> will be included in the approval.</p> <p>This parameter is marked as <code>Required: No</code>, but your request must include a value for either <code>ApproveUntilDate</code> or <code>ApproveAfterDays</code>.</p> <p>Not supported for Debian Server or Ubuntu Server.</p> <important> <p>Use caution when setting this value for Windows Server patch baselines. Because patch updates that are replaced by later updates are removed, setting too broad a value for this parameter can result in crucial patches not being installed. For more information, see the <b>Windows Server</b> tab in the topic <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-selecting-patches.html">How security patches are selected</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> </important>"""
    enable_non_security: NotRequired["capo_ssm.types.boolean.Boolean"]
    """<p>For managed nodes identified by the approval rule filters, enables a patch baseline to apply non-security updates available in the specified repository. The default value is <code>false</code>. Applies to Linux managed nodes only.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchRule) -> dict:
    out: dict = {}
    import capo_ssm.types.patch_filter_group

    out["PatchFilterGroup"] = capo_ssm.types.patch_filter_group.serialize_aws_json_1_1(
        value["patch_filter_group"]
    )
    if "compliance_level" in value:
        import capo_ssm.types.patch_compliance_level

        out["ComplianceLevel"] = (
            capo_ssm.types.patch_compliance_level.serialize_aws_json_1_1(
                value["compliance_level"]
            )
        )
    if "approve_after_days" in value:
        out["ApproveAfterDays"] = value["approve_after_days"]
    if "approve_until_date" in value:
        out["ApproveUntilDate"] = value["approve_until_date"]
    if "enable_non_security" in value:
        out["EnableNonSecurity"] = value["enable_non_security"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PatchRule:
    out: PatchRule = {}  # type: ignore[typeddict-item]
    if data.get("PatchFilterGroup") is not None:
        import capo_ssm.types.patch_filter_group

        out["patch_filter_group"] = (
            capo_ssm.types.patch_filter_group.deserialize_aws_json_1_1(
                data["PatchFilterGroup"]
            )
        )
    else:
        raise DeserializationError("PatchRule.patch_filter_group required")
    if data.get("ComplianceLevel") is not None:
        import capo_ssm.types.patch_compliance_level

        out["compliance_level"] = (
            capo_ssm.types.patch_compliance_level.deserialize_aws_json_1_1(
                data["ComplianceLevel"]
            )
        )
    if data.get("ApproveAfterDays") is not None:
        out["approve_after_days"] = data["ApproveAfterDays"]
    if data.get("ApproveUntilDate") is not None:
        out["approve_until_date"] = data["ApproveUntilDate"]
    if data.get("EnableNonSecurity") is not None:
        out["enable_non_security"] = data["EnableNonSecurity"]
    return out
