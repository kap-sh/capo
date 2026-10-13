"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GeneratedQueries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.generated_query

GeneratedQueries: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.generated_query.GeneratedQuery"
]


# --- restJson1 ser/de ---
def serialize_json(value: GeneratedQueries) -> list:
    import capo_bedrock_agent_runtime.types.generated_query

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.generated_query.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GeneratedQueries:
    import capo_bedrock_agent_runtime.types.generated_query

    out: GeneratedQueries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.generated_query.deserialize_json(item)
        )
    return out


def redact_sensitive(value: GeneratedQueries) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
