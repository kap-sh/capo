"""Generated from Smithy shape ``com.amazonaws.bedrockagent#QueryGenerationConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.query_execution_timeout_seconds
    import capo_bedrock_agent.types.query_generation_context


class QueryGenerationConfiguration(TypedDict, closed=True):
    execution_timeout_seconds: NotRequired[
        "capo_bedrock_agent.types.query_execution_timeout_seconds.QueryExecutionTimeoutSeconds"
    ]
    """<p>The time after which query generation will time out.</p>"""
    generation_context: NotRequired[
        "capo_bedrock_agent.types.query_generation_context.QueryGenerationContext"
    ]
    """<p>Specifies configurations for context to use during query generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryGenerationConfiguration) -> dict:
    out: dict = {}
    if "execution_timeout_seconds" in value:
        out["executionTimeoutSeconds"] = value["execution_timeout_seconds"]
    if "generation_context" in value:
        import capo_bedrock_agent.types.query_generation_context

        out["generationContext"] = (
            capo_bedrock_agent.types.query_generation_context.serialize_json(
                value["generation_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> QueryGenerationConfiguration:
    out: QueryGenerationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("executionTimeoutSeconds") is not None:
        out["execution_timeout_seconds"] = data["executionTimeoutSeconds"]
    if data.get("generationContext") is not None:
        import capo_bedrock_agent.types.query_generation_context

        out["generation_context"] = (
            capo_bedrock_agent.types.query_generation_context.deserialize_json(
                data["generationContext"]
            )
        )
    return out


def redact_sensitive(value: QueryGenerationConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "generation_context" in value:
        out["generation_context"] = "*** Sensitive Data Redacted ***"
    return out
