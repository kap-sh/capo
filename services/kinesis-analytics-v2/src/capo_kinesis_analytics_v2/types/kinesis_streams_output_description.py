"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#KinesisStreamsOutputDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.resource_arn
    import capo_kinesis_analytics_v2.types.role_arn


class KinesisStreamsOutputDescription(TypedDict, closed=True):
    resource_arn: "capo_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the Kinesis data stream.</p>"""
    role_arn: NotRequired["capo_kinesis_analytics_v2.types.role_arn.RoleARN"]
    """<p>The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.</p> <note> <p>Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisStreamsOutputDescription) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisStreamsOutputDescription:
    out: KinesisStreamsOutputDescription = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    return out
