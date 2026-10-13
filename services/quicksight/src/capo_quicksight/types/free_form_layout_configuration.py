"""Generated from Smithy shape ``com.amazonaws.quicksight#FreeFormLayoutConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.free_form_layout_canvas_size_options
    import capo_quicksight.types.free_from_layout_element_list
    import capo_quicksight.types.sheet_layout_group_list


class FreeFormLayoutConfiguration(TypedDict, closed=True):
    elements: (
        "capo_quicksight.types.free_from_layout_element_list.FreeFromLayoutElementList"
    )
    """<p>The elements that are included in a free-form layout.</p>"""
    canvas_size_options: NotRequired[
        "capo_quicksight.types.free_form_layout_canvas_size_options.FreeFormLayoutCanvasSizeOptions"
    ]
    groups: NotRequired[
        "capo_quicksight.types.sheet_layout_group_list.SheetLayoutGroupList"
    ]
    """<p>The groups that are included in a free-form layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FreeFormLayoutConfiguration) -> dict:
    out: dict = {}
    import capo_quicksight.types.free_from_layout_element_list

    out["Elements"] = (
        capo_quicksight.types.free_from_layout_element_list.serialize_json(
            value["elements"]
        )
    )
    if "canvas_size_options" in value:
        import capo_quicksight.types.free_form_layout_canvas_size_options

        out["CanvasSizeOptions"] = (
            capo_quicksight.types.free_form_layout_canvas_size_options.serialize_json(
                value["canvas_size_options"]
            )
        )
    if "groups" in value:
        import capo_quicksight.types.sheet_layout_group_list

        out["Groups"] = capo_quicksight.types.sheet_layout_group_list.serialize_json(
            value["groups"]
        )
    return out


def deserialize_json(data: dict) -> FreeFormLayoutConfiguration:
    out: FreeFormLayoutConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Elements") is not None:
        import capo_quicksight.types.free_from_layout_element_list

        out["elements"] = (
            capo_quicksight.types.free_from_layout_element_list.deserialize_json(
                data["Elements"]
            )
        )
    else:
        raise DeserializationError("FreeFormLayoutConfiguration.elements required")
    if data.get("CanvasSizeOptions") is not None:
        import capo_quicksight.types.free_form_layout_canvas_size_options

        out["canvas_size_options"] = (
            capo_quicksight.types.free_form_layout_canvas_size_options.deserialize_json(
                data["CanvasSizeOptions"]
            )
        )
    if data.get("Groups") is not None:
        import capo_quicksight.types.sheet_layout_group_list

        out["groups"] = capo_quicksight.types.sheet_layout_group_list.deserialize_json(
            data["Groups"]
        )
    return out


def redact_sensitive(value: FreeFormLayoutConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "elements" in value:
        import capo_quicksight.types.free_from_layout_element_list

        out["elements"] = (
            capo_quicksight.types.free_from_layout_element_list.redact_sensitive(
                value["elements"]
            )
        )
    return out
