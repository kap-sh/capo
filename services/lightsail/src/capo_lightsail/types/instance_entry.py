"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.port_info_source_type
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.string


class InstanceEntry(TypedDict, closed=True):
    source_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the export snapshot record, which contains the exported Lightsail instance snapshot that will be used as the source of the new Amazon EC2 instance.</p> <p>Use the <code>get export snapshot records</code> operation to get a list of export snapshot records that you can use to create a CloudFormation stack.</p>"""
    instance_type: "capo_lightsail.types.non_empty_string.NonEmptyString"
    """<p>The instance type (<code>t2.micro</code>) to use for the new Amazon EC2 instance.</p>"""
    port_info_source: "capo_lightsail.types.port_info_source_type.PortInfoSourceType"
    """<p>The port configuration to use for the new Amazon EC2 instance.</p> <p>The following configuration options are available:</p> <ul> <li> <p> <code>DEFAULT</code> - Use the default firewall settings from the Lightsail instance blueprint. If this is specified, then IPv4 and IPv6 will be configured for the new instance that is created in Amazon EC2.</p> </li> <li> <p> <code>INSTANCE</code> - Use the configured firewall settings from the source Lightsail instance. If this is specified, the new instance that is created in Amazon EC2 will be configured to match the configuration of the source Lightsail instance. For example, if the source instance is configured for dual-stack (IPv4 and IPv6), then IPv4 and IPv6 will be configured for the new instance that is created in Amazon EC2. If the source instance is configured for IPv4 only, then only IPv4 will be configured for the new instance that is created in Amazon EC2.</p> </li> <li> <p> <code>NONE</code> - Use the default Amazon EC2 security group. If this is specified, then only IPv4 will be configured for the new instance that is created in Amazon EC2.</p> </li> <li> <p> <code>CLOSED</code> - All ports closed. If this is specified, then only IPv4 will be configured for the new instance that is created in Amazon EC2.</p> </li> </ul> <note> <p>If you configured <code>lightsail-connect</code> as a <code>cidrListAliases</code> on your instance, or if you chose to allow the Lightsail browser-based SSH or RDP clients to connect to your instance, that configuration is not carried over to your new Amazon EC2 instance.</p> </note>"""
    user_data: NotRequired["capo_lightsail.types.string.string"]
    """<p>A launch script you can create that configures a server with additional user data. For example, you might want to run <code>apt-get -y update</code>.</p> <note> <p>Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use <code>yum</code>, Debian and Ubuntu use <code>apt-get</code>, and FreeBSD uses <code>pkg</code>.</p> </note>"""
    availability_zone: "capo_lightsail.types.string.string"
    """<p>The Availability Zone for the new Amazon EC2 instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceEntry) -> dict:
    out: dict = {}
    out["sourceName"] = value["source_name"]
    out["instanceType"] = value["instance_type"]
    import capo_lightsail.types.port_info_source_type

    out["portInfoSource"] = (
        capo_lightsail.types.port_info_source_type.serialize_aws_json_1_1(
            value["port_info_source"]
        )
    )
    if "user_data" in value:
        out["userData"] = value["user_data"]
    out["availabilityZone"] = value["availability_zone"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceEntry:
    out: InstanceEntry = {}  # type: ignore[typeddict-item]
    if data.get("sourceName") is not None:
        out["source_name"] = data["sourceName"]
    else:
        out["source_name"] = ""
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    else:
        out["instance_type"] = ""
    if data.get("portInfoSource") is not None:
        import capo_lightsail.types.port_info_source_type

        out["port_info_source"] = (
            capo_lightsail.types.port_info_source_type.deserialize_aws_json_1_1(
                data["portInfoSource"]
            )
        )
    else:
        import typing

        out["port_info_source"] = typing.cast(
            "capo_lightsail.types.port_info_source_type.PortInfoSourceType", ""
        )
    if data.get("userData") is not None:
        out["user_data"] = data["userData"]
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    else:
        out["availability_zone"] = ""
    return out
