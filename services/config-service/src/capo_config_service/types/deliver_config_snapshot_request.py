"""Generated from Smithy shape ``com.amazonaws.configservice#DeliverConfigSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.channel_name


class DeliverConfigSnapshotRequest(TypedDict, closed=True):
    delivery_channel_name: "capo_config_service.types.channel_name.ChannelName"
    """<p>The name of the delivery channel through which the snapshot is delivered.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliverConfigSnapshotRequest) -> dict:
    out: dict = {}
    out["deliveryChannelName"] = value["delivery_channel_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeliverConfigSnapshotRequest:
    out: DeliverConfigSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("deliveryChannelName") is not None:
        out["delivery_channel_name"] = data["deliveryChannelName"]
    else:
        out["delivery_channel_name"] = ""
    return out
