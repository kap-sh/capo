"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetStringListFilterCondition``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_string_list_filter_operator
    import capo_quicksight.types.data_set_string_list_filter_value


class DataSetStringListFilterCondition(TypedDict, closed=True):
    operator: "capo_quicksight.types.data_set_string_list_filter_operator.DataSetStringListFilterOperator"
    """<p>The list operator to use, either <code>INCLUDE</code> to match values in the list or <code>EXCLUDE</code> to filter out values in the list.</p>"""
    values: NotRequired[
        "capo_quicksight.types.data_set_string_list_filter_value.DataSetStringListFilterValue"
    ]
    """<p>The list of string values to include or exclude in the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetStringListFilterCondition) -> dict:
    out: dict = {}
    import capo_quicksight.types.data_set_string_list_filter_operator

    out["Operator"] = (
        capo_quicksight.types.data_set_string_list_filter_operator.serialize_json(
            value["operator"]
        )
    )
    if "values" in value:
        import capo_quicksight.types.data_set_string_list_filter_value

        out["Values"] = (
            capo_quicksight.types.data_set_string_list_filter_value.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSetStringListFilterCondition:
    out: DataSetStringListFilterCondition = {}  # type: ignore[typeddict-item]
    if data.get("Operator") is not None:
        import capo_quicksight.types.data_set_string_list_filter_operator

        out["operator"] = (
            capo_quicksight.types.data_set_string_list_filter_operator.deserialize_json(
                data["Operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_quicksight.types.data_set_string_list_filter_operator.DataSetStringListFilterOperator",
            "",
        )
    if data.get("Values") is not None:
        import capo_quicksight.types.data_set_string_list_filter_value

        out["values"] = (
            capo_quicksight.types.data_set_string_list_filter_value.deserialize_json(
                data["Values"]
            )
        )
    return out


def redact_sensitive(value: DataSetStringListFilterCondition) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "values" in value:
        import capo_quicksight.types.data_set_string_list_filter_value

        out["values"] = (
            capo_quicksight.types.data_set_string_list_filter_value.redact_sensitive(
                value["values"]
            )
        )
    return out
