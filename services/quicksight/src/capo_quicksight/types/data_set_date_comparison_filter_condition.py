"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetDateComparisonFilterCondition``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_date_comparison_filter_operator
    import capo_quicksight.types.data_set_date_filter_value


class DataSetDateComparisonFilterCondition(TypedDict, closed=True):
    operator: "capo_quicksight.types.data_set_date_comparison_filter_operator.DataSetDateComparisonFilterOperator"
    """<p>The comparison operator to use, such as <code>BEFORE</code>, <code>BEFORE_OR_EQUALS_TO</code>, <code>AFTER</code>, or <code>AFTER_OR_EQUALS_TO</code>.</p>"""
    value: NotRequired[
        "capo_quicksight.types.data_set_date_filter_value.DataSetDateFilterValue"
    ]
    """<p>The date value to compare against.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetDateComparisonFilterCondition) -> dict:
    out: dict = {}
    import capo_quicksight.types.data_set_date_comparison_filter_operator

    out["Operator"] = (
        capo_quicksight.types.data_set_date_comparison_filter_operator.serialize_json(
            value["operator"]
        )
    )
    if "value" in value:
        import capo_quicksight.types.data_set_date_filter_value

        out["Value"] = capo_quicksight.types.data_set_date_filter_value.serialize_json(
            value["value"]
        )
    return out


def deserialize_json(data: dict) -> DataSetDateComparisonFilterCondition:
    out: DataSetDateComparisonFilterCondition = {}  # type: ignore[typeddict-item]
    if data.get("Operator") is not None:
        import capo_quicksight.types.data_set_date_comparison_filter_operator

        out["operator"] = (
            capo_quicksight.types.data_set_date_comparison_filter_operator.deserialize_json(
                data["Operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_quicksight.types.data_set_date_comparison_filter_operator.DataSetDateComparisonFilterOperator",
            "",
        )
    if data.get("Value") is not None:
        import capo_quicksight.types.data_set_date_filter_value

        out["value"] = (
            capo_quicksight.types.data_set_date_filter_value.deserialize_json(
                data["Value"]
            )
        )
    return out


def redact_sensitive(value: DataSetDateComparisonFilterCondition) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        import capo_quicksight.types.data_set_date_filter_value

        out["value"] = (
            capo_quicksight.types.data_set_date_filter_value.redact_sensitive(
                value["value"]
            )
        )
    return out
