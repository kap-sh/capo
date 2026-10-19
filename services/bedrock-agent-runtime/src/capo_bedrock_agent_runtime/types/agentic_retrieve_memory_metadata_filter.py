"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveMemoryMetadataFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_left
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_operator
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_right


class AgenticRetrieveMemoryMetadataFilter(TypedDict, closed=True):
    left: "capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_left.AgenticRetrieveMemoryMetadataFilterLeft"
    """<p>The metadata key that the expression evaluates.</p>"""
    operator: "capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_operator.AgenticRetrieveMemoryMetadataFilterOperator"
    """<p>The relationship that the metadata key and value must have for a memory record to match.</p>"""
    right: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_right.AgenticRetrieveMemoryMetadataFilterRight"
    ]
    """<p>The value that the expression compares the metadata key against. Supply this value for every operator except EXISTS and NOT_EXISTS.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveMemoryMetadataFilter) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_left

    out["left"] = (
        capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_left.serialize_json(
            value["left"]
        )
    )
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_operator

    out["operator"] = (
        capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_operator.serialize_json(
            value["operator"]
        )
    )
    if "right" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_right

        out["right"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_right.serialize_json(
                value["right"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgenticRetrieveMemoryMetadataFilter:
    out: AgenticRetrieveMemoryMetadataFilter = {}  # type: ignore[typeddict-item]
    if data.get("left") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_left

        out["left"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_left.deserialize_json(
                data["left"]
            )
        )
    else:
        import capo_bedrock_agent_runtime.types._unknown

        out["left"] = capo_bedrock_agent_runtime.types._unknown.UnknownUnionMember("")
    if data.get("operator") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_operator

        out["operator"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_operator.deserialize_json(
                data["operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_operator.AgenticRetrieveMemoryMetadataFilterOperator",
            "",
        )
    if data.get("right") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_right

        out["right"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_right.deserialize_json(
                data["right"]
            )
        )
    return out
