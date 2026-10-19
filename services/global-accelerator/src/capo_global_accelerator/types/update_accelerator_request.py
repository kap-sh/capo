"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#UpdateAcceleratorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.generic_boolean
    import capo_global_accelerator.types.generic_string
    import capo_global_accelerator.types.ip_address_type
    import capo_global_accelerator.types.ip_addresses


class UpdateAcceleratorRequest(TypedDict, closed=True):
    accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the accelerator to update.</p>"""
    name: NotRequired["capo_global_accelerator.types.generic_string.GenericString"]
    """<p>The name of the accelerator. The name can have a maximum of 64 characters, must contain only alphanumeric characters, periods (.), or hyphens (-), and must not begin or end with a hyphen or period.</p>"""
    ip_address_type: NotRequired[
        "capo_global_accelerator.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address type that an accelerator supports. For a standard accelerator, the value can be IPV4 or DUAL_STACK.</p>"""
    ip_addresses: NotRequired["capo_global_accelerator.types.ip_addresses.IpAddresses"]
    """<p>The IP addresses for an accelerator.</p>"""
    enabled: NotRequired["capo_global_accelerator.types.generic_boolean.GenericBoolean"]
    """<p>Indicates whether an accelerator is enabled. The value is true or false. The default value is true. </p> <p>If the value is set to true, the accelerator cannot be deleted. If set to false, the accelerator can be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAcceleratorRequest) -> dict:
    out: dict = {}
    out["AcceleratorArn"] = value["accelerator_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "ip_address_type" in value:
        import capo_global_accelerator.types.ip_address_type

        out["IpAddressType"] = (
            capo_global_accelerator.types.ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    if "ip_addresses" in value:
        import capo_global_accelerator.types.ip_addresses

        out["IpAddresses"] = (
            capo_global_accelerator.types.ip_addresses.serialize_aws_json_1_1(
                value["ip_addresses"]
            )
        )
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAcceleratorRequest:
    out: UpdateAcceleratorRequest = {}  # type: ignore[typeddict-item]
    if data.get("AcceleratorArn") is not None:
        out["accelerator_arn"] = data["AcceleratorArn"]
    else:
        out["accelerator_arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("IpAddressType") is not None:
        import capo_global_accelerator.types.ip_address_type

        out["ip_address_type"] = (
            capo_global_accelerator.types.ip_address_type.deserialize_aws_json_1_1(
                data["IpAddressType"]
            )
        )
    if data.get("IpAddresses") is not None:
        import capo_global_accelerator.types.ip_addresses

        out["ip_addresses"] = (
            capo_global_accelerator.types.ip_addresses.deserialize_aws_json_1_1(
                data["IpAddresses"]
            )
        )
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    return out
