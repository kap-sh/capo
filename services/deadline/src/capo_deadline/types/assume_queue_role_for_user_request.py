"""Generated from Smithy shape ``com.amazonaws.deadline#AssumeQueueRoleForUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.queue_id


class AssumeQueueRoleForUserRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the queue that the user assumes the role for."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID of the queue that the user assumes the role for."""


# --- restJson1 ser/de ---
def serialize_json(value: AssumeQueueRoleForUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssumeQueueRoleForUserRequest:
    out: AssumeQueueRoleForUserRequest = {}  # type: ignore[typeddict-item]
    return out
