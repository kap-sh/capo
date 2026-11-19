"""Generated from Smithy shape ``com.amazonaws.kinesis#QueueStreamFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.queue_stream_filter

QueueStreamFilterList: TypeAlias = list[
    "capo_kinesis.types.queue_stream_filter.QueueStreamFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueueStreamFilterList) -> list:
    import capo_kinesis.types.queue_stream_filter

    out: list = []
    for item in value:
        out.append(capo_kinesis.types.queue_stream_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> QueueStreamFilterList:
    import capo_kinesis.types.queue_stream_filter

    out: QueueStreamFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kinesis.types.queue_stream_filter.deserialize_aws_json_1_1(item)
        )
    return out
