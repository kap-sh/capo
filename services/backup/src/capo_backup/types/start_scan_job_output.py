"""Generated from Smithy shape ``com.amazonaws.backup#StartScanJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class StartScanJobOutput(TypedDict, closed=True):
    creation_date: "datetime.datetime"
    """<p>The date and time that a backup job is created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    scan_job_id: "str"
    """<p>Uniquely identifies a request to Backup to back up a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartScanJobOutput) -> dict:
    out: dict = {}
    import capo_backup.types._prelude.timestamp

    out["CreationDate"] = capo_backup.types._prelude.timestamp.serialize_json(
        value["creation_date"]
    )
    out["ScanJobId"] = value["scan_job_id"]
    return out


def deserialize_json(data: dict) -> StartScanJobOutput:
    out: StartScanJobOutput = {}  # type: ignore[typeddict-item]
    if data.get("CreationDate") is not None:
        import capo_backup.types._prelude.timestamp

        out["creation_date"] = capo_backup.types._prelude.timestamp.deserialize_json(
            data["CreationDate"]
        )
    else:
        import datetime

        out["creation_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("ScanJobId") is not None:
        out["scan_job_id"] = data["ScanJobId"]
    else:
        out["scan_job_id"] = ""
    return out
