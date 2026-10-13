"""Generated from Smithy shape ``com.amazonaws.quicksight#HeaderFooterSectionConfigurationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.header_footer_section_configuration

HeaderFooterSectionConfigurationList: TypeAlias = list[
    "capo_quicksight.types.header_footer_section_configuration.HeaderFooterSectionConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: HeaderFooterSectionConfigurationList) -> list:
    import capo_quicksight.types.header_footer_section_configuration

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.header_footer_section_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> HeaderFooterSectionConfigurationList:
    import capo_quicksight.types.header_footer_section_configuration

    out: HeaderFooterSectionConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.header_footer_section_configuration.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: HeaderFooterSectionConfigurationList) -> list[Any]:
    import capo_quicksight.types.header_footer_section_configuration

    return [
        capo_quicksight.types.header_footer_section_configuration.redact_sensitive(item)
        for item in value
    ]
