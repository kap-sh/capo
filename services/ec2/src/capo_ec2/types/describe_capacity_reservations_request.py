"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityReservationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.capacity_reservation_id_set
    import capo_ec2.types.describe_capacity_reservations_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.string


class DescribeCapacityReservationsRequest(TypedDict, closed=True):
    capacity_reservation_ids: NotRequired[
        "capo_ec2.types.capacity_reservation_id_set.CapacityReservationIdSet"
    ]
    """<p>The ID of the Capacity Reservation.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_capacity_reservations_max_results.DescribeCapacityReservationsMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>instance-type</code> - The type of instance for which the Capacity Reservation reserves capacity.</p> </li> <li> <p> <code>owner-id</code> - The ID of the Amazon Web Services account that owns the Capacity Reservation.</p> </li> <li> <p> <code>instance-platform</code> - The type of operating system for which the Capacity Reservation reserves capacity.</p> </li> <li> <p> <code>availability-zone</code> - The Availability Zone of the Capacity Reservation.</p> </li> <li> <p> <code>tenancy</code> - Indicates the tenancy of the Capacity Reservation. A Capacity Reservation can have one of the following tenancy settings:</p> <ul> <li> <p> <code>default</code> - The Capacity Reservation is created on hardware that is shared with other Amazon Web Services accounts.</p> </li> <li> <p> <code>dedicated</code> - The Capacity Reservation is created on single-tenant hardware that is dedicated to a single Amazon Web Services account.</p> </li> </ul> </li> <li> <p> <code>outpost-arn</code> - The Amazon Resource Name (ARN) of the Outpost on which the Capacity Reservation was created.</p> </li> <li> <p> <code>state</code> - The current state of the Capacity Reservation. A Capacity Reservation can be in one of the following states:</p> <ul> <li> <p> <code>active</code>- The Capacity Reservation is active and the capacity is available for your use.</p> </li> <li> <p> <code>expired</code> - The Capacity Reservation expired automatically at the date and time specified in your request. The reserved capacity is no longer available for your use.</p> </li> <li> <p> <code>cancelled</code> - The Capacity Reservation was cancelled. The reserved capacity is no longer available for your use.</p> </li> <li> <p> <code>pending</code> - The Capacity Reservation request was successful but the capacity provisioning is still pending.</p> </li> <li> <p> <code>failed</code> - The Capacity Reservation request has failed. A request might fail due to invalid request parameters, capacity constraints, or instance limit constraints. Failed requests are retained for 60 minutes.</p> </li> </ul> </li> <li> <p> <code>start-date</code> - The date and time at which the Capacity Reservation was started.</p> </li> <li> <p> <code>end-date</code> - The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. The Capacity Reservation's state changes to expired when it reaches its end date and time.</p> </li> <li> <p> <code>end-date-type</code> - Indicates the way in which the Capacity Reservation ends. A Capacity Reservation can have one of the following end types:</p> <ul> <li> <p> <code>unlimited</code> - The Capacity Reservation remains active until you explicitly cancel it.</p> </li> <li> <p> <code>limited</code> - The Capacity Reservation expires automatically at a specified date and time.</p> </li> </ul> </li> <li> <p> <code>instance-match-criteria</code> - Indicates the type of instance launches that the Capacity Reservation accepts. The options include:</p> <ul> <li> <p> <code>open</code> - The Capacity Reservation accepts all instances that have matching attributes (instance type, platform, and Availability Zone). Instances that have matching attributes launch into the Capacity Reservation automatically without specifying any additional parameters.</p> </li> <li> <p> <code>targeted</code> - The Capacity Reservation only accepts instances that have matching attributes (instance type, platform, and Availability Zone), and explicitly target the Capacity Reservation. This ensures that only permitted instances can use the reserved capacity.</p> </li> </ul> </li> <li> <p> <code>placement-group-arn</code> - The ARN of the cluster placement group in which the Capacity Reservation was created.</p> </li> </ul>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityReservationsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_reservation_ids" in value:
        import capo_ec2.types.capacity_reservation_id_set

        capo_ec2.types.capacity_reservation_id_set.serialize_ec2_query(
            value["capacity_reservation_ids"],
            pairs,
            f"{key_prefix}CapacityReservationId",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DescribeCapacityReservationsRequest:
    out: DescribeCapacityReservationsRequest = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_ids = el.find("CapacityReservationId")
    if child_capacity_reservation_ids is not None:
        import capo_ec2.types.capacity_reservation_id_set

        out["capacity_reservation_ids"] = (
            capo_ec2.types.capacity_reservation_id_set.deserialize_ec2_query(
                child_capacity_reservation_ids
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
