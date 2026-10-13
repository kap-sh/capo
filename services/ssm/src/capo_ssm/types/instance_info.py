"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceInfo``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.agent_type
    import capo_ssm.types.agent_version
    import capo_ssm.types.availability_zone
    import capo_ssm.types.availability_zone_id
    import capo_ssm.types.computer_name
    import capo_ssm.types.instance_status
    import capo_ssm.types.ip_address
    import capo_ssm.types.managed_status
    import capo_ssm.types.node_name
    import capo_ssm.types.platform_name
    import capo_ssm.types.platform_type
    import capo_ssm.types.platform_version
    import capo_ssm.types.resource_type
    import capo_ssm.types.source_id
    import capo_ssm.types.source_location
    import capo_ssm.types.source_type


class InstanceInfo(TypedDict, closed=True):
    agent_type: NotRequired["capo_ssm.types.agent_type.AgentType"]
    """<p>The type of agent installed on the node.</p>"""
    agent_version: NotRequired["capo_ssm.types.agent_version.AgentVersion"]
    """<p>The version number of the agent installed on the node.</p>"""
    computer_name: NotRequired["capo_ssm.types.computer_name.ComputerName"]
    """<p>The fully qualified host name of the managed node.</p>"""
    instance_status: NotRequired["capo_ssm.types.instance_status.InstanceStatus"]
    """<p>The current status of the managed node.</p>"""
    ip_address: NotRequired["capo_ssm.types.ip_address.IPAddress"]
    """<p>The IP address of the managed node.</p>"""
    managed_status: NotRequired["capo_ssm.types.managed_status.ManagedStatus"]
    """<p>Indicates whether the node is managed by Systems Manager.</p>"""
    name: NotRequired["capo_ssm.types.node_name.NodeName"]
    """<p>The name assigned to the managed node.</p>"""
    platform_type: NotRequired["capo_ssm.types.platform_type.PlatformType"]
    """<p>The operating system platform type of the managed node.</p>"""
    platform_name: NotRequired["capo_ssm.types.platform_name.PlatformName"]
    """<p>The name of the operating system platform running on your managed node.</p>"""
    platform_version: NotRequired["capo_ssm.types.platform_version.PlatformVersion"]
    """<p>The version of the OS platform running on your managed node. </p>"""
    resource_type: NotRequired["capo_ssm.types.resource_type.ResourceType"]
    """<p>The type of instance, either an EC2 instance or another supported machine type in a hybrid fleet.</p>"""
    source_type: NotRequired["capo_ssm.types.source_type.SourceType"]
    """<p>The type of the source resource. For IoT Greengrass devices, <code>SourceType</code> is <code>AWS::IoT::Thing</code>.</p>"""
    source_id: NotRequired["capo_ssm.types.source_id.SourceId"]
    """<p>The ID of the source resource. For IoT Greengrass devices, <code>SourceId</code> is the Thing name.</p>"""
    source_location: NotRequired["capo_ssm.types.source_location.SourceLocation"]
    """<p>The location of the source resource in the third-party cloud environment.</p>"""
    availability_zone: NotRequired["capo_ssm.types.availability_zone.AvailabilityZone"]
    """<p>The Availability Zone where the managed node is located.</p>"""
    availability_zone_id: NotRequired[
        "capo_ssm.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The Availability Zone ID where the managed node is located.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceInfo) -> dict:
    out: dict = {}
    if "agent_type" in value:
        out["AgentType"] = value["agent_type"]
    if "agent_version" in value:
        out["AgentVersion"] = value["agent_version"]
    if "computer_name" in value:
        out["ComputerName"] = value["computer_name"]
    if "instance_status" in value:
        out["InstanceStatus"] = value["instance_status"]
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "managed_status" in value:
        import capo_ssm.types.managed_status

        out["ManagedStatus"] = capo_ssm.types.managed_status.serialize_aws_json_1_1(
            value["managed_status"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "platform_type" in value:
        import capo_ssm.types.platform_type

        out["PlatformType"] = capo_ssm.types.platform_type.serialize_aws_json_1_1(
            value["platform_type"]
        )
    if "platform_name" in value:
        out["PlatformName"] = value["platform_name"]
    if "platform_version" in value:
        out["PlatformVersion"] = value["platform_version"]
    if "resource_type" in value:
        import capo_ssm.types.resource_type

        out["ResourceType"] = capo_ssm.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    if "source_type" in value:
        import capo_ssm.types.source_type

        out["SourceType"] = capo_ssm.types.source_type.serialize_aws_json_1_1(
            value["source_type"]
        )
    if "source_id" in value:
        out["SourceId"] = value["source_id"]
    if "source_location" in value:
        out["SourceLocation"] = value["source_location"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "availability_zone_id" in value:
        out["AvailabilityZoneId"] = value["availability_zone_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceInfo:
    out: InstanceInfo = {}  # type: ignore[typeddict-item]
    if data.get("AgentType") is not None:
        out["agent_type"] = data["AgentType"]
    if data.get("AgentVersion") is not None:
        out["agent_version"] = data["AgentVersion"]
    if data.get("ComputerName") is not None:
        out["computer_name"] = data["ComputerName"]
    if data.get("InstanceStatus") is not None:
        out["instance_status"] = data["InstanceStatus"]
    if data.get("IpAddress") is not None:
        out["ip_address"] = data["IpAddress"]
    if data.get("ManagedStatus") is not None:
        import capo_ssm.types.managed_status

        out["managed_status"] = capo_ssm.types.managed_status.deserialize_aws_json_1_1(
            data["ManagedStatus"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("PlatformType") is not None:
        import capo_ssm.types.platform_type

        out["platform_type"] = capo_ssm.types.platform_type.deserialize_aws_json_1_1(
            data["PlatformType"]
        )
    if data.get("PlatformName") is not None:
        out["platform_name"] = data["PlatformName"]
    if data.get("PlatformVersion") is not None:
        out["platform_version"] = data["PlatformVersion"]
    if data.get("ResourceType") is not None:
        import capo_ssm.types.resource_type

        out["resource_type"] = capo_ssm.types.resource_type.deserialize_aws_json_1_1(
            data["ResourceType"]
        )
    if data.get("SourceType") is not None:
        import capo_ssm.types.source_type

        out["source_type"] = capo_ssm.types.source_type.deserialize_aws_json_1_1(
            data["SourceType"]
        )
    if data.get("SourceId") is not None:
        out["source_id"] = data["SourceId"]
    if data.get("SourceLocation") is not None:
        out["source_location"] = data["SourceLocation"]
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("AvailabilityZoneId") is not None:
        out["availability_zone_id"] = data["AvailabilityZoneId"]
    return out


def redact_sensitive(value: InstanceInfo) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ip_address" in value:
        out["ip_address"] = "*** Sensitive Data Redacted ***"
    return out
