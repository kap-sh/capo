"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#EventList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchmemory.types.event

EventList: TypeAlias = list["capo_opensearchmemory.types.event.Event"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EventList) -> list:
    import capo_opensearchmemory.types.event

    out: list = []
    for item in value:
        out.append(capo_opensearchmemory.types.event.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> EventList:
    import capo_opensearchmemory.types.event

    out: EventList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_opensearchmemory.types.event.deserialize_aws_json_1_0(item))
    return out


def redact_sensitive(value: EventList) -> list[Any]:
    import capo_opensearchmemory.types.event

    return [capo_opensearchmemory.types.event.redact_sensitive(item) for item in value]
