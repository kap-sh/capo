"""Generated from Smithy shape ``com.amazonaws.qconnect#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.filter_field
    import capo_qconnect.types.filter_operator
    import capo_qconnect.types.non_empty_string


class Filter(TypedDict, closed=True):
    field: "capo_qconnect.types.filter_field.FilterField"
    """<p>The field on which to filter.</p>"""
    operator: "capo_qconnect.types.filter_operator.FilterOperator"
    """<p>The operator to use for comparing the field’s value with the provided value.</p>"""
    value: "capo_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The desired field value on which to filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    out["field"] = value["field"]
    out["operator"] = value["operator"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("field") is not None:
        out["field"] = data["field"]
    else:
        out["field"] = ""
    if data.get("operator") is not None:
        out["operator"] = data["operator"]
    else:
        out["operator"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
