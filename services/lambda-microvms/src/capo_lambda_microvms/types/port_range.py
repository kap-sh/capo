"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#PortRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_microvms.types.port_number


class PortRange(TypedDict, closed=True):
    start_port: "capo_lambda_microvms.types.port_number.PortNumber"
    """<p>The starting port number of the range.</p>"""
    end_port: "capo_lambda_microvms.types.port_number.PortNumber"
    """<p>The ending port number of the range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PortRange) -> dict:
    out: dict = {}
    out["startPort"] = value["start_port"]
    out["endPort"] = value["end_port"]
    return out


def deserialize_json(data: dict) -> PortRange:
    out: PortRange = {}  # type: ignore[typeddict-item]
    if data.get("startPort") is not None:
        out["start_port"] = data["startPort"]
    else:
        out["start_port"] = 0
    if data.get("endPort") is not None:
        out["end_port"] = data["endPort"]
    else:
        out["end_port"] = 0
    return out
