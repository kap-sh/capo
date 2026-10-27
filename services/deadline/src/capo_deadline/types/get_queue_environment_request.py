"""Generated from Smithy shape ``com.amazonaws.deadline#GetQueueEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.queue_environment_id
    import capo_deadline.types.queue_id


class GetQueueEnvironmentRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID for the queue environment."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID for the queue environment."""
    queue_environment_id: "capo_deadline.types.queue_environment_id.QueueEnvironmentId"
    """The queue environment ID."""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueueEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQueueEnvironmentRequest:
    out: GetQueueEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
