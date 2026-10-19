"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ContractFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.chain_address
    import capo_managedblockchain_query.types.query_network
    import capo_managedblockchain_query.types.query_token_standard


class ContractFilter(TypedDict, closed=True):
    network: "capo_managedblockchain_query.types.query_network.QueryNetwork"
    """<p>The blockchain network of the contract.</p>"""
    token_standard: (
        "capo_managedblockchain_query.types.query_token_standard.QueryTokenStandard"
    )
    """<p>The container for the token standard.</p>"""
    deployer_address: "capo_managedblockchain_query.types.chain_address.ChainAddress"
    """<p>The network address of the deployer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContractFilter) -> dict:
    out: dict = {}
    out["network"] = value["network"]
    out["tokenStandard"] = value["token_standard"]
    out["deployerAddress"] = value["deployer_address"]
    return out


def deserialize_json(data: dict) -> ContractFilter:
    out: ContractFilter = {}  # type: ignore[typeddict-item]
    if data.get("network") is not None:
        out["network"] = data["network"]
    else:
        out["network"] = ""
    if data.get("tokenStandard") is not None:
        out["token_standard"] = data["tokenStandard"]
    else:
        out["token_standard"] = ""
    if data.get("deployerAddress") is not None:
        out["deployer_address"] = data["deployerAddress"]
    else:
        out["deployer_address"] = ""
    return out
