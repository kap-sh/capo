"""Generated from Smithy shape ``com.amazonaws.ses#KinesisFirehoseDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.amazon_resource_name


class KinesisFirehoseDestination(TypedDict, closed=True):
    iam_role_arn: "capo_ses.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon Kinesis Firehose stream.</p>"""
    delivery_stream_arn: "capo_ses.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the Amazon Kinesis Firehose stream that email sending events should be published to.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: KinesisFirehoseDestination, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}IAMRoleARN", str(value["iam_role_arn"])))
    pairs.append((f"{key_prefix}DeliveryStreamARN", str(value["delivery_stream_arn"])))


def deserialize_query(el: Element) -> KinesisFirehoseDestination:
    out: KinesisFirehoseDestination = {}  # type: ignore[typeddict-item]
    child_iam_role_arn = el.find("IAMRoleARN")
    if child_iam_role_arn is not None:
        out["iam_role_arn"] = str(child_iam_role_arn.text or "")
    else:
        out["iam_role_arn"] = ""
    child_delivery_stream_arn = el.find("DeliveryStreamARN")
    if child_delivery_stream_arn is not None:
        out["delivery_stream_arn"] = str(child_delivery_stream_arn.text or "")
    else:
        out["delivery_stream_arn"] = ""
    return out
