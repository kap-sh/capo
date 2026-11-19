"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#FilterParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.filter_operator
    import capo_networkflowmonitor.types.filter_values


class FilterParameter(TypedDict, closed=True):
    field: "str"
    """<p>The name of the field that you want to filter on. The fields that you can specify depend on the type of query.</p>"""
    operator: "capo_networkflowmonitor.types.filter_operator.FilterOperator"
    """<p>The operator to use to compare the field with the values that you specify. The operator can be one of the following</p> <ul> <li> <p> <code>EQUALS</code>: The field matches a single value.</p> </li> <li> <p> <code>NOT_EQUALS</code>: The field doesn't match a single value.</p> </li> <li> <p> <code>IN</code>: The field matches any one of several values.</p> </li> <li> <p> <code>CONTAINS</code>: The field contains a value.</p> </li> </ul>"""
    values: "capo_networkflowmonitor.types.filter_values.FilterValues"
    """<p>The values to compare the field with.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterParameter) -> dict:
    out: dict = {}
    out["field"] = value["field"]
    import capo_networkflowmonitor.types.filter_operator

    out["operator"] = capo_networkflowmonitor.types.filter_operator.serialize_json(
        value["operator"]
    )
    import capo_networkflowmonitor.types.filter_values

    out["values"] = capo_networkflowmonitor.types.filter_values.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> FilterParameter:
    out: FilterParameter = {}  # type: ignore[typeddict-item]
    if data.get("field") is not None:
        out["field"] = data["field"]
    else:
        out["field"] = ""
    if data.get("operator") is not None:
        import capo_networkflowmonitor.types.filter_operator

        out["operator"] = (
            capo_networkflowmonitor.types.filter_operator.deserialize_json(
                data["operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_networkflowmonitor.types.filter_operator.FilterOperator", ""
        )
    if data.get("values") is not None:
        import capo_networkflowmonitor.types.filter_values

        out["values"] = capo_networkflowmonitor.types.filter_values.deserialize_json(
            data["values"]
        )
    else:
        out["values"] = []
    return out
