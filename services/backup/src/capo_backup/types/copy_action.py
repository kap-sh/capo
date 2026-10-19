"""Generated from Smithy shape ``com.amazonaws.backup#CopyAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.lifecycle


class CopyAction(TypedDict, closed=True):
    lifecycle: NotRequired["capo_backup.types.lifecycle.Lifecycle"]
    destination_backup_vault_arn: "capo_backup.types.arn.ARN"
    """<p>An Amazon Resource Name (ARN) that uniquely identifies the destination backup vault for the copied backup. For example, <code>arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CopyAction) -> dict:
    out: dict = {}
    if "lifecycle" in value:
        import capo_backup.types.lifecycle

        out["Lifecycle"] = capo_backup.types.lifecycle.serialize_json(
            value["lifecycle"]
        )
    out["DestinationBackupVaultArn"] = value["destination_backup_vault_arn"]
    return out


def deserialize_json(data: dict) -> CopyAction:
    out: CopyAction = {}  # type: ignore[typeddict-item]
    if data.get("Lifecycle") is not None:
        import capo_backup.types.lifecycle

        out["lifecycle"] = capo_backup.types.lifecycle.deserialize_json(
            data["Lifecycle"]
        )
    if data.get("DestinationBackupVaultArn") is not None:
        out["destination_backup_vault_arn"] = data["DestinationBackupVaultArn"]
    else:
        out["destination_backup_vault_arn"] = ""
    return out
