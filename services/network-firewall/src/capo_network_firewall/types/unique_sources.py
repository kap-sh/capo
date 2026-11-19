"""Generated from Smithy shape ``com.amazonaws.networkfirewall#UniqueSources``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.count


class UniqueSources(TypedDict, closed=True):
    count: "capo_network_firewall.types.count.Count"
    """<p>The number of unique source IP addresses that connected to a domain.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UniqueSources) -> dict:
    out: dict = {}
    out["Count"] = value.get("count", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> UniqueSources:
    out: UniqueSources = {}  # type: ignore[typeddict-item]
    if data.get("Count") is not None:
        out["count"] = data["Count"]
    else:
        out["count"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UniqueSources) -> dict:
    out: dict = {}
    out["Count"] = value.get("count", 0)
    return out


def deserialize_cbor(data: dict) -> UniqueSources:
    out: UniqueSources = {}  # type: ignore[typeddict-item]
    if data.get("Count") is not None:
        out["count"] = data["Count"]
    else:
        out["count"] = 0
    return out
