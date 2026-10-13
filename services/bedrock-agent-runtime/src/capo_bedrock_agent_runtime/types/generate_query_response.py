"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GenerateQueryResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.generated_queries


class GenerateQueryResponse(TypedDict, closed=True):
    queries: NotRequired[
        "capo_bedrock_agent_runtime.types.generated_queries.GeneratedQueries"
    ]
    """<p>A list of objects, each of which defines a generated query that can correspond to the natural language queries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateQueryResponse) -> dict:
    out: dict = {}
    if "queries" in value:
        import capo_bedrock_agent_runtime.types.generated_queries

        out["queries"] = (
            capo_bedrock_agent_runtime.types.generated_queries.serialize_json(
                value["queries"]
            )
        )
    return out


def deserialize_json(data: dict) -> GenerateQueryResponse:
    out: GenerateQueryResponse = {}  # type: ignore[typeddict-item]
    if data.get("queries") is not None:
        import capo_bedrock_agent_runtime.types.generated_queries

        out["queries"] = (
            capo_bedrock_agent_runtime.types.generated_queries.deserialize_json(
                data["queries"]
            )
        )
    return out


def redact_sensitive(value: GenerateQueryResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "queries" in value:
        import capo_bedrock_agent_runtime.types.generated_queries

        out["queries"] = (
            capo_bedrock_agent_runtime.types.generated_queries.redact_sensitive(
                value["queries"]
            )
        )
    return out
