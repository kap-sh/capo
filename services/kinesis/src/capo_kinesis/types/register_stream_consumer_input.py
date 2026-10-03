"""Generated from Smithy shape ``com.amazonaws.kinesis#RegisterStreamConsumerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.consumer_name
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_id
    import capo_kinesis.types.tag_map


class RegisterStreamConsumerInput(TypedDict, closed=True):
    stream_arn: "capo_kinesis.types.stream_arn.StreamARN"
    """<p>The ARN of the Kinesis data stream that you want to register the consumer with. For more info, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p>"""
    consumer_name: "capo_kinesis.types.consumer_name.ConsumerName"
    """<p>For a given Kinesis data stream, each consumer must have a unique name. However, consumer names don't have to be unique across data streams.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""
    tags: NotRequired["capo_kinesis.types.tag_map.TagMap"]
    """<p>A set of up to 50 key-value pairs. A tag consists of a required key and an optional value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterStreamConsumerInput) -> dict:
    out: dict = {}
    out["StreamARN"] = value["stream_arn"]
    out["ConsumerName"] = value["consumer_name"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    if "tags" in value:
        import capo_kinesis.types.tag_map

        out["Tags"] = capo_kinesis.types.tag_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterStreamConsumerInput:
    out: RegisterStreamConsumerInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    else:
        raise DeserializationError("RegisterStreamConsumerInput.stream_arn required")
    if data.get("ConsumerName") is not None:
        out["consumer_name"] = data["ConsumerName"]
    else:
        raise DeserializationError("RegisterStreamConsumerInput.consumer_name required")
    if data.get("StreamId") is not None:
        out["stream_id"] = data["StreamId"]
    if data.get("Tags") is not None:
        import capo_kinesis.types.tag_map

        out["tags"] = capo_kinesis.types.tag_map.deserialize_aws_json_1_1(data["Tags"])
    return out
