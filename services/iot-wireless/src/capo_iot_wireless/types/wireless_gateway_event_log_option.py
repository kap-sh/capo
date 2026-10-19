"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayEventLogOption``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.log_level
    import capo_iot_wireless.types.wireless_gateway_event


class WirelessGatewayEventLogOption(TypedDict, closed=True):
    event: "capo_iot_wireless.types.wireless_gateway_event.WirelessGatewayEvent"
    log_level: "capo_iot_wireless.types.log_level.LogLevel"


# --- restJson1 ser/de ---
def serialize_json(value: WirelessGatewayEventLogOption) -> dict:
    out: dict = {}
    import capo_iot_wireless.types.wireless_gateway_event

    out["Event"] = capo_iot_wireless.types.wireless_gateway_event.serialize_json(
        value["event"]
    )
    import capo_iot_wireless.types.log_level

    out["LogLevel"] = capo_iot_wireless.types.log_level.serialize_json(
        value["log_level"]
    )
    return out


def deserialize_json(data: dict) -> WirelessGatewayEventLogOption:
    out: WirelessGatewayEventLogOption = {}  # type: ignore[typeddict-item]
    if data.get("Event") is not None:
        import capo_iot_wireless.types.wireless_gateway_event

        out["event"] = capo_iot_wireless.types.wireless_gateway_event.deserialize_json(
            data["Event"]
        )
    else:
        import typing

        out["event"] = typing.cast(
            "capo_iot_wireless.types.wireless_gateway_event.WirelessGatewayEvent", ""
        )
    if data.get("LogLevel") is not None:
        import capo_iot_wireless.types.log_level

        out["log_level"] = capo_iot_wireless.types.log_level.deserialize_json(
            data["LogLevel"]
        )
    else:
        import typing

        out["log_level"] = typing.cast("capo_iot_wireless.types.log_level.LogLevel", "")
    return out
