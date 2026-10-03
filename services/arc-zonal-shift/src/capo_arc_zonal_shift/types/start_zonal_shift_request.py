"""Generated from Smithy shape ``com.amazonaws.arczonalshift#StartZonalShiftRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_arc_zonal_shift.errors import DeserializationError

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.availability_zone
    import capo_arc_zonal_shift.types.expires_in
    import capo_arc_zonal_shift.types.resource_identifier
    import capo_arc_zonal_shift.types.zonal_shift_comment


class StartZonalShiftRequest(TypedDict, closed=True):
    resource_identifier: (
        "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier"
    )
    """<p>The identifier for the resource that Amazon Web Services shifts traffic for. The identifier is the Amazon Resource Name (ARN) for the resource.</p> <p>Amazon Application Recovery Controller currently supports enabling the following resources for zonal shift and zonal autoshift:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ec2-auto-scaling-groups.html">Amazon EC2 Auto Scaling groups</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.eks.html">Amazon Elastic Kubernetes Service</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.app-load-balancers.html">Application Load Balancer</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html">Network Load Balancer</a> </p> </li> </ul>"""
    away_from: "capo_arc_zonal_shift.types.availability_zone.AvailabilityZone"
    """<p>The Availability Zone (for example, <code>use1-az1</code>) that traffic is moved away from for a resource when you start a zonal shift. Until the zonal shift expires or you cancel it, traffic for the resource is instead moved to other Availability Zones in the Amazon Web Services Region.</p>"""
    expires_in: "capo_arc_zonal_shift.types.expires_in.ExpiresIn"
    """<p>The length of time that you want a zonal shift to be active, which ARC converts to an expiry time (expiration time). Zonal shifts are temporary. You can set a zonal shift to be active initially for up to three days (72 hours).</p> <p>If you want to still keep traffic away from an Availability Zone, you can update the zonal shift and set a new expiration. You can also cancel a zonal shift, before it expires, for example, if you're ready to restore traffic to the Availability Zone.</p> <p>To set a length of time for a zonal shift to be active, specify a whole number, and then one of the following, with no space:</p> <ul> <li> <p> <b>A lowercase letter m:</b> To specify that the value is in minutes.</p> </li> <li> <p> <b>A lowercase letter h:</b> To specify that the value is in hours.</p> </li> </ul> <p>For example: <code>20h</code> means the zonal shift expires in 20 hours. <code>120m</code> means the zonal shift expires in 120 minutes (2 hours).</p>"""
    comment: "capo_arc_zonal_shift.types.zonal_shift_comment.ZonalShiftComment"
    """<p>A comment that you enter about the zonal shift. Only the latest comment is retained; no comment history is maintained. A new comment overwrites any existing comment string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartZonalShiftRequest) -> dict:
    out: dict = {}
    out["resourceIdentifier"] = value["resource_identifier"]
    out["awayFrom"] = value["away_from"]
    out["expiresIn"] = value["expires_in"]
    out["comment"] = value["comment"]
    return out


def deserialize_json(data: dict) -> StartZonalShiftRequest:
    out: StartZonalShiftRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceIdentifier") is not None:
        out["resource_identifier"] = data["resourceIdentifier"]
    else:
        raise DeserializationError(
            "StartZonalShiftRequest.resource_identifier required"
        )
    if data.get("awayFrom") is not None:
        out["away_from"] = data["awayFrom"]
    else:
        raise DeserializationError("StartZonalShiftRequest.away_from required")
    if data.get("expiresIn") is not None:
        out["expires_in"] = data["expiresIn"]
    else:
        raise DeserializationError("StartZonalShiftRequest.expires_in required")
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    else:
        raise DeserializationError("StartZonalShiftRequest.comment required")
    return out
