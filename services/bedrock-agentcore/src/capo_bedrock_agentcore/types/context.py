"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Context``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.span_context


class ContextSpanContextMember(TypedDict, closed=True):
    spanContext: "capo_bedrock_agentcore.types.span_context.SpanContext"


Context: TypeAlias = ContextSpanContextMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Context) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Context: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "spanContext" in value:
        import capo_bedrock_agentcore.types.span_context

        return {
            "spanContext": capo_bedrock_agentcore.types.span_context.serialize_json(
                value["spanContext"]
            )
        }
    else:
        raise SerializationError("Context: no variant present")


def deserialize_json(data: dict) -> Context:
    if data.get("spanContext") is not None:
        import capo_bedrock_agentcore.types.span_context

        return {
            "spanContext": capo_bedrock_agentcore.types.span_context.deserialize_json(
                data["spanContext"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Context: no recognized variant key")
