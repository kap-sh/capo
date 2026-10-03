"""Generated from Smithy shape ``com.amazonaws.devicefarm#Device``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.boolean
    import capo_device_farm.types.cpu
    import capo_device_farm.types.device_availability
    import capo_device_farm.types.device_form_factor
    import capo_device_farm.types.device_instances
    import capo_device_farm.types.device_platform
    import capo_device_farm.types.long
    import capo_device_farm.types.name
    import capo_device_farm.types.resolution
    import capo_device_farm.types.string


class Device(TypedDict, closed=True):
    arn: NotRequired["capo_device_farm.types.amazon_resource_name.AmazonResourceName"]
    """<p>The device's ARN.</p>"""
    name: NotRequired["capo_device_farm.types.name.Name"]
    """<p>The device's display name.</p>"""
    manufacturer: NotRequired["capo_device_farm.types.string.String"]
    """<p>The device's manufacturer name.</p>"""
    model: NotRequired["capo_device_farm.types.string.String"]
    """<p>The device's model name.</p>"""
    model_id: NotRequired["capo_device_farm.types.string.String"]
    """<p>The device's model ID.</p>"""
    form_factor: NotRequired[
        "capo_device_farm.types.device_form_factor.DeviceFormFactor"
    ]
    """<p>The device's form factor.</p> <p>Allowed values include:</p> <ul> <li> <p>PHONE</p> </li> <li> <p>TABLET</p> </li> </ul>"""
    platform: NotRequired["capo_device_farm.types.device_platform.DevicePlatform"]
    """<p>The device's platform.</p> <p>Allowed values include:</p> <ul> <li> <p>ANDROID</p> </li> <li> <p>IOS</p> </li> </ul>"""
    os: NotRequired["capo_device_farm.types.string.String"]
    """<p>The device's operating system type.</p>"""
    cpu: NotRequired["capo_device_farm.types.cpu.CPU"]
    """<p>Information about the device's CPU.</p>"""
    resolution: NotRequired["capo_device_farm.types.resolution.Resolution"]
    """<p>The resolution of the device.</p>"""
    heap_size: NotRequired["capo_device_farm.types.long.Long"]
    """<p>The device's heap size, expressed in bytes.</p>"""
    memory: NotRequired["capo_device_farm.types.long.Long"]
    """<p>The device's total memory size, expressed in bytes.</p>"""
    image: NotRequired["capo_device_farm.types.string.String"]
    """<p>The device's image name.</p>"""
    carrier: NotRequired["capo_device_farm.types.string.String"]
    """<p>The device's carrier.</p>"""
    radio: NotRequired["capo_device_farm.types.string.String"]
    """<p>The device's radio.</p>"""
    remote_access_enabled: NotRequired["capo_device_farm.types.boolean.Boolean"]
    """<p>Specifies whether remote access has been enabled for the specified device.</p>"""
    remote_debug_enabled: NotRequired["capo_device_farm.types.boolean.Boolean"]
    """<p>This flag is set to <code>true</code> if remote debugging is enabled for the device.</p> <p>Remote debugging is <a href="https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html">no longer supported</a>.</p>"""
    fleet_type: NotRequired["capo_device_farm.types.string.String"]
    """<p>The type of fleet to which this device belongs. Possible values are PRIVATE and PUBLIC.</p>"""
    fleet_name: NotRequired["capo_device_farm.types.string.String"]
    """<p>The name of the fleet to which this device belongs.</p>"""
    instances: NotRequired["capo_device_farm.types.device_instances.DeviceInstances"]
    """<p>The instances that belong to this device.</p>"""
    availability: NotRequired[
        "capo_device_farm.types.device_availability.DeviceAvailability"
    ]
    """<p>Indicates how likely a device is available for a test run. Currently available in the <a>ListDevices</a> and GetDevice API methods.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Device) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "manufacturer" in value:
        out["manufacturer"] = value["manufacturer"]
    if "model" in value:
        out["model"] = value["model"]
    if "model_id" in value:
        out["modelId"] = value["model_id"]
    if "form_factor" in value:
        import capo_device_farm.types.device_form_factor

        out["formFactor"] = (
            capo_device_farm.types.device_form_factor.serialize_aws_json_1_1(
                value["form_factor"]
            )
        )
    if "platform" in value:
        import capo_device_farm.types.device_platform

        out["platform"] = capo_device_farm.types.device_platform.serialize_aws_json_1_1(
            value["platform"]
        )
    if "os" in value:
        out["os"] = value["os"]
    if "cpu" in value:
        import capo_device_farm.types.cpu

        out["cpu"] = capo_device_farm.types.cpu.serialize_aws_json_1_1(value["cpu"])
    if "resolution" in value:
        import capo_device_farm.types.resolution

        out["resolution"] = capo_device_farm.types.resolution.serialize_aws_json_1_1(
            value["resolution"]
        )
    if "heap_size" in value:
        out["heapSize"] = value["heap_size"]
    if "memory" in value:
        out["memory"] = value["memory"]
    if "image" in value:
        out["image"] = value["image"]
    if "carrier" in value:
        out["carrier"] = value["carrier"]
    if "radio" in value:
        out["radio"] = value["radio"]
    if "remote_access_enabled" in value:
        out["remoteAccessEnabled"] = value["remote_access_enabled"]
    if "remote_debug_enabled" in value:
        out["remoteDebugEnabled"] = value["remote_debug_enabled"]
    if "fleet_type" in value:
        out["fleetType"] = value["fleet_type"]
    if "fleet_name" in value:
        out["fleetName"] = value["fleet_name"]
    if "instances" in value:
        import capo_device_farm.types.device_instances

        out["instances"] = (
            capo_device_farm.types.device_instances.serialize_aws_json_1_1(
                value["instances"]
            )
        )
    if "availability" in value:
        import capo_device_farm.types.device_availability

        out["availability"] = (
            capo_device_farm.types.device_availability.serialize_aws_json_1_1(
                value["availability"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Device:
    out: Device = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("manufacturer") is not None:
        out["manufacturer"] = data["manufacturer"]
    if data.get("model") is not None:
        out["model"] = data["model"]
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    if data.get("formFactor") is not None:
        import capo_device_farm.types.device_form_factor

        out["form_factor"] = (
            capo_device_farm.types.device_form_factor.deserialize_aws_json_1_1(
                data["formFactor"]
            )
        )
    if data.get("platform") is not None:
        import capo_device_farm.types.device_platform

        out["platform"] = (
            capo_device_farm.types.device_platform.deserialize_aws_json_1_1(
                data["platform"]
            )
        )
    if data.get("os") is not None:
        out["os"] = data["os"]
    if data.get("cpu") is not None:
        import capo_device_farm.types.cpu

        out["cpu"] = capo_device_farm.types.cpu.deserialize_aws_json_1_1(data["cpu"])
    if data.get("resolution") is not None:
        import capo_device_farm.types.resolution

        out["resolution"] = capo_device_farm.types.resolution.deserialize_aws_json_1_1(
            data["resolution"]
        )
    if data.get("heapSize") is not None:
        out["heap_size"] = data["heapSize"]
    if data.get("memory") is not None:
        out["memory"] = data["memory"]
    if data.get("image") is not None:
        out["image"] = data["image"]
    if data.get("carrier") is not None:
        out["carrier"] = data["carrier"]
    if data.get("radio") is not None:
        out["radio"] = data["radio"]
    if data.get("remoteAccessEnabled") is not None:
        out["remote_access_enabled"] = data["remoteAccessEnabled"]
    if data.get("remoteDebugEnabled") is not None:
        out["remote_debug_enabled"] = data["remoteDebugEnabled"]
    if data.get("fleetType") is not None:
        out["fleet_type"] = data["fleetType"]
    if data.get("fleetName") is not None:
        out["fleet_name"] = data["fleetName"]
    if data.get("instances") is not None:
        import capo_device_farm.types.device_instances

        out["instances"] = (
            capo_device_farm.types.device_instances.deserialize_aws_json_1_1(
                data["instances"]
            )
        )
    if data.get("availability") is not None:
        import capo_device_farm.types.device_availability

        out["availability"] = (
            capo_device_farm.types.device_availability.deserialize_aws_json_1_1(
                data["availability"]
            )
        )
    return out
