"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ListTransactionEventsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.next_token
    import capo_managedblockchain_query.types.transaction_event_list


class ListTransactionEventsOutput(TypedDict, closed=True):
    events: (
        "capo_managedblockchain_query.types.transaction_event_list.TransactionEventList"
    )
    """<p>An array of <code>TransactionEvent</code> objects. Each object contains details about the transaction events.</p>"""
    next_token: NotRequired["capo_managedblockchain_query.types.next_token.NextToken"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTransactionEventsOutput) -> dict:
    out: dict = {}
    import capo_managedblockchain_query.types.transaction_event_list

    out["events"] = (
        capo_managedblockchain_query.types.transaction_event_list.serialize_json(
            value["events"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTransactionEventsOutput:
    out: ListTransactionEventsOutput = {}  # type: ignore[typeddict-item]
    if data.get("events") is not None:
        import capo_managedblockchain_query.types.transaction_event_list

        out["events"] = (
            capo_managedblockchain_query.types.transaction_event_list.deserialize_json(
                data["events"]
            )
        )
    else:
        out["events"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
