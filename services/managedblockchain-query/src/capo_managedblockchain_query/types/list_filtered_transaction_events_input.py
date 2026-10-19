"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ListFilteredTransactionEventsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.address_identifier_filter
    import capo_managedblockchain_query.types.confirmation_status_filter
    import capo_managedblockchain_query.types.list_filtered_transaction_events_sort
    import capo_managedblockchain_query.types.next_token
    import capo_managedblockchain_query.types.time_filter
    import capo_managedblockchain_query.types.vout_filter


class ListFilteredTransactionEventsInput(TypedDict, closed=True):
    network: "str"
    """<p>The blockchain network where the transaction occurred.</p> <p>Valid Values: <code>BITCOIN_MAINNET</code> | <code>BITCOIN_TESTNET</code> </p>"""
    address_identifier_filter: "capo_managedblockchain_query.types.address_identifier_filter.AddressIdentifierFilter"
    """<p>This is the unique public address on the blockchain for which the transaction events are being requested.</p>"""
    time_filter: NotRequired[
        "capo_managedblockchain_query.types.time_filter.TimeFilter"
    ]
    """<p>This container specifies the time frame for the transaction events returned in the response.</p>"""
    vout_filter: NotRequired[
        "capo_managedblockchain_query.types.vout_filter.VoutFilter"
    ]
    """<p>This container specifies filtering attributes related to BITCOIN_VOUT event types</p>"""
    confirmation_status_filter: NotRequired[
        "capo_managedblockchain_query.types.confirmation_status_filter.ConfirmationStatusFilter"
    ]
    sort: NotRequired[
        "capo_managedblockchain_query.types.list_filtered_transaction_events_sort.ListFilteredTransactionEventsSort"
    ]
    """<p>The order by which the results will be sorted.</p>"""
    next_token: NotRequired["capo_managedblockchain_query.types.next_token.NextToken"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of transaction events to list.</p> <p>Default: <code>100</code> </p> <note> <p>Even if additional results can be retrieved, the request can return less results than <code>maxResults</code> or an empty array of results.</p> <p>To retrieve the next set of results, make another request with the returned <code>nextToken</code> value. The value of <code>nextToken</code> is <code>null</code> when there are no more results to return</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFilteredTransactionEventsInput) -> dict:
    out: dict = {}
    out["network"] = value["network"]
    import capo_managedblockchain_query.types.address_identifier_filter

    out["addressIdentifierFilter"] = (
        capo_managedblockchain_query.types.address_identifier_filter.serialize_json(
            value["address_identifier_filter"]
        )
    )
    if "time_filter" in value:
        import capo_managedblockchain_query.types.time_filter

        out["timeFilter"] = (
            capo_managedblockchain_query.types.time_filter.serialize_json(
                value["time_filter"]
            )
        )
    if "vout_filter" in value:
        import capo_managedblockchain_query.types.vout_filter

        out["voutFilter"] = (
            capo_managedblockchain_query.types.vout_filter.serialize_json(
                value["vout_filter"]
            )
        )
    if "confirmation_status_filter" in value:
        import capo_managedblockchain_query.types.confirmation_status_filter

        out["confirmationStatusFilter"] = (
            capo_managedblockchain_query.types.confirmation_status_filter.serialize_json(
                value["confirmation_status_filter"]
            )
        )
    if "sort" in value:
        import capo_managedblockchain_query.types.list_filtered_transaction_events_sort

        out["sort"] = (
            capo_managedblockchain_query.types.list_filtered_transaction_events_sort.serialize_json(
                value["sort"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListFilteredTransactionEventsInput:
    out: ListFilteredTransactionEventsInput = {}  # type: ignore[typeddict-item]
    if data.get("network") is not None:
        out["network"] = data["network"]
    else:
        out["network"] = ""
    if data.get("addressIdentifierFilter") is not None:
        import capo_managedblockchain_query.types.address_identifier_filter

        out["address_identifier_filter"] = (
            capo_managedblockchain_query.types.address_identifier_filter.deserialize_json(
                data["addressIdentifierFilter"]
            )
        )
    else:
        raise DeserializationError(
            "ListFilteredTransactionEventsInput.address_identifier_filter required"
        )
    if data.get("timeFilter") is not None:
        import capo_managedblockchain_query.types.time_filter

        out["time_filter"] = (
            capo_managedblockchain_query.types.time_filter.deserialize_json(
                data["timeFilter"]
            )
        )
    if data.get("voutFilter") is not None:
        import capo_managedblockchain_query.types.vout_filter

        out["vout_filter"] = (
            capo_managedblockchain_query.types.vout_filter.deserialize_json(
                data["voutFilter"]
            )
        )
    if data.get("confirmationStatusFilter") is not None:
        import capo_managedblockchain_query.types.confirmation_status_filter

        out["confirmation_status_filter"] = (
            capo_managedblockchain_query.types.confirmation_status_filter.deserialize_json(
                data["confirmationStatusFilter"]
            )
        )
    if data.get("sort") is not None:
        import capo_managedblockchain_query.types.list_filtered_transaction_events_sort

        out["sort"] = (
            capo_managedblockchain_query.types.list_filtered_transaction_events_sort.deserialize_json(
                data["sort"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
