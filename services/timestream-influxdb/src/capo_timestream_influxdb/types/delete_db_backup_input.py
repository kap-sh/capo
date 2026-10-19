"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DeleteDbBackupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_backup_id


class DeleteDbBackupInput(TypedDict, closed=True):
    identifier: "capo_timestream_influxdb.types.db_backup_id.DbBackupId"
    """<p>The identifier of the backup to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteDbBackupInput) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteDbBackupInput:
    out: DeleteDbBackupInput = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    return out
