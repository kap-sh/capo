"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ListTransactionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.blockchain_instant
    import capo_managedblockchain_query.types.chain_address
    import capo_managedblockchain_query.types.confirmation_status_filter
    import capo_managedblockchain_query.types.list_transactions_sort
    import capo_managedblockchain_query.types.next_token
    import capo_managedblockchain_query.types.query_network


class ListTransactionsInput(TypedDict, closed=True):
    address: "capo_managedblockchain_query.types.chain_address.ChainAddress"
    """<p>The address (either a contract or wallet), whose transactions are being requested.</p>"""
    network: "capo_managedblockchain_query.types.query_network.QueryNetwork"
    """<p>The blockchain network where the transactions occurred.</p>"""
    from_blockchain_instant: NotRequired[
        "capo_managedblockchain_query.types.blockchain_instant.BlockchainInstant"
    ]
    to_blockchain_instant: NotRequired[
        "capo_managedblockchain_query.types.blockchain_instant.BlockchainInstant"
    ]
    sort: NotRequired[
        "capo_managedblockchain_query.types.list_transactions_sort.ListTransactionsSort"
    ]
    """<p>The order by which the results will be sorted. </p>"""
    next_token: NotRequired["capo_managedblockchain_query.types.next_token.NextToken"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of transactions to list.</p> <p>Default: <code>100</code> </p> <note> <p>Even if additional results can be retrieved, the request can return less results than <code>maxResults</code> or an empty array of results.</p> <p>To retrieve the next set of results, make another request with the returned <code>nextToken</code> value. The value of <code>nextToken</code> is <code>null</code> when there are no more results to return</p> </note>"""
    confirmation_status_filter: NotRequired[
        "capo_managedblockchain_query.types.confirmation_status_filter.ConfirmationStatusFilter"
    ]
    """<p>This filter is used to include transactions in the response that haven't reached <a href="https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/key-concepts.html#finality"> <i>finality</i> </a>. Transactions that have reached finality are always part of the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTransactionsInput) -> dict:
    out: dict = {}
    out["address"] = value["address"]
    out["network"] = value["network"]
    if "from_blockchain_instant" in value:
        import capo_managedblockchain_query.types.blockchain_instant

        out["fromBlockchainInstant"] = (
            capo_managedblockchain_query.types.blockchain_instant.serialize_json(
                value["from_blockchain_instant"]
            )
        )
    if "to_blockchain_instant" in value:
        import capo_managedblockchain_query.types.blockchain_instant

        out["toBlockchainInstant"] = (
            capo_managedblockchain_query.types.blockchain_instant.serialize_json(
                value["to_blockchain_instant"]
            )
        )
    if "sort" in value:
        import capo_managedblockchain_query.types.list_transactions_sort

        out["sort"] = (
            capo_managedblockchain_query.types.list_transactions_sort.serialize_json(
                value["sort"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "confirmation_status_filter" in value:
        import capo_managedblockchain_query.types.confirmation_status_filter

        out["confirmationStatusFilter"] = (
            capo_managedblockchain_query.types.confirmation_status_filter.serialize_json(
                value["confirmation_status_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListTransactionsInput:
    out: ListTransactionsInput = {}  # type: ignore[typeddict-item]
    if data.get("address") is not None:
        out["address"] = data["address"]
    else:
        raise DeserializationError("ListTransactionsInput.address required")
    if data.get("network") is not None:
        out["network"] = data["network"]
    else:
        raise DeserializationError("ListTransactionsInput.network required")
    if data.get("fromBlockchainInstant") is not None:
        import capo_managedblockchain_query.types.blockchain_instant

        out["from_blockchain_instant"] = (
            capo_managedblockchain_query.types.blockchain_instant.deserialize_json(
                data["fromBlockchainInstant"]
            )
        )
    if data.get("toBlockchainInstant") is not None:
        import capo_managedblockchain_query.types.blockchain_instant

        out["to_blockchain_instant"] = (
            capo_managedblockchain_query.types.blockchain_instant.deserialize_json(
                data["toBlockchainInstant"]
            )
        )
    if data.get("sort") is not None:
        import capo_managedblockchain_query.types.list_transactions_sort

        out["sort"] = (
            capo_managedblockchain_query.types.list_transactions_sort.deserialize_json(
                data["sort"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("confirmationStatusFilter") is not None:
        import capo_managedblockchain_query.types.confirmation_status_filter

        out["confirmation_status_filter"] = (
            capo_managedblockchain_query.types.confirmation_status_filter.deserialize_json(
                data["confirmationStatusFilter"]
            )
        )
    return out
