"""Generated from Smithy shape ``com.amazonaws.cloudfront#KinesisStreamConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class KinesisStreamConfig(TypedDict, closed=True):
    role_arn: "capo_cloudfront.types.string.string"
    """<p>The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFront can use to send real-time log data to your Kinesis data stream.</p> <p>For more information the IAM role, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-iam-role">Real-time log configuration IAM role</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    stream_arn: "capo_cloudfront.types.string.string"
    """<p>The Amazon Resource Name (ARN) of the Kinesis data stream where you are sending real-time log data.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: KinesisStreamConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "RoleARN").text = str(value["role_arn"])
    SubElement(el, "StreamARN").text = str(value["stream_arn"])


def deserialize_xml(el: Element) -> KinesisStreamConfig:
    out: KinesisStreamConfig = {}  # type: ignore[typeddict-item]
    child_role_arn = el.find("RoleARN")
    if child_role_arn is not None:
        out["role_arn"] = str(child_role_arn.text or "")
    else:
        raise DeserializationError("KinesisStreamConfig.role_arn required")
    child_stream_arn = el.find("StreamARN")
    if child_stream_arn is not None:
        out["stream_arn"] = str(child_stream_arn.text or "")
    else:
        raise DeserializationError("KinesisStreamConfig.stream_arn required")
    return out
