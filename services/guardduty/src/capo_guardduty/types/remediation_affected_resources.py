"""Generated from Smithy shape ``com.amazonaws.guardduty#RemediationAffectedResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.affected_resource

RemediationAffectedResources: TypeAlias = list[
    "capo_guardduty.types.affected_resource.AffectedResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: RemediationAffectedResources) -> list:
    import capo_guardduty.types.affected_resource

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.affected_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> RemediationAffectedResources:
    import capo_guardduty.types.affected_resource

    out: RemediationAffectedResources = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.affected_resource.deserialize_json(item))
    return out
