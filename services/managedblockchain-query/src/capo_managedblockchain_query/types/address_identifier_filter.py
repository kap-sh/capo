"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#AddressIdentifierFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.chain_addresses


class AddressIdentifierFilter(TypedDict, closed=True):
    transaction_event_to_address: (
        "capo_managedblockchain_query.types.chain_addresses.ChainAddresses"
    )
    """<p>The container for the recipient address of the transaction. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddressIdentifierFilter) -> dict:
    out: dict = {}
    import capo_managedblockchain_query.types.chain_addresses

    out["transactionEventToAddress"] = (
        capo_managedblockchain_query.types.chain_addresses.serialize_json(
            value["transaction_event_to_address"]
        )
    )
    return out


def deserialize_json(data: dict) -> AddressIdentifierFilter:
    out: AddressIdentifierFilter = {}  # type: ignore[typeddict-item]
    if data.get("transactionEventToAddress") is not None:
        import capo_managedblockchain_query.types.chain_addresses

        out["transaction_event_to_address"] = (
            capo_managedblockchain_query.types.chain_addresses.deserialize_json(
                data["transactionEventToAddress"]
            )
        )
    else:
        out["transaction_event_to_address"] = []
    return out
