"""Generated from Smithy shape ``com.amazonaws.backupsearch#EBSResultItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_backupsearch.types.file_path


class EBSResultItem(TypedDict, closed=True):
    backup_resource_arn: NotRequired["str"]
    """<p>These are one or more items in the results that match values for the Amazon Resource Name (ARN) of recovery points returned in a search of Amazon EBS backup metadata.</p>"""
    source_resource_arn: NotRequired["str"]
    """<p>These are one or more items in the results that match values for the Amazon Resource Name (ARN) of source resources returned in a search of Amazon EBS backup metadata.</p>"""
    backup_vault_name: NotRequired["str"]
    """<p>The name of the backup vault.</p>"""
    file_system_identifier: NotRequired["str"]
    """<p>These are one or more items in the results that match values for file systems returned in a search of Amazon EBS backup metadata.</p>"""
    file_path: NotRequired["capo_backupsearch.types.file_path.FilePath"]
    """<p>These are one or more items in the results that match values for file paths returned in a search of Amazon EBS backup metadata.</p>"""
    file_size: NotRequired["int"]
    """<p>These are one or more items in the results that match values for file sizes returned in a search of Amazon EBS backup metadata.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>These are one or more items in the results that match values for creation times returned in a search of Amazon EBS backup metadata.</p>"""
    last_modified_time: NotRequired["datetime.datetime"]
    """<p>These are one or more items in the results that match values for Last Modified Time returned in a search of Amazon EBS backup metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EBSResultItem) -> dict:
    out: dict = {}
    if "backup_resource_arn" in value:
        out["BackupResourceArn"] = value["backup_resource_arn"]
    if "source_resource_arn" in value:
        out["SourceResourceArn"] = value["source_resource_arn"]
    if "backup_vault_name" in value:
        out["BackupVaultName"] = value["backup_vault_name"]
    if "file_system_identifier" in value:
        out["FileSystemIdentifier"] = value["file_system_identifier"]
    if "file_path" in value:
        out["FilePath"] = value["file_path"]
    if "file_size" in value:
        out["FileSize"] = value["file_size"]
    if "creation_time" in value:
        import capo_backupsearch.types._prelude.timestamp

        out["CreationTime"] = capo_backupsearch.types._prelude.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_backupsearch.types._prelude.timestamp

        out["LastModifiedTime"] = (
            capo_backupsearch.types._prelude.timestamp.serialize_json(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> EBSResultItem:
    out: EBSResultItem = {}  # type: ignore[typeddict-item]
    if data.get("BackupResourceArn") is not None:
        out["backup_resource_arn"] = data["BackupResourceArn"]
    if data.get("SourceResourceArn") is not None:
        out["source_resource_arn"] = data["SourceResourceArn"]
    if data.get("BackupVaultName") is not None:
        out["backup_vault_name"] = data["BackupVaultName"]
    if data.get("FileSystemIdentifier") is not None:
        out["file_system_identifier"] = data["FileSystemIdentifier"]
    if data.get("FilePath") is not None:
        out["file_path"] = data["FilePath"]
    if data.get("FileSize") is not None:
        out["file_size"] = data["FileSize"]
    if data.get("CreationTime") is not None:
        import capo_backupsearch.types._prelude.timestamp

        out["creation_time"] = (
            capo_backupsearch.types._prelude.timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    if data.get("LastModifiedTime") is not None:
        import capo_backupsearch.types._prelude.timestamp

        out["last_modified_time"] = (
            capo_backupsearch.types._prelude.timestamp.deserialize_json(
                data["LastModifiedTime"]
            )
        )
    return out


def redact_sensitive(value: EBSResultItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "file_path" in value:
        out["file_path"] = "*** Sensitive Data Redacted ***"
    return out
