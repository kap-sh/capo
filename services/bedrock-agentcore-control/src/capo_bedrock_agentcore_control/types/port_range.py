"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PortRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.port

PortRange = TypedDict(
    "PortRange",
    {
        "from": "capo_bedrock_agentcore_control.types.port.Port",
        "to": "capo_bedrock_agentcore_control.types.port.Port",
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: PortRange) -> dict:
    out: dict = {}
    out["from"] = value["from"]
    out["to"] = value["to"]
    return out


def deserialize_json(data: dict) -> PortRange:
    out: PortRange = {}  # type: ignore[typeddict-item]
    if data.get("from") is not None:
        out["from"] = data["from"]
    else:
        out["from"] = 0
    if data.get("to") is not None:
        out["to"] = data["to"]
    else:
        out["to"] = 0
    return out
