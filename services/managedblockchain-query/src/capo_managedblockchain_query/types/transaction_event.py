"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#TransactionEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.blockchain_instant
    import capo_managedblockchain_query.types.chain_address
    import capo_managedblockchain_query.types.confirmation_status
    import capo_managedblockchain_query.types.query_network
    import capo_managedblockchain_query.types.query_token_id
    import capo_managedblockchain_query.types.query_transaction_event_type
    import capo_managedblockchain_query.types.query_transaction_hash

TransactionEvent = TypedDict(
    "TransactionEvent",
    {
        "network": "capo_managedblockchain_query.types.query_network.QueryNetwork",
        "transaction_hash": "capo_managedblockchain_query.types.query_transaction_hash.QueryTransactionHash",
        "event_type": "capo_managedblockchain_query.types.query_transaction_event_type.QueryTransactionEventType",
        "from": NotRequired[
            "capo_managedblockchain_query.types.chain_address.ChainAddress"
        ],
        "to": NotRequired[
            "capo_managedblockchain_query.types.chain_address.ChainAddress"
        ],
        "value": NotRequired["str"],
        "contract_address": NotRequired[
            "capo_managedblockchain_query.types.chain_address.ChainAddress"
        ],
        "token_id": NotRequired[
            "capo_managedblockchain_query.types.query_token_id.QueryTokenId"
        ],
        "transaction_id": NotRequired["str"],
        "vout_index": NotRequired["int"],
        "vout_spent": NotRequired["bool"],
        "spent_vout_transaction_id": NotRequired["str"],
        "spent_vout_transaction_hash": NotRequired["str"],
        "spent_vout_index": NotRequired["int"],
        "blockchain_instant": NotRequired[
            "capo_managedblockchain_query.types.blockchain_instant.BlockchainInstant"
        ],
        "confirmation_status": NotRequired[
            "capo_managedblockchain_query.types.confirmation_status.ConfirmationStatus"
        ],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: TransactionEvent) -> dict:
    out: dict = {}
    out["network"] = value["network"]
    out["transactionHash"] = value["transaction_hash"]
    out["eventType"] = value["event_type"]
    if "from" in value:
        out["from"] = value["from"]
    if "to" in value:
        out["to"] = value["to"]
    if "value" in value:
        out["value"] = value["value"]
    if "contract_address" in value:
        out["contractAddress"] = value["contract_address"]
    if "token_id" in value:
        out["tokenId"] = value["token_id"]
    if "transaction_id" in value:
        out["transactionId"] = value["transaction_id"]
    if "vout_index" in value:
        out["voutIndex"] = value["vout_index"]
    if "vout_spent" in value:
        out["voutSpent"] = value["vout_spent"]
    if "spent_vout_transaction_id" in value:
        out["spentVoutTransactionId"] = value["spent_vout_transaction_id"]
    if "spent_vout_transaction_hash" in value:
        out["spentVoutTransactionHash"] = value["spent_vout_transaction_hash"]
    if "spent_vout_index" in value:
        out["spentVoutIndex"] = value["spent_vout_index"]
    if "blockchain_instant" in value:
        import capo_managedblockchain_query.types.blockchain_instant

        out["blockchainInstant"] = (
            capo_managedblockchain_query.types.blockchain_instant.serialize_json(
                value["blockchain_instant"]
            )
        )
    if "confirmation_status" in value:
        out["confirmationStatus"] = value["confirmation_status"]
    return out


def deserialize_json(data: dict) -> TransactionEvent:
    out: TransactionEvent = {}  # type: ignore[typeddict-item]
    if data.get("network") is not None:
        out["network"] = data["network"]
    else:
        out["network"] = ""
    if data.get("transactionHash") is not None:
        out["transaction_hash"] = data["transactionHash"]
    else:
        out["transaction_hash"] = ""
    if data.get("eventType") is not None:
        out["event_type"] = data["eventType"]
    else:
        out["event_type"] = ""
    if data.get("from") is not None:
        out["from"] = data["from"]
    if data.get("to") is not None:
        out["to"] = data["to"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    if data.get("contractAddress") is not None:
        out["contract_address"] = data["contractAddress"]
    if data.get("tokenId") is not None:
        out["token_id"] = data["tokenId"]
    if data.get("transactionId") is not None:
        out["transaction_id"] = data["transactionId"]
    if data.get("voutIndex") is not None:
        out["vout_index"] = data["voutIndex"]
    if data.get("voutSpent") is not None:
        out["vout_spent"] = data["voutSpent"]
    if data.get("spentVoutTransactionId") is not None:
        out["spent_vout_transaction_id"] = data["spentVoutTransactionId"]
    if data.get("spentVoutTransactionHash") is not None:
        out["spent_vout_transaction_hash"] = data["spentVoutTransactionHash"]
    if data.get("spentVoutIndex") is not None:
        out["spent_vout_index"] = data["spentVoutIndex"]
    if data.get("blockchainInstant") is not None:
        import capo_managedblockchain_query.types.blockchain_instant

        out["blockchain_instant"] = (
            capo_managedblockchain_query.types.blockchain_instant.deserialize_json(
                data["blockchainInstant"]
            )
        )
    if data.get("confirmationStatus") is not None:
        out["confirmation_status"] = data["confirmationStatus"]
    return out
