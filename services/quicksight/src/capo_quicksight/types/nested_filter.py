"""Generated from Smithy shape ``com.amazonaws.quicksight#NestedFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.boolean
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.inner_filter
    import capo_quicksight.types.short_restrictive_resource_id


class NestedFilter(TypedDict, closed=True):
    filter_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>An identifier that uniquely identifies a filter within a dashboard, analysis, or template.</p>"""
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the filter is applied to.</p>"""
    include_inner_set: "capo_quicksight.types.boolean.Boolean"
    """<p>A boolean condition to include or exclude the subset that is defined by the values of the nested inner filter.</p>"""
    inner_filter: "capo_quicksight.types.inner_filter.InnerFilter"
    """<p>The <code>InnerFilter</code> defines the subset of data to be used with the <code>NestedFilter</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NestedFilter) -> dict:
    out: dict = {}
    out["FilterId"] = value["filter_id"]
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    out["IncludeInnerSet"] = value.get("include_inner_set", False)
    import capo_quicksight.types.inner_filter

    out["InnerFilter"] = capo_quicksight.types.inner_filter.serialize_json(
        value["inner_filter"]
    )
    return out


def deserialize_json(data: dict) -> NestedFilter:
    out: NestedFilter = {}  # type: ignore[typeddict-item]
    if data.get("FilterId") is not None:
        out["filter_id"] = data["FilterId"]
    else:
        out["filter_id"] = ""
    if data.get("Column") is not None:
        import capo_quicksight.types.column_identifier

        out["column"] = capo_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("NestedFilter.column required")
    if data.get("IncludeInnerSet") is not None:
        out["include_inner_set"] = data["IncludeInnerSet"]
    else:
        out["include_inner_set"] = False
    if data.get("InnerFilter") is not None:
        import capo_quicksight.types.inner_filter

        out["inner_filter"] = capo_quicksight.types.inner_filter.deserialize_json(
            data["InnerFilter"]
        )
    else:
        raise DeserializationError("NestedFilter.inner_filter required")
    return out
