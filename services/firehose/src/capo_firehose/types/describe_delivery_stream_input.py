"""Generated from Smithy shape ``com.amazonaws.firehose#DescribeDeliveryStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.delivery_stream_name
    import capo_firehose.types.describe_delivery_stream_input_limit
    import capo_firehose.types.destination_id


class DescribeDeliveryStreamInput(TypedDict, closed=True):
    delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName"
    """<p>The name of the Firehose stream.</p>"""
    limit: NotRequired[
        "capo_firehose.types.describe_delivery_stream_input_limit.DescribeDeliveryStreamInputLimit"
    ]
    """<p>The limit on the number of destinations to return. You can have one destination per Firehose stream.</p>"""
    exclusive_start_destination_id: NotRequired[
        "capo_firehose.types.destination_id.DestinationId"
    ]
    """<p>The ID of the destination to start returning the destination information. Firehose supports one destination per Firehose stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeliveryStreamInput) -> dict:
    out: dict = {}
    out["DeliveryStreamName"] = value["delivery_stream_name"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "exclusive_start_destination_id" in value:
        out["ExclusiveStartDestinationId"] = value["exclusive_start_destination_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeliveryStreamInput:
    out: DescribeDeliveryStreamInput = {}  # type: ignore[typeddict-item]
    if data.get("DeliveryStreamName") is not None:
        out["delivery_stream_name"] = data["DeliveryStreamName"]
    else:
        out["delivery_stream_name"] = ""
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("ExclusiveStartDestinationId") is not None:
        out["exclusive_start_destination_id"] = data["ExclusiveStartDestinationId"]
    return out
