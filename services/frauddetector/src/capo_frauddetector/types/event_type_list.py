"""Generated from Smithy shape ``com.amazonaws.frauddetector#eventTypeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.event_type

eventTypeList: TypeAlias = list["capo_frauddetector.types.event_type.EventType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: eventTypeList) -> list:
    import capo_frauddetector.types.event_type

    out: list = []
    for item in value:
        out.append(capo_frauddetector.types.event_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> eventTypeList:
    import capo_frauddetector.types.event_type

    out: eventTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_frauddetector.types.event_type.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: eventTypeList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
