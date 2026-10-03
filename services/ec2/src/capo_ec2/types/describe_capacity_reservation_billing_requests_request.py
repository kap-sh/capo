"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityReservationBillingRequestsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.caller_role
    import capo_ec2.types.capacity_reservation_id_set
    import capo_ec2.types.describe_capacity_reservation_billing_requests_request_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.string


class DescribeCapacityReservationBillingRequestsRequest(TypedDict, closed=True):
    capacity_reservation_ids: NotRequired[
        "capo_ec2.types.capacity_reservation_id_set.CapacityReservationIdSet"
    ]
    """<p>The ID of the Capacity Reservation.</p>"""
    role: NotRequired["capo_ec2.types.caller_role.CallerRole"]
    """<p>Specify one of the following:</p> <ul> <li> <p> <code>odcr-owner</code> - If you are the Capacity Reservation owner, specify this value to view requests that you have initiated. Not supported with the <code>requested-by</code> filter.</p> </li> <li> <p> <code>unused-reservation-billing-owner</code> - If you are the consumer account, specify this value to view requests that have been sent to you. Not supported with the <code>unused-reservation-billing-owner</code> filter.</p> </li> </ul>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_capacity_reservation_billing_requests_request_max_results.DescribeCapacityReservationBillingRequestsRequestMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>status</code> - The state of the request (<code>pending</code> | <code>accepted</code> | <code>rejected</code> | <code>cancelled</code> | <code>revoked</code> | <code>expired</code>).</p> </li> <li> <p> <code>requested-by</code> - The account ID of the Capacity Reservation owner that initiated the request. Not supported if you specify <code>requested-by</code> for <b>Role</b>.</p> </li> <li> <p> <code>unused-reservation-billing-owner</code> - The ID of the consumer account to which the request was sent. Not supported if you specify <code>unused-reservation-billing-owner</code> for <b>Role</b>.</p> </li> </ul>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityReservationBillingRequestsRequest,
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
    if "role" in value:
        import capo_ec2.types.caller_role

        capo_ec2.types.caller_role.serialize_ec2_query(
            value["role"], pairs, f"{key_prefix}Role"
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


def deserialize_ec2_query(
    el: Element,
) -> DescribeCapacityReservationBillingRequestsRequest:
    out: DescribeCapacityReservationBillingRequestsRequest = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_ids = el.find("CapacityReservationId")
    if child_capacity_reservation_ids is not None:
        import capo_ec2.types.capacity_reservation_id_set

        out["capacity_reservation_ids"] = (
            capo_ec2.types.capacity_reservation_id_set.deserialize_ec2_query(
                child_capacity_reservation_ids
            )
        )
    child_role = el.find("Role")
    if child_role is not None:
        import capo_ec2.types.caller_role

        out["role"] = capo_ec2.types.caller_role.deserialize_ec2_query(child_role)
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
