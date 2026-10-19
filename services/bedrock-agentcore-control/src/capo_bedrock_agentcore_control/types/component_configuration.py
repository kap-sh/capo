"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ComponentConfiguration``."""

from typing_extensions import TypedDict


class ComponentConfiguration(TypedDict, closed=True):
    configuration: "object"
    """<p>The configuration values as a flexible JSON document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentConfiguration) -> dict:
    out: dict = {}
    out["configuration"] = value["configuration"]
    return out


def deserialize_json(data: dict) -> ComponentConfiguration:
    out: ComponentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("configuration") is not None:
        out["configuration"] = data["configuration"]
    else:
        out["configuration"] = None
    return out
