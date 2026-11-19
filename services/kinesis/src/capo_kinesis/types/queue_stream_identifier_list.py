"""Generated from Smithy shape ``com.amazonaws.kinesis#QueueStreamIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.queue_stream_identifier

QueueStreamIdentifierList: TypeAlias = list[
    "capo_kinesis.types.queue_stream_identifier.QueueStreamIdentifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueueStreamIdentifierList) -> list:
    import capo_kinesis.types.queue_stream_identifier

    out: list = []
    for item in value:
        out.append(
            capo_kinesis.types.queue_stream_identifier.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> QueueStreamIdentifierList:
    import capo_kinesis.types.queue_stream_identifier

    out: QueueStreamIdentifierList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kinesis.types.queue_stream_identifier.deserialize_aws_json_1_1(item)
        )
    return out
