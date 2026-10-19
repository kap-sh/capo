"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GreengrassV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.core_device_operating_system
    import capo_iotsitewise.types.core_device_thing_name


class GreengrassV2(TypedDict, closed=True):
    core_device_thing_name: (
        "capo_iotsitewise.types.core_device_thing_name.CoreDeviceThingName"
    )
    """<p>The name of the IoT thing for your IoT Greengrass V2 core device.</p>"""
    core_device_operating_system: NotRequired[
        "capo_iotsitewise.types.core_device_operating_system.CoreDeviceOperatingSystem"
    ]
    """<p>The operating system of the core device in IoT Greengrass V2. Specifying the operating system is required for MQTT-enabled, V3 gateways (<code>gatewayVersion</code> <code>3</code>) and not applicable for Classic stream, V2 gateways (<code>gatewayVersion</code> <code>2</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GreengrassV2) -> dict:
    out: dict = {}
    out["coreDeviceThingName"] = value["core_device_thing_name"]
    if "core_device_operating_system" in value:
        import capo_iotsitewise.types.core_device_operating_system

        out["coreDeviceOperatingSystem"] = (
            capo_iotsitewise.types.core_device_operating_system.serialize_json(
                value["core_device_operating_system"]
            )
        )
    return out


def deserialize_json(data: dict) -> GreengrassV2:
    out: GreengrassV2 = {}  # type: ignore[typeddict-item]
    if data.get("coreDeviceThingName") is not None:
        out["core_device_thing_name"] = data["coreDeviceThingName"]
    else:
        out["core_device_thing_name"] = ""
    if data.get("coreDeviceOperatingSystem") is not None:
        import capo_iotsitewise.types.core_device_operating_system

        out["core_device_operating_system"] = (
            capo_iotsitewise.types.core_device_operating_system.deserialize_json(
                data["coreDeviceOperatingSystem"]
            )
        )
    return out
