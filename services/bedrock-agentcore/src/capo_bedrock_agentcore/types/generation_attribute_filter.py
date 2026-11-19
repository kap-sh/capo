"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GenerationAttributeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.generation_filter_operator
    import capo_bedrock_agentcore.types.generation_filter_value


class GenerationAttributeFilter(TypedDict, closed=True):
    key: "str"
    """<p>The attribute key.</p>"""
    operator: "capo_bedrock_agentcore.types.generation_filter_operator.GenerationFilterOperator"
    """<p>How to compare the attribute with <code>value</code>.</p>"""
    value: "capo_bedrock_agentcore.types.generation_filter_value.GenerationFilterValue"
    """<p>The value to compare the attribute with.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerationAttributeFilter) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_bedrock_agentcore.types.generation_filter_operator

    out["operator"] = (
        capo_bedrock_agentcore.types.generation_filter_operator.serialize_json(
            value["operator"]
        )
    )
    import capo_bedrock_agentcore.types.generation_filter_value

    out["value"] = capo_bedrock_agentcore.types.generation_filter_value.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> GenerationAttributeFilter:
    out: GenerationAttributeFilter = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("operator") is not None:
        import capo_bedrock_agentcore.types.generation_filter_operator

        out["operator"] = (
            capo_bedrock_agentcore.types.generation_filter_operator.deserialize_json(
                data["operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_bedrock_agentcore.types.generation_filter_operator.GenerationFilterOperator",
            "",
        )
    if data.get("value") is not None:
        import capo_bedrock_agentcore.types.generation_filter_value

        out["value"] = (
            capo_bedrock_agentcore.types.generation_filter_value.deserialize_json(
                data["value"]
            )
        )
    else:
        out["value"] = {"$unknown": {"name": ""}}
    return out
