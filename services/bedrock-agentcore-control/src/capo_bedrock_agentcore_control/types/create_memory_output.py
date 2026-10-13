"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateMemoryOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.memory


class CreateMemoryOutput(TypedDict, closed=True):
    memory: NotRequired["capo_bedrock_agentcore_control.types.memory.Memory"]
    """<p>The details of the created memory, including its ID, ARN, name, description, and configuration settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMemoryOutput) -> dict:
    out: dict = {}
    if "memory" in value:
        import capo_bedrock_agentcore_control.types.memory

        out["memory"] = capo_bedrock_agentcore_control.types.memory.serialize_json(
            value["memory"]
        )
    return out


def deserialize_json(data: dict) -> CreateMemoryOutput:
    out: CreateMemoryOutput = {}  # type: ignore[typeddict-item]
    if data.get("memory") is not None:
        import capo_bedrock_agentcore_control.types.memory

        out["memory"] = capo_bedrock_agentcore_control.types.memory.deserialize_json(
            data["memory"]
        )
    return out


def redact_sensitive(value: CreateMemoryOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "memory" in value:
        import capo_bedrock_agentcore_control.types.memory

        out["memory"] = capo_bedrock_agentcore_control.types.memory.redact_sensitive(
            value["memory"]
        )
    return out
