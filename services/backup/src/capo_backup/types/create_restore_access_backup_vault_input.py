"""Generated from Smithy shape ``com.amazonaws.backup#CreateRestoreAccessBackupVaultInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.backup_vault_name
    import capo_backup.types.requester_comment
    import capo_backup.types.string
    import capo_backup.types.tags


class CreateRestoreAccessBackupVaultInput(TypedDict, closed=True):
    source_backup_vault_arn: "capo_backup.types.arn.ARN"
    """<p>The ARN of the source backup vault containing the recovery points to which temporary access is requested.</p>"""
    backup_vault_name: NotRequired[
        "capo_backup.types.backup_vault_name.BackupVaultName"
    ]
    """<p>The name of the backup vault to associate with an MPA approval team.</p>"""
    backup_vault_tags: NotRequired["capo_backup.types.tags.Tags"]
    """<p>Optional tags to assign to the restore access backup vault.</p>"""
    creator_request_id: NotRequired["capo_backup.types.string.string"]
    """<p>A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.</p>"""
    requester_comment: NotRequired[
        "capo_backup.types.requester_comment.RequesterComment"
    ]
    """<p>A comment explaining the reason for requesting restore access to the backup vault.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRestoreAccessBackupVaultInput) -> dict:
    out: dict = {}
    out["SourceBackupVaultArn"] = value["source_backup_vault_arn"]
    if "backup_vault_name" in value:
        out["BackupVaultName"] = value["backup_vault_name"]
    if "backup_vault_tags" in value:
        import capo_backup.types.tags

        out["BackupVaultTags"] = capo_backup.types.tags.serialize_json(
            value["backup_vault_tags"]
        )
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "requester_comment" in value:
        out["RequesterComment"] = value["requester_comment"]
    return out


def deserialize_json(data: dict) -> CreateRestoreAccessBackupVaultInput:
    out: CreateRestoreAccessBackupVaultInput = {}  # type: ignore[typeddict-item]
    if data.get("SourceBackupVaultArn") is not None:
        out["source_backup_vault_arn"] = data["SourceBackupVaultArn"]
    else:
        out["source_backup_vault_arn"] = ""
    if data.get("BackupVaultName") is not None:
        out["backup_vault_name"] = data["BackupVaultName"]
    if data.get("BackupVaultTags") is not None:
        import capo_backup.types.tags

        out["backup_vault_tags"] = capo_backup.types.tags.deserialize_json(
            data["BackupVaultTags"]
        )
    if data.get("CreatorRequestId") is not None:
        out["creator_request_id"] = data["CreatorRequestId"]
    if data.get("RequesterComment") is not None:
        out["requester_comment"] = data["RequesterComment"]
    return out


def redact_sensitive(value: CreateRestoreAccessBackupVaultInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "backup_vault_tags" in value:
        out["backup_vault_tags"] = "*** Sensitive Data Redacted ***"
    if "requester_comment" in value:
        out["requester_comment"] = "*** Sensitive Data Redacted ***"
    return out
