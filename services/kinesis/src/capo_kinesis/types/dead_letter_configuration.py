"""Generated from Smithy shape ``com.amazonaws.kinesis#DeadLetterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.max_receive_count
    import capo_kinesis.types.target_type


class DeadLetterConfiguration(TypedDict, closed=True):
    target_type: "capo_kinesis.types.target_type.TargetType"
    """<p>Whether dead-letter handling is enabled for the queue. <code>BUILT_IN</code> enables it: when a record has been received <code>MaxReceiveCount</code> times without being acknowledged, it becomes a dead-letter record and <a>ReceiveQueueRecords</a> no longer returns it. <code>NONE</code> disables it, and an unacknowledged record continues to be redelivered until it is acknowledged or its retention period ends.</p>"""
    max_receive_count: NotRequired[
        "capo_kinesis.types.max_receive_count.MaxReceiveCount"
    ]
    """<p>The number of times a record can be received without being acknowledged before it becomes a dead-letter record. Required when <code>TargetType</code> is <code>BUILT_IN</code>. A queue that you create without <code>DeadLetterConfiguration</code> gets a <code>MaxReceiveCount</code> of 6.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeadLetterConfiguration) -> dict:
    out: dict = {}
    import capo_kinesis.types.target_type

    out["TargetType"] = capo_kinesis.types.target_type.serialize_aws_json_1_1(
        value["target_type"]
    )
    if "max_receive_count" in value:
        out["MaxReceiveCount"] = value["max_receive_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeadLetterConfiguration:
    out: DeadLetterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("TargetType") is not None:
        import capo_kinesis.types.target_type

        out["target_type"] = capo_kinesis.types.target_type.deserialize_aws_json_1_1(
            data["TargetType"]
        )
    else:
        import typing

        out["target_type"] = typing.cast(
            "capo_kinesis.types.target_type.TargetType", ""
        )
    if data.get("MaxReceiveCount") is not None:
        out["max_receive_count"] = data["MaxReceiveCount"]
    return out
