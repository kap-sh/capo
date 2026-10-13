"""Generated from Smithy shape ``com.amazonaws.quicksight#BodySectionConfigurationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.body_section_configuration

BodySectionConfigurationList: TypeAlias = list[
    "capo_quicksight.types.body_section_configuration.BodySectionConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: BodySectionConfigurationList) -> list:
    import capo_quicksight.types.body_section_configuration

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.body_section_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BodySectionConfigurationList:
    import capo_quicksight.types.body_section_configuration

    out: BodySectionConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.body_section_configuration.deserialize_json(item)
        )
    return out


def redact_sensitive(value: BodySectionConfigurationList) -> list[Any]:
    import capo_quicksight.types.body_section_configuration

    return [
        capo_quicksight.types.body_section_configuration.redact_sensitive(item)
        for item in value
    ]
