"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryMetadataFilterExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.memory_record_left_expression
    import capo_bedrock_agentcore.types.memory_record_operator_type
    import capo_bedrock_agentcore.types.memory_record_right_expression


class MemoryMetadataFilterExpression(TypedDict, closed=True):
    left: "capo_bedrock_agentcore.types.memory_record_left_expression.MemoryRecordLeftExpression"
    """<p>The metadata key to evaluate.</p>"""
    operator: "capo_bedrock_agentcore.types.memory_record_operator_type.MemoryRecordOperatorType"
    """<p>The relationship between the metadata key and value to match when applying the metadata filter.</p>"""
    right: NotRequired[
        "capo_bedrock_agentcore.types.memory_record_right_expression.MemoryRecordRightExpression"
    ]
    """<p>The value to compare against. Required for all operators except EXISTS and NOT_EXISTS.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemoryMetadataFilterExpression) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.memory_record_left_expression

    out["left"] = (
        capo_bedrock_agentcore.types.memory_record_left_expression.serialize_json(
            value["left"]
        )
    )
    import capo_bedrock_agentcore.types.memory_record_operator_type

    out["operator"] = (
        capo_bedrock_agentcore.types.memory_record_operator_type.serialize_json(
            value["operator"]
        )
    )
    if "right" in value:
        import capo_bedrock_agentcore.types.memory_record_right_expression

        out["right"] = (
            capo_bedrock_agentcore.types.memory_record_right_expression.serialize_json(
                value["right"]
            )
        )
    return out


def deserialize_json(data: dict) -> MemoryMetadataFilterExpression:
    out: MemoryMetadataFilterExpression = {}  # type: ignore[typeddict-item]
    if data.get("left") is not None:
        import capo_bedrock_agentcore.types.memory_record_left_expression

        out["left"] = (
            capo_bedrock_agentcore.types.memory_record_left_expression.deserialize_json(
                data["left"]
            )
        )
    else:
        import capo_bedrock_agentcore.types._unknown

        out["left"] = capo_bedrock_agentcore.types._unknown.UnknownUnionMember("")
    if data.get("operator") is not None:
        import capo_bedrock_agentcore.types.memory_record_operator_type

        out["operator"] = (
            capo_bedrock_agentcore.types.memory_record_operator_type.deserialize_json(
                data["operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_bedrock_agentcore.types.memory_record_operator_type.MemoryRecordOperatorType",
            "",
        )
    if data.get("right") is not None:
        import capo_bedrock_agentcore.types.memory_record_right_expression

        out["right"] = (
            capo_bedrock_agentcore.types.memory_record_right_expression.deserialize_json(
                data["right"]
            )
        )
    return out
