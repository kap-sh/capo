"""Generated from Smithy shape ``com.amazonaws.backupsearch#S3ResultItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_backupsearch.types.object_key


class S3ResultItem(TypedDict, closed=True):
    backup_resource_arn: NotRequired["str"]
    """<p>These are items in the returned results that match recovery point Amazon Resource Names (ARN) input during a search of Amazon S3 backup metadata.</p>"""
    source_resource_arn: NotRequired["str"]
    """<p>These are items in the returned results that match source Amazon Resource Names (ARN) input during a search of Amazon S3 backup metadata.</p>"""
    backup_vault_name: NotRequired["str"]
    """<p>The name of the backup vault.</p>"""
    object_key: NotRequired["capo_backupsearch.types.object_key.ObjectKey"]
    """<p>This is one or more items returned in the results of a search of Amazon S3 backup metadata that match the values input for object key.</p>"""
    object_size: NotRequired["int"]
    """<p>These are items in the returned results that match values for object size(s) input during a search of Amazon S3 backup metadata.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>These are one or more items in the returned results that match values for item creation time input during a search of Amazon S3 backup metadata.</p>"""
    e_tag: NotRequired["str"]
    """<p>These are one or more items in the returned results that match values for ETags input during a search of Amazon S3 backup metadata.</p>"""
    version_id: NotRequired["str"]
    """<p>These are one or more items in the returned results that match values for version IDs input during a search of Amazon S3 backup metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ResultItem) -> dict:
    out: dict = {}
    if "backup_resource_arn" in value:
        out["BackupResourceArn"] = value["backup_resource_arn"]
    if "source_resource_arn" in value:
        out["SourceResourceArn"] = value["source_resource_arn"]
    if "backup_vault_name" in value:
        out["BackupVaultName"] = value["backup_vault_name"]
    if "object_key" in value:
        out["ObjectKey"] = value["object_key"]
    if "object_size" in value:
        out["ObjectSize"] = value["object_size"]
    if "creation_time" in value:
        import capo_backupsearch.types._prelude.timestamp

        out["CreationTime"] = capo_backupsearch.types._prelude.timestamp.serialize_json(
            value["creation_time"]
        )
    if "e_tag" in value:
        out["ETag"] = value["e_tag"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> S3ResultItem:
    out: S3ResultItem = {}  # type: ignore[typeddict-item]
    if data.get("BackupResourceArn") is not None:
        out["backup_resource_arn"] = data["BackupResourceArn"]
    if data.get("SourceResourceArn") is not None:
        out["source_resource_arn"] = data["SourceResourceArn"]
    if data.get("BackupVaultName") is not None:
        out["backup_vault_name"] = data["BackupVaultName"]
    if data.get("ObjectKey") is not None:
        out["object_key"] = data["ObjectKey"]
    if data.get("ObjectSize") is not None:
        out["object_size"] = data["ObjectSize"]
    if data.get("CreationTime") is not None:
        import capo_backupsearch.types._prelude.timestamp

        out["creation_time"] = (
            capo_backupsearch.types._prelude.timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    if data.get("ETag") is not None:
        out["e_tag"] = data["ETag"]
    if data.get("VersionId") is not None:
        out["version_id"] = data["VersionId"]
    return out


def redact_sensitive(value: S3ResultItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "object_key" in value:
        out["object_key"] = "*** Sensitive Data Redacted ***"
    return out
