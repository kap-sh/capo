"""Generated from Smithy shape ``com.amazonaws.quicksight#LayoutConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.free_form_layout_configuration
    import capo_quicksight.types.grid_layout_configuration
    import capo_quicksight.types.section_based_layout_configuration


class LayoutConfiguration(TypedDict, closed=True):
    grid_layout: NotRequired[
        "capo_quicksight.types.grid_layout_configuration.GridLayoutConfiguration"
    ]
    """<p>A type of layout that can be used on a sheet. In a grid layout, visuals snap to a grid with standard spacing and alignment. Dashboards are displayed as designed, with options to fit to screen or view at actual size. A grid layout can be configured to behave in one of two ways when the viewport is resized: <code>FIXED</code> or <code>RESPONSIVE</code>.</p>"""
    free_form_layout: NotRequired[
        "capo_quicksight.types.free_form_layout_configuration.FreeFormLayoutConfiguration"
    ]
    """<p>A free-form is optimized for a fixed width and has more control over the exact placement of layout elements.</p>"""
    section_based_layout: NotRequired[
        "capo_quicksight.types.section_based_layout_configuration.SectionBasedLayoutConfiguration"
    ]
    """<p>A section based layout organizes visuals into multiple sections and has customized header, footer and page break.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LayoutConfiguration) -> dict:
    out: dict = {}
    if "grid_layout" in value:
        import capo_quicksight.types.grid_layout_configuration

        out["GridLayout"] = (
            capo_quicksight.types.grid_layout_configuration.serialize_json(
                value["grid_layout"]
            )
        )
    if "free_form_layout" in value:
        import capo_quicksight.types.free_form_layout_configuration

        out["FreeFormLayout"] = (
            capo_quicksight.types.free_form_layout_configuration.serialize_json(
                value["free_form_layout"]
            )
        )
    if "section_based_layout" in value:
        import capo_quicksight.types.section_based_layout_configuration

        out["SectionBasedLayout"] = (
            capo_quicksight.types.section_based_layout_configuration.serialize_json(
                value["section_based_layout"]
            )
        )
    return out


def deserialize_json(data: dict) -> LayoutConfiguration:
    out: LayoutConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("GridLayout") is not None:
        import capo_quicksight.types.grid_layout_configuration

        out["grid_layout"] = (
            capo_quicksight.types.grid_layout_configuration.deserialize_json(
                data["GridLayout"]
            )
        )
    if data.get("FreeFormLayout") is not None:
        import capo_quicksight.types.free_form_layout_configuration

        out["free_form_layout"] = (
            capo_quicksight.types.free_form_layout_configuration.deserialize_json(
                data["FreeFormLayout"]
            )
        )
    if data.get("SectionBasedLayout") is not None:
        import capo_quicksight.types.section_based_layout_configuration

        out["section_based_layout"] = (
            capo_quicksight.types.section_based_layout_configuration.deserialize_json(
                data["SectionBasedLayout"]
            )
        )
    return out


def redact_sensitive(value: LayoutConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "free_form_layout" in value:
        import capo_quicksight.types.free_form_layout_configuration

        out["free_form_layout"] = (
            capo_quicksight.types.free_form_layout_configuration.redact_sensitive(
                value["free_form_layout"]
            )
        )
    if "section_based_layout" in value:
        import capo_quicksight.types.section_based_layout_configuration

        out["section_based_layout"] = (
            capo_quicksight.types.section_based_layout_configuration.redact_sensitive(
                value["section_based_layout"]
            )
        )
    return out
