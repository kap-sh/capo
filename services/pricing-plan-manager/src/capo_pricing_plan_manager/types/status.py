"""Generated from Smithy shape ``com.amazonaws.pricingplanmanager#Status``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a flat-rate pricing subscription.</p> <p>Possible values:</p> <ul> <li> <p> <code>PENDING_APPROVAL</code> — The subscription was created with manual approval and is waiting for an <code>ApprovePaidSubscription</code> call.</p> </li> <li> <p> <code>ACTIVE</code> — The subscription is active and resources are covered by flat-rate pricing.</p> </li> <li> <p> <code>SYNC_IN_PROGRESS</code> — A change is being applied to the subscription. Wait for the operation to complete before making additional changes.</p> </li> <li> <p> <code>FAILED</code> — The subscription encountered an error. Check the <code>statusReason</code> field for details.</p> </li> </ul>"""
Status: TypeAlias = Literal[
    "PENDING_APPROVAL",
    "ACTIVE",
    "SYNC_IN_PROGRESS",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
