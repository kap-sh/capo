"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyCapacityReservationFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.capacity_reservation_fleet_id
    import capo_ec2.types.integer
    import capo_ec2.types.millisecond_date_time


class ModifyCapacityReservationFleetRequest(TypedDict, closed=True):
    capacity_reservation_fleet_id: NotRequired[
        "capo_ec2.types.capacity_reservation_fleet_id.CapacityReservationFleetId"
    ]
    """<p>The ID of the Capacity Reservation Fleet to modify.</p>"""
    total_target_capacity: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The total number of capacity units to be reserved by the Capacity Reservation Fleet. This value, together with the instance type weights that you assign to each instance type used by the Fleet determine the number of instances for which the Fleet reserves capacity. Both values are based on units that make sense for your workload. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#target-capacity">Total target capacity</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    end_date: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The date and time at which the Capacity Reservation Fleet expires. When the Capacity Reservation Fleet expires, its state changes to <code>expired</code> and all of the Capacity Reservations in the Fleet expire.</p> <p>The Capacity Reservation Fleet expires within an hour after the specified time. For example, if you specify <code>5/31/2019</code>, <code>13:30:55</code>, the Capacity Reservation Fleet is guaranteed to expire between <code>13:30:55</code> and <code>14:30:55</code> on <code>5/31/2019</code>.</p> <p>You can't specify <b>EndDate</b> and <b> RemoveEndDate</b> in the same request.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    remove_end_date: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to remove the end date from the Capacity Reservation Fleet. If you remove the end date, the Capacity Reservation Fleet does not expire and it remains active until you explicitly cancel it using the <b>CancelCapacityReservationFleet</b> action.</p> <p>You can't specify <b>RemoveEndDate</b> and <b> EndDate</b> in the same request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyCapacityReservationFleetRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_reservation_fleet_id" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityReservationFleetId",
                str(value["capacity_reservation_fleet_id"]),
            )
        )
    if "total_target_capacity" in value:
        pairs.append(
            (f"{key_prefix}TotalTargetCapacity", str(value["total_target_capacity"]))
        )
    if "end_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["end_date"], pairs, f"{key_prefix}EndDate"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "remove_end_date" in value:
        pairs.append(
            (
                f"{key_prefix}RemoveEndDate",
                "true" if value["remove_end_date"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> ModifyCapacityReservationFleetRequest:
    out: ModifyCapacityReservationFleetRequest = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_fleet_id = el.find("CapacityReservationFleetId")
    if child_capacity_reservation_fleet_id is not None:
        out["capacity_reservation_fleet_id"] = str(
            child_capacity_reservation_fleet_id.text or ""
        )
    child_total_target_capacity = el.find("TotalTargetCapacity")
    if child_total_target_capacity is not None:
        out["total_target_capacity"] = int(child_total_target_capacity.text or "")
    child_end_date = el.find("EndDate")
    if child_end_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["end_date"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_end_date
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_remove_end_date = el.find("RemoveEndDate")
    if child_remove_end_date is not None:
        out["remove_end_date"] = (child_remove_end_date.text or "").lower() == "true"
    return out
