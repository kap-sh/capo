"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ListTransactionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.next_token
    import capo_managedblockchain_query.types.transaction_output_list


class ListTransactionsOutput(TypedDict, closed=True):
    transactions: "capo_managedblockchain_query.types.transaction_output_list.TransactionOutputList"
    """<p>The array of transactions returned by the request.</p>"""
    next_token: NotRequired["capo_managedblockchain_query.types.next_token.NextToken"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTransactionsOutput) -> dict:
    out: dict = {}
    import capo_managedblockchain_query.types.transaction_output_list

    out["transactions"] = (
        capo_managedblockchain_query.types.transaction_output_list.serialize_json(
            value["transactions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTransactionsOutput:
    out: ListTransactionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("transactions") is not None:
        import capo_managedblockchain_query.types.transaction_output_list

        out["transactions"] = (
            capo_managedblockchain_query.types.transaction_output_list.deserialize_json(
                data["transactions"]
            )
        )
    else:
        out["transactions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
