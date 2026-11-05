"""Generated from Smithy shape ``com.amazonaws.securityhub#SoftwareResourceResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.software_resource_result

SoftwareResourceResultList: TypeAlias = list[
    "capo_securityhub.types.software_resource_result.SoftwareResourceResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareResourceResultList) -> list:
    import capo_securityhub.types.software_resource_result

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.software_resource_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> SoftwareResourceResultList:
    import capo_securityhub.types.software_resource_result

    out: SoftwareResourceResultList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityhub.types.software_resource_result.deserialize_json(item)
        )
    return out
