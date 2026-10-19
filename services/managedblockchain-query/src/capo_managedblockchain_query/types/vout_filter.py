"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#VoutFilter``."""

from typing_extensions import TypedDict


class VoutFilter(TypedDict, closed=True):
    vout_spent: "bool"
    """<p>Specifies if the transaction output is spent or unspent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoutFilter) -> dict:
    out: dict = {}
    out["voutSpent"] = value["vout_spent"]
    return out


def deserialize_json(data: dict) -> VoutFilter:
    out: VoutFilter = {}  # type: ignore[typeddict-item]
    if data.get("voutSpent") is not None:
        out["vout_spent"] = data["voutSpent"]
    else:
        out["vout_spent"] = False
    return out
