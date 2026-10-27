"""Generated from Smithy shape ``com.amazonaws.deadline#DeleteQueueEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.queue_environment_id
    import capo_deadline.types.queue_id


class DeleteQueueEnvironmentRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the farm from which to remove the queue environment."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID of the queue environment to delete."""
    queue_environment_id: "capo_deadline.types.queue_environment_id.QueueEnvironmentId"
    """The queue environment ID of the queue environment to delete."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQueueEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteQueueEnvironmentRequest:
    out: DeleteQueueEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
