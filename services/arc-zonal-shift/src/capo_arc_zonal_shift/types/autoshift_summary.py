"""Generated from Smithy shape ``com.amazonaws.arczonalshift#AutoshiftSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.autoshift_execution_status
    import capo_arc_zonal_shift.types.availability_zone
    import capo_arc_zonal_shift.types.expiry_time
    import capo_arc_zonal_shift.types.start_time


class AutoshiftSummary(TypedDict, closed=True):
    away_from: "capo_arc_zonal_shift.types.availability_zone.AvailabilityZone"
    """<p>The Availability Zone (for example, <code>use1-az1</code>) that traffic is shifted away from for a resource when Amazon Web Services starts an autoshift. Until the autoshift ends, traffic for the resource is instead directed to other Availability Zones in the Amazon Web Services Region. An autoshift can end for a resource, for example, when Amazon Web Services ends the autoshift for the Availability Zone or when you disable zonal autoshift for the resource.</p>"""
    end_time: NotRequired["capo_arc_zonal_shift.types.expiry_time.ExpiryTime"]
    """<p>The time (in UTC) when the autoshift ended.</p>"""
    start_time: "capo_arc_zonal_shift.types.start_time.StartTime"
    """<p>The time (in UTC) when the autoshift started.</p>"""
    status: (
        "capo_arc_zonal_shift.types.autoshift_execution_status.AutoshiftExecutionStatus"
    )
    """<p>The status for an autoshift. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoshiftSummary) -> dict:
    out: dict = {}
    out["awayFrom"] = value["away_from"]
    if "end_time" in value:
        import capo_arc_zonal_shift.types.expiry_time

        out["endTime"] = capo_arc_zonal_shift.types.expiry_time.serialize_json(
            value["end_time"]
        )
    import capo_arc_zonal_shift.types.start_time

    out["startTime"] = capo_arc_zonal_shift.types.start_time.serialize_json(
        value["start_time"]
    )
    import capo_arc_zonal_shift.types.autoshift_execution_status

    out["status"] = (
        capo_arc_zonal_shift.types.autoshift_execution_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutoshiftSummary:
    out: AutoshiftSummary = {}  # type: ignore[typeddict-item]
    if data.get("awayFrom") is not None:
        out["away_from"] = data["awayFrom"]
    else:
        out["away_from"] = ""
    if data.get("endTime") is not None:
        import capo_arc_zonal_shift.types.expiry_time

        out["end_time"] = capo_arc_zonal_shift.types.expiry_time.deserialize_json(
            data["endTime"]
        )
    if data.get("startTime") is not None:
        import capo_arc_zonal_shift.types.start_time

        out["start_time"] = capo_arc_zonal_shift.types.start_time.deserialize_json(
            data["startTime"]
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("status") is not None:
        import capo_arc_zonal_shift.types.autoshift_execution_status

        out["status"] = (
            capo_arc_zonal_shift.types.autoshift_execution_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_arc_zonal_shift.types.autoshift_execution_status.AutoshiftExecutionStatus",
            "",
        )
    return out
