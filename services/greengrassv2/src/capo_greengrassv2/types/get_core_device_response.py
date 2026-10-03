"""Generated from Smithy shape ``com.amazonaws.greengrassv2#GetCoreDeviceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.core_device_architecture_string
    import capo_greengrassv2.types.core_device_platform_string
    import capo_greengrassv2.types.core_device_runtime_string
    import capo_greengrassv2.types.core_device_status
    import capo_greengrassv2.types.core_device_thing_name
    import capo_greengrassv2.types.ggc_version
    import capo_greengrassv2.types.tag_map
    import capo_greengrassv2.types.timestamp


class GetCoreDeviceResponse(TypedDict, closed=True):
    core_device_thing_name: NotRequired[
        "capo_greengrassv2.types.core_device_thing_name.CoreDeviceThingName"
    ]
    """<p>The name of the core device. This is also the name of the IoT thing.</p>"""
    core_version: NotRequired["capo_greengrassv2.types.ggc_version.GGCVersion"]
    """<p>The version of the IoT Greengrass Core software that the core device runs. This version is equivalent to the version of the Greengrass nucleus component that runs on the core device. For more information, see the <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html">Greengrass nucleus component</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p>"""
    platform: NotRequired[
        "capo_greengrassv2.types.core_device_platform_string.CoreDevicePlatformString"
    ]
    """<p>The operating system platform that the core device runs.</p>"""
    architecture: NotRequired[
        "capo_greengrassv2.types.core_device_architecture_string.CoreDeviceArchitectureString"
    ]
    """<p>The computer architecture of the core device.</p>"""
    runtime: NotRequired[
        "capo_greengrassv2.types.core_device_runtime_string.CoreDeviceRuntimeString"
    ]
    """<p>The runtime for the core device. The runtime can be:</p> <ul> <li> <p> <code>aws_nucleus_classic</code> </p> </li> <li> <p> <code>aws_nucleus_lite</code> </p> </li> </ul>"""
    status: NotRequired["capo_greengrassv2.types.core_device_status.CoreDeviceStatus"]
    """<p>The status of the core device. The core device status can be:</p> <ul> <li> <p> <code>HEALTHY</code> – The IoT Greengrass Core software and all components run on the core device without issue.</p> </li> <li> <p> <code>UNHEALTHY</code> – The IoT Greengrass Core software or a component is in a failed state on the core device.</p> </li> </ul>"""
    last_status_update_timestamp: NotRequired[
        "capo_greengrassv2.types.timestamp.Timestamp"
    ]
    """<p>The time at which the core device's status last updated, expressed in ISO 8601 format.</p>"""
    tags: NotRequired["capo_greengrassv2.types.tag_map.TagMap"]
    """<p>A list of key-value pairs that contain metadata for the resource. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html">Tag your resources</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCoreDeviceResponse) -> dict:
    out: dict = {}
    if "core_device_thing_name" in value:
        out["coreDeviceThingName"] = value["core_device_thing_name"]
    if "core_version" in value:
        out["coreVersion"] = value["core_version"]
    if "platform" in value:
        out["platform"] = value["platform"]
    if "architecture" in value:
        out["architecture"] = value["architecture"]
    if "runtime" in value:
        out["runtime"] = value["runtime"]
    if "status" in value:
        import capo_greengrassv2.types.core_device_status

        out["status"] = capo_greengrassv2.types.core_device_status.serialize_json(
            value["status"]
        )
    if "last_status_update_timestamp" in value:
        import capo_greengrassv2.types.timestamp

        out["lastStatusUpdateTimestamp"] = (
            capo_greengrassv2.types.timestamp.serialize_json(
                value["last_status_update_timestamp"]
            )
        )
    if "tags" in value:
        import capo_greengrassv2.types.tag_map

        out["tags"] = capo_greengrassv2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetCoreDeviceResponse:
    out: GetCoreDeviceResponse = {}  # type: ignore[typeddict-item]
    if data.get("coreDeviceThingName") is not None:
        out["core_device_thing_name"] = data["coreDeviceThingName"]
    if data.get("coreVersion") is not None:
        out["core_version"] = data["coreVersion"]
    if data.get("platform") is not None:
        out["platform"] = data["platform"]
    if data.get("architecture") is not None:
        out["architecture"] = data["architecture"]
    if data.get("runtime") is not None:
        out["runtime"] = data["runtime"]
    if data.get("status") is not None:
        import capo_greengrassv2.types.core_device_status

        out["status"] = capo_greengrassv2.types.core_device_status.deserialize_json(
            data["status"]
        )
    if data.get("lastStatusUpdateTimestamp") is not None:
        import capo_greengrassv2.types.timestamp

        out["last_status_update_timestamp"] = (
            capo_greengrassv2.types.timestamp.deserialize_json(
                data["lastStatusUpdateTimestamp"]
            )
        )
    if data.get("tags") is not None:
        import capo_greengrassv2.types.tag_map

        out["tags"] = capo_greengrassv2.types.tag_map.deserialize_json(data["tags"])
    return out
