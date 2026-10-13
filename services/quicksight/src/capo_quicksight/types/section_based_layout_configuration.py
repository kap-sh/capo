"""Generated from Smithy shape ``com.amazonaws.quicksight#SectionBasedLayoutConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.body_section_configuration_list
    import capo_quicksight.types.header_footer_section_configuration_list
    import capo_quicksight.types.section_based_layout_canvas_size_options


class SectionBasedLayoutConfiguration(TypedDict, closed=True):
    header_sections: "capo_quicksight.types.header_footer_section_configuration_list.HeaderFooterSectionConfigurationList"
    """<p>A list of header section configurations.</p>"""
    body_sections: "capo_quicksight.types.body_section_configuration_list.BodySectionConfigurationList"
    """<p>A list of body section configurations.</p>"""
    footer_sections: "capo_quicksight.types.header_footer_section_configuration_list.HeaderFooterSectionConfigurationList"
    """<p>A list of footer section configurations.</p>"""
    canvas_size_options: "capo_quicksight.types.section_based_layout_canvas_size_options.SectionBasedLayoutCanvasSizeOptions"
    """<p>The options for the canvas of a section-based layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SectionBasedLayoutConfiguration) -> dict:
    out: dict = {}
    import capo_quicksight.types.header_footer_section_configuration_list

    out["HeaderSections"] = (
        capo_quicksight.types.header_footer_section_configuration_list.serialize_json(
            value["header_sections"]
        )
    )
    import capo_quicksight.types.body_section_configuration_list

    out["BodySections"] = (
        capo_quicksight.types.body_section_configuration_list.serialize_json(
            value["body_sections"]
        )
    )
    import capo_quicksight.types.header_footer_section_configuration_list

    out["FooterSections"] = (
        capo_quicksight.types.header_footer_section_configuration_list.serialize_json(
            value["footer_sections"]
        )
    )
    import capo_quicksight.types.section_based_layout_canvas_size_options

    out["CanvasSizeOptions"] = (
        capo_quicksight.types.section_based_layout_canvas_size_options.serialize_json(
            value["canvas_size_options"]
        )
    )
    return out


def deserialize_json(data: dict) -> SectionBasedLayoutConfiguration:
    out: SectionBasedLayoutConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("HeaderSections") is not None:
        import capo_quicksight.types.header_footer_section_configuration_list

        out["header_sections"] = (
            capo_quicksight.types.header_footer_section_configuration_list.deserialize_json(
                data["HeaderSections"]
            )
        )
    else:
        raise DeserializationError(
            "SectionBasedLayoutConfiguration.header_sections required"
        )
    if data.get("BodySections") is not None:
        import capo_quicksight.types.body_section_configuration_list

        out["body_sections"] = (
            capo_quicksight.types.body_section_configuration_list.deserialize_json(
                data["BodySections"]
            )
        )
    else:
        raise DeserializationError(
            "SectionBasedLayoutConfiguration.body_sections required"
        )
    if data.get("FooterSections") is not None:
        import capo_quicksight.types.header_footer_section_configuration_list

        out["footer_sections"] = (
            capo_quicksight.types.header_footer_section_configuration_list.deserialize_json(
                data["FooterSections"]
            )
        )
    else:
        raise DeserializationError(
            "SectionBasedLayoutConfiguration.footer_sections required"
        )
    if data.get("CanvasSizeOptions") is not None:
        import capo_quicksight.types.section_based_layout_canvas_size_options

        out["canvas_size_options"] = (
            capo_quicksight.types.section_based_layout_canvas_size_options.deserialize_json(
                data["CanvasSizeOptions"]
            )
        )
    else:
        raise DeserializationError(
            "SectionBasedLayoutConfiguration.canvas_size_options required"
        )
    return out


def redact_sensitive(value: SectionBasedLayoutConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "header_sections" in value:
        import capo_quicksight.types.header_footer_section_configuration_list

        out["header_sections"] = (
            capo_quicksight.types.header_footer_section_configuration_list.redact_sensitive(
                value["header_sections"]
            )
        )
    if "body_sections" in value:
        import capo_quicksight.types.body_section_configuration_list

        out["body_sections"] = (
            capo_quicksight.types.body_section_configuration_list.redact_sensitive(
                value["body_sections"]
            )
        )
    if "footer_sections" in value:
        import capo_quicksight.types.header_footer_section_configuration_list

        out["footer_sections"] = (
            capo_quicksight.types.header_footer_section_configuration_list.redact_sensitive(
                value["footer_sections"]
            )
        )
    return out
