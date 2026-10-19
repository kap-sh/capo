"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EventMetadataFilterExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.left_expression
    import capo_bedrock_agentcore.types.operator_type
    import capo_bedrock_agentcore.types.right_expression


class EventMetadataFilterExpression(TypedDict, closed=True):
    left: "capo_bedrock_agentcore.types.left_expression.LeftExpression"
    """<p>Left operand of the event metadata filter expression.</p>"""
    operator: "capo_bedrock_agentcore.types.operator_type.OperatorType"
    """<p>Operator applied to the event metadata filter expression.</p>"""
    right: NotRequired["capo_bedrock_agentcore.types.right_expression.RightExpression"]
    """<p>Right operand of the event metadata filter expression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventMetadataFilterExpression) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.left_expression

    out["left"] = capo_bedrock_agentcore.types.left_expression.serialize_json(
        value["left"]
    )
    import capo_bedrock_agentcore.types.operator_type

    out["operator"] = capo_bedrock_agentcore.types.operator_type.serialize_json(
        value["operator"]
    )
    if "right" in value:
        import capo_bedrock_agentcore.types.right_expression

        out["right"] = capo_bedrock_agentcore.types.right_expression.serialize_json(
            value["right"]
        )
    return out


def deserialize_json(data: dict) -> EventMetadataFilterExpression:
    out: EventMetadataFilterExpression = {}  # type: ignore[typeddict-item]
    if data.get("left") is not None:
        import capo_bedrock_agentcore.types.left_expression

        out["left"] = capo_bedrock_agentcore.types.left_expression.deserialize_json(
            data["left"]
        )
    else:
        import capo_bedrock_agentcore.types._unknown

        out["left"] = capo_bedrock_agentcore.types._unknown.UnknownUnionMember("")
    if data.get("operator") is not None:
        import capo_bedrock_agentcore.types.operator_type

        out["operator"] = capo_bedrock_agentcore.types.operator_type.deserialize_json(
            data["operator"]
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_bedrock_agentcore.types.operator_type.OperatorType", ""
        )
    if data.get("right") is not None:
        import capo_bedrock_agentcore.types.right_expression

        out["right"] = capo_bedrock_agentcore.types.right_expression.deserialize_json(
            data["right"]
        )
    return out
