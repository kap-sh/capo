"""Generated from Smithy shape ``com.amazonaws.arczonalshift#StartPracticeRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_arc_zonal_shift.errors import DeserializationError

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.availability_zone
    import capo_arc_zonal_shift.types.expiry_time
    import capo_arc_zonal_shift.types.resource_identifier
    import capo_arc_zonal_shift.types.start_time
    import capo_arc_zonal_shift.types.zonal_shift_comment
    import capo_arc_zonal_shift.types.zonal_shift_id
    import capo_arc_zonal_shift.types.zonal_shift_status


class StartPracticeRunResponse(TypedDict, closed=True):
    zonal_shift_id: "capo_arc_zonal_shift.types.zonal_shift_id.ZonalShiftId"
    """<p>The identifier of a practice run zonal shift.</p>"""
    resource_identifier: (
        "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier"
    )
    """<p>The identifier for the resource that you want to shift traffic for. The identifier is the Amazon Resource Name (ARN) for the resource.</p>"""
    away_from: "capo_arc_zonal_shift.types.availability_zone.AvailabilityZone"
    """<p>The Availability Zone (for example, <code>use1-az1</code>) that traffic is shifted away from for the resource that you specify for the practice run.</p>"""
    expiry_time: "capo_arc_zonal_shift.types.expiry_time.ExpiryTime"
    """<p>The expiry time (expiration time) for an on-demand practice run zonal shift is 30 minutes from the time when you start the practice run, unless you cancel it before that time. However, be aware that the <code>expiryTime</code> field for practice run zonal shifts always has a value of 1 minute. </p>"""
    start_time: "capo_arc_zonal_shift.types.start_time.StartTime"
    """<p>The time (UTC) when the zonal shift starts.</p>"""
    status: "capo_arc_zonal_shift.types.zonal_shift_status.ZonalShiftStatus"
    """<p>A status for the practice run (expected status is <b>ACTIVE</b>).</p>"""
    comment: "capo_arc_zonal_shift.types.zonal_shift_comment.ZonalShiftComment"
    """<p>The initial comment that you enter about the practice run. Be aware that this comment can be overwritten by Amazon Web Services if the automatic check for balanced capacity fails. For more information, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.capacity-check.html"> Capacity checks for practice runs</a> in the Amazon Application Recovery Controller Developer Guide. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartPracticeRunResponse) -> dict:
    out: dict = {}
    out["zonalShiftId"] = value["zonal_shift_id"]
    out["resourceIdentifier"] = value["resource_identifier"]
    out["awayFrom"] = value["away_from"]
    import capo_arc_zonal_shift.types.expiry_time

    out["expiryTime"] = capo_arc_zonal_shift.types.expiry_time.serialize_json(
        value["expiry_time"]
    )
    import capo_arc_zonal_shift.types.start_time

    out["startTime"] = capo_arc_zonal_shift.types.start_time.serialize_json(
        value["start_time"]
    )
    import capo_arc_zonal_shift.types.zonal_shift_status

    out["status"] = capo_arc_zonal_shift.types.zonal_shift_status.serialize_json(
        value["status"]
    )
    out["comment"] = value["comment"]
    return out


def deserialize_json(data: dict) -> StartPracticeRunResponse:
    out: StartPracticeRunResponse = {}  # type: ignore[typeddict-item]
    if data.get("zonalShiftId") is not None:
        out["zonal_shift_id"] = data["zonalShiftId"]
    else:
        raise DeserializationError("StartPracticeRunResponse.zonal_shift_id required")
    if data.get("resourceIdentifier") is not None:
        out["resource_identifier"] = data["resourceIdentifier"]
    else:
        raise DeserializationError(
            "StartPracticeRunResponse.resource_identifier required"
        )
    if data.get("awayFrom") is not None:
        out["away_from"] = data["awayFrom"]
    else:
        raise DeserializationError("StartPracticeRunResponse.away_from required")
    if data.get("expiryTime") is not None:
        import capo_arc_zonal_shift.types.expiry_time

        out["expiry_time"] = capo_arc_zonal_shift.types.expiry_time.deserialize_json(
            data["expiryTime"]
        )
    else:
        raise DeserializationError("StartPracticeRunResponse.expiry_time required")
    if data.get("startTime") is not None:
        import capo_arc_zonal_shift.types.start_time

        out["start_time"] = capo_arc_zonal_shift.types.start_time.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("StartPracticeRunResponse.start_time required")
    if data.get("status") is not None:
        import capo_arc_zonal_shift.types.zonal_shift_status

        out["status"] = capo_arc_zonal_shift.types.zonal_shift_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("StartPracticeRunResponse.status required")
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    else:
        raise DeserializationError("StartPracticeRunResponse.comment required")
    return out
