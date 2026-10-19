"""Generated from Smithy shape ``com.amazonaws.quicksight#CategoryDrillDownFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.category_value_list
    import capo_quicksight.types.column_identifier


class CategoryDrillDownFilter(TypedDict, closed=True):
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the filter is applied to.</p>"""
    category_values: "capo_quicksight.types.category_value_list.CategoryValueList"
    """<p>A list of the string inputs that are the values of the category drill down filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CategoryDrillDownFilter) -> dict:
    out: dict = {}
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    import capo_quicksight.types.category_value_list

    out["CategoryValues"] = capo_quicksight.types.category_value_list.serialize_json(
        value["category_values"]
    )
    return out


def deserialize_json(data: dict) -> CategoryDrillDownFilter:
    out: CategoryDrillDownFilter = {}  # type: ignore[typeddict-item]
    if data.get("Column") is not None:
        import capo_quicksight.types.column_identifier

        out["column"] = capo_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("CategoryDrillDownFilter.column required")
    if data.get("CategoryValues") is not None:
        import capo_quicksight.types.category_value_list

        out["category_values"] = (
            capo_quicksight.types.category_value_list.deserialize_json(
                data["CategoryValues"]
            )
        )
    else:
        out["category_values"] = []
    return out
