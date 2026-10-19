"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#TokenIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.chain_address
    import capo_managedblockchain_query.types.query_network
    import capo_managedblockchain_query.types.query_token_id


class TokenIdentifier(TypedDict, closed=True):
    network: "capo_managedblockchain_query.types.query_network.QueryNetwork"
    """<p>The blockchain network of the token.</p>"""
    contract_address: NotRequired[
        "capo_managedblockchain_query.types.chain_address.ChainAddress"
    ]
    """<p>This is the token's contract address.</p>"""
    token_id: NotRequired[
        "capo_managedblockchain_query.types.query_token_id.QueryTokenId"
    ]
    """<p>The unique identifier of the token.</p> <note> <p>For native tokens, use the 3 character abbreviation that best matches your token. For example, btc for Bitcoin, eth for Ether, etc. For all other token types you must specify the <code>tokenId</code> in the 64 character hexadecimal <code>tokenid</code> format.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: TokenIdentifier) -> dict:
    out: dict = {}
    out["network"] = value["network"]
    if "contract_address" in value:
        out["contractAddress"] = value["contract_address"]
    if "token_id" in value:
        out["tokenId"] = value["token_id"]
    return out


def deserialize_json(data: dict) -> TokenIdentifier:
    out: TokenIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("network") is not None:
        out["network"] = data["network"]
    else:
        out["network"] = ""
    if data.get("contractAddress") is not None:
        out["contract_address"] = data["contractAddress"]
    if data.get("tokenId") is not None:
        out["token_id"] = data["tokenId"]
    return out
