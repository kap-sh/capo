"""Generated from Smithy shape ``com.amazonaws.arczonalshift#StartPracticeRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_arc_zonal_shift.errors import DeserializationError

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.availability_zone
    import capo_arc_zonal_shift.types.resource_identifier
    import capo_arc_zonal_shift.types.zonal_shift_comment


class StartPracticeRunRequest(TypedDict, closed=True):
    resource_identifier: (
        "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier"
    )
    """<p>The identifier for the resource that you want to start a practice run zonal shift for. The identifier is the Amazon Resource Name (ARN) for the resource.</p>"""
    away_from: "capo_arc_zonal_shift.types.availability_zone.AvailabilityZone"
    """<p>The Availability Zone (for example, <code>use1-az1</code>) that traffic is shifted away from for the resource that you specify for the practice run.</p>"""
    comment: "capo_arc_zonal_shift.types.zonal_shift_comment.ZonalShiftComment"
    """<p>The initial comment that you enter about the practice run. Be aware that this comment can be overwritten by Amazon Web Services if the automatic check for balanced capacity fails. For more information, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.capacity-check.html"> Capacity checks for practice runs</a> in the Amazon Application Recovery Controller Developer Guide. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartPracticeRunRequest) -> dict:
    out: dict = {}
    out["resourceIdentifier"] = value["resource_identifier"]
    out["awayFrom"] = value["away_from"]
    out["comment"] = value["comment"]
    return out


def deserialize_json(data: dict) -> StartPracticeRunRequest:
    out: StartPracticeRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceIdentifier") is not None:
        out["resource_identifier"] = data["resourceIdentifier"]
    else:
        raise DeserializationError(
            "StartPracticeRunRequest.resource_identifier required"
        )
    if data.get("awayFrom") is not None:
        out["away_from"] = data["awayFrom"]
    else:
        raise DeserializationError("StartPracticeRunRequest.away_from required")
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    else:
        raise DeserializationError("StartPracticeRunRequest.comment required")
    return out
