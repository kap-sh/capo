"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetVisualScopingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.filter_visual_scope
    import capo_quicksight.types.filtered_visuals_list
    import capo_quicksight.types.short_restrictive_resource_id


class SheetVisualScopingConfiguration(TypedDict, closed=True):
    sheet_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The selected sheet that the filter is applied to.</p>"""
    scope: "capo_quicksight.types.filter_visual_scope.FilterVisualScope"
    """<p>The scope of the applied entities. Choose one of the following options:</p> <ul> <li> <p> <code>ALL_VISUALS</code> </p> </li> <li> <p> <code>SELECTED_VISUALS</code> </p> </li> </ul>"""
    visual_ids: NotRequired[
        "capo_quicksight.types.filtered_visuals_list.FilteredVisualsList"
    ]
    """<p>The selected visuals that the filter is applied to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetVisualScopingConfiguration) -> dict:
    out: dict = {}
    out["SheetId"] = value["sheet_id"]
    import capo_quicksight.types.filter_visual_scope

    out["Scope"] = capo_quicksight.types.filter_visual_scope.serialize_json(
        value["scope"]
    )
    if "visual_ids" in value:
        import capo_quicksight.types.filtered_visuals_list

        out["VisualIds"] = capo_quicksight.types.filtered_visuals_list.serialize_json(
            value["visual_ids"]
        )
    return out


def deserialize_json(data: dict) -> SheetVisualScopingConfiguration:
    out: SheetVisualScopingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SheetId") is not None:
        out["sheet_id"] = data["SheetId"]
    else:
        out["sheet_id"] = ""
    if data.get("Scope") is not None:
        import capo_quicksight.types.filter_visual_scope

        out["scope"] = capo_quicksight.types.filter_visual_scope.deserialize_json(
            data["Scope"]
        )
    else:
        import typing

        out["scope"] = typing.cast(
            "capo_quicksight.types.filter_visual_scope.FilterVisualScope", ""
        )
    if data.get("VisualIds") is not None:
        import capo_quicksight.types.filtered_visuals_list

        out["visual_ids"] = (
            capo_quicksight.types.filtered_visuals_list.deserialize_json(
                data["VisualIds"]
            )
        )
    return out
