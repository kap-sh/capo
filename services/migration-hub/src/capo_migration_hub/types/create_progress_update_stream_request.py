"""Generated from Smithy shape ``com.amazonaws.migrationhub#CreateProgressUpdateStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_migration_hub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_migration_hub.types.dry_run
    import capo_migration_hub.types.progress_update_stream


class CreateProgressUpdateStreamRequest(TypedDict, closed=True):
    progress_update_stream_name: (
        "capo_migration_hub.types.progress_update_stream.ProgressUpdateStream"
    )
    """<p>The name of the ProgressUpdateStream. <i>Do not store personal data in this field.</i> </p>"""
    dry_run: NotRequired["capo_migration_hub.types.dry_run.DryRun"]
    """<p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProgressUpdateStreamRequest) -> dict:
    out: dict = {}
    out["ProgressUpdateStreamName"] = value["progress_update_stream_name"]
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProgressUpdateStreamRequest:
    out: CreateProgressUpdateStreamRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProgressUpdateStreamName") is not None:
        out["progress_update_stream_name"] = data["ProgressUpdateStreamName"]
    else:
        raise DeserializationError(
            "CreateProgressUpdateStreamRequest.progress_update_stream_name required"
        )
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    return out
