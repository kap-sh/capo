"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateDevicePoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.integer
    import capo_device_farm.types.message
    import capo_device_farm.types.name
    import capo_device_farm.types.rules


class CreateDevicePoolRequest(TypedDict, closed=True):
    project_arn: "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the project for the device pool.</p>"""
    name: "capo_device_farm.types.name.Name"
    """<p>The device pool's name.</p>"""
    description: NotRequired["capo_device_farm.types.message.Message"]
    """<p>The device pool's description.</p>"""
    rules: "capo_device_farm.types.rules.Rules"
    """<p>The device pool's rules.</p>"""
    max_devices: NotRequired["capo_device_farm.types.integer.Integer"]
    """<p>The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and meet the criteria that you assign for the <code>rules</code> parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.</p> <p>By specifying the maximum number of devices, you can control the costs that you incur by running tests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDevicePoolRequest) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_device_farm.types.rules

    out["rules"] = capo_device_farm.types.rules.serialize_aws_json_1_1(value["rules"])
    if "max_devices" in value:
        out["maxDevices"] = value["max_devices"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDevicePoolRequest:
    out: CreateDevicePoolRequest = {}  # type: ignore[typeddict-item]
    if data.get("projectArn") is not None:
        out["project_arn"] = data["projectArn"]
    else:
        out["project_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("rules") is not None:
        import capo_device_farm.types.rules

        out["rules"] = capo_device_farm.types.rules.deserialize_aws_json_1_1(
            data["rules"]
        )
    else:
        out["rules"] = []
    if data.get("maxDevices") is not None:
        out["max_devices"] = data["maxDevices"]
    return out
