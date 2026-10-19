"""Generated from Smithy shape ``com.amazonaws.iotwireless#PutResourceLogLevelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.log_level
    import capo_iot_wireless.types.resource_identifier
    import capo_iot_wireless.types.resource_type


class PutResourceLogLevelRequest(TypedDict, closed=True):
    resource_identifier: (
        "capo_iot_wireless.types.resource_identifier.ResourceIdentifier"
    )
    resource_type: "capo_iot_wireless.types.resource_type.ResourceType"
    """<p>The type of resource, which can be <code>WirelessDevice</code>, <code>WirelessGateway</code>, or <code>FuotaTask</code>.</p>"""
    log_level: "capo_iot_wireless.types.log_level.LogLevel"


# --- restJson1 ser/de ---
def serialize_json(value: PutResourceLogLevelRequest) -> dict:
    out: dict = {}
    import capo_iot_wireless.types.log_level

    out["LogLevel"] = capo_iot_wireless.types.log_level.serialize_json(
        value["log_level"]
    )
    return out


def deserialize_json(data: dict) -> PutResourceLogLevelRequest:
    out: PutResourceLogLevelRequest = {}  # type: ignore[typeddict-item]
    if data.get("LogLevel") is not None:
        import capo_iot_wireless.types.log_level

        out["log_level"] = capo_iot_wireless.types.log_level.deserialize_json(
            data["LogLevel"]
        )
    else:
        import typing

        out["log_level"] = typing.cast("capo_iot_wireless.types.log_level.LogLevel", "")
    return out
