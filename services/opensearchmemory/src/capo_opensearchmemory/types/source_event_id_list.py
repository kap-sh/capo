"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#SourceEventIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchmemory.types.event_id

SourceEventIdList: TypeAlias = list["capo_opensearchmemory.types.event_id.EventId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SourceEventIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> SourceEventIdList:
    return [item for item in data if item is not None]
