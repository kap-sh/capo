"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#TargetRef``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.target_name


class TargetRef(TypedDict, closed=True):
    name: "capo_bedrock_agentcore.types.target_name.TargetName"
    """<p>The name of the gateway target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetRef) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> TargetRef:
    out: TargetRef = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
