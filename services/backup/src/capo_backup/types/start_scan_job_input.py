"""Generated from Smithy shape ``com.amazonaws.backup#StartScanJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_backup.types.malware_scanner
    import capo_backup.types.scan_mode


class StartScanJobInput(TypedDict, closed=True):
    backup_vault_name: "str"
    r"""<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p> <p>Pattern: <code>^[a-zA-Z0-9\-\_]{2,50}$</code> </p>"""
    continuous_scan_end_time: NotRequired["datetime.datetime"]
    """<p>The point in time the scan job will scan up to for a continuous backup.</p>"""
    iam_role_arn: "str"
    """<p>Specifies the IAM role ARN used to create the target recovery point; for example, <code>arn:aws:iam::123456789012:role/S3Access</code>.</p>"""
    idempotency_token: NotRequired["str"]
    """<p>A customer-chosen string that you can use to distinguish between otherwise identical calls to <code>StartScanJob</code>. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>"""
    malware_scanner: "capo_backup.types.malware_scanner.MalwareScanner"
    """<p>Specifies the malware scanner used during the scan job. Currently only supports <code>GUARDDUTY</code>.</p>"""
    recovery_point_arn: "str"
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a recovery point. This is your target recovery point for a full scan. If you are running an incremental scan, this will be your a recovery point which has been created after your base recovery point selection.</p>"""
    scan_base_recovery_point_arn: NotRequired["str"]
    """<p>An ARN that uniquely identifies the base recovery point to be used for incremental scanning.</p>"""
    scan_mode: "capo_backup.types.scan_mode.ScanMode"
    """<p>Specifies the scan type use for the scan job.</p> <p>Includes:</p> <ul> <li> <p> <code>FULL_SCAN</code> will scan the entire data lineage within the backup.</p> </li> <li> <p> <code>INCREMENTAL_SCAN</code> will scan the data difference between the target recovery point and base recovery point ARN.</p> </li> </ul>"""
    scanner_role_arn: "str"
    """<p>Specified the IAM scanner role ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartScanJobInput) -> dict:
    out: dict = {}
    out["BackupVaultName"] = value["backup_vault_name"]
    if "continuous_scan_end_time" in value:
        import capo_backup.types._prelude.timestamp

        out["ContinuousScanEndTime"] = (
            capo_backup.types._prelude.timestamp.serialize_json(
                value["continuous_scan_end_time"]
            )
        )
    out["IamRoleArn"] = value["iam_role_arn"]
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    import capo_backup.types.malware_scanner

    out["MalwareScanner"] = capo_backup.types.malware_scanner.serialize_json(
        value["malware_scanner"]
    )
    out["RecoveryPointArn"] = value["recovery_point_arn"]
    if "scan_base_recovery_point_arn" in value:
        out["ScanBaseRecoveryPointArn"] = value["scan_base_recovery_point_arn"]
    import capo_backup.types.scan_mode

    out["ScanMode"] = capo_backup.types.scan_mode.serialize_json(value["scan_mode"])
    out["ScannerRoleArn"] = value["scanner_role_arn"]
    return out


def deserialize_json(data: dict) -> StartScanJobInput:
    out: StartScanJobInput = {}  # type: ignore[typeddict-item]
    if data.get("BackupVaultName") is not None:
        out["backup_vault_name"] = data["BackupVaultName"]
    else:
        out["backup_vault_name"] = ""
    if data.get("ContinuousScanEndTime") is not None:
        import capo_backup.types._prelude.timestamp

        out["continuous_scan_end_time"] = (
            capo_backup.types._prelude.timestamp.deserialize_json(
                data["ContinuousScanEndTime"]
            )
        )
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        out["iam_role_arn"] = ""
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    if data.get("MalwareScanner") is not None:
        import capo_backup.types.malware_scanner

        out["malware_scanner"] = capo_backup.types.malware_scanner.deserialize_json(
            data["MalwareScanner"]
        )
    else:
        import typing

        out["malware_scanner"] = typing.cast(
            "capo_backup.types.malware_scanner.MalwareScanner", ""
        )
    if data.get("RecoveryPointArn") is not None:
        out["recovery_point_arn"] = data["RecoveryPointArn"]
    else:
        out["recovery_point_arn"] = ""
    if data.get("ScanBaseRecoveryPointArn") is not None:
        out["scan_base_recovery_point_arn"] = data["ScanBaseRecoveryPointArn"]
    if data.get("ScanMode") is not None:
        import capo_backup.types.scan_mode

        out["scan_mode"] = capo_backup.types.scan_mode.deserialize_json(
            data["ScanMode"]
        )
    else:
        import typing

        out["scan_mode"] = typing.cast("capo_backup.types.scan_mode.ScanMode", "")
    if data.get("ScannerRoleArn") is not None:
        out["scanner_role_arn"] = data["ScannerRoleArn"]
    else:
        out["scanner_role_arn"] = ""
    return out
