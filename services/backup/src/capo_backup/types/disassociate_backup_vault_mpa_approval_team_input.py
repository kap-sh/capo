"""Generated from Smithy shape ``com.amazonaws.backup#DisassociateBackupVaultMpaApprovalTeamInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.backup_vault_name
    import capo_backup.types.requester_comment


class DisassociateBackupVaultMpaApprovalTeamInput(TypedDict, closed=True):
    backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of the backup vault from which to disassociate the MPA approval team.</p>"""
    requester_comment: NotRequired[
        "capo_backup.types.requester_comment.RequesterComment"
    ]
    """<p>An optional comment explaining the reason for disassociating the MPA approval team from the backup vault.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateBackupVaultMpaApprovalTeamInput) -> dict:
    out: dict = {}
    if "requester_comment" in value:
        out["RequesterComment"] = value["requester_comment"]
    return out


def deserialize_json(data: dict) -> DisassociateBackupVaultMpaApprovalTeamInput:
    out: DisassociateBackupVaultMpaApprovalTeamInput = {}  # type: ignore[typeddict-item]
    if data.get("RequesterComment") is not None:
        out["requester_comment"] = data["RequesterComment"]
    return out


def redact_sensitive(
    value: DisassociateBackupVaultMpaApprovalTeamInput,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "requester_comment" in value:
        out["requester_comment"] = "*** Sensitive Data Redacted ***"
    return out
