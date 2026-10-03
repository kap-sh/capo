"""Generated from Smithy shape ``com.amazonaws.databrew#FilterExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import capo_databrew.types.expression
    import capo_databrew.types.values_map


class FilterExpression(TypedDict, closed=True):
    expression: "capo_databrew.types.expression.Expression"
    """<p>The expression which includes condition names followed by substitution variables, possibly grouped and combined with other conditions. For example, "(starts_with :prefix1 or starts_with :prefix2) and (ends_with :suffix1 or ends_with :suffix2)". Substitution variables should start with ':' symbol.</p>"""
    values_map: "capo_databrew.types.values_map.ValuesMap"
    """<p>The map of substitution variable names to their values used in this filter expression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterExpression) -> dict:
    out: dict = {}
    out["Expression"] = value["expression"]
    import capo_databrew.types.values_map

    out["ValuesMap"] = capo_databrew.types.values_map.serialize_json(
        value["values_map"]
    )
    return out


def deserialize_json(data: dict) -> FilterExpression:
    out: FilterExpression = {}  # type: ignore[typeddict-item]
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    else:
        raise DeserializationError("FilterExpression.expression required")
    if data.get("ValuesMap") is not None:
        import capo_databrew.types.values_map

        out["values_map"] = capo_databrew.types.values_map.deserialize_json(
            data["ValuesMap"]
        )
    else:
        raise DeserializationError("FilterExpression.values_map required")
    return out
