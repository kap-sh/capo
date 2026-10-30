"""Generated from Smithy shape ``com.amazonaws.continuum#IssuePatchDeliveryFailureReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.delivery_reason

IssuePatchDeliveryFailureReasons: TypeAlias = list[
    "capo_continuum.types.delivery_reason.DeliveryReason"
]


# --- restJson1 ser/de ---
def serialize_json(value: IssuePatchDeliveryFailureReasons) -> list:
    import capo_continuum.types.delivery_reason

    out: list = []
    for item in value:
        out.append(capo_continuum.types.delivery_reason.serialize_json(item))
    return out


def deserialize_json(data: list) -> IssuePatchDeliveryFailureReasons:
    import capo_continuum.types.delivery_reason

    out: IssuePatchDeliveryFailureReasons = []
    for item in data:
        if item is None:
            continue
        out.append(capo_continuum.types.delivery_reason.deserialize_json(item))
    return out
