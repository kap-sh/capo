"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ListTransactionEventsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.next_token
    import capo_managedblockchain_query.types.query_network
    import capo_managedblockchain_query.types.query_transaction_hash
    import capo_managedblockchain_query.types.query_transaction_id


class ListTransactionEventsInput(TypedDict, closed=True):
    transaction_hash: NotRequired[
        "capo_managedblockchain_query.types.query_transaction_hash.QueryTransactionHash"
    ]
    """<p>The hash of a transaction. It is generated when a transaction is created.</p>"""
    transaction_id: NotRequired[
        "capo_managedblockchain_query.types.query_transaction_id.QueryTransactionId"
    ]
    """<p>The identifier of a Bitcoin transaction. It is generated when a transaction is created.</p> <note> <p> <code>transactionId</code> is only supported on the Bitcoin networks.</p> </note>"""
    network: "capo_managedblockchain_query.types.query_network.QueryNetwork"
    """<p>The blockchain network where the transaction events occurred.</p>"""
    next_token: NotRequired["capo_managedblockchain_query.types.next_token.NextToken"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of transaction events to list.</p> <p>Default: <code>100</code> </p> <note> <p>Even if additional results can be retrieved, the request can return less results than <code>maxResults</code> or an empty array of results.</p> <p>To retrieve the next set of results, make another request with the returned <code>nextToken</code> value. The value of <code>nextToken</code> is <code>null</code> when there are no more results to return</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTransactionEventsInput) -> dict:
    out: dict = {}
    if "transaction_hash" in value:
        out["transactionHash"] = value["transaction_hash"]
    if "transaction_id" in value:
        out["transactionId"] = value["transaction_id"]
    out["network"] = value["network"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListTransactionEventsInput:
    out: ListTransactionEventsInput = {}  # type: ignore[typeddict-item]
    if data.get("transactionHash") is not None:
        out["transaction_hash"] = data["transactionHash"]
    if data.get("transactionId") is not None:
        out["transaction_id"] = data["transactionId"]
    if data.get("network") is not None:
        out["network"] = data["network"]
    else:
        out["network"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
