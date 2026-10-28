"""Generated from Smithy shape ``com.amazonaws.deadline#UsageTrackingResource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError
from capo_deadline.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_deadline.types.queue_id


class UsageTrackingResourceQueueIdMember(TypedDict, closed=True):
    queueId: "capo_deadline.types.queue_id.QueueId"


UsageTrackingResource: TypeAlias = (
    UsageTrackingResourceQueueIdMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: UsageTrackingResource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"UsageTrackingResource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "queueId" in value:
        return {"queueId": value["queueId"]}
    else:
        raise SerializationError("UsageTrackingResource: no variant present")


def deserialize_json(data: dict) -> UsageTrackingResource:
    if data.get("queueId") is not None:
        return {"queueId": data["queueId"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("UsageTrackingResource: no recognized variant key")
