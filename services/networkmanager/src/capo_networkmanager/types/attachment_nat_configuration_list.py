"""Generated from Smithy shape ``com.amazonaws.networkmanager#AttachmentNatConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment_nat_configuration

AttachmentNatConfigurationList: TypeAlias = list[
    "capo_networkmanager.types.attachment_nat_configuration.AttachmentNatConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentNatConfigurationList) -> list:
    import capo_networkmanager.types.attachment_nat_configuration

    out: list = []
    for item in value:
        out.append(
            capo_networkmanager.types.attachment_nat_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AttachmentNatConfigurationList:
    import capo_networkmanager.types.attachment_nat_configuration

    out: AttachmentNatConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_networkmanager.types.attachment_nat_configuration.deserialize_json(
                item
            )
        )
    return out
