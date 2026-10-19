"""Generated from Smithy shape ``com.amazonaws.deadline#StringListFilterExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.comparison_operator
    import capo_deadline.types.string
    import capo_deadline.types.string_filter_list


class StringListFilterExpression(TypedDict, closed=True):
    name: "capo_deadline.types.string.String"
    """<p>The field name to search.</p>"""
    operator: "capo_deadline.types.comparison_operator.ComparisonOperator"
    """<p>The type of comparison to use for this search.</p>"""
    values: "capo_deadline.types.string_filter_list.StringFilterList"
    """<p>The list of string values to search for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringListFilterExpression) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_deadline.types.comparison_operator

    out["operator"] = capo_deadline.types.comparison_operator.serialize_json(
        value["operator"]
    )
    import capo_deadline.types.string_filter_list

    out["values"] = capo_deadline.types.string_filter_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> StringListFilterExpression:
    out: StringListFilterExpression = {}  # type: ignore[typeddict-item]
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
    if data.get("values") is not None:
        import capo_deadline.types.string_filter_list

        out["values"] = capo_deadline.types.string_filter_list.deserialize_json(
            data["values"]
        )
    else:
        out["values"] = []
    return out
