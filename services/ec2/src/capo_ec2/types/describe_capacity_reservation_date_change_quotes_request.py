"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityReservationDateChangeQuotesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.capacity_reservation_modification_quote_id_set
    import capo_ec2.types.describe_capacity_reservation_date_change_quotes_request_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.string


class DescribeCapacityReservationDateChangeQuotesRequest(TypedDict, closed=True):
    capacity_reservation_modification_quote_ids: NotRequired[
        "capo_ec2.types.capacity_reservation_modification_quote_id_set.CapacityReservationModificationQuoteIdSet"
    ]
    """<p>The IDs of the date change quotes to describe.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_capacity_reservation_date_change_quotes_request_max_results.DescribeCapacityReservationDateChangeQuotesRequestMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. Filter names and values are case-sensitive.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityReservationDateChangeQuotesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_reservation_modification_quote_ids" in value:
        import capo_ec2.types.capacity_reservation_modification_quote_id_set

        capo_ec2.types.capacity_reservation_modification_quote_id_set.serialize_ec2_query(
            value["capacity_reservation_modification_quote_ids"],
            pairs,
            f"{key_prefix}CapacityReservationModificationQuoteId",
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )


def deserialize_ec2_query(
    el: Element,
) -> DescribeCapacityReservationDateChangeQuotesRequest:
    out: DescribeCapacityReservationDateChangeQuotesRequest = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_modification_quote_ids = el.find(
        "CapacityReservationModificationQuoteId"
    )
    if child_capacity_reservation_modification_quote_ids is not None:
        import capo_ec2.types.capacity_reservation_modification_quote_id_set

        out["capacity_reservation_modification_quote_ids"] = (
            capo_ec2.types.capacity_reservation_modification_quote_id_set.deserialize_ec2_query(
                child_capacity_reservation_modification_quote_ids
            )
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    return out
