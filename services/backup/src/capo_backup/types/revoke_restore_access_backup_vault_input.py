"""Generated from Smithy shape ``com.amazonaws.backup#RevokeRestoreAccessBackupVaultInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.backup_vault_name
    import capo_backup.types.requester_comment


class RevokeRestoreAccessBackupVaultInput(TypedDict, closed=True):
    backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of the source backup vault associated with the restore access backup vault to be revoked.</p>"""
    restore_access_backup_vault_arn: "capo_backup.types.arn.ARN"
    """<p>The ARN of the restore access backup vault to revoke.</p>"""
    requester_comment: NotRequired[
        "capo_backup.types.requester_comment.RequesterComment"
    ]
    """<p>A comment explaining the reason for revoking access to the restore access backup vault.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevokeRestoreAccessBackupVaultInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RevokeRestoreAccessBackupVaultInput:
    out: RevokeRestoreAccessBackupVaultInput = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: RevokeRestoreAccessBackupVaultInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "requester_comment" in value:
        out["requester_comment"] = "*** Sensitive Data Redacted ***"
    return out
