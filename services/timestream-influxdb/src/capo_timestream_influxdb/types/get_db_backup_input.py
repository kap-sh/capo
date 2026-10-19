"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#GetDbBackupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_backup_id


class GetDbBackupInput(TypedDict, closed=True):
    identifier: "capo_timestream_influxdb.types.db_backup_id.DbBackupId"
    """<p>The identifier of the backup to retrieve information for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDbBackupInput) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDbBackupInput:
    out: GetDbBackupInput = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    return out
