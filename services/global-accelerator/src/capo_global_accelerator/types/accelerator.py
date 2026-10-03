"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#Accelerator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.accelerator_events
    import capo_global_accelerator.types.accelerator_status
    import capo_global_accelerator.types.generic_boolean
    import capo_global_accelerator.types.generic_string
    import capo_global_accelerator.types.ip_address_type
    import capo_global_accelerator.types.ip_sets
    import capo_global_accelerator.types.timestamp


class Accelerator(TypedDict, closed=True):
    accelerator_arn: NotRequired[
        "capo_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The Amazon Resource Name (ARN) of the accelerator.</p>"""
    name: NotRequired["capo_global_accelerator.types.generic_string.GenericString"]
    """<p>The name of the accelerator. The name must contain only alphanumeric characters or hyphens (-), and must not begin or end with a hyphen.</p>"""
    ip_address_type: NotRequired[
        "capo_global_accelerator.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address type that an accelerator supports. For a standard accelerator, the value can be IPV4 or DUAL_STACK.</p>"""
    enabled: NotRequired["capo_global_accelerator.types.generic_boolean.GenericBoolean"]
    """<p>Indicates whether the accelerator is enabled. The value is true or false. The default value is true. </p> <p>If the value is set to true, the accelerator cannot be deleted. If set to false, accelerator can be deleted.</p>"""
    ip_sets: NotRequired["capo_global_accelerator.types.ip_sets.IpSets"]
    """<p>The static IP addresses that Global Accelerator associates with the accelerator.</p>"""
    dns_name: NotRequired["capo_global_accelerator.types.generic_string.GenericString"]
    """<p>The Domain Name System (DNS) name that Global Accelerator creates that points to an accelerator's static IPv4 addresses.</p> <p>The naming convention for the DNS name for an accelerator is the following: A lowercase letter a, followed by a 16-bit random hex string, followed by .awsglobalaccelerator.com. For example: a1234567890abcdef.awsglobalaccelerator.com.</p> <p>If you have a dual-stack accelerator, you also have a second DNS name, <code>DualStackDnsName</code>, that points to both the A record and the AAAA record for all four static addresses for the accelerator: two IPv4 addresses and two IPv6 addresses.</p> <p>For more information about the default DNS name, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/dns-addressing-custom-domains.dns-addressing.html"> Support for DNS addressing in Global Accelerator</a> in the <i>Global Accelerator Developer Guide</i>.</p>"""
    status: NotRequired[
        "capo_global_accelerator.types.accelerator_status.AcceleratorStatus"
    ]
    """<p>Describes the deployment status of the accelerator.</p>"""
    created_time: NotRequired["capo_global_accelerator.types.timestamp.Timestamp"]
    """<p>The date and time that the accelerator was created.</p>"""
    last_modified_time: NotRequired["capo_global_accelerator.types.timestamp.Timestamp"]
    """<p>The date and time that the accelerator was last modified.</p>"""
    dual_stack_dns_name: NotRequired[
        "capo_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The Domain Name System (DNS) name that Global Accelerator creates that points to a dual-stack accelerator's four static IP addresses: two IPv4 addresses and two IPv6 addresses.</p> <p>The naming convention for the dual-stack DNS name is the following: A lowercase letter a, followed by a 16-bit random hex string, followed by .dualstack.awsglobalaccelerator.com. For example: a1234567890abcdef.dualstack.awsglobalaccelerator.com.</p> <p>Note: Global Accelerator also assigns a default DNS name, <code>DnsName</code>, to your accelerator that points just to the static IPv4 addresses. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.html#about-accelerators.dns-addressing"> Support for DNS addressing in Global Accelerator</a> in the <i>Global Accelerator Developer Guide</i>.</p>"""
    events: NotRequired[
        "capo_global_accelerator.types.accelerator_events.AcceleratorEvents"
    ]
    """<p>A history of changes that you make to an accelerator in Global Accelerator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Accelerator) -> dict:
    out: dict = {}
    if "accelerator_arn" in value:
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
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "ip_sets" in value:
        import capo_global_accelerator.types.ip_sets

        out["IpSets"] = capo_global_accelerator.types.ip_sets.serialize_aws_json_1_1(
            value["ip_sets"]
        )
    if "dns_name" in value:
        out["DnsName"] = value["dns_name"]
    if "status" in value:
        import capo_global_accelerator.types.accelerator_status

        out["Status"] = (
            capo_global_accelerator.types.accelerator_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "created_time" in value:
        import capo_global_accelerator.types.timestamp

        out["CreatedTime"] = (
            capo_global_accelerator.types.timestamp.serialize_aws_json_1_1(
                value["created_time"]
            )
        )
    if "last_modified_time" in value:
        import capo_global_accelerator.types.timestamp

        out["LastModifiedTime"] = (
            capo_global_accelerator.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "dual_stack_dns_name" in value:
        out["DualStackDnsName"] = value["dual_stack_dns_name"]
    if "events" in value:
        import capo_global_accelerator.types.accelerator_events

        out["Events"] = (
            capo_global_accelerator.types.accelerator_events.serialize_aws_json_1_1(
                value["events"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Accelerator:
    out: Accelerator = {}  # type: ignore[typeddict-item]
    if data.get("AcceleratorArn") is not None:
        out["accelerator_arn"] = data["AcceleratorArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("IpAddressType") is not None:
        import capo_global_accelerator.types.ip_address_type

        out["ip_address_type"] = (
            capo_global_accelerator.types.ip_address_type.deserialize_aws_json_1_1(
                data["IpAddressType"]
            )
        )
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("IpSets") is not None:
        import capo_global_accelerator.types.ip_sets

        out["ip_sets"] = capo_global_accelerator.types.ip_sets.deserialize_aws_json_1_1(
            data["IpSets"]
        )
    if data.get("DnsName") is not None:
        out["dns_name"] = data["DnsName"]
    if data.get("Status") is not None:
        import capo_global_accelerator.types.accelerator_status

        out["status"] = (
            capo_global_accelerator.types.accelerator_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("CreatedTime") is not None:
        import capo_global_accelerator.types.timestamp

        out["created_time"] = (
            capo_global_accelerator.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedTime"]
            )
        )
    if data.get("LastModifiedTime") is not None:
        import capo_global_accelerator.types.timestamp

        out["last_modified_time"] = (
            capo_global_accelerator.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("DualStackDnsName") is not None:
        out["dual_stack_dns_name"] = data["DualStackDnsName"]
    if data.get("Events") is not None:
        import capo_global_accelerator.types.accelerator_events

        out["events"] = (
            capo_global_accelerator.types.accelerator_events.deserialize_aws_json_1_1(
                data["Events"]
            )
        )
    return out
