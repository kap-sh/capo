"""Generated from Smithy shape ``com.amazonaws.quicksight#TooltipSheetDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.layout_list
    import capo_quicksight.types.sheet_name
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.tooltip_sheet_image_list
    import capo_quicksight.types.tooltip_sheet_text_box_list
    import capo_quicksight.types.tooltip_sheet_visual_list


class TooltipSheetDefinition(TypedDict, closed=True):
    sheet_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The unique identifier of a tooltip sheet.</p>"""
    name: NotRequired["capo_quicksight.types.sheet_name.SheetName"]
    """<p>The name of the tooltip sheet. This name is displayed on the sheet's tab in the Quick console.</p>"""
    visuals: NotRequired[
        "capo_quicksight.types.tooltip_sheet_visual_list.TooltipSheetVisualList"
    ]
    """<p>A list of the visuals that are on a tooltip sheet.</p>"""
    text_boxes: NotRequired[
        "capo_quicksight.types.tooltip_sheet_text_box_list.TooltipSheetTextBoxList"
    ]
    """<p>The text boxes that are on a tooltip sheet.</p>"""
    images: NotRequired[
        "capo_quicksight.types.tooltip_sheet_image_list.TooltipSheetImageList"
    ]
    """<p>A list of images on a tooltip sheet.</p>"""
    layouts: NotRequired["capo_quicksight.types.layout_list.LayoutList"]
    """<p>Layouts define how the components of a tooltip sheet are arranged.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/types-of-layout.html">Types of layout</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TooltipSheetDefinition) -> dict:
    out: dict = {}
    out["SheetId"] = value["sheet_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "visuals" in value:
        import capo_quicksight.types.tooltip_sheet_visual_list

        out["Visuals"] = capo_quicksight.types.tooltip_sheet_visual_list.serialize_json(
            value["visuals"]
        )
    if "text_boxes" in value:
        import capo_quicksight.types.tooltip_sheet_text_box_list

        out["TextBoxes"] = (
            capo_quicksight.types.tooltip_sheet_text_box_list.serialize_json(
                value["text_boxes"]
            )
        )
    if "images" in value:
        import capo_quicksight.types.tooltip_sheet_image_list

        out["Images"] = capo_quicksight.types.tooltip_sheet_image_list.serialize_json(
            value["images"]
        )
    if "layouts" in value:
        import capo_quicksight.types.layout_list

        out["Layouts"] = capo_quicksight.types.layout_list.serialize_json(
            value["layouts"]
        )
    return out


def deserialize_json(data: dict) -> TooltipSheetDefinition:
    out: TooltipSheetDefinition = {}  # type: ignore[typeddict-item]
    if data.get("SheetId") is not None:
        out["sheet_id"] = data["SheetId"]
    else:
        raise DeserializationError("TooltipSheetDefinition.sheet_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Visuals") is not None:
        import capo_quicksight.types.tooltip_sheet_visual_list

        out["visuals"] = (
            capo_quicksight.types.tooltip_sheet_visual_list.deserialize_json(
                data["Visuals"]
            )
        )
    if data.get("TextBoxes") is not None:
        import capo_quicksight.types.tooltip_sheet_text_box_list

        out["text_boxes"] = (
            capo_quicksight.types.tooltip_sheet_text_box_list.deserialize_json(
                data["TextBoxes"]
            )
        )
    if data.get("Images") is not None:
        import capo_quicksight.types.tooltip_sheet_image_list

        out["images"] = capo_quicksight.types.tooltip_sheet_image_list.deserialize_json(
            data["Images"]
        )
    if data.get("Layouts") is not None:
        import capo_quicksight.types.layout_list

        out["layouts"] = capo_quicksight.types.layout_list.deserialize_json(
            data["Layouts"]
        )
    return out
