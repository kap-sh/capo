"""Generated from Smithy shape ``com.amazonaws.gamelift#EventList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.event

EventList: TypeAlias = list["capo_gamelift.types.event.Event"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventList) -> list:
    import capo_gamelift.types.event

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.event.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EventList:
    import capo_gamelift.types.event

    out: EventList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.event.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: EventList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
