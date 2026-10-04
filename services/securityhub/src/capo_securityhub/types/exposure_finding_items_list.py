"""Generated from Smithy shape ``com.amazonaws.securityhub#ExposureFindingItemsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.exposure_finding

ExposureFindingItemsList: TypeAlias = list[
    "capo_securityhub.types.exposure_finding.ExposureFinding"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExposureFindingItemsList) -> list:
    import capo_securityhub.types.exposure_finding

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.exposure_finding.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExposureFindingItemsList:
    import capo_securityhub.types.exposure_finding

    out: ExposureFindingItemsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityhub.types.exposure_finding.deserialize_json(item))
    return out
