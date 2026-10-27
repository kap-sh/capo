"""Generated from Smithy shape ``com.amazonaws.deadline#DisassociateMemberFromQueueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.identity_center_principal_id
    import capo_deadline.types.queue_id


class DisassociateMemberFromQueueRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID for the queue to disassociate from a member."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID of the queue in which you're disassociating from a member."""
    principal_id: (
        "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
    )
    """A member's principal ID to disassociate from a queue."""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateMemberFromQueueRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateMemberFromQueueRequest:
    out: DisassociateMemberFromQueueRequest = {}  # type: ignore[typeddict-item]
    return out
