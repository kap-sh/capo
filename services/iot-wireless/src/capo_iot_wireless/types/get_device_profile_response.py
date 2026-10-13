"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetDeviceProfileResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.device_profile_arn
    import capo_iot_wireless.types.device_profile_id
    import capo_iot_wireless.types.device_profile_name
    import capo_iot_wireless.types.lo_ra_wan_device_profile
    import capo_iot_wireless.types.sidewalk_get_device_profile


class GetDeviceProfileResponse(TypedDict, closed=True):
    arn: NotRequired["capo_iot_wireless.types.device_profile_arn.DeviceProfileArn"]
    """<p>The Amazon Resource Name of the resource.</p>"""
    name: NotRequired["capo_iot_wireless.types.device_profile_name.DeviceProfileName"]
    """<p>The name of the resource.</p>"""
    id: NotRequired["capo_iot_wireless.types.device_profile_id.DeviceProfileId"]
    """<p>The ID of the device profile.</p>"""
    lo_ra_wan: NotRequired[
        "capo_iot_wireless.types.lo_ra_wan_device_profile.LoRaWANDeviceProfile"
    ]
    """<p>Information about the device profile.</p>"""
    sidewalk: NotRequired[
        "capo_iot_wireless.types.sidewalk_get_device_profile.SidewalkGetDeviceProfile"
    ]
    """<p>Information about the Sidewalk parameters in the device profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeviceProfileResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "lo_ra_wan" in value:
        import capo_iot_wireless.types.lo_ra_wan_device_profile

        out["LoRaWAN"] = (
            capo_iot_wireless.types.lo_ra_wan_device_profile.serialize_json(
                value["lo_ra_wan"]
            )
        )
    if "sidewalk" in value:
        import capo_iot_wireless.types.sidewalk_get_device_profile

        out["Sidewalk"] = (
            capo_iot_wireless.types.sidewalk_get_device_profile.serialize_json(
                value["sidewalk"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDeviceProfileResponse:
    out: GetDeviceProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("LoRaWAN") is not None:
        import capo_iot_wireless.types.lo_ra_wan_device_profile

        out["lo_ra_wan"] = (
            capo_iot_wireless.types.lo_ra_wan_device_profile.deserialize_json(
                data["LoRaWAN"]
            )
        )
    if data.get("Sidewalk") is not None:
        import capo_iot_wireless.types.sidewalk_get_device_profile

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_get_device_profile.deserialize_json(
                data["Sidewalk"]
            )
        )
    return out


def redact_sensitive(value: GetDeviceProfileResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sidewalk" in value:
        import capo_iot_wireless.types.sidewalk_get_device_profile

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_get_device_profile.redact_sensitive(
                value["sidewalk"]
            )
        )
    return out
