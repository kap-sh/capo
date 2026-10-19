"""Generated from Smithy shape ``com.amazonaws.inspector2#PortRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.port


class PortRange(TypedDict, closed=True):
    begin: "capo_inspector2.types.port.Port"
    """<p>The beginning port in a port range.</p>"""
    end: "capo_inspector2.types.port.Port"
    """<p>The ending port in a port range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PortRange) -> dict:
    out: dict = {}
    out["begin"] = value["begin"]
    out["end"] = value["end"]
    return out


def deserialize_json(data: dict) -> PortRange:
    out: PortRange = {}  # type: ignore[typeddict-item]
    if data.get("begin") is not None:
        out["begin"] = data["begin"]
    else:
        out["begin"] = 0
    if data.get("end") is not None:
        out["end"] = data["end"]
    else:
        out["end"] = 0
    return out
