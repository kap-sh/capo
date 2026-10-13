"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetMemoryRecordOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.memory_record


class GetMemoryRecordOutput(TypedDict, closed=True):
    memory_record: "capo_bedrock_agentcore.types.memory_record.MemoryRecord"
    """<p>The requested memory record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMemoryRecordOutput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.memory_record

    out["memoryRecord"] = capo_bedrock_agentcore.types.memory_record.serialize_json(
        value["memory_record"]
    )
    return out


def deserialize_json(data: dict) -> GetMemoryRecordOutput:
    out: GetMemoryRecordOutput = {}  # type: ignore[typeddict-item]
    if data.get("memoryRecord") is not None:
        import capo_bedrock_agentcore.types.memory_record

        out["memory_record"] = (
            capo_bedrock_agentcore.types.memory_record.deserialize_json(
                data["memoryRecord"]
            )
        )
    else:
        raise DeserializationError("GetMemoryRecordOutput.memory_record required")
    return out


def redact_sensitive(value: GetMemoryRecordOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "memory_record" in value:
        import capo_bedrock_agentcore.types.memory_record

        out["memory_record"] = (
            capo_bedrock_agentcore.types.memory_record.redact_sensitive(
                value["memory_record"]
            )
        )
    return out
