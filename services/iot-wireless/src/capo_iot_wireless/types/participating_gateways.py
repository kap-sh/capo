"""Generated from Smithy shape ``com.amazonaws.iotwireless#ParticipatingGateways``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.downlink_mode
    import capo_iot_wireless.types.gateway_list
    import capo_iot_wireless.types.transmission_interval


class ParticipatingGateways(TypedDict, closed=True):
    downlink_mode: "capo_iot_wireless.types.downlink_mode.DownlinkMode"
    """<p>Indicates whether to send the downlink message in sequential mode or concurrent mode, or to use only the chosen gateways from the previous uplink message transmission.</p>"""
    gateway_list: "capo_iot_wireless.types.gateway_list.GatewayList"
    """<p>The list of gateways that you want to use for sending the downlink data traffic.</p>"""
    transmission_interval: (
        "capo_iot_wireless.types.transmission_interval.TransmissionInterval"
    )
    """<p>The duration of time for which AWS IoT Core for LoRaWAN will wait before transmitting the payload to the next gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipatingGateways) -> dict:
    out: dict = {}
    import capo_iot_wireless.types.downlink_mode

    out["DownlinkMode"] = capo_iot_wireless.types.downlink_mode.serialize_json(
        value["downlink_mode"]
    )
    import capo_iot_wireless.types.gateway_list

    out["GatewayList"] = capo_iot_wireless.types.gateway_list.serialize_json(
        value["gateway_list"]
    )
    out["TransmissionInterval"] = value["transmission_interval"]
    return out


def deserialize_json(data: dict) -> ParticipatingGateways:
    out: ParticipatingGateways = {}  # type: ignore[typeddict-item]
    if data.get("DownlinkMode") is not None:
        import capo_iot_wireless.types.downlink_mode

        out["downlink_mode"] = capo_iot_wireless.types.downlink_mode.deserialize_json(
            data["DownlinkMode"]
        )
    else:
        import typing

        out["downlink_mode"] = typing.cast(
            "capo_iot_wireless.types.downlink_mode.DownlinkMode", ""
        )
    if data.get("GatewayList") is not None:
        import capo_iot_wireless.types.gateway_list

        out["gateway_list"] = capo_iot_wireless.types.gateway_list.deserialize_json(
            data["GatewayList"]
        )
    else:
        out["gateway_list"] = []
    if data.get("TransmissionInterval") is not None:
        out["transmission_interval"] = data["TransmissionInterval"]
    else:
        out["transmission_interval"] = 0
    return out
