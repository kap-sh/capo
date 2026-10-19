"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#KinesisFirehoseInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.resource_arn
    import capo_kinesis_analytics.types.role_arn


class KinesisFirehoseInput(TypedDict, closed=True):
    resource_arn: "capo_kinesis_analytics.types.resource_arn.ResourceARN"
    """<p>ARN of the input delivery stream.</p>"""
    role_arn: "capo_kinesis_analytics.types.role_arn.RoleARN"
    """<p>ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to make sure that the role has the necessary permissions to access the stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisFirehoseInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    out["RoleARN"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisFirehoseInput:
    out: KinesisFirehoseInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    else:
        out["role_arn"] = ""
    return out
