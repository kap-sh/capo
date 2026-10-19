"""Generated from Smithy shape ``com.amazonaws.vpclattice#TxtMethodConfig``."""

from typing_extensions import TypedDict


class TxtMethodConfig(TypedDict, closed=True):
    value: "str"
    """<p> The value that must be added to the TXT record for domain verification. </p>"""
    name: "str"
    """<p> The name of the TXT record that must be created for domain verification. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TxtMethodConfig) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> TxtMethodConfig:
    out: TxtMethodConfig = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
