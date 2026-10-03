"""Generated from Smithy shape ``com.amazonaws.arczonalshift#AutoshiftInResource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_arc_zonal_shift.errors import DeserializationError

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.autoshift_applied_status
    import capo_arc_zonal_shift.types.availability_zone
    import capo_arc_zonal_shift.types.start_time


class AutoshiftInResource(TypedDict, closed=True):
    applied_status: (
        "capo_arc_zonal_shift.types.autoshift_applied_status.AutoshiftAppliedStatus"
    )
    """<p>The <code>appliedStatus</code> field specifies which application traffic shift is in effect for a resource when there is more than one active traffic shift. There can be more than one application traffic shift in progress at the same time - that is, practice run zonal shifts, customer-initiated zonal shifts, or an autoshift. The <code>appliedStatus</code> field for a shift that is in progress for a resource can have one of two values: <code>APPLIED</code> or <code>NOT_APPLIED</code>. The zonal shift or autoshift that is currently in effect for the resource has an <code>appliedStatus</code> set to <code>APPLIED</code>.</p> <p>The overall principle for precedence is that zonal shifts that you start as a customer take precedence autoshifts, which take precedence over practice runs. That is, customer-initiated zonal shifts &gt; autoshifts &gt; practice run zonal shifts.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.html">How zonal autoshift and practice runs work</a> in the Amazon Application Recovery Controller Developer Guide.</p>"""
    away_from: "capo_arc_zonal_shift.types.availability_zone.AvailabilityZone"
    """<p>The Availability Zone (for example, <code>use1-az1</code>) that traffic is shifted away from for a resource, when Amazon Web Services starts an autoshift. Until the autoshift ends, traffic for the resource is instead directed to other Availability Zones in the Amazon Web Services Region. An autoshift can end for a resource, for example, when Amazon Web Services ends the autoshift for the Availability Zone or when you disable zonal autoshift for the resource.</p>"""
    start_time: "capo_arc_zonal_shift.types.start_time.StartTime"
    """<p>The time (UTC) when the autoshift started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoshiftInResource) -> dict:
    out: dict = {}
    import capo_arc_zonal_shift.types.autoshift_applied_status

    out["appliedStatus"] = (
        capo_arc_zonal_shift.types.autoshift_applied_status.serialize_json(
            value["applied_status"]
        )
    )
    out["awayFrom"] = value["away_from"]
    import capo_arc_zonal_shift.types.start_time

    out["startTime"] = capo_arc_zonal_shift.types.start_time.serialize_json(
        value["start_time"]
    )
    return out


def deserialize_json(data: dict) -> AutoshiftInResource:
    out: AutoshiftInResource = {}  # type: ignore[typeddict-item]
    if data.get("appliedStatus") is not None:
        import capo_arc_zonal_shift.types.autoshift_applied_status

        out["applied_status"] = (
            capo_arc_zonal_shift.types.autoshift_applied_status.deserialize_json(
                data["appliedStatus"]
            )
        )
    else:
        raise DeserializationError("AutoshiftInResource.applied_status required")
    if data.get("awayFrom") is not None:
        out["away_from"] = data["awayFrom"]
    else:
        raise DeserializationError("AutoshiftInResource.away_from required")
    if data.get("startTime") is not None:
        import capo_arc_zonal_shift.types.start_time

        out["start_time"] = capo_arc_zonal_shift.types.start_time.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("AutoshiftInResource.start_time required")
    return out
