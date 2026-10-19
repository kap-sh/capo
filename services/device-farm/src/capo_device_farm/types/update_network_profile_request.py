"""Generated from Smithy shape ``com.amazonaws.devicefarm#UpdateNetworkProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.long
    import capo_device_farm.types.message
    import capo_device_farm.types.name
    import capo_device_farm.types.network_profile_type
    import capo_device_farm.types.percent_integer


class UpdateNetworkProfileRequest(TypedDict, closed=True):
    arn: "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the project for which you want to update network profile settings.</p>"""
    name: NotRequired["capo_device_farm.types.name.Name"]
    """<p>The name of the network profile about which you are returning information.</p>"""
    description: NotRequired["capo_device_farm.types.message.Message"]
    """<p>The description of the network profile about which you are returning information.</p>"""
    type: NotRequired["capo_device_farm.types.network_profile_type.NetworkProfileType"]
    """<p>The type of network profile to return information about. Valid values are listed here.</p>"""
    uplink_bandwidth_bits: NotRequired["capo_device_farm.types.long.Long"]
    """<p>The data throughput rate in bits per second, as an integer from 0 to 104857600.</p>"""
    downlink_bandwidth_bits: NotRequired["capo_device_farm.types.long.Long"]
    """<p>The data throughput rate in bits per second, as an integer from 0 to 104857600.</p>"""
    uplink_delay_ms: NotRequired["capo_device_farm.types.long.Long"]
    """<p>Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.</p>"""
    downlink_delay_ms: NotRequired["capo_device_farm.types.long.Long"]
    """<p>Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.</p>"""
    uplink_jitter_ms: NotRequired["capo_device_farm.types.long.Long"]
    """<p>Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.</p>"""
    downlink_jitter_ms: NotRequired["capo_device_farm.types.long.Long"]
    """<p>Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.</p>"""
    uplink_loss_percent: NotRequired[
        "capo_device_farm.types.percent_integer.PercentInteger"
    ]
    """<p>Proportion of transmitted packets that fail to arrive from 0 to 100 percent.</p>"""
    downlink_loss_percent: NotRequired[
        "capo_device_farm.types.percent_integer.PercentInteger"
    ]
    """<p>Proportion of received packets that fail to arrive from 0 to 100 percent.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateNetworkProfileRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "type" in value:
        import capo_device_farm.types.network_profile_type

        out["type"] = (
            capo_device_farm.types.network_profile_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "uplink_bandwidth_bits" in value:
        out["uplinkBandwidthBits"] = value["uplink_bandwidth_bits"]
    if "downlink_bandwidth_bits" in value:
        out["downlinkBandwidthBits"] = value["downlink_bandwidth_bits"]
    if "uplink_delay_ms" in value:
        out["uplinkDelayMs"] = value["uplink_delay_ms"]
    if "downlink_delay_ms" in value:
        out["downlinkDelayMs"] = value["downlink_delay_ms"]
    if "uplink_jitter_ms" in value:
        out["uplinkJitterMs"] = value["uplink_jitter_ms"]
    if "downlink_jitter_ms" in value:
        out["downlinkJitterMs"] = value["downlink_jitter_ms"]
    if "uplink_loss_percent" in value:
        out["uplinkLossPercent"] = value["uplink_loss_percent"]
    if "downlink_loss_percent" in value:
        out["downlinkLossPercent"] = value["downlink_loss_percent"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateNetworkProfileRequest:
    out: UpdateNetworkProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateNetworkProfileRequest.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("type") is not None:
        import capo_device_farm.types.network_profile_type

        out["type"] = (
            capo_device_farm.types.network_profile_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    if data.get("uplinkBandwidthBits") is not None:
        out["uplink_bandwidth_bits"] = data["uplinkBandwidthBits"]
    if data.get("downlinkBandwidthBits") is not None:
        out["downlink_bandwidth_bits"] = data["downlinkBandwidthBits"]
    if data.get("uplinkDelayMs") is not None:
        out["uplink_delay_ms"] = data["uplinkDelayMs"]
    if data.get("downlinkDelayMs") is not None:
        out["downlink_delay_ms"] = data["downlinkDelayMs"]
    if data.get("uplinkJitterMs") is not None:
        out["uplink_jitter_ms"] = data["uplinkJitterMs"]
    if data.get("downlinkJitterMs") is not None:
        out["downlink_jitter_ms"] = data["downlinkJitterMs"]
    if data.get("uplinkLossPercent") is not None:
        out["uplink_loss_percent"] = data["uplinkLossPercent"]
    if data.get("downlinkLossPercent") is not None:
        out["downlink_loss_percent"] = data["downlinkLossPercent"]
    return out
