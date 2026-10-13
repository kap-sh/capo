"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetMemoryOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.memory


class GetMemoryOutput(TypedDict, closed=True):
    memory: "capo_bedrock_agentcore_control.types.memory.Memory"
    """<p>The retrieved AgentCore Memory resource details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMemoryOutput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.memory

    out["memory"] = capo_bedrock_agentcore_control.types.memory.serialize_json(
        value["memory"]
    )
    return out


def deserialize_json(data: dict) -> GetMemoryOutput:
    out: GetMemoryOutput = {}  # type: ignore[typeddict-item]
    if data.get("memory") is not None:
        import capo_bedrock_agentcore_control.types.memory

        out["memory"] = capo_bedrock_agentcore_control.types.memory.deserialize_json(
            data["memory"]
        )
    else:
        raise DeserializationError("GetMemoryOutput.memory required")
    return out


def redact_sensitive(value: GetMemoryOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "memory" in value:
        import capo_bedrock_agentcore_control.types.memory

        out["memory"] = capo_bedrock_agentcore_control.types.memory.redact_sensitive(
            value["memory"]
        )
    return out
