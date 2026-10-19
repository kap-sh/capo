"""Generated from Smithy shape ``com.amazonaws.groundstation#RangedSocketAddress``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.integer_range
    import capo_groundstation.types.ip_v4_address


class RangedSocketAddress(TypedDict, closed=True):
    name: "capo_groundstation.types.ip_v4_address.IpV4Address"
    """<p>IPv4 socket address.</p>"""
    port_range: "capo_groundstation.types.integer_range.IntegerRange"
    """<p>Port range of a socket address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RangedSocketAddress) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_groundstation.types.integer_range

    out["portRange"] = capo_groundstation.types.integer_range.serialize_json(
        value["port_range"]
    )
    return out


def deserialize_json(data: dict) -> RangedSocketAddress:
    out: RangedSocketAddress = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("portRange") is not None:
        import capo_groundstation.types.integer_range

        out["port_range"] = capo_groundstation.types.integer_range.deserialize_json(
            data["portRange"]
        )
    else:
        raise DeserializationError("RangedSocketAddress.port_range required")
    return out
