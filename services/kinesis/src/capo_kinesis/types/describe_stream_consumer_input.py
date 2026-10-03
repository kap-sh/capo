"""Generated from Smithy shape ``com.amazonaws.kinesis#DescribeStreamConsumerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.consumer_arn
    import capo_kinesis.types.consumer_name
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_id


class DescribeStreamConsumerInput(TypedDict, closed=True):
    stream_arn: NotRequired["capo_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the Kinesis data stream that the consumer is registered with. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p>"""
    consumer_name: NotRequired["capo_kinesis.types.consumer_name.ConsumerName"]
    """<p>The name that you gave to the consumer.</p>"""
    consumer_arn: NotRequired["capo_kinesis.types.consumer_arn.ConsumerARN"]
    """<p>The ARN returned by Kinesis Data Streams when you registered the consumer.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeStreamConsumerInput) -> dict:
    out: dict = {}
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "consumer_name" in value:
        out["ConsumerName"] = value["consumer_name"]
    if "consumer_arn" in value:
        out["ConsumerARN"] = value["consumer_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeStreamConsumerInput:
    out: DescribeStreamConsumerInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("ConsumerName") is not None:
        out["consumer_name"] = data["ConsumerName"]
    if data.get("ConsumerARN") is not None:
        out["consumer_arn"] = data["ConsumerARN"]
    if data.get("StreamId") is not None:
        out["stream_id"] = data["StreamId"]
    return out
