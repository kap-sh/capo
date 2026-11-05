"""Generated from Smithy shape ``com.amazonaws.securityhub#SoftwareStringFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.software_string_filter

SoftwareStringFilterList: TypeAlias = list[
    "capo_securityhub.types.software_string_filter.SoftwareStringFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareStringFilterList) -> list:
    import capo_securityhub.types.software_string_filter

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.software_string_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> SoftwareStringFilterList:
    import capo_securityhub.types.software_string_filter

    out: SoftwareStringFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityhub.types.software_string_filter.deserialize_json(item))
    return out
