"""Generated from Smithy shape ``com.amazonaws.kinesis#QueueStreamConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.queue_stream_configuration

QueueStreamConfigurationList: TypeAlias = list[
    "capo_kinesis.types.queue_stream_configuration.QueueStreamConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueueStreamConfigurationList) -> list:
    import capo_kinesis.types.queue_stream_configuration

    out: list = []
    for item in value:
        out.append(
            capo_kinesis.types.queue_stream_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> QueueStreamConfigurationList:
    import capo_kinesis.types.queue_stream_configuration

    out: QueueStreamConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kinesis.types.queue_stream_configuration.deserialize_aws_json_1_1(item)
        )
    return out
