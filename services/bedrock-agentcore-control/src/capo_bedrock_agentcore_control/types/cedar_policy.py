"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CedarPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.statement


class CedarPolicy(TypedDict, closed=True):
    statement: "capo_bedrock_agentcore_control.types.statement.Statement"
    """<p>The Cedar policy statement that defines the authorization logic. This statement follows Cedar syntax and specifies principals, actions, resources, and conditions that determine when access should be allowed or denied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CedarPolicy) -> dict:
    out: dict = {}
    out["statement"] = value["statement"]
    return out


def deserialize_json(data: dict) -> CedarPolicy:
    out: CedarPolicy = {}  # type: ignore[typeddict-item]
    if data.get("statement") is not None:
        out["statement"] = data["statement"]
    else:
        out["statement"] = ""
    return out
