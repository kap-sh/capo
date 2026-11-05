"""Generated from Smithy shape ``com.amazonaws.securityhub#SoftwareCompositeFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.software_composite_filter

SoftwareCompositeFilterList: TypeAlias = list[
    "capo_securityhub.types.software_composite_filter.SoftwareCompositeFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareCompositeFilterList) -> list:
    import capo_securityhub.types.software_composite_filter

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.software_composite_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SoftwareCompositeFilterList:
    import capo_securityhub.types.software_composite_filter

    out: SoftwareCompositeFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityhub.types.software_composite_filter.deserialize_json(item)
        )
    return out
