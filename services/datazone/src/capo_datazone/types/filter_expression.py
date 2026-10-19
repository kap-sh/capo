"""Generated from Smithy shape ``com.amazonaws.datazone#FilterExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.filter_expression_type


class FilterExpression(TypedDict, closed=True):
    type: "capo_datazone.types.filter_expression_type.FilterExpressionType"
    """<p>The search filter explresison type.</p>"""
    expression: "str"
    """<p>The search filter expression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterExpression) -> dict:
    out: dict = {}
    import capo_datazone.types.filter_expression_type

    out["type"] = capo_datazone.types.filter_expression_type.serialize_json(
        value["type"]
    )
    out["expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> FilterExpression:
    out: FilterExpression = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_datazone.types.filter_expression_type

        out["type"] = capo_datazone.types.filter_expression_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_datazone.types.filter_expression_type.FilterExpressionType", ""
        )
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    else:
        out["expression"] = ""
    return out
