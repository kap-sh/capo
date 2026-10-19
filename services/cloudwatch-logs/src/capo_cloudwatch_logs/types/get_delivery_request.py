"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetDeliveryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.delivery_id


class GetDeliveryRequest(TypedDict, closed=True):
    id: "capo_cloudwatch_logs.types.delivery_id.DeliveryId"
    """<p>The ID of the delivery that you want to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeliveryRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeliveryRequest:
    out: GetDeliveryRequest = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
