"""Generated from Smithy shape ``com.amazonaws.backup#CreateBackupAccessPointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup.types.access_point_arn
    import capo_backup.types.access_point_status


class CreateBackupAccessPointResponse(TypedDict, closed=True):
    access_point_arn: "capo_backup.types.access_point_arn.AccessPointArn"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the created backup access point.</p>"""
    status: "capo_backup.types.access_point_status.AccessPointStatus"
    """<p>The current status of the backup access point. A newly created backup access point begins in the <code>CREATING</code> state and becomes usable when it reaches <code>AVAILABLE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBackupAccessPointResponse) -> dict:
    out: dict = {}
    out["AccessPointArn"] = value["access_point_arn"]
    import capo_backup.types.access_point_status

    out["Status"] = capo_backup.types.access_point_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> CreateBackupAccessPointResponse:
    out: CreateBackupAccessPointResponse = {}  # type: ignore[typeddict-item]
    if data.get("AccessPointArn") is not None:
        out["access_point_arn"] = data["AccessPointArn"]
    else:
        out["access_point_arn"] = ""
    if data.get("Status") is not None:
        import capo_backup.types.access_point_status

        out["status"] = capo_backup.types.access_point_status.deserialize_json(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_backup.types.access_point_status.AccessPointStatus", ""
        )
    return out
