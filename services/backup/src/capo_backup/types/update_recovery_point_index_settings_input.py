"""Generated from Smithy shape ``com.amazonaws.backup#UpdateRecoveryPointIndexSettingsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.backup_vault_name
    import capo_backup.types.iam_role_arn
    import capo_backup.types.index


class UpdateRecoveryPointIndexSettingsInput(TypedDict, closed=True):
    backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created.</p> <p>Accepted characters include lowercase letters, numbers, and hyphens.</p>"""
    recovery_point_arn: "capo_backup.types.arn.ARN"
    """<p>An ARN that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>"""
    iam_role_arn: NotRequired["capo_backup.types.iam_role_arn.IAMRoleArn"]
    """<p>This specifies the IAM role ARN used for this operation.</p> <p>For example, arn:aws:iam::123456789012:role/S3Access</p>"""
    index: "capo_backup.types.index.Index"
    """<p>Index can have 1 of 2 possible values, either <code>ENABLED</code> or <code>DISABLED</code>.</p> <p>To create a backup index for an eligible <code>ACTIVE</code> recovery point that does not yet have a backup index, set value to <code>ENABLED</code>.</p> <p>To delete a backup index, set value to <code>DISABLED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecoveryPointIndexSettingsInput) -> dict:
    out: dict = {}
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    import capo_backup.types.index

    out["Index"] = capo_backup.types.index.serialize_json(value["index"])
    return out


def deserialize_json(data: dict) -> UpdateRecoveryPointIndexSettingsInput:
    out: UpdateRecoveryPointIndexSettingsInput = {}  # type: ignore[typeddict-item]
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    if data.get("Index") is not None:
        import capo_backup.types.index

        out["index"] = capo_backup.types.index.deserialize_json(data["Index"])
    else:
        import typing

        out["index"] = typing.cast("capo_backup.types.index.Index", "")
    return out
