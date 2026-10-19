"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteDeliveryChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.channel_name


class DeleteDeliveryChannelRequest(TypedDict, closed=True):
    delivery_channel_name: "capo_config_service.types.channel_name.ChannelName"
    """<p>The name of the delivery channel that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDeliveryChannelRequest) -> dict:
    out: dict = {}
    out["DeliveryChannelName"] = value["delivery_channel_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDeliveryChannelRequest:
    out: DeleteDeliveryChannelRequest = {}  # type: ignore[typeddict-item]
    if data.get("DeliveryChannelName") is not None:
        out["delivery_channel_name"] = data["DeliveryChannelName"]
    else:
        out["delivery_channel_name"] = ""
    return out
