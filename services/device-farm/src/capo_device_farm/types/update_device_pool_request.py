"""Generated from Smithy shape ``com.amazonaws.devicefarm#UpdateDevicePoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.boolean
    import capo_device_farm.types.integer
    import capo_device_farm.types.message
    import capo_device_farm.types.name
    import capo_device_farm.types.rules


class UpdateDevicePoolRequest(TypedDict, closed=True):
    arn: "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the Device Farm device pool to update.</p>"""
    name: NotRequired["capo_device_farm.types.name.Name"]
    """<p>A string that represents the name of the device pool to update.</p>"""
    description: NotRequired["capo_device_farm.types.message.Message"]
    """<p>A description of the device pool to update.</p>"""
    rules: NotRequired["capo_device_farm.types.rules.Rules"]
    """<p>Represents the rules to modify for the device pool. Updating rules is optional. If you update rules for your request, the update replaces the existing rules.</p>"""
    max_devices: NotRequired["capo_device_farm.types.integer.Integer"]
    """<p>The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and that meet the criteria that you assign for the <code>rules</code> parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.</p> <p>By specifying the maximum number of devices, you can control the costs that you incur by running tests.</p> <p>If you use this parameter in your request, you cannot use the <code>clearMaxDevices</code> parameter in the same request.</p>"""
    clear_max_devices: NotRequired["capo_device_farm.types.boolean.Boolean"]
    """<p>Sets whether the <code>maxDevices</code> parameter applies to your device pool. If you set this parameter to <code>true</code>, the <code>maxDevices</code> parameter does not apply, and Device Farm does not limit the number of devices that it adds to your device pool. In this case, Device Farm adds all available devices that meet the criteria specified in the <code>rules</code> parameter.</p> <p>If you use this parameter in your request, you cannot use the <code>maxDevices</code> parameter in the same request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDevicePoolRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "rules" in value:
        import capo_device_farm.types.rules

        out["rules"] = capo_device_farm.types.rules.serialize_aws_json_1_1(
            value["rules"]
        )
    if "max_devices" in value:
        out["maxDevices"] = value["max_devices"]
    if "clear_max_devices" in value:
        out["clearMaxDevices"] = value["clear_max_devices"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDevicePoolRequest:
    out: UpdateDevicePoolRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("rules") is not None:
        import capo_device_farm.types.rules

        out["rules"] = capo_device_farm.types.rules.deserialize_aws_json_1_1(
            data["rules"]
        )
    if data.get("maxDevices") is not None:
        out["max_devices"] = data["maxDevices"]
    if data.get("clearMaxDevices") is not None:
        out["clear_max_devices"] = data["clearMaxDevices"]
    return out
