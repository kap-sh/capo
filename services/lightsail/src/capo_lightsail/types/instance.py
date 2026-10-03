"""Generated from Smithy shape ``com.amazonaws.lightsail#Instance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.add_on_list
    import capo_lightsail.types.boolean
    import capo_lightsail.types.instance_hardware
    import capo_lightsail.types.instance_metadata_options
    import capo_lightsail.types.instance_networking
    import capo_lightsail.types.instance_state
    import capo_lightsail.types.ip_address
    import capo_lightsail.types.ip_address_type
    import capo_lightsail.types.ipv6_address_list
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.resource_location
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.resource_type
    import capo_lightsail.types.string
    import capo_lightsail.types.tag_list


class Instance(TypedDict, closed=True):
    name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The name the user gave the instance (<code>Amazon_Linux_2023-1</code>).</p>"""
    arn: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the instance (<code>arn:aws:lightsail:us-east-2:123456789101:Instance/244ad76f-8aad-4741-809f-12345EXAMPLE</code>).</p>"""
    support_code: NotRequired["capo_lightsail.types.string.string"]
    """<p>The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.</p>"""
    created_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the instance was created (<code>1479734909.17</code>) in Unix time format.</p>"""
    location: NotRequired["capo_lightsail.types.resource_location.ResourceLocation"]
    """<p>The region name and Availability Zone where the instance is located.</p>"""
    resource_type: NotRequired["capo_lightsail.types.resource_type.ResourceType"]
    """<p>The type of resource (usually <code>Instance</code>).</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values for the resource. For more information about tags in Lightsail, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags">Amazon Lightsail Developer Guide</a>.</p>"""
    blueprint_id: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The blueprint ID (<code>amazon_linux_2023</code>).</p>"""
    blueprint_name: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The friendly name of the blueprint (<code>Amazon Linux 2023</code>).</p>"""
    bundle_id: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The bundle for the instance (<code>micro_x_x</code>).</p>"""
    add_ons: NotRequired["capo_lightsail.types.add_on_list.AddOnList"]
    """<p>An array of objects representing the add-ons enabled on the instance.</p>"""
    is_static_ip: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether this instance has a static IP assigned to it.</p>"""
    private_ip_address: NotRequired["capo_lightsail.types.ip_address.IpAddress"]
    """<p>The private IP address of the instance.</p>"""
    public_ip_address: NotRequired["capo_lightsail.types.ip_address.IpAddress"]
    """<p>The public IP address of the instance.</p>"""
    ipv6_addresses: NotRequired[
        "capo_lightsail.types.ipv6_address_list.Ipv6AddressList"
    ]
    """<p>The IPv6 addresses of the instance.</p>"""
    ip_address_type: NotRequired["capo_lightsail.types.ip_address_type.IpAddressType"]
    """<p>The IP address type of the instance.</p> <p>The possible values are <code>ipv4</code> for IPv4 only, <code>ipv6</code> for IPv6 only, and <code>dualstack</code> for IPv4 and IPv6.</p>"""
    hardware: NotRequired["capo_lightsail.types.instance_hardware.InstanceHardware"]
    """<p>The size of the vCPU and the amount of RAM for the instance.</p>"""
    networking: NotRequired[
        "capo_lightsail.types.instance_networking.InstanceNetworking"
    ]
    """<p>Information about the public ports and monthly data transfer rates for the instance.</p>"""
    state: NotRequired["capo_lightsail.types.instance_state.InstanceState"]
    """<p>The status code and the state (<code>running</code>) for the instance.</p>"""
    username: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The user name for connecting to the instance (<code>ec2-user</code>).</p>"""
    ssh_key_name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the SSH key being used to connect to the instance (<code>LightsailDefaultKeyPair</code>).</p>"""
    metadata_options: NotRequired[
        "capo_lightsail.types.instance_metadata_options.InstanceMetadataOptions"
    ]
    """<p>The metadata options for the Amazon Lightsail instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Instance) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "support_code" in value:
        out["supportCode"] = value["support_code"]
    if "created_at" in value:
        import capo_lightsail.types.iso_date

        out["createdAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "location" in value:
        import capo_lightsail.types.resource_location

        out["location"] = capo_lightsail.types.resource_location.serialize_aws_json_1_1(
            value["location"]
        )
    if "resource_type" in value:
        import capo_lightsail.types.resource_type

        out["resourceType"] = capo_lightsail.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "blueprint_id" in value:
        out["blueprintId"] = value["blueprint_id"]
    if "blueprint_name" in value:
        out["blueprintName"] = value["blueprint_name"]
    if "bundle_id" in value:
        out["bundleId"] = value["bundle_id"]
    if "add_ons" in value:
        import capo_lightsail.types.add_on_list

        out["addOns"] = capo_lightsail.types.add_on_list.serialize_aws_json_1_1(
            value["add_ons"]
        )
    if "is_static_ip" in value:
        out["isStaticIp"] = value["is_static_ip"]
    if "private_ip_address" in value:
        out["privateIpAddress"] = value["private_ip_address"]
    if "public_ip_address" in value:
        out["publicIpAddress"] = value["public_ip_address"]
    if "ipv6_addresses" in value:
        import capo_lightsail.types.ipv6_address_list

        out["ipv6Addresses"] = (
            capo_lightsail.types.ipv6_address_list.serialize_aws_json_1_1(
                value["ipv6_addresses"]
            )
        )
    if "ip_address_type" in value:
        import capo_lightsail.types.ip_address_type

        out["ipAddressType"] = (
            capo_lightsail.types.ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    if "hardware" in value:
        import capo_lightsail.types.instance_hardware

        out["hardware"] = capo_lightsail.types.instance_hardware.serialize_aws_json_1_1(
            value["hardware"]
        )
    if "networking" in value:
        import capo_lightsail.types.instance_networking

        out["networking"] = (
            capo_lightsail.types.instance_networking.serialize_aws_json_1_1(
                value["networking"]
            )
        )
    if "state" in value:
        import capo_lightsail.types.instance_state

        out["state"] = capo_lightsail.types.instance_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "username" in value:
        out["username"] = value["username"]
    if "ssh_key_name" in value:
        out["sshKeyName"] = value["ssh_key_name"]
    if "metadata_options" in value:
        import capo_lightsail.types.instance_metadata_options

        out["metadataOptions"] = (
            capo_lightsail.types.instance_metadata_options.serialize_aws_json_1_1(
                value["metadata_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Instance:
    out: Instance = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("supportCode") is not None:
        out["support_code"] = data["supportCode"]
    if data.get("createdAt") is not None:
        import capo_lightsail.types.iso_date

        out["created_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if data.get("location") is not None:
        import capo_lightsail.types.resource_location

        out["location"] = (
            capo_lightsail.types.resource_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    if data.get("resourceType") is not None:
        import capo_lightsail.types.resource_type

        out["resource_type"] = (
            capo_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("blueprintId") is not None:
        out["blueprint_id"] = data["blueprintId"]
    if data.get("blueprintName") is not None:
        out["blueprint_name"] = data["blueprintName"]
    if data.get("bundleId") is not None:
        out["bundle_id"] = data["bundleId"]
    if data.get("addOns") is not None:
        import capo_lightsail.types.add_on_list

        out["add_ons"] = capo_lightsail.types.add_on_list.deserialize_aws_json_1_1(
            data["addOns"]
        )
    if data.get("isStaticIp") is not None:
        out["is_static_ip"] = data["isStaticIp"]
    if data.get("privateIpAddress") is not None:
        out["private_ip_address"] = data["privateIpAddress"]
    if data.get("publicIpAddress") is not None:
        out["public_ip_address"] = data["publicIpAddress"]
    if data.get("ipv6Addresses") is not None:
        import capo_lightsail.types.ipv6_address_list

        out["ipv6_addresses"] = (
            capo_lightsail.types.ipv6_address_list.deserialize_aws_json_1_1(
                data["ipv6Addresses"]
            )
        )
    if data.get("ipAddressType") is not None:
        import capo_lightsail.types.ip_address_type

        out["ip_address_type"] = (
            capo_lightsail.types.ip_address_type.deserialize_aws_json_1_1(
                data["ipAddressType"]
            )
        )
    if data.get("hardware") is not None:
        import capo_lightsail.types.instance_hardware

        out["hardware"] = (
            capo_lightsail.types.instance_hardware.deserialize_aws_json_1_1(
                data["hardware"]
            )
        )
    if data.get("networking") is not None:
        import capo_lightsail.types.instance_networking

        out["networking"] = (
            capo_lightsail.types.instance_networking.deserialize_aws_json_1_1(
                data["networking"]
            )
        )
    if data.get("state") is not None:
        import capo_lightsail.types.instance_state

        out["state"] = capo_lightsail.types.instance_state.deserialize_aws_json_1_1(
            data["state"]
        )
    if data.get("username") is not None:
        out["username"] = data["username"]
    if data.get("sshKeyName") is not None:
        out["ssh_key_name"] = data["sshKeyName"]
    if data.get("metadataOptions") is not None:
        import capo_lightsail.types.instance_metadata_options

        out["metadata_options"] = (
            capo_lightsail.types.instance_metadata_options.deserialize_aws_json_1_1(
                data["metadataOptions"]
            )
        )
    return out
