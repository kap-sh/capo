"""Generated from Smithy shape ``com.amazonaws.datazone#SubscriptionTargets``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.subscription_target_summary

SubscriptionTargets: TypeAlias = list[
    "capo_datazone.types.subscription_target_summary.SubscriptionTargetSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionTargets) -> list:
    import capo_datazone.types.subscription_target_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.subscription_target_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubscriptionTargets:
    import capo_datazone.types.subscription_target_summary

    out: SubscriptionTargets = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_datazone.types.subscription_target_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: SubscriptionTargets) -> list[Any]:
    import capo_datazone.types.subscription_target_summary

    return [
        capo_datazone.types.subscription_target_summary.redact_sensitive(item)
        for item in value
    ]
