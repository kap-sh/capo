"""Generated from Smithy shape ``com.amazonaws.kinesis#QueueRecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.queue_record

QueueRecordList: TypeAlias = list["capo_kinesis.types.queue_record.QueueRecord"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueueRecordList) -> list:
    import capo_kinesis.types.queue_record

    out: list = []
    for item in value:
        out.append(capo_kinesis.types.queue_record.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> QueueRecordList:
    import capo_kinesis.types.queue_record

    out: QueueRecordList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_kinesis.types.queue_record.deserialize_aws_json_1_1(item))
    return out
