"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#QueryGenerationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.input_query_type


class QueryGenerationInput(TypedDict, closed=True):
    type: "capo_bedrock_agent_runtime.types.input_query_type.InputQueryType"
    """<p>The type of the query.</p>"""
    text: "str"
    """<p>The text of the query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryGenerationInput) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.input_query_type

    out["type"] = capo_bedrock_agent_runtime.types.input_query_type.serialize_json(
        value["type"]
    )
    out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> QueryGenerationInput:
    out: QueryGenerationInput = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent_runtime.types.input_query_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.input_query_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent_runtime.types.input_query_type.InputQueryType", ""
        )
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    return out
