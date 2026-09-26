"""Generated from Smithy shape ``com.amazonaws.pricingplanmanager#ScheduledChangeType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of pending change on a subscription.</p> <p>Possible values:</p> <ul> <li> <p> <code>DOWNGRADE</code> — The subscription tier is being lowered at the end of the billing period.</p> </li> <li> <p> <code>CANCELLATION</code> — The subscription is being terminated at the end of the billing period.</p> </li> </ul>"""
ScheduledChangeType: TypeAlias = Literal[
    "DOWNGRADE",
    "CANCELLATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduledChangeType) -> str:
    return value


def deserialize_json(data: str) -> ScheduledChangeType:
    return cast(ScheduledChangeType, data)
