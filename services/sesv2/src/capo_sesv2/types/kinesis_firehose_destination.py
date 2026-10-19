"""Generated from Smithy shape ``com.amazonaws.sesv2#KinesisFirehoseDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.amazon_resource_name


class KinesisFirehoseDestination(TypedDict, closed=True):
    iam_role_arn: "capo_sesv2.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the IAM role that the Amazon SES API v2 uses to send email events to the Amazon Kinesis Data Firehose stream.</p>"""
    delivery_stream_arn: "capo_sesv2.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose stream that the Amazon SES API v2 sends email events to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisFirehoseDestination) -> dict:
    out: dict = {}
    out["IamRoleArn"] = value["iam_role_arn"]
    out["DeliveryStreamArn"] = value["delivery_stream_arn"]
    return out


def deserialize_json(data: dict) -> KinesisFirehoseDestination:
    out: KinesisFirehoseDestination = {}  # type: ignore[typeddict-item]
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        out["iam_role_arn"] = ""
    if data.get("DeliveryStreamArn") is not None:
        out["delivery_stream_arn"] = data["DeliveryStreamArn"]
    else:
        out["delivery_stream_arn"] = ""
    return out
