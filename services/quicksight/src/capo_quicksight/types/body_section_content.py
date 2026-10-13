"""Generated from Smithy shape ``com.amazonaws.quicksight#BodySectionContent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.section_layout_configuration


class BodySectionContent(TypedDict, closed=True):
    layout: NotRequired[
        "capo_quicksight.types.section_layout_configuration.SectionLayoutConfiguration"
    ]
    """<p>The layout configuration of a body section.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BodySectionContent) -> dict:
    out: dict = {}
    if "layout" in value:
        import capo_quicksight.types.section_layout_configuration

        out["Layout"] = (
            capo_quicksight.types.section_layout_configuration.serialize_json(
                value["layout"]
            )
        )
    return out


def deserialize_json(data: dict) -> BodySectionContent:
    out: BodySectionContent = {}  # type: ignore[typeddict-item]
    if data.get("Layout") is not None:
        import capo_quicksight.types.section_layout_configuration

        out["layout"] = (
            capo_quicksight.types.section_layout_configuration.deserialize_json(
                data["Layout"]
            )
        )
    return out


def redact_sensitive(value: BodySectionContent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "layout" in value:
        import capo_quicksight.types.section_layout_configuration

        out["layout"] = (
            capo_quicksight.types.section_layout_configuration.redact_sensitive(
                value["layout"]
            )
        )
    return out
