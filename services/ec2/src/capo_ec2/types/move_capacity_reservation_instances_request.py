"""Generated from Smithy shape ``com.amazonaws.ec2#MoveCapacityReservationInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.capacity_reservation_id
    import capo_ec2.types.integer
    import capo_ec2.types.string


class MoveCapacityReservationInstancesRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensure Idempotency</a>.</p>"""
    source_capacity_reservation_id: NotRequired[
        "capo_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p> The ID of the Capacity Reservation from which you want to move capacity. </p>"""
    destination_capacity_reservation_id: NotRequired[
        "capo_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p> The ID of the Capacity Reservation that you want to move capacity into. </p>"""
    instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of instances that you want to move from the source Capacity Reservation. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MoveCapacityReservationInstancesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "source_capacity_reservation_id" in value:
        pairs.append(
            (
                f"{key_prefix}SourceCapacityReservationId",
                str(value["source_capacity_reservation_id"]),
            )
        )
    if "destination_capacity_reservation_id" in value:
        pairs.append(
            (
                f"{key_prefix}DestinationCapacityReservationId",
                str(value["destination_capacity_reservation_id"]),
            )
        )
    if "instance_count" in value:
        pairs.append((f"{key_prefix}InstanceCount", str(value["instance_count"])))


def deserialize_ec2_query(el: Element) -> MoveCapacityReservationInstancesRequest:
    out: MoveCapacityReservationInstancesRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_source_capacity_reservation_id = el.find("SourceCapacityReservationId")
    if child_source_capacity_reservation_id is not None:
        out["source_capacity_reservation_id"] = str(
            child_source_capacity_reservation_id.text or ""
        )
    child_destination_capacity_reservation_id = el.find(
        "DestinationCapacityReservationId"
    )
    if child_destination_capacity_reservation_id is not None:
        out["destination_capacity_reservation_id"] = str(
            child_destination_capacity_reservation_id.text or ""
        )
    child_instance_count = el.find("InstanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    return out
