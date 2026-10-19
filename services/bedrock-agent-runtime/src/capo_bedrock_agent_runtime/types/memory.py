"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Memory``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.memory_session_summary


class _Memory_sessionSummary(TypedDict, closed=True):
    sessionSummary: (
        "capo_bedrock_agent_runtime.types.memory_session_summary.MemorySessionSummary"
    )


Memory: TypeAlias = _Memory_sessionSummary | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Memory) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"Memory: cannot serialize unknown variant {value.name!r}"
        )
    elif "sessionSummary" in value:
        import capo_bedrock_agent_runtime.types.memory_session_summary

        return {
            "sessionSummary": capo_bedrock_agent_runtime.types.memory_session_summary.serialize_json(
                value["sessionSummary"]
            )
        }
    else:
        raise SerializationError("Memory: no variant present")


def deserialize_json(data: dict) -> Memory:
    if data.get("sessionSummary") is not None:
        import capo_bedrock_agent_runtime.types.memory_session_summary

        return {
            "sessionSummary": capo_bedrock_agent_runtime.types.memory_session_summary.deserialize_json(
                data["sessionSummary"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("Memory: no recognized variant key")
