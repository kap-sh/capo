"""Generated from Smithy shape ``com.amazonaws.continuum#FindingResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.finding_resource

FindingResourceList: TypeAlias = list[
    "capo_continuum.types.finding_resource.FindingResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingResourceList) -> list:
    import capo_continuum.types.finding_resource

    out: list = []
    for item in value:
        out.append(capo_continuum.types.finding_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingResourceList:
    import capo_continuum.types.finding_resource

    out: FindingResourceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_continuum.types.finding_resource.deserialize_json(item))
    return out
