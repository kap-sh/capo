"""Generated from Smithy shape ``com.amazonaws.directoryservice#EventTopics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.event_topic

EventTopics: TypeAlias = list["capo_directory_service.types.event_topic.EventTopic"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventTopics) -> list:
    import capo_directory_service.types.event_topic

    out: list = []
    for item in value:
        out.append(
            capo_directory_service.types.event_topic.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EventTopics:
    import capo_directory_service.types.event_topic

    out: EventTopics = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_directory_service.types.event_topic.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventTopics) -> list:
    import capo_directory_service.types.event_topic

    out: list = []
    for item in value:
        out.append(capo_directory_service.types.event_topic.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EventTopics:
    import capo_directory_service.types.event_topic

    out: EventTopics = []
    for item in data:
        if item is None:
            continue
        out.append(capo_directory_service.types.event_topic.deserialize_cbor(item))
    return out
