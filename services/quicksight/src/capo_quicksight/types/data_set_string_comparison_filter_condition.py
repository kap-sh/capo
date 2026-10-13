"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetStringComparisonFilterCondition``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_string_comparison_filter_operator
    import capo_quicksight.types.data_set_string_filter_value


class DataSetStringComparisonFilterCondition(TypedDict, closed=True):
    operator: "capo_quicksight.types.data_set_string_comparison_filter_operator.DataSetStringComparisonFilterOperator"
    """<p>The comparison operator to use, such as <code>EQUALS</code>, <code>CONTAINS</code>, <code>STARTS_WITH</code>, <code>ENDS_WITH</code>, or their negations.</p>"""
    value: NotRequired[
        "capo_quicksight.types.data_set_string_filter_value.DataSetStringFilterValue"
    ]
    """<p>The string value to compare against.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetStringComparisonFilterCondition) -> dict:
    out: dict = {}
    import capo_quicksight.types.data_set_string_comparison_filter_operator

    out["Operator"] = (
        capo_quicksight.types.data_set_string_comparison_filter_operator.serialize_json(
            value["operator"]
        )
    )
    if "value" in value:
        import capo_quicksight.types.data_set_string_filter_value

        out["Value"] = (
            capo_quicksight.types.data_set_string_filter_value.serialize_json(
                value["value"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSetStringComparisonFilterCondition:
    out: DataSetStringComparisonFilterCondition = {}  # type: ignore[typeddict-item]
    if data.get("Operator") is not None:
        import capo_quicksight.types.data_set_string_comparison_filter_operator

        out["operator"] = (
            capo_quicksight.types.data_set_string_comparison_filter_operator.deserialize_json(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError(
            "DataSetStringComparisonFilterCondition.operator required"
        )
    if data.get("Value") is not None:
        import capo_quicksight.types.data_set_string_filter_value

        out["value"] = (
            capo_quicksight.types.data_set_string_filter_value.deserialize_json(
                data["Value"]
            )
        )
    return out


def redact_sensitive(value: DataSetStringComparisonFilterCondition) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        import capo_quicksight.types.data_set_string_filter_value

        out["value"] = (
            capo_quicksight.types.data_set_string_filter_value.redact_sensitive(
                value["value"]
            )
        )
    return out
