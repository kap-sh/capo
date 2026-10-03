"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteDeliveryDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.delivery_destination_name


class DeleteDeliveryDestinationRequest(TypedDict, closed=True):
    name: "capo_cloudwatch_logs.types.delivery_destination_name.DeliveryDestinationName"
    """<p>The name of the delivery destination that you want to delete. You can find a list of delivery destination names by using the <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliveryDestinations.html">DescribeDeliveryDestinations</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDeliveryDestinationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDeliveryDestinationRequest:
    out: DeleteDeliveryDestinationRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteDeliveryDestinationRequest.name required")
    return out
