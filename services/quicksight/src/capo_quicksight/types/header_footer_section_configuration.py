"""Generated from Smithy shape ``com.amazonaws.quicksight#HeaderFooterSectionConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.section_layout_configuration
    import capo_quicksight.types.section_style
    import capo_quicksight.types.short_restrictive_resource_id


class HeaderFooterSectionConfiguration(TypedDict, closed=True):
    section_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The unique identifier of the header or footer section.</p>"""
    layout: (
        "capo_quicksight.types.section_layout_configuration.SectionLayoutConfiguration"
    )
    """<p>The layout configuration of the header or footer section.</p>"""
    style: NotRequired["capo_quicksight.types.section_style.SectionStyle"]
    """<p>The style options of a header or footer section.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HeaderFooterSectionConfiguration) -> dict:
    out: dict = {}
    out["SectionId"] = value["section_id"]
    import capo_quicksight.types.section_layout_configuration

    out["Layout"] = capo_quicksight.types.section_layout_configuration.serialize_json(
        value["layout"]
    )
    if "style" in value:
        import capo_quicksight.types.section_style

        out["Style"] = capo_quicksight.types.section_style.serialize_json(
            value["style"]
        )
    return out


def deserialize_json(data: dict) -> HeaderFooterSectionConfiguration:
    out: HeaderFooterSectionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SectionId") is not None:
        out["section_id"] = data["SectionId"]
    else:
        out["section_id"] = ""
    if data.get("Layout") is not None:
        import capo_quicksight.types.section_layout_configuration

        out["layout"] = (
            capo_quicksight.types.section_layout_configuration.deserialize_json(
                data["Layout"]
            )
        )
    else:
        raise DeserializationError("HeaderFooterSectionConfiguration.layout required")
    if data.get("Style") is not None:
        import capo_quicksight.types.section_style

        out["style"] = capo_quicksight.types.section_style.deserialize_json(
            data["Style"]
        )
    return out


def redact_sensitive(value: HeaderFooterSectionConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "layout" in value:
        import capo_quicksight.types.section_layout_configuration

        out["layout"] = (
            capo_quicksight.types.section_layout_configuration.redact_sensitive(
                value["layout"]
            )
        )
    return out
