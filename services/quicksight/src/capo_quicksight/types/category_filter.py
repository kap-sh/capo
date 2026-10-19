"""Generated from Smithy shape ``com.amazonaws.quicksight#CategoryFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.category_filter_configuration
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.default_filter_control_configuration
    import capo_quicksight.types.short_restrictive_resource_id


class CategoryFilter(TypedDict, closed=True):
    filter_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>An identifier that uniquely identifies a filter within a dashboard, analysis, or template.</p>"""
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the filter is applied to.</p>"""
    configuration: "capo_quicksight.types.category_filter_configuration.CategoryFilterConfiguration"
    """<p>The configuration for a <code>CategoryFilter</code>.</p>"""
    default_filter_control_configuration: NotRequired[
        "capo_quicksight.types.default_filter_control_configuration.DefaultFilterControlConfiguration"
    ]
    """<p>The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CategoryFilter) -> dict:
    out: dict = {}
    out["FilterId"] = value["filter_id"]
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    import capo_quicksight.types.category_filter_configuration

    out["Configuration"] = (
        capo_quicksight.types.category_filter_configuration.serialize_json(
            value["configuration"]
        )
    )
    if "default_filter_control_configuration" in value:
        import capo_quicksight.types.default_filter_control_configuration

        out["DefaultFilterControlConfiguration"] = (
            capo_quicksight.types.default_filter_control_configuration.serialize_json(
                value["default_filter_control_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CategoryFilter:
    out: CategoryFilter = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("CategoryFilter.column required")
    if data.get("Configuration") is not None:
        import capo_quicksight.types.category_filter_configuration

        out["configuration"] = (
            capo_quicksight.types.category_filter_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    else:
        raise DeserializationError("CategoryFilter.configuration required")
    if data.get("DefaultFilterControlConfiguration") is not None:
        import capo_quicksight.types.default_filter_control_configuration

        out["default_filter_control_configuration"] = (
            capo_quicksight.types.default_filter_control_configuration.deserialize_json(
                data["DefaultFilterControlConfiguration"]
            )
        )
    return out
