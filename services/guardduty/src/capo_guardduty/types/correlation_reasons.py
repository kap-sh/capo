"""Generated from Smithy shape ``com.amazonaws.guardduty#CorrelationReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.correlation_reason

CorrelationReasons: TypeAlias = list[
    "capo_guardduty.types.correlation_reason.CorrelationReason"
]


# --- restJson1 ser/de ---
def serialize_json(value: CorrelationReasons) -> list:
    import capo_guardduty.types.correlation_reason

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.correlation_reason.serialize_json(item))
    return out


def deserialize_json(data: list) -> CorrelationReasons:
    import capo_guardduty.types.correlation_reason

    out: CorrelationReasons = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.correlation_reason.deserialize_json(item))
    return out
