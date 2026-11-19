"""Generated from Smithy shape ``com.amazonaws.kinesis#QueueSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.queue_summary

QueueSummaryList: TypeAlias = list["capo_kinesis.types.queue_summary.QueueSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueueSummaryList) -> list:
    import capo_kinesis.types.queue_summary

    out: list = []
    for item in value:
        out.append(capo_kinesis.types.queue_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> QueueSummaryList:
    import capo_kinesis.types.queue_summary

    out: QueueSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_kinesis.types.queue_summary.deserialize_aws_json_1_1(item))
    return out
