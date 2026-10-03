"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityReservationTopologyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.capacity_reservation_id_set
    import capo_ec2.types.describe_capacity_reservation_topology_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.string


class DescribeCapacityReservationTopologyRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_capacity_reservation_topology_max_results.DescribeCapacityReservationTopologyMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p> <p>You can't specify this parameter and the Capacity Reservation IDs parameter in the same request.</p> <p>Default: <code>10</code> </p>"""
    capacity_reservation_ids: NotRequired[
        "capo_ec2.types.capacity_reservation_id_set.CapacityReservationIdSet"
    ]
    """<p>The Capacity Reservation IDs.</p> <p>Default: Describes all your Capacity Reservations.</p> <p>Constraints: Maximum 10 explicitly specified Capacity Reservation IDs.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>availability-zone</code> - The name of the Availability Zone (for example, <code>us-west-2a</code>) or Local Zone (for example, <code>us-west-2-lax-1b</code>) that the Capacity Reservation is in.</p> </li> <li> <p> <code>instance-type</code> - The instance type (for example, <code>p4d.24xlarge</code>) or instance family (for example, <code>p4d*</code>). You can use the <code>*</code> wildcard to match zero or more characters, or the <code>?</code> wildcard to match zero or one character.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityReservationTopologyRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "capacity_reservation_ids" in value:
        import capo_ec2.types.capacity_reservation_id_set

        capo_ec2.types.capacity_reservation_id_set.serialize_ec2_query(
            value["capacity_reservation_ids"],
            pairs,
            f"{key_prefix}CapacityReservationId",
        )
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )


def deserialize_ec2_query(el: Element) -> DescribeCapacityReservationTopologyRequest:
    out: DescribeCapacityReservationTopologyRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_capacity_reservation_ids = el.find("CapacityReservationId")
    if child_capacity_reservation_ids is not None:
        import capo_ec2.types.capacity_reservation_id_set

        out["capacity_reservation_ids"] = (
            capo_ec2.types.capacity_reservation_id_set.deserialize_ec2_query(
                child_capacity_reservation_ids
            )
        )
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    return out
