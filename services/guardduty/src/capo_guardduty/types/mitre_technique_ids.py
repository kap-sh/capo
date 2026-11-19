"""Generated from Smithy shape ``com.amazonaws.guardduty#MitreTechniqueIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.mitre_threat_id

MitreTechniqueIds: TypeAlias = list[
    "capo_guardduty.types.mitre_threat_id.MitreThreatId"
]


# --- restJson1 ser/de ---
def serialize_json(value: MitreTechniqueIds) -> list:
    return list(value)


def deserialize_json(data: list) -> MitreTechniqueIds:
    return [item for item in data if item is not None]
