"""Generated from Smithy shape ``com.amazonaws.deadline#ParameterFilterExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.comparison_operator
    import capo_deadline.types.parameter_value
    import capo_deadline.types.string


class ParameterFilterExpression(TypedDict, closed=True):
    name: "capo_deadline.types.string.String"
    """The name of the parameter to filter on."""
    operator: "capo_deadline.types.comparison_operator.ComparisonOperator"
    """The type of comparison to use to filter results."""
    value: "capo_deadline.types.parameter_value.ParameterValue"
    """The parameter's value."""


# --- restJson1 ser/de ---
def serialize_json(value: ParameterFilterExpression) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_deadline.types.comparison_operator

    out["operator"] = capo_deadline.types.comparison_operator.serialize_json(
        value["operator"]
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ParameterFilterExpression:
    out: ParameterFilterExpression = {}  # type: ignore[typeddict-item]
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
