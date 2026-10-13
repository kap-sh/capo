"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#TargetsBatch``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_codestar_notifications.types.target_summary

TargetsBatch: TypeAlias = list[
    "capo_codestar_notifications.types.target_summary.TargetSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetsBatch) -> list:
    import capo_codestar_notifications.types.target_summary

    out: list = []
    for item in value:
        out.append(
            capo_codestar_notifications.types.target_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TargetsBatch:
    import capo_codestar_notifications.types.target_summary

    out: TargetsBatch = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codestar_notifications.types.target_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: TargetsBatch) -> list[Any]:
    import capo_codestar_notifications.types.target_summary

    return [
        capo_codestar_notifications.types.target_summary.redact_sensitive(item)
        for item in value
    ]
