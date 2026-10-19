"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InvocationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.arn


class InvocationConfiguration(TypedDict, closed=True):
    topic_arn: "capo_bedrock_agentcore_control.types.arn.Arn"
    """<p>The ARN of the SNS topic for job notifications.</p>"""
    payload_delivery_bucket_name: "str"
    """<p>The S3 bucket name for event payload delivery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvocationConfiguration) -> dict:
    out: dict = {}
    out["topicArn"] = value["topic_arn"]
    out["payloadDeliveryBucketName"] = value["payload_delivery_bucket_name"]
    return out


def deserialize_json(data: dict) -> InvocationConfiguration:
    out: InvocationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("topicArn") is not None:
        out["topic_arn"] = data["topicArn"]
    else:
        out["topic_arn"] = ""
    if data.get("payloadDeliveryBucketName") is not None:
        out["payload_delivery_bucket_name"] = data["payloadDeliveryBucketName"]
    else:
        out["payload_delivery_bucket_name"] = ""
    return out
