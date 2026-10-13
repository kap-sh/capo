"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceProperty``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.activation_id
    import capo_ssm.types.architecture
    import capo_ssm.types.availability_zone
    import capo_ssm.types.computer_name
    import capo_ssm.types.date_time
    import capo_ssm.types.iam_role
    import capo_ssm.types.instance_aggregated_association_overview
    import capo_ssm.types.instance_id
    import capo_ssm.types.instance_name
    import capo_ssm.types.instance_role
    import capo_ssm.types.instance_state
    import capo_ssm.types.instance_type
    import capo_ssm.types.ip_address
    import capo_ssm.types.key_name
    import capo_ssm.types.ping_status
    import capo_ssm.types.platform_name
    import capo_ssm.types.platform_type
    import capo_ssm.types.platform_version
    import capo_ssm.types.source_id
    import capo_ssm.types.source_location
    import capo_ssm.types.source_type
    import capo_ssm.types.status_name
    import capo_ssm.types.string
    import capo_ssm.types.version


class InstanceProperty(TypedDict, closed=True):
    name: NotRequired["capo_ssm.types.instance_name.InstanceName"]
    """<p>The value of the EC2 <code>Name</code> tag associated with the node. If a <code>Name</code> tag hasn't been applied to the node, this value is blank.</p>"""
    instance_id: NotRequired["capo_ssm.types.instance_id.InstanceId"]
    """<p>The ID of the managed node.</p>"""
    instance_type: NotRequired["capo_ssm.types.instance_type.InstanceType"]
    """<p>The instance type of the managed node. For example, t3.large.</p>"""
    instance_role: NotRequired["capo_ssm.types.instance_role.InstanceRole"]
    """<p>The instance profile attached to the node. If an instance profile isn't attached to the node, this value is blank.</p>"""
    key_name: NotRequired["capo_ssm.types.key_name.KeyName"]
    """<p>The name of the key pair associated with the node. If a key pair isnt't associated with the node, this value is blank.</p>"""
    instance_state: NotRequired["capo_ssm.types.instance_state.InstanceState"]
    """<p>The current state of the node.</p>"""
    architecture: NotRequired["capo_ssm.types.architecture.Architecture"]
    """<p>The CPU architecture of the node. For example, <code>x86_64</code>.</p>"""
    ip_address: NotRequired["capo_ssm.types.ip_address.IPAddress"]
    """<p>The public IPv4 address assigned to the node. If a public IPv4 address isn't assigned to the node, this value is blank.</p>"""
    launch_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The timestamp for when the node was launched.</p>"""
    ping_status: NotRequired["capo_ssm.types.ping_status.PingStatus"]
    """<p>Connection status of the SSM Agent on the managed node.</p>"""
    last_ping_date_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date and time when the SSM Agent last pinged the Systems Manager service.</p>"""
    agent_version: NotRequired["capo_ssm.types.version.Version"]
    """<p>The version of SSM Agent running on your managed node.</p>"""
    platform_type: NotRequired["capo_ssm.types.platform_type.PlatformType"]
    """<p>The operating system platform type of the managed node. For example, Windows Server or Amazon Linux 2.</p>"""
    platform_name: NotRequired["capo_ssm.types.platform_name.PlatformName"]
    """<p>The name of the operating system platform running on your managed node.</p>"""
    platform_version: NotRequired["capo_ssm.types.platform_version.PlatformVersion"]
    """<p>The version of the OS platform running on your managed node.</p>"""
    activation_id: NotRequired["capo_ssm.types.activation_id.ActivationId"]
    """<p>The activation ID created by Systems Manager when the server or virtual machine (VM) was registered</p>"""
    iam_role: NotRequired["capo_ssm.types.iam_role.IamRole"]
    """<p>The IAM role used in the hybrid activation to register the node with Systems Manager.</p>"""
    registration_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date the node was registered with Systems Manager.</p>"""
    resource_type: NotRequired["capo_ssm.types.string.String"]
    """<p>The type of managed node.</p>"""
    computer_name: NotRequired["capo_ssm.types.computer_name.ComputerName"]
    """<p>The fully qualified host name of the managed node.</p>"""
    association_status: NotRequired["capo_ssm.types.status_name.StatusName"]
    """<p>The status of the State Manager association applied to the managed node.</p>"""
    last_association_execution_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date the association was last run.</p>"""
    last_successful_association_execution_date: NotRequired[
        "capo_ssm.types.date_time.DateTime"
    ]
    """<p>The last date the association was successfully run.</p>"""
    association_overview: NotRequired[
        "capo_ssm.types.instance_aggregated_association_overview.InstanceAggregatedAssociationOverview"
    ]
    source_id: NotRequired["capo_ssm.types.source_id.SourceId"]
    """<p>The ID of the source resource.</p>"""
    source_type: NotRequired["capo_ssm.types.source_type.SourceType"]
    """<p>The type of the source resource. Valid values: <code>AWS::EC2::Instance</code> | <code>AWS::SSM::ManagedInstance</code> | <code>AWS::IoT::Thing</code> | <code>Microsoft.Compute/virtualMachines</code>.</p>"""
    source_location: NotRequired["capo_ssm.types.source_location.SourceLocation"]
    """<p>The location of the source resource in the third-party cloud environment.</p>"""
    availability_zone: NotRequired["capo_ssm.types.availability_zone.AvailabilityZone"]
    """<p>The Availability Zone where the managed node is located.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceProperty) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "instance_role" in value:
        out["InstanceRole"] = value["instance_role"]
    if "key_name" in value:
        out["KeyName"] = value["key_name"]
    if "instance_state" in value:
        out["InstanceState"] = value["instance_state"]
    if "architecture" in value:
        out["Architecture"] = value["architecture"]
    if "ip_address" in value:
        out["IPAddress"] = value["ip_address"]
    if "launch_time" in value:
        import capo_ssm.types.date_time

        out["LaunchTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["launch_time"]
        )
    if "ping_status" in value:
        import capo_ssm.types.ping_status

        out["PingStatus"] = capo_ssm.types.ping_status.serialize_aws_json_1_1(
            value["ping_status"]
        )
    if "last_ping_date_time" in value:
        import capo_ssm.types.date_time

        out["LastPingDateTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["last_ping_date_time"]
        )
    if "agent_version" in value:
        out["AgentVersion"] = value["agent_version"]
    if "platform_type" in value:
        import capo_ssm.types.platform_type

        out["PlatformType"] = capo_ssm.types.platform_type.serialize_aws_json_1_1(
            value["platform_type"]
        )
    if "platform_name" in value:
        out["PlatformName"] = value["platform_name"]
    if "platform_version" in value:
        out["PlatformVersion"] = value["platform_version"]
    if "activation_id" in value:
        out["ActivationId"] = value["activation_id"]
    if "iam_role" in value:
        out["IamRole"] = value["iam_role"]
    if "registration_date" in value:
        import capo_ssm.types.date_time

        out["RegistrationDate"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["registration_date"]
        )
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "computer_name" in value:
        out["ComputerName"] = value["computer_name"]
    if "association_status" in value:
        out["AssociationStatus"] = value["association_status"]
    if "last_association_execution_date" in value:
        import capo_ssm.types.date_time

        out["LastAssociationExecutionDate"] = (
            capo_ssm.types.date_time.serialize_aws_json_1_1(
                value["last_association_execution_date"]
            )
        )
    if "last_successful_association_execution_date" in value:
        import capo_ssm.types.date_time

        out["LastSuccessfulAssociationExecutionDate"] = (
            capo_ssm.types.date_time.serialize_aws_json_1_1(
                value["last_successful_association_execution_date"]
            )
        )
    if "association_overview" in value:
        import capo_ssm.types.instance_aggregated_association_overview

        out["AssociationOverview"] = (
            capo_ssm.types.instance_aggregated_association_overview.serialize_aws_json_1_1(
                value["association_overview"]
            )
        )
    if "source_id" in value:
        out["SourceId"] = value["source_id"]
    if "source_type" in value:
        import capo_ssm.types.source_type

        out["SourceType"] = capo_ssm.types.source_type.serialize_aws_json_1_1(
            value["source_type"]
        )
    if "source_location" in value:
        out["SourceLocation"] = value["source_location"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceProperty:
    out: InstanceProperty = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("InstanceType") is not None:
        out["instance_type"] = data["InstanceType"]
    if data.get("InstanceRole") is not None:
        out["instance_role"] = data["InstanceRole"]
    if data.get("KeyName") is not None:
        out["key_name"] = data["KeyName"]
    if data.get("InstanceState") is not None:
        out["instance_state"] = data["InstanceState"]
    if data.get("Architecture") is not None:
        out["architecture"] = data["Architecture"]
    if data.get("IPAddress") is not None:
        out["ip_address"] = data["IPAddress"]
    if data.get("LaunchTime") is not None:
        import capo_ssm.types.date_time

        out["launch_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["LaunchTime"]
        )
    if data.get("PingStatus") is not None:
        import capo_ssm.types.ping_status

        out["ping_status"] = capo_ssm.types.ping_status.deserialize_aws_json_1_1(
            data["PingStatus"]
        )
    if data.get("LastPingDateTime") is not None:
        import capo_ssm.types.date_time

        out["last_ping_date_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["LastPingDateTime"]
        )
    if data.get("AgentVersion") is not None:
        out["agent_version"] = data["AgentVersion"]
    if data.get("PlatformType") is not None:
        import capo_ssm.types.platform_type

        out["platform_type"] = capo_ssm.types.platform_type.deserialize_aws_json_1_1(
            data["PlatformType"]
        )
    if data.get("PlatformName") is not None:
        out["platform_name"] = data["PlatformName"]
    if data.get("PlatformVersion") is not None:
        out["platform_version"] = data["PlatformVersion"]
    if data.get("ActivationId") is not None:
        out["activation_id"] = data["ActivationId"]
    if data.get("IamRole") is not None:
        out["iam_role"] = data["IamRole"]
    if data.get("RegistrationDate") is not None:
        import capo_ssm.types.date_time

        out["registration_date"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["RegistrationDate"]
        )
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("ComputerName") is not None:
        out["computer_name"] = data["ComputerName"]
    if data.get("AssociationStatus") is not None:
        out["association_status"] = data["AssociationStatus"]
    if data.get("LastAssociationExecutionDate") is not None:
        import capo_ssm.types.date_time

        out["last_association_execution_date"] = (
            capo_ssm.types.date_time.deserialize_aws_json_1_1(
                data["LastAssociationExecutionDate"]
            )
        )
    if data.get("LastSuccessfulAssociationExecutionDate") is not None:
        import capo_ssm.types.date_time

        out["last_successful_association_execution_date"] = (
            capo_ssm.types.date_time.deserialize_aws_json_1_1(
                data["LastSuccessfulAssociationExecutionDate"]
            )
        )
    if data.get("AssociationOverview") is not None:
        import capo_ssm.types.instance_aggregated_association_overview

        out["association_overview"] = (
            capo_ssm.types.instance_aggregated_association_overview.deserialize_aws_json_1_1(
                data["AssociationOverview"]
            )
        )
    if data.get("SourceId") is not None:
        out["source_id"] = data["SourceId"]
    if data.get("SourceType") is not None:
        import capo_ssm.types.source_type

        out["source_type"] = capo_ssm.types.source_type.deserialize_aws_json_1_1(
            data["SourceType"]
        )
    if data.get("SourceLocation") is not None:
        out["source_location"] = data["SourceLocation"]
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    return out


def redact_sensitive(value: InstanceProperty) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ip_address" in value:
        out["ip_address"] = "*** Sensitive Data Redacted ***"
    return out
