"""Generated from Smithy shape ``com.amazonaws.kinesis#UpdateStreamRecordDistributionStrategyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.record_distribution_strategy
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_id


class UpdateStreamRecordDistributionStrategyInput(TypedDict, closed=True):
    stream_arn: "capo_kinesis.types.stream_arn.StreamARN"
    """<p>The Amazon Resource Name (ARN) of the stream to update.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""
    record_distribution_strategy: (
        "capo_kinesis.types.record_distribution_strategy.RecordDistributionStrategy"
    )
    """<p>The record distribution strategy to apply to the stream. Specify one of the following values:</p> <ul> <li> <p> <code>AUTO</code> – Amazon Kinesis Data Streams distributes records evenly across shards and ignores any partition key and <code>ExplicitHashKey</code> that producers supply.</p> </li> <li> <p> <code>USER_PARTITION_KEY</code> – Producers must supply a partition key, which Amazon Kinesis Data Streams uses to determine shard placement. This is the default.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateStreamRecordDistributionStrategyInput) -> dict:
    out: dict = {}
    out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    import capo_kinesis.types.record_distribution_strategy

    out["RecordDistributionStrategy"] = (
        capo_kinesis.types.record_distribution_strategy.serialize_aws_json_1_1(
            value["record_distribution_strategy"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateStreamRecordDistributionStrategyInput:
    out: UpdateStreamRecordDistributionStrategyInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    else:
        out["stream_arn"] = ""
    if data.get("StreamId") is not None:
        out["stream_id"] = data["StreamId"]
    if data.get("RecordDistributionStrategy") is not None:
        import capo_kinesis.types.record_distribution_strategy

        out["record_distribution_strategy"] = (
            capo_kinesis.types.record_distribution_strategy.deserialize_aws_json_1_1(
                data["RecordDistributionStrategy"]
            )
        )
    else:
        import typing

        out["record_distribution_strategy"] = typing.cast(
            "capo_kinesis.types.record_distribution_strategy.RecordDistributionStrategy",
            "",
        )
    return out
