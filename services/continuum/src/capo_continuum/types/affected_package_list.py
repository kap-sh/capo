"""Generated from Smithy shape ``com.amazonaws.continuum#AffectedPackageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.affected_package

AffectedPackageList: TypeAlias = list[
    "capo_continuum.types.affected_package.AffectedPackage"
]


# --- restJson1 ser/de ---
def serialize_json(value: AffectedPackageList) -> list:
    import capo_continuum.types.affected_package

    out: list = []
    for item in value:
        out.append(capo_continuum.types.affected_package.serialize_json(item))
    return out


def deserialize_json(data: list) -> AffectedPackageList:
    import capo_continuum.types.affected_package

    out: AffectedPackageList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_continuum.types.affected_package.deserialize_json(item))
    return out
