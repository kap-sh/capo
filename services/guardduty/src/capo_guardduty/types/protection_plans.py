"""Generated from Smithy shape ``com.amazonaws.guardduty#ProtectionPlans``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.protection_plan

ProtectionPlans: TypeAlias = list["capo_guardduty.types.protection_plan.ProtectionPlan"]


# --- restJson1 ser/de ---
def serialize_json(value: ProtectionPlans) -> list:
    import capo_guardduty.types.protection_plan

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.protection_plan.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProtectionPlans:
    import capo_guardduty.types.protection_plan

    out: ProtectionPlans = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.protection_plan.deserialize_json(item))
    return out
