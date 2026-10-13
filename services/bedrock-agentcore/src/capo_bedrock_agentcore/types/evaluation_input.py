"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluationInput``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.spans


class _EvaluationInput_sessionSpans(TypedDict, closed=True):
    sessionSpans: "capo_bedrock_agentcore.types.spans.Spans"


EvaluationInput: TypeAlias = _EvaluationInput_sessionSpans


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationInput) -> dict:
    if "sessionSpans" in value:
        import capo_bedrock_agentcore.types.spans

        return {
            "sessionSpans": capo_bedrock_agentcore.types.spans.serialize_json(
                value["sessionSpans"]
            )
        }
    else:
        raise SerializationError("EvaluationInput: no variant present")


def deserialize_json(data: dict) -> EvaluationInput:
    if data.get("sessionSpans") is not None:
        import capo_bedrock_agentcore.types.spans

        return {
            "sessionSpans": capo_bedrock_agentcore.types.spans.deserialize_json(
                data["sessionSpans"]
            )
        }
    else:
        raise DeserializationError("EvaluationInput: no recognized variant key")


def redact_sensitive(value: EvaluationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sessionSpans" in value:
        out["sessionSpans"] = "*** Sensitive Data Redacted ***"
    return out
