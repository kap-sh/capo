"""Generated from Smithy shape ``com.amazonaws.efs#BackupPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_efs.types.status


class BackupPolicy(TypedDict, closed=True):
    status: "capo_efs.types.status.Status"
    """<p>Describes the status of the file system's backup policy.</p> <ul> <li> <p> <b> <code>ENABLED</code> </b> – EFS is automatically backing up the file system.</p> </li> <li> <p> <b> <code>ENABLING</code> </b> – EFS is turning on automatic backups for the file system.</p> </li> <li> <p> <b> <code>DISABLED</code> </b> – Automatic back ups are turned off for the file system.</p> </li> <li> <p> <b> <code>DISABLING</code> </b> – EFS is turning off automatic backups for the file system.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackupPolicy) -> dict:
    out: dict = {}
    import capo_efs.types.status

    out["Status"] = capo_efs.types.status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> BackupPolicy:
    out: BackupPolicy = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_efs.types.status

        out["status"] = capo_efs.types.status.deserialize_json(data["Status"])
    else:
        import typing

        out["status"] = typing.cast("capo_efs.types.status.Status", "")
    return out
