"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ZonalShiftSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_arc_zonal_shift.errors import DeserializationError

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.availability_zone
    import capo_arc_zonal_shift.types.expiry_time
    import capo_arc_zonal_shift.types.practice_run_outcome
    import capo_arc_zonal_shift.types.resource_identifier
    import capo_arc_zonal_shift.types.shift_type
    import capo_arc_zonal_shift.types.start_time
    import capo_arc_zonal_shift.types.zonal_shift_comment
    import capo_arc_zonal_shift.types.zonal_shift_id
    import capo_arc_zonal_shift.types.zonal_shift_status


class ZonalShiftSummary(TypedDict, closed=True):
    zonal_shift_id: "capo_arc_zonal_shift.types.zonal_shift_id.ZonalShiftId"
    """<p>The identifier of a zonal shift.</p>"""
    resource_identifier: (
        "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier"
    )
    """<p>The identifier for the resource to include in a zonal shift. The identifier is the Amazon Resource Name (ARN) for the resource.</p> <p>Amazon Application Recovery Controller currently supports enabling the following resources for zonal shift and zonal autoshift:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ec2-auto-scaling-groups.html">Amazon EC2 Auto Scaling groups</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.eks.html">Amazon Elastic Kubernetes Service</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.app-load-balancers.html">Application Load Balancers</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html">Network Load Balancers</a> </p> </li> </ul>"""
    away_from: "capo_arc_zonal_shift.types.availability_zone.AvailabilityZone"
    """<p>The Availability Zone (for example, <code>use1-az1</code>) that traffic is moved away from for a resource when you start a zonal shift. Until the zonal shift expires or you cancel it, traffic for the resource is instead moved to other Availability Zones in the Amazon Web Services Region.</p>"""
    expiry_time: "capo_arc_zonal_shift.types.expiry_time.ExpiryTime"
    """<p>The expiry time (expiration time) for a customer-initiated zonal shift. A zonal shift is temporary and must be set to expire when you start the zonal shift. You can initially set a zonal shift to expire in a maximum of three days (72 hours). However, you can update a zonal shift to set a new expiration at any time. </p> <p>When you start a zonal shift, you specify how long you want it to be active, which ARC converts to an expiry time (expiration time). You can cancel a zonal shift when you're ready to restore traffic to the Availability Zone, or just wait for it to expire. Or you can update the zonal shift to specify another length of time to expire in.</p>"""
    start_time: "capo_arc_zonal_shift.types.start_time.StartTime"
    """<p>The time (UTC) when the zonal shift starts.</p>"""
    status: "capo_arc_zonal_shift.types.zonal_shift_status.ZonalShiftStatus"
    """<p>A status for a zonal shift.</p> <p>The <code>Status</code> for a zonal shift can have one of the following values:</p> <ul> <li> <p> <b>ACTIVE:</b> The zonal shift has been started and is active.</p> </li> <li> <p> <b>EXPIRED:</b> The zonal shift has expired (the expiry time was exceeded).</p> </li> <li> <p> <b>CANCELED:</b> The zonal shift was canceled.</p> </li> </ul>"""
    comment: "capo_arc_zonal_shift.types.zonal_shift_comment.ZonalShiftComment"
    """<p>A comment that you enter about the zonal shift. Only the latest comment is retained; no comment history is maintained. That is, a new comment overwrites any existing comment string.</p>"""
    shift_type: NotRequired["capo_arc_zonal_shift.types.shift_type.ShiftType"]
    """<p>Defines the zonal shift type.</p>"""
    practice_run_outcome: NotRequired[
        "capo_arc_zonal_shift.types.practice_run_outcome.PracticeRunOutcome"
    ]
    """<p>The outcome, or end state, of a practice run. The following values can be returned:</p> <ul> <li> <p> <b>PENDING:</b> Outcome value when the practice run is in progress.</p> </li> <li> <p> <b>SUCCEEDED:</b> Outcome value when the outcome alarm specified for the practice run configuration does not go into an <code>ALARM</code> state during the practice run, and the practice run was not interrupted before it completed.</p> </li> <li> <p> <b>INTERRUPTED:</b> Outcome value when the practice run did not run for the expected 30 minutes or there was another problem with the practice run that created an inconclusive outcome.</p> </li> <li> <p> <b>FAILED:</b> Outcome value when the outcome alarm specified for the practice run configuration goes into an <code>ALARM</code> state during the practice run, and the practice run was not interrupted before it completed.</p> </li> <li> <p> <b>CAPACITY_CHECK_FAILED:</b> The check for balanced capacity across Availability Zones for your load balancing and Auto Scaling group resources failed.</p> </li> </ul> <p>For more information about practice run outcomes, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.configure.html"> Considerations when you configure zonal autoshift</a> in the Amazon Application Recovery Controller Developer Guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ZonalShiftSummary) -> dict:
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
    if "shift_type" in value:
        import capo_arc_zonal_shift.types.shift_type

        out["shiftType"] = capo_arc_zonal_shift.types.shift_type.serialize_json(
            value["shift_type"]
        )
    if "practice_run_outcome" in value:
        import capo_arc_zonal_shift.types.practice_run_outcome

        out["practiceRunOutcome"] = (
            capo_arc_zonal_shift.types.practice_run_outcome.serialize_json(
                value["practice_run_outcome"]
            )
        )
    return out


def deserialize_json(data: dict) -> ZonalShiftSummary:
    out: ZonalShiftSummary = {}  # type: ignore[typeddict-item]
    if data.get("zonalShiftId") is not None:
        out["zonal_shift_id"] = data["zonalShiftId"]
    else:
        raise DeserializationError("ZonalShiftSummary.zonal_shift_id required")
    if data.get("resourceIdentifier") is not None:
        out["resource_identifier"] = data["resourceIdentifier"]
    else:
        raise DeserializationError("ZonalShiftSummary.resource_identifier required")
    if data.get("awayFrom") is not None:
        out["away_from"] = data["awayFrom"]
    else:
        raise DeserializationError("ZonalShiftSummary.away_from required")
    if data.get("expiryTime") is not None:
        import capo_arc_zonal_shift.types.expiry_time

        out["expiry_time"] = capo_arc_zonal_shift.types.expiry_time.deserialize_json(
            data["expiryTime"]
        )
    else:
        raise DeserializationError("ZonalShiftSummary.expiry_time required")
    if data.get("startTime") is not None:
        import capo_arc_zonal_shift.types.start_time

        out["start_time"] = capo_arc_zonal_shift.types.start_time.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("ZonalShiftSummary.start_time required")
    if data.get("status") is not None:
        import capo_arc_zonal_shift.types.zonal_shift_status

        out["status"] = capo_arc_zonal_shift.types.zonal_shift_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("ZonalShiftSummary.status required")
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    else:
        raise DeserializationError("ZonalShiftSummary.comment required")
    if data.get("shiftType") is not None:
        import capo_arc_zonal_shift.types.shift_type

        out["shift_type"] = capo_arc_zonal_shift.types.shift_type.deserialize_json(
            data["shiftType"]
        )
    if data.get("practiceRunOutcome") is not None:
        import capo_arc_zonal_shift.types.practice_run_outcome

        out["practice_run_outcome"] = (
            capo_arc_zonal_shift.types.practice_run_outcome.deserialize_json(
                data["practiceRunOutcome"]
            )
        )
    return out
