"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ContractIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.chain_address
    import capo_managedblockchain_query.types.query_network


class ContractIdentifier(TypedDict, closed=True):
    network: "capo_managedblockchain_query.types.query_network.QueryNetwork"
    """<p>The blockchain network of the contract.</p>"""
    contract_address: "capo_managedblockchain_query.types.chain_address.ChainAddress"
    """<p>Container for the blockchain address about a contract.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContractIdentifier) -> dict:
    out: dict = {}
    out["network"] = value["network"]
    out["contractAddress"] = value["contract_address"]
    return out


def deserialize_json(data: dict) -> ContractIdentifier:
    out: ContractIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("network") is not None:
        out["network"] = data["network"]
    else:
        out["network"] = ""
    if data.get("contractAddress") is not None:
        out["contract_address"] = data["contractAddress"]
    else:
        out["contract_address"] = ""
    return out
