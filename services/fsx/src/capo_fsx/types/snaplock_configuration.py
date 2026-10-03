"""Generated from Smithy shape ``com.amazonaws.fsx#SnaplockConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.autocommit_period
    import capo_fsx.types.flag
    import capo_fsx.types.privileged_delete
    import capo_fsx.types.snaplock_retention_period
    import capo_fsx.types.snaplock_type


class SnaplockConfiguration(TypedDict, closed=True):
    audit_log_volume: NotRequired["capo_fsx.types.flag.Flag"]
    """<p>Enables or disables the audit log volume for an FSx for ONTAP SnapLock volume. The default value is <code>false</code>. If you set <code>AuditLogVolume</code> to <code>true</code>, the SnapLock volume is created as an audit log volume. The minimum retention period for an audit log volume is six months. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/how-snaplock-works.html#snaplock-audit-log-volume"> SnapLock audit log volumes</a>. </p>"""
    autocommit_period: NotRequired["capo_fsx.types.autocommit_period.AutocommitPeriod"]
    """<p>The configuration object for setting the autocommit period of files in an FSx for ONTAP SnapLock volume. </p>"""
    privileged_delete: NotRequired["capo_fsx.types.privileged_delete.PrivilegedDelete"]
    """<p>Enables, disables, or permanently disables privileged delete on an FSx for ONTAP SnapLock Enterprise volume. Enabling privileged delete allows SnapLock administrators to delete write once, read many (WORM) files even if they have active retention periods. <code>PERMANENTLY_DISABLED</code> is a terminal state. If privileged delete is permanently disabled on a SnapLock volume, you can't re-enable it. The default value is <code>DISABLED</code>. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-enterprise.html#privileged-delete">Privileged delete</a>. </p>"""
    retention_period: NotRequired[
        "capo_fsx.types.snaplock_retention_period.SnaplockRetentionPeriod"
    ]
    """<p>Specifies the retention period of an FSx for ONTAP SnapLock volume. </p>"""
    snaplock_type: NotRequired["capo_fsx.types.snaplock_type.SnaplockType"]
    """<p>Specifies the retention mode of an FSx for ONTAP SnapLock volume. After it is set, it can't be changed. You can choose one of the following retention modes: </p> <ul> <li> <p> <code>COMPLIANCE</code>: Files transitioned to write once, read many (WORM) on a Compliance volume can't be deleted until their retention periods expire. This retention mode is used to address government or industry-specific mandates or to protect against ransomware attacks. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-compliance.html">SnapLock Compliance</a>. </p> </li> <li> <p> <code>ENTERPRISE</code>: Files transitioned to WORM on an Enterprise volume can be deleted by authorized users before their retention periods expire using privileged delete. This retention mode is used to advance an organization's data integrity and internal compliance or to test retention settings before using SnapLock Compliance. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-enterprise.html">SnapLock Enterprise</a>. </p> </li> </ul>"""
    volume_append_mode_enabled: NotRequired["capo_fsx.types.flag.Flag"]
    """<p>Enables or disables volume-append mode on an FSx for ONTAP SnapLock volume. Volume-append mode allows you to create WORM-appendable files and write data to them incrementally. The default value is <code>false</code>. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/worm-state.html#worm-state-append">Volume-append mode</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnaplockConfiguration) -> dict:
    out: dict = {}
    if "audit_log_volume" in value:
        out["AuditLogVolume"] = value["audit_log_volume"]
    if "autocommit_period" in value:
        import capo_fsx.types.autocommit_period

        out["AutocommitPeriod"] = (
            capo_fsx.types.autocommit_period.serialize_aws_json_1_1(
                value["autocommit_period"]
            )
        )
    if "privileged_delete" in value:
        import capo_fsx.types.privileged_delete

        out["PrivilegedDelete"] = (
            capo_fsx.types.privileged_delete.serialize_aws_json_1_1(
                value["privileged_delete"]
            )
        )
    if "retention_period" in value:
        import capo_fsx.types.snaplock_retention_period

        out["RetentionPeriod"] = (
            capo_fsx.types.snaplock_retention_period.serialize_aws_json_1_1(
                value["retention_period"]
            )
        )
    if "snaplock_type" in value:
        import capo_fsx.types.snaplock_type

        out["SnaplockType"] = capo_fsx.types.snaplock_type.serialize_aws_json_1_1(
            value["snaplock_type"]
        )
    if "volume_append_mode_enabled" in value:
        out["VolumeAppendModeEnabled"] = value["volume_append_mode_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SnaplockConfiguration:
    out: SnaplockConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AuditLogVolume") is not None:
        out["audit_log_volume"] = data["AuditLogVolume"]
    if data.get("AutocommitPeriod") is not None:
        import capo_fsx.types.autocommit_period

        out["autocommit_period"] = (
            capo_fsx.types.autocommit_period.deserialize_aws_json_1_1(
                data["AutocommitPeriod"]
            )
        )
    if data.get("PrivilegedDelete") is not None:
        import capo_fsx.types.privileged_delete

        out["privileged_delete"] = (
            capo_fsx.types.privileged_delete.deserialize_aws_json_1_1(
                data["PrivilegedDelete"]
            )
        )
    if data.get("RetentionPeriod") is not None:
        import capo_fsx.types.snaplock_retention_period

        out["retention_period"] = (
            capo_fsx.types.snaplock_retention_period.deserialize_aws_json_1_1(
                data["RetentionPeriod"]
            )
        )
    if data.get("SnaplockType") is not None:
        import capo_fsx.types.snaplock_type

        out["snaplock_type"] = capo_fsx.types.snaplock_type.deserialize_aws_json_1_1(
            data["SnaplockType"]
        )
    if data.get("VolumeAppendModeEnabled") is not None:
        out["volume_append_mode_enabled"] = data["VolumeAppendModeEnabled"]
    return out
