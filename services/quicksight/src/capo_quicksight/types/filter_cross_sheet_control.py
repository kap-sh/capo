"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterCrossSheetControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.cascading_control_configuration
    import capo_quicksight.types.short_restrictive_resource_id


class FilterCrossSheetControl(TypedDict, closed=True):
    filter_control_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the <code>FilterCrossSheetControl</code>.</p>"""
    source_filter_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The source filter ID of the <code>FilterCrossSheetControl</code>.</p>"""
    cascading_control_configuration: NotRequired[
        "capo_quicksight.types.cascading_control_configuration.CascadingControlConfiguration"
    ]
    """<p>The values that are displayed in a control can be configured to only show values that are valid based on what's selected in other controls.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterCrossSheetControl) -> dict:
    out: dict = {}
    out["FilterControlId"] = value["filter_control_id"]
    out["SourceFilterId"] = value["source_filter_id"]
    if "cascading_control_configuration" in value:
        import capo_quicksight.types.cascading_control_configuration

        out["CascadingControlConfiguration"] = (
            capo_quicksight.types.cascading_control_configuration.serialize_json(
                value["cascading_control_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterCrossSheetControl:
    out: FilterCrossSheetControl = {}  # type: ignore[typeddict-item]
    if data.get("FilterControlId") is not None:
        out["filter_control_id"] = data["FilterControlId"]
    else:
        out["filter_control_id"] = ""
    if data.get("SourceFilterId") is not None:
        out["source_filter_id"] = data["SourceFilterId"]
    else:
        out["source_filter_id"] = ""
    if data.get("CascadingControlConfiguration") is not None:
        import capo_quicksight.types.cascading_control_configuration

        out["cascading_control_configuration"] = (
            capo_quicksight.types.cascading_control_configuration.deserialize_json(
                data["CascadingControlConfiguration"]
            )
        )
    return out
