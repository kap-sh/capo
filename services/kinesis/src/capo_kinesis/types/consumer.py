"""Generated from Smithy shape ``com.amazonaws.kinesis#Consumer``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.consumer_arn
    import capo_kinesis.types.consumer_name
    import capo_kinesis.types.consumer_status
    import capo_kinesis.types.timestamp


class Consumer(TypedDict, closed=True):
    consumer_name: "capo_kinesis.types.consumer_name.ConsumerName"
    """<p>The name of the consumer is something you choose when you register the consumer.</p>"""
    consumer_arn: "capo_kinesis.types.consumer_arn.ConsumerARN"
    """<p>When you register a consumer, Kinesis Data Streams generates an ARN for it. You need this ARN to be able to call <a>SubscribeToShard</a>.</p> <p>If you delete a consumer and then create a new one with the same name, it won't have the same ARN. That's because consumer ARNs contain the creation timestamp. This is important to keep in mind if you have IAM policies that reference consumer ARNs.</p>"""
    consumer_status: "capo_kinesis.types.consumer_status.ConsumerStatus"
    """<p>A consumer can't read data while in the <code>CREATING</code> or <code>DELETING</code> states.</p>"""
    consumer_creation_timestamp: "capo_kinesis.types.timestamp.Timestamp"
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Consumer) -> dict:
    out: dict = {}
    out["ConsumerName"] = value["consumer_name"]
    out["ConsumerARN"] = value["consumer_arn"]
    import capo_kinesis.types.consumer_status

    out["ConsumerStatus"] = capo_kinesis.types.consumer_status.serialize_aws_json_1_1(
        value["consumer_status"]
    )
    import capo_kinesis.types.timestamp

    out["ConsumerCreationTimestamp"] = (
        capo_kinesis.types.timestamp.serialize_aws_json_1_1(
            value["consumer_creation_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Consumer:
    out: Consumer = {}  # type: ignore[typeddict-item]
    if data.get("ConsumerName") is not None:
        out["consumer_name"] = data["ConsumerName"]
    else:
        out["consumer_name"] = ""
    if data.get("ConsumerARN") is not None:
        out["consumer_arn"] = data["ConsumerARN"]
    else:
        out["consumer_arn"] = ""
    if data.get("ConsumerStatus") is not None:
        import capo_kinesis.types.consumer_status

        out["consumer_status"] = (
            capo_kinesis.types.consumer_status.deserialize_aws_json_1_1(
                data["ConsumerStatus"]
            )
        )
    else:
        import typing

        out["consumer_status"] = typing.cast(
            "capo_kinesis.types.consumer_status.ConsumerStatus", ""
        )
    if data.get("ConsumerCreationTimestamp") is not None:
        import capo_kinesis.types.timestamp

        out["consumer_creation_timestamp"] = (
            capo_kinesis.types.timestamp.deserialize_aws_json_1_1(
                data["ConsumerCreationTimestamp"]
            )
        )
    else:
        import datetime

        out["consumer_creation_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
