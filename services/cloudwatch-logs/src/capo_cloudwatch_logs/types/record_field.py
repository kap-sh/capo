"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#RecordField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.boolean
    import capo_cloudwatch_logs.types.field_header


class RecordField(TypedDict, closed=True):
    name: NotRequired["capo_cloudwatch_logs.types.field_header.FieldHeader"]
    """<p>The name to use when specifying this record field in a <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html">CreateDelivery</a> or <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateDeliveryConfiguration.html">UpdateDeliveryConfiguration</a> operation. </p>"""
    mandatory: NotRequired["capo_cloudwatch_logs.types.boolean.Boolean"]
    """<p>If this is <code>true</code>, the record field must be present in the <code>recordFields</code> parameter provided to a <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html">CreateDelivery</a> or <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateDeliveryConfiguration.html">UpdateDeliveryConfiguration</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordField) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "mandatory" in value:
        out["mandatory"] = value["mandatory"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecordField:
    out: RecordField = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("mandatory") is not None:
        out["mandatory"] = data["mandatory"]
    return out
