"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#Transaction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_managedblockchain_query.types.block_hash
    import capo_managedblockchain_query.types.chain_address
    import capo_managedblockchain_query.types.confirmation_status
    import capo_managedblockchain_query.types.execution_status
    import capo_managedblockchain_query.types.query_network
    import capo_managedblockchain_query.types.query_transaction_hash

Transaction = TypedDict(
    "Transaction",
    {
        "network": "capo_managedblockchain_query.types.query_network.QueryNetwork",
        "block_hash": NotRequired[
            "capo_managedblockchain_query.types.block_hash.BlockHash"
        ],
        "transaction_hash": "capo_managedblockchain_query.types.query_transaction_hash.QueryTransactionHash",
        "block_number": NotRequired["str"],
        "transaction_timestamp": "datetime.datetime",
        "transaction_index": "int",
        "number_of_transactions": "int",
        "to": "capo_managedblockchain_query.types.chain_address.ChainAddress",
        "from": NotRequired[
            "capo_managedblockchain_query.types.chain_address.ChainAddress"
        ],
        "contract_address": NotRequired[
            "capo_managedblockchain_query.types.chain_address.ChainAddress"
        ],
        "gas_used": NotRequired["str"],
        "cumulative_gas_used": NotRequired["str"],
        "effective_gas_price": NotRequired["str"],
        "signature_v": NotRequired["int"],
        "signature_r": NotRequired["str"],
        "signature_s": NotRequired["str"],
        "transaction_fee": NotRequired["str"],
        "transaction_id": NotRequired["str"],
        "confirmation_status": NotRequired[
            "capo_managedblockchain_query.types.confirmation_status.ConfirmationStatus"
        ],
        "execution_status": NotRequired[
            "capo_managedblockchain_query.types.execution_status.ExecutionStatus"
        ],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: Transaction) -> dict:
    out: dict = {}
    out["network"] = value["network"]
    if "block_hash" in value:
        out["blockHash"] = value["block_hash"]
    out["transactionHash"] = value["transaction_hash"]
    if "block_number" in value:
        out["blockNumber"] = value["block_number"]
    import capo_managedblockchain_query.types._prelude.timestamp

    out["transactionTimestamp"] = (
        capo_managedblockchain_query.types._prelude.timestamp.serialize_json(
            value["transaction_timestamp"]
        )
    )
    out["transactionIndex"] = value["transaction_index"]
    out["numberOfTransactions"] = value["number_of_transactions"]
    out["to"] = value["to"]
    if "from" in value:
        out["from"] = value["from"]
    if "contract_address" in value:
        out["contractAddress"] = value["contract_address"]
    if "gas_used" in value:
        out["gasUsed"] = value["gas_used"]
    if "cumulative_gas_used" in value:
        out["cumulativeGasUsed"] = value["cumulative_gas_used"]
    if "effective_gas_price" in value:
        out["effectiveGasPrice"] = value["effective_gas_price"]
    if "signature_v" in value:
        out["signatureV"] = value["signature_v"]
    if "signature_r" in value:
        out["signatureR"] = value["signature_r"]
    if "signature_s" in value:
        out["signatureS"] = value["signature_s"]
    if "transaction_fee" in value:
        out["transactionFee"] = value["transaction_fee"]
    if "transaction_id" in value:
        out["transactionId"] = value["transaction_id"]
    if "confirmation_status" in value:
        out["confirmationStatus"] = value["confirmation_status"]
    if "execution_status" in value:
        out["executionStatus"] = value["execution_status"]
    return out


def deserialize_json(data: dict) -> Transaction:
    out: Transaction = {}  # type: ignore[typeddict-item]
    if data.get("network") is not None:
        out["network"] = data["network"]
    else:
        out["network"] = ""
    if data.get("blockHash") is not None:
        out["block_hash"] = data["blockHash"]
    if data.get("transactionHash") is not None:
        out["transaction_hash"] = data["transactionHash"]
    else:
        out["transaction_hash"] = ""
    if data.get("blockNumber") is not None:
        out["block_number"] = data["blockNumber"]
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
    if data.get("transactionIndex") is not None:
        out["transaction_index"] = data["transactionIndex"]
    else:
        out["transaction_index"] = 0
    if data.get("numberOfTransactions") is not None:
        out["number_of_transactions"] = data["numberOfTransactions"]
    else:
        out["number_of_transactions"] = 0
    if data.get("to") is not None:
        out["to"] = data["to"]
    else:
        out["to"] = ""
    if data.get("from") is not None:
        out["from"] = data["from"]
    if data.get("contractAddress") is not None:
        out["contract_address"] = data["contractAddress"]
    if data.get("gasUsed") is not None:
        out["gas_used"] = data["gasUsed"]
    if data.get("cumulativeGasUsed") is not None:
        out["cumulative_gas_used"] = data["cumulativeGasUsed"]
    if data.get("effectiveGasPrice") is not None:
        out["effective_gas_price"] = data["effectiveGasPrice"]
    if data.get("signatureV") is not None:
        out["signature_v"] = data["signatureV"]
    if data.get("signatureR") is not None:
        out["signature_r"] = data["signatureR"]
    if data.get("signatureS") is not None:
        out["signature_s"] = data["signatureS"]
    if data.get("transactionFee") is not None:
        out["transaction_fee"] = data["transactionFee"]
    if data.get("transactionId") is not None:
        out["transaction_id"] = data["transactionId"]
    if data.get("confirmationStatus") is not None:
        out["confirmation_status"] = data["confirmationStatus"]
    if data.get("executionStatus") is not None:
        out["execution_status"] = data["executionStatus"]
    return out
