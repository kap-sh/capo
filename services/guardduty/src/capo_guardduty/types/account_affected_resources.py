"""Generated from Smithy shape ``com.amazonaws.guardduty#AccountAffectedResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.account_affected_resource

AccountAffectedResources: TypeAlias = list[
    "capo_guardduty.types.account_affected_resource.AccountAffectedResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountAffectedResources) -> list:
    import capo_guardduty.types.account_affected_resource

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.account_affected_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountAffectedResources:
    import capo_guardduty.types.account_affected_resource

    out: AccountAffectedResources = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_guardduty.types.account_affected_resource.deserialize_json(item)
        )
    return out
