"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CreateAcceleratorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_global_accelerator.types.generic_boolean
    import capo_global_accelerator.types.generic_string
    import capo_global_accelerator.types.idempotency_token
    import capo_global_accelerator.types.ip_address_type
    import capo_global_accelerator.types.ip_addresses
    import capo_global_accelerator.types.tags


class CreateAcceleratorRequest(TypedDict, closed=True):
    name: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The name of the accelerator. The name can have a maximum of 64 characters, must contain only alphanumeric characters, periods (.), or hyphens (-), and must not begin or end with a hyphen or period.</p>"""
    ip_address_type: NotRequired[
        "capo_global_accelerator.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address type that an accelerator supports. For a standard accelerator, the value can be IPV4 or DUAL_STACK.</p>"""
    ip_addresses: NotRequired["capo_global_accelerator.types.ip_addresses.IpAddresses"]
    """<p>Optionally, if you've added your own IP address pool to Global Accelerator (BYOIP), you can choose an IPv4 address from your own pool to use for the accelerator's static IPv4 address when you create an accelerator. </p> <p>After you bring an address range to Amazon Web Services, it appears in your account as an address pool. When you create an accelerator, you can assign one IPv4 address from your range to it. Global Accelerator assigns you a second static IPv4 address from an Amazon IP address range. If you bring two IPv4 address ranges to Amazon Web Services, you can assign one IPv4 address from each range to your accelerator. This restriction is because Global Accelerator assigns each address range to a different network zone, for high availability.</p> <p>You can specify one or two addresses, separated by a space. Do not include the /32 suffix.</p> <p>Note that you can't update IP addresses for an existing accelerator. To change them, you must create a new accelerator with the new addresses.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html">Bring your own IP addresses (BYOIP)</a> in the <i>Global Accelerator Developer Guide</i>.</p>"""
    enabled: NotRequired["capo_global_accelerator.types.generic_boolean.GenericBoolean"]
    """<p>Indicates whether an accelerator is enabled. The value is true or false. The default value is true. </p> <p>If the value is set to true, an accelerator cannot be deleted. If set to false, the accelerator can be deleted.</p>"""
    idempotency_token: (
        "capo_global_accelerator.types.idempotency_token.IdempotencyToken"
    )
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of an accelerator.</p>"""
    tags: NotRequired["capo_global_accelerator.types.tags.Tags"]
    """<p>Create tags for an accelerator.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html">Tagging in Global Accelerator</a> in the <i>Global Accelerator Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAcceleratorRequest) -> dict:
    out: dict = {}
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
    out["IdempotencyToken"] = value["idempotency_token"]
    if "tags" in value:
        import capo_global_accelerator.types.tags

        out["Tags"] = capo_global_accelerator.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAcceleratorRequest:
    out: CreateAcceleratorRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateAcceleratorRequest.name required")
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
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        raise DeserializationError(
            "CreateAcceleratorRequest.idempotency_token required"
        )
    if data.get("Tags") is not None:
        import capo_global_accelerator.types.tags

        out["tags"] = capo_global_accelerator.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
