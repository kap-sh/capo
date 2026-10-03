"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.filter_control_list
    import capo_quicksight.types.layout_list
    import capo_quicksight.types.parameter_control_list
    import capo_quicksight.types.sheet_content_type
    import capo_quicksight.types.sheet_control_layout_list
    import capo_quicksight.types.sheet_description
    import capo_quicksight.types.sheet_image_list
    import capo_quicksight.types.sheet_name
    import capo_quicksight.types.sheet_text_box_list
    import capo_quicksight.types.sheet_title
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.visual_custom_action_defaults
    import capo_quicksight.types.visual_list


class SheetDefinition(TypedDict, closed=True):
    sheet_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The unique identifier of a sheet.</p>"""
    title: NotRequired["capo_quicksight.types.sheet_title.SheetTitle"]
    """<p>The title of the sheet.</p>"""
    description: NotRequired["capo_quicksight.types.sheet_description.SheetDescription"]
    """<p>A description of the sheet.</p>"""
    name: NotRequired["capo_quicksight.types.sheet_name.SheetName"]
    """<p>The name of the sheet. This name is displayed on the sheet's tab in the Quick console.</p>"""
    parameter_controls: NotRequired[
        "capo_quicksight.types.parameter_control_list.ParameterControlList"
    ]
    """<p>The list of parameter controls that are on a sheet.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/parameters-controls.html">Using a Control with a Parameter in Amazon Quick Sight</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    filter_controls: NotRequired[
        "capo_quicksight.types.filter_control_list.FilterControlList"
    ]
    """<p>The list of filter controls that are on a sheet.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/filter-controls.html">Adding filter controls to analysis sheets</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    visuals: NotRequired["capo_quicksight.types.visual_list.VisualList"]
    """<p>A list of the visuals that are on a sheet. Visual placement is determined by the layout of the sheet.</p>"""
    text_boxes: NotRequired[
        "capo_quicksight.types.sheet_text_box_list.SheetTextBoxList"
    ]
    """<p>The text boxes that are on a sheet.</p>"""
    images: NotRequired["capo_quicksight.types.sheet_image_list.SheetImageList"]
    """<p>A list of images on a sheet.</p>"""
    layouts: NotRequired["capo_quicksight.types.layout_list.LayoutList"]
    """<p>Layouts define how the components of a sheet are arranged.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/types-of-layout.html">Types of layout</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    sheet_control_layouts: NotRequired[
        "capo_quicksight.types.sheet_control_layout_list.SheetControlLayoutList"
    ]
    """<p>The control layouts of the sheet.</p>"""
    content_type: NotRequired[
        "capo_quicksight.types.sheet_content_type.SheetContentType"
    ]
    """<p>The layout content type of the sheet. Choose one of the following options:</p> <ul> <li> <p> <code>PAGINATED</code>: Creates a sheet for a paginated report.</p> </li> <li> <p> <code>INTERACTIVE</code>: Creates a sheet for an interactive dashboard.</p> </li> </ul>"""
    custom_action_defaults: NotRequired[
        "capo_quicksight.types.visual_custom_action_defaults.VisualCustomActionDefaults"
    ]
    """<p>A list of visual custom actions for the sheet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetDefinition) -> dict:
    out: dict = {}
    out["SheetId"] = value["sheet_id"]
    if "title" in value:
        out["Title"] = value["title"]
    if "description" in value:
        out["Description"] = value["description"]
    if "name" in value:
        out["Name"] = value["name"]
    if "parameter_controls" in value:
        import capo_quicksight.types.parameter_control_list

        out["ParameterControls"] = (
            capo_quicksight.types.parameter_control_list.serialize_json(
                value["parameter_controls"]
            )
        )
    if "filter_controls" in value:
        import capo_quicksight.types.filter_control_list

        out["FilterControls"] = (
            capo_quicksight.types.filter_control_list.serialize_json(
                value["filter_controls"]
            )
        )
    if "visuals" in value:
        import capo_quicksight.types.visual_list

        out["Visuals"] = capo_quicksight.types.visual_list.serialize_json(
            value["visuals"]
        )
    if "text_boxes" in value:
        import capo_quicksight.types.sheet_text_box_list

        out["TextBoxes"] = capo_quicksight.types.sheet_text_box_list.serialize_json(
            value["text_boxes"]
        )
    if "images" in value:
        import capo_quicksight.types.sheet_image_list

        out["Images"] = capo_quicksight.types.sheet_image_list.serialize_json(
            value["images"]
        )
    if "layouts" in value:
        import capo_quicksight.types.layout_list

        out["Layouts"] = capo_quicksight.types.layout_list.serialize_json(
            value["layouts"]
        )
    if "sheet_control_layouts" in value:
        import capo_quicksight.types.sheet_control_layout_list

        out["SheetControlLayouts"] = (
            capo_quicksight.types.sheet_control_layout_list.serialize_json(
                value["sheet_control_layouts"]
            )
        )
    if "content_type" in value:
        import capo_quicksight.types.sheet_content_type

        out["ContentType"] = capo_quicksight.types.sheet_content_type.serialize_json(
            value["content_type"]
        )
    if "custom_action_defaults" in value:
        import capo_quicksight.types.visual_custom_action_defaults

        out["CustomActionDefaults"] = (
            capo_quicksight.types.visual_custom_action_defaults.serialize_json(
                value["custom_action_defaults"]
            )
        )
    return out


def deserialize_json(data: dict) -> SheetDefinition:
    out: SheetDefinition = {}  # type: ignore[typeddict-item]
    if data.get("SheetId") is not None:
        out["sheet_id"] = data["SheetId"]
    else:
        raise DeserializationError("SheetDefinition.sheet_id required")
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ParameterControls") is not None:
        import capo_quicksight.types.parameter_control_list

        out["parameter_controls"] = (
            capo_quicksight.types.parameter_control_list.deserialize_json(
                data["ParameterControls"]
            )
        )
    if data.get("FilterControls") is not None:
        import capo_quicksight.types.filter_control_list

        out["filter_controls"] = (
            capo_quicksight.types.filter_control_list.deserialize_json(
                data["FilterControls"]
            )
        )
    if data.get("Visuals") is not None:
        import capo_quicksight.types.visual_list

        out["visuals"] = capo_quicksight.types.visual_list.deserialize_json(
            data["Visuals"]
        )
    if data.get("TextBoxes") is not None:
        import capo_quicksight.types.sheet_text_box_list

        out["text_boxes"] = capo_quicksight.types.sheet_text_box_list.deserialize_json(
            data["TextBoxes"]
        )
    if data.get("Images") is not None:
        import capo_quicksight.types.sheet_image_list

        out["images"] = capo_quicksight.types.sheet_image_list.deserialize_json(
            data["Images"]
        )
    if data.get("Layouts") is not None:
        import capo_quicksight.types.layout_list

        out["layouts"] = capo_quicksight.types.layout_list.deserialize_json(
            data["Layouts"]
        )
    if data.get("SheetControlLayouts") is not None:
        import capo_quicksight.types.sheet_control_layout_list

        out["sheet_control_layouts"] = (
            capo_quicksight.types.sheet_control_layout_list.deserialize_json(
                data["SheetControlLayouts"]
            )
        )
    if data.get("ContentType") is not None:
        import capo_quicksight.types.sheet_content_type

        out["content_type"] = capo_quicksight.types.sheet_content_type.deserialize_json(
            data["ContentType"]
        )
    if data.get("CustomActionDefaults") is not None:
        import capo_quicksight.types.visual_custom_action_defaults

        out["custom_action_defaults"] = (
            capo_quicksight.types.visual_custom_action_defaults.deserialize_json(
                data["CustomActionDefaults"]
            )
        )
    return out
