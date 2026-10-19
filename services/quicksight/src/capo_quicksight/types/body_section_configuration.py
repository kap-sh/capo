"""Generated from Smithy shape ``com.amazonaws.quicksight#BodySectionConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.body_section_content
    import capo_quicksight.types.body_section_repeat_configuration
    import capo_quicksight.types.section_page_break_configuration
    import capo_quicksight.types.section_style
    import capo_quicksight.types.short_restrictive_resource_id


class BodySectionConfiguration(TypedDict, closed=True):
    section_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The unique identifier of a body section.</p>"""
    content: "capo_quicksight.types.body_section_content.BodySectionContent"
    """<p>The configuration of content in a body section.</p>"""
    style: NotRequired["capo_quicksight.types.section_style.SectionStyle"]
    """<p>The style options of a body section.</p>"""
    page_break_configuration: NotRequired[
        "capo_quicksight.types.section_page_break_configuration.SectionPageBreakConfiguration"
    ]
    """<p>The configuration of a page break for a section.</p>"""
    repeat_configuration: NotRequired[
        "capo_quicksight.types.body_section_repeat_configuration.BodySectionRepeatConfiguration"
    ]
    """<p>Describes the configurations that are required to declare a section as repeating.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BodySectionConfiguration) -> dict:
    out: dict = {}
    out["SectionId"] = value["section_id"]
    import capo_quicksight.types.body_section_content

    out["Content"] = capo_quicksight.types.body_section_content.serialize_json(
        value["content"]
    )
    if "style" in value:
        import capo_quicksight.types.section_style

        out["Style"] = capo_quicksight.types.section_style.serialize_json(
            value["style"]
        )
    if "page_break_configuration" in value:
        import capo_quicksight.types.section_page_break_configuration

        out["PageBreakConfiguration"] = (
            capo_quicksight.types.section_page_break_configuration.serialize_json(
                value["page_break_configuration"]
            )
        )
    if "repeat_configuration" in value:
        import capo_quicksight.types.body_section_repeat_configuration

        out["RepeatConfiguration"] = (
            capo_quicksight.types.body_section_repeat_configuration.serialize_json(
                value["repeat_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> BodySectionConfiguration:
    out: BodySectionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SectionId") is not None:
        out["section_id"] = data["SectionId"]
    else:
        out["section_id"] = ""
    if data.get("Content") is not None:
        import capo_quicksight.types.body_section_content

        out["content"] = capo_quicksight.types.body_section_content.deserialize_json(
            data["Content"]
        )
    else:
        raise DeserializationError("BodySectionConfiguration.content required")
    if data.get("Style") is not None:
        import capo_quicksight.types.section_style

        out["style"] = capo_quicksight.types.section_style.deserialize_json(
            data["Style"]
        )
    if data.get("PageBreakConfiguration") is not None:
        import capo_quicksight.types.section_page_break_configuration

        out["page_break_configuration"] = (
            capo_quicksight.types.section_page_break_configuration.deserialize_json(
                data["PageBreakConfiguration"]
            )
        )
    if data.get("RepeatConfiguration") is not None:
        import capo_quicksight.types.body_section_repeat_configuration

        out["repeat_configuration"] = (
            capo_quicksight.types.body_section_repeat_configuration.deserialize_json(
                data["RepeatConfiguration"]
            )
        )
    return out


def redact_sensitive(value: BodySectionConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_quicksight.types.body_section_content

        out["content"] = capo_quicksight.types.body_section_content.redact_sensitive(
            value["content"]
        )
    return out
