"""Generated from Smithy shape ``com.amazonaws.securityhub#SoftwareList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.software_result

SoftwareList: TypeAlias = list["capo_securityhub.types.software_result.SoftwareResult"]


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareList) -> list:
    import capo_securityhub.types.software_result

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.software_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> SoftwareList:
    import capo_securityhub.types.software_result

    out: SoftwareList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityhub.types.software_result.deserialize_json(item))
    return out
