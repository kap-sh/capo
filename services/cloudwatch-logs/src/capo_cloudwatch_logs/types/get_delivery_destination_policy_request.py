"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetDeliveryDestinationPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.delivery_destination_name


class GetDeliveryDestinationPolicyRequest(TypedDict, closed=True):
    delivery_destination_name: (
        "capo_cloudwatch_logs.types.delivery_destination_name.DeliveryDestinationName"
    )
    """<p>The name of the delivery destination that you want to retrieve the policy of.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeliveryDestinationPolicyRequest) -> dict:
    out: dict = {}
    out["deliveryDestinationName"] = value["delivery_destination_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeliveryDestinationPolicyRequest:
    out: GetDeliveryDestinationPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("deliveryDestinationName") is not None:
        out["delivery_destination_name"] = data["deliveryDestinationName"]
    else:
        out["delivery_destination_name"] = ""
    return out
