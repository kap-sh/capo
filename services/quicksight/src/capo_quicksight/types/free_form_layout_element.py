"""Generated from Smithy shape ``com.amazonaws.quicksight#FreeFormLayoutElement``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.border_radius
    import capo_quicksight.types.free_form_layout_element_background_style
    import capo_quicksight.types.free_form_layout_element_border_style
    import capo_quicksight.types.layout_element_type
    import capo_quicksight.types.loading_animation
    import capo_quicksight.types.padding
    import capo_quicksight.types.pixel_length
    import capo_quicksight.types.sheet_element_rendering_rule_list
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.unlimited_pixel_length
    import capo_quicksight.types.visibility


class FreeFormLayoutElement(TypedDict, closed=True):
    element_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>A unique identifier for an element within a free-form layout.</p>"""
    element_type: "capo_quicksight.types.layout_element_type.LayoutElementType"
    """<p>The type of element.</p>"""
    x_axis_location: "capo_quicksight.types.pixel_length.PixelLength"
    """<p>The x-axis coordinate of the element.</p>"""
    y_axis_location: "capo_quicksight.types.unlimited_pixel_length.UnlimitedPixelLength"
    """<p>The y-axis coordinate of the element.</p>"""
    width: "capo_quicksight.types.pixel_length.PixelLength"
    """<p>The width of an element within a free-form layout.</p>"""
    height: "capo_quicksight.types.pixel_length.PixelLength"
    """<p>The height of an element within a free-form layout.</p>"""
    visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The visibility of an element within a free-form layout.</p>"""
    rendering_rules: NotRequired[
        "capo_quicksight.types.sheet_element_rendering_rule_list.SheetElementRenderingRuleList"
    ]
    """<p>The rendering rules that determine when an element should be displayed within a free-form layout.</p>"""
    border_style: NotRequired[
        "capo_quicksight.types.free_form_layout_element_border_style.FreeFormLayoutElementBorderStyle"
    ]
    """<p>The border style configuration of a free-form layout element.</p>"""
    selected_border_style: NotRequired[
        "capo_quicksight.types.free_form_layout_element_border_style.FreeFormLayoutElementBorderStyle"
    ]
    """<p>The border style configuration of a free-form layout element. This border style is used when the element is selected.</p>"""
    background_style: NotRequired[
        "capo_quicksight.types.free_form_layout_element_background_style.FreeFormLayoutElementBackgroundStyle"
    ]
    """<p>The background style configuration of a free-form layout element.</p>"""
    loading_animation: NotRequired[
        "capo_quicksight.types.loading_animation.LoadingAnimation"
    ]
    """<p>The loading animation configuration of a free-form layout element.</p>"""
    border_radius: NotRequired["capo_quicksight.types.border_radius.BorderRadius"]
    """<p>The border radius of a free-form layout element.</p>"""
    padding: NotRequired["capo_quicksight.types.padding.Padding"]
    """<p>The padding of a free-form layout element.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FreeFormLayoutElement) -> dict:
    out: dict = {}
    out["ElementId"] = value["element_id"]
    import capo_quicksight.types.layout_element_type

    out["ElementType"] = capo_quicksight.types.layout_element_type.serialize_json(
        value["element_type"]
    )
    out["XAxisLocation"] = value["x_axis_location"]
    out["YAxisLocation"] = value["y_axis_location"]
    out["Width"] = value["width"]
    out["Height"] = value["height"]
    if "visibility" in value:
        import capo_quicksight.types.visibility

        out["Visibility"] = capo_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "rendering_rules" in value:
        import capo_quicksight.types.sheet_element_rendering_rule_list

        out["RenderingRules"] = (
            capo_quicksight.types.sheet_element_rendering_rule_list.serialize_json(
                value["rendering_rules"]
            )
        )
    if "border_style" in value:
        import capo_quicksight.types.free_form_layout_element_border_style

        out["BorderStyle"] = (
            capo_quicksight.types.free_form_layout_element_border_style.serialize_json(
                value["border_style"]
            )
        )
    if "selected_border_style" in value:
        import capo_quicksight.types.free_form_layout_element_border_style

        out["SelectedBorderStyle"] = (
            capo_quicksight.types.free_form_layout_element_border_style.serialize_json(
                value["selected_border_style"]
            )
        )
    if "background_style" in value:
        import capo_quicksight.types.free_form_layout_element_background_style

        out["BackgroundStyle"] = (
            capo_quicksight.types.free_form_layout_element_background_style.serialize_json(
                value["background_style"]
            )
        )
    if "loading_animation" in value:
        import capo_quicksight.types.loading_animation

        out["LoadingAnimation"] = (
            capo_quicksight.types.loading_animation.serialize_json(
                value["loading_animation"]
            )
        )
    if "border_radius" in value:
        out["BorderRadius"] = value["border_radius"]
    if "padding" in value:
        out["Padding"] = value["padding"]
    return out


def deserialize_json(data: dict) -> FreeFormLayoutElement:
    out: FreeFormLayoutElement = {}  # type: ignore[typeddict-item]
    if data.get("ElementId") is not None:
        out["element_id"] = data["ElementId"]
    else:
        raise DeserializationError("FreeFormLayoutElement.element_id required")
    if data.get("ElementType") is not None:
        import capo_quicksight.types.layout_element_type

        out["element_type"] = (
            capo_quicksight.types.layout_element_type.deserialize_json(
                data["ElementType"]
            )
        )
    else:
        raise DeserializationError("FreeFormLayoutElement.element_type required")
    if data.get("XAxisLocation") is not None:
        out["x_axis_location"] = data["XAxisLocation"]
    else:
        raise DeserializationError("FreeFormLayoutElement.x_axis_location required")
    if data.get("YAxisLocation") is not None:
        out["y_axis_location"] = data["YAxisLocation"]
    else:
        raise DeserializationError("FreeFormLayoutElement.y_axis_location required")
    if data.get("Width") is not None:
        out["width"] = data["Width"]
    else:
        raise DeserializationError("FreeFormLayoutElement.width required")
    if data.get("Height") is not None:
        out["height"] = data["Height"]
    else:
        raise DeserializationError("FreeFormLayoutElement.height required")
    if data.get("Visibility") is not None:
        import capo_quicksight.types.visibility

        out["visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if data.get("RenderingRules") is not None:
        import capo_quicksight.types.sheet_element_rendering_rule_list

        out["rendering_rules"] = (
            capo_quicksight.types.sheet_element_rendering_rule_list.deserialize_json(
                data["RenderingRules"]
            )
        )
    if data.get("BorderStyle") is not None:
        import capo_quicksight.types.free_form_layout_element_border_style

        out["border_style"] = (
            capo_quicksight.types.free_form_layout_element_border_style.deserialize_json(
                data["BorderStyle"]
            )
        )
    if data.get("SelectedBorderStyle") is not None:
        import capo_quicksight.types.free_form_layout_element_border_style

        out["selected_border_style"] = (
            capo_quicksight.types.free_form_layout_element_border_style.deserialize_json(
                data["SelectedBorderStyle"]
            )
        )
    if data.get("BackgroundStyle") is not None:
        import capo_quicksight.types.free_form_layout_element_background_style

        out["background_style"] = (
            capo_quicksight.types.free_form_layout_element_background_style.deserialize_json(
                data["BackgroundStyle"]
            )
        )
    if data.get("LoadingAnimation") is not None:
        import capo_quicksight.types.loading_animation

        out["loading_animation"] = (
            capo_quicksight.types.loading_animation.deserialize_json(
                data["LoadingAnimation"]
            )
        )
    if data.get("BorderRadius") is not None:
        out["border_radius"] = data["BorderRadius"]
    if data.get("Padding") is not None:
        out["padding"] = data["Padding"]
    return out


def redact_sensitive(value: FreeFormLayoutElement) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "rendering_rules" in value:
        import capo_quicksight.types.sheet_element_rendering_rule_list

        out["rendering_rules"] = (
            capo_quicksight.types.sheet_element_rendering_rule_list.redact_sensitive(
                value["rendering_rules"]
            )
        )
    return out
