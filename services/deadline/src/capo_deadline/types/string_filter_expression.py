"""Generated from Smithy shape ``com.amazonaws.deadline#StringFilterExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.comparison_operator
    import capo_deadline.types.string
    import capo_deadline.types.string_filter


class StringFilterExpression(TypedDict, closed=True):
    name: "capo_deadline.types.string.String"
    """The field name to search."""
    operator: "capo_deadline.types.comparison_operator.ComparisonOperator"
    """The type of comparison to use for this search."""
    value: "capo_deadline.types.string_filter.StringFilter"
    """The string to search for."""


# --- restJson1 ser/de ---
def serialize_json(value: StringFilterExpression) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_deadline.types.comparison_operator

    out["operator"] = capo_deadline.types.comparison_operator.serialize_json(
        value["operator"]
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> StringFilterExpression:
    out: StringFilterExpression = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("operator") is not None:
        import capo_deadline.types.comparison_operator

        out["operator"] = capo_deadline.types.comparison_operator.deserialize_json(
            data["operator"]
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_deadline.types.comparison_operator.ComparisonOperator", ""
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
