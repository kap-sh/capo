"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#OwnerFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.chain_address


class OwnerFilter(TypedDict, closed=True):
    address: "capo_managedblockchain_query.types.chain_address.ChainAddress"
    """<p>The contract or wallet address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OwnerFilter) -> dict:
    out: dict = {}
    out["address"] = value["address"]
    return out


def deserialize_json(data: dict) -> OwnerFilter:
    out: OwnerFilter = {}  # type: ignore[typeddict-item]
    if data.get("address") is not None:
        out["address"] = data["address"]
    else:
        out["address"] = ""
    return out
