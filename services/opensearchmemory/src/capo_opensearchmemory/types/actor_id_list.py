"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#ActorIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchmemory.types.actor_id

ActorIdList: TypeAlias = list["capo_opensearchmemory.types.actor_id.ActorId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActorIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ActorIdList:
    return [item for item in data if item is not None]
