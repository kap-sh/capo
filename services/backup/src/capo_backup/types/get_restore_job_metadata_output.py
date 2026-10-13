"""Generated from Smithy shape ``com.amazonaws.backup#GetRestoreJobMetadataOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.metadata
    import capo_backup.types.restore_job_id


class GetRestoreJobMetadataOutput(TypedDict, closed=True):
    restore_job_id: NotRequired["capo_backup.types.restore_job_id.RestoreJobId"]
    """<p>This is a unique identifier of a restore job within Backup.</p>"""
    metadata: NotRequired["capo_backup.types.metadata.Metadata"]
    """<p>This contains the metadata of the specified backup job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRestoreJobMetadataOutput) -> dict:
    out: dict = {}
    if "restore_job_id" in value:
        out["RestoreJobId"] = value["restore_job_id"]
    if "metadata" in value:
        import capo_backup.types.metadata

        out["Metadata"] = capo_backup.types.metadata.serialize_json(value["metadata"])
    return out


def deserialize_json(data: dict) -> GetRestoreJobMetadataOutput:
    out: GetRestoreJobMetadataOutput = {}  # type: ignore[typeddict-item]
    if data.get("RestoreJobId") is not None:
        out["restore_job_id"] = data["RestoreJobId"]
    if data.get("Metadata") is not None:
        import capo_backup.types.metadata

        out["metadata"] = capo_backup.types.metadata.deserialize_json(data["Metadata"])
    return out


def redact_sensitive(value: GetRestoreJobMetadataOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "metadata" in value:
        out["metadata"] = "*** Sensitive Data Redacted ***"
    return out
