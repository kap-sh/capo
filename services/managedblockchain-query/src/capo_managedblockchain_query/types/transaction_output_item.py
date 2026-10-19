"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#TransactionOutputItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_managedblockchain_query.types.confirmation_status
    import capo_managedblockchain_query.types.query_network
    import capo_managedblockchain_query.types.query_transaction_hash
    import capo_managedblockchain_query.types.query_transaction_id


class TransactionOutputItem(TypedDict, closed=True):
    transaction_hash: (
        "capo_managedblockchain_query.types.query_transaction_hash.QueryTransactionHash"
    )
    """<p>The hash of a transaction. It is generated when a transaction is created.</p>"""
    transaction_id: NotRequired[
        "capo_managedblockchain_query.types.query_transaction_id.QueryTransactionId"
    ]
    """<p>The identifier of a Bitcoin transaction. It is generated when a transaction is created.</p>"""
    network: "capo_managedblockchain_query.types.query_network.QueryNetwork"
    """<p>The blockchain network where the transaction occurred.</p>"""
    transaction_timestamp: "datetime.datetime"
    """<p>The time when the transaction occurred.</p>"""
    confirmation_status: NotRequired[
        "capo_managedblockchain_query.types.confirmation_status.ConfirmationStatus"
    ]
    """<p>Specifies whether to list transactions that have not reached Finality.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransactionOutputItem) -> dict:
    out: dict = {}
    out["transactionHash"] = value["transaction_hash"]
    if "transaction_id" in value:
        out["transactionId"] = value["transaction_id"]
    out["network"] = value["network"]
    import capo_managedblockchain_query.types._prelude.timestamp

    out["transactionTimestamp"] = (
        capo_managedblockchain_query.types._prelude.timestamp.serialize_json(
            value["transaction_timestamp"]
        )
    )
    if "confirmation_status" in value:
        out["confirmationStatus"] = value["confirmation_status"]
    return out


def deserialize_json(data: dict) -> TransactionOutputItem:
    out: TransactionOutputItem = {}  # type: ignore[typeddict-item]
    if data.get("transactionHash") is not None:
        out["transaction_hash"] = data["transactionHash"]
    else:
        out["transaction_hash"] = ""
    if data.get("transactionId") is not None:
        out["transaction_id"] = data["transactionId"]
    if data.get("network") is not None:
        out["network"] = data["network"]
    else:
        out["network"] = ""
    if data.get("transactionTimestamp") is not None:
        import capo_managedblockchain_query.types._prelude.timestamp

        out["transaction_timestamp"] = (
            capo_managedblockchain_query.types._prelude.timestamp.deserialize_json(
                data["transactionTimestamp"]
            )
        )
    else:
        import datetime

        out["transaction_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("confirmationStatus") is not None:
        out["confirmation_status"] = data["confirmationStatus"]
    return out
