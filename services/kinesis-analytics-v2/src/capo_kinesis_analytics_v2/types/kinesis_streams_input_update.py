"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#KinesisStreamsInputUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.resource_arn


class KinesisStreamsInputUpdate(TypedDict, closed=True):
    resource_arn_update: "capo_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the input Kinesis data stream to read.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisStreamsInputUpdate) -> dict:
    out: dict = {}
    out["ResourceARNUpdate"] = value["resource_arn_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisStreamsInputUpdate:
    out: KinesisStreamsInputUpdate = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARNUpdate") is not None:
        out["resource_arn_update"] = data["ResourceARNUpdate"]
    else:
        out["resource_arn_update"] = ""
    return out
