"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteDeliveryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.delivery_id


class DeleteDeliveryRequest(TypedDict, closed=True):
    id: "capo_cloudwatch_logs.types.delivery_id.DeliveryId"
    """<p>The unique ID of the delivery to delete. You can find the ID of a delivery with the <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliveries.html">DescribeDeliveries</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDeliveryRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDeliveryRequest:
    out: DeleteDeliveryRequest = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteDeliveryRequest.id required")
    return out
