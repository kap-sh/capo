"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#GetTransactionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.query_network
    import capo_managedblockchain_query.types.query_transaction_hash
    import capo_managedblockchain_query.types.query_transaction_id


class GetTransactionInput(TypedDict, closed=True):
    transaction_hash: NotRequired[
        "capo_managedblockchain_query.types.query_transaction_hash.QueryTransactionHash"
    ]
    """<p>The hash of a transaction. It is generated when a transaction is created.</p>"""
    transaction_id: NotRequired[
        "capo_managedblockchain_query.types.query_transaction_id.QueryTransactionId"
    ]
    """<p>The identifier of a Bitcoin transaction. It is generated when a transaction is created.</p> <note> <p> <code>transactionId</code> is only supported on the Bitcoin networks.</p> </note>"""
    network: "capo_managedblockchain_query.types.query_network.QueryNetwork"
    """<p>The blockchain network where the transaction occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTransactionInput) -> dict:
    out: dict = {}
    if "transaction_hash" in value:
        out["transactionHash"] = value["transaction_hash"]
    if "transaction_id" in value:
        out["transactionId"] = value["transaction_id"]
    out["network"] = value["network"]
    return out


def deserialize_json(data: dict) -> GetTransactionInput:
    out: GetTransactionInput = {}  # type: ignore[typeddict-item]
    if data.get("transactionHash") is not None:
        out["transaction_hash"] = data["transactionHash"]
    if data.get("transactionId") is not None:
        out["transaction_id"] = data["transactionId"]
    if data.get("network") is not None:
        out["network"] = data["network"]
    else:
        out["network"] = ""
    return out
