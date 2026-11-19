"""Generated from Smithy shape ``com.amazonaws.memorydb#Endpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.integer
    import capo_memorydb.types.string


class Endpoint(TypedDict, closed=True):
    address: NotRequired["capo_memorydb.types.string.String"]
    """<p>The DNS hostname of the node.</p>"""
    port: "capo_memorydb.types.integer.Integer"
    """<p>The port number that the engine is listening on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Endpoint) -> dict:
    out: dict = {}
    if "address" in value:
        out["Address"] = value["address"]
    out["Port"] = value.get("port", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    if data.get("Address") is not None:
        out["address"] = data["Address"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    else:
        out["port"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Endpoint) -> dict:
    out: dict = {}
    if "address" in value:
        out["Address"] = value["address"]
    out["Port"] = value.get("port", 0)
    return out


def deserialize_cbor(data: dict) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    if data.get("Address") is not None:
        out["address"] = data["Address"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    else:
        out["port"] = 0
    return out
