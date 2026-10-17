"""Generated from Smithy shape ``com.amazonaws.securityhub#CriticalitySourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.criticality_source

CriticalitySourceList: TypeAlias = list[
    "capo_securityhub.types.criticality_source.CriticalitySource"
]


# --- restJson1 ser/de ---
def serialize_json(value: CriticalitySourceList) -> list:
    import capo_securityhub.types.criticality_source

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.criticality_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> CriticalitySourceList:
    import capo_securityhub.types.criticality_source

    out: CriticalitySourceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityhub.types.criticality_source.deserialize_json(item))
    return out
