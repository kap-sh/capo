"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.activation_id
    import capo_ssm.types.boolean
    import capo_ssm.types.computer_name
    import capo_ssm.types.date_time
    import capo_ssm.types.iam_role
    import capo_ssm.types.instance_aggregated_association_overview
    import capo_ssm.types.instance_id
    import capo_ssm.types.ip_address
    import capo_ssm.types.ping_status
    import capo_ssm.types.platform_type
    import capo_ssm.types.resource_type
    import capo_ssm.types.source_id
    import capo_ssm.types.source_location
    import capo_ssm.types.source_type
    import capo_ssm.types.status_name
    import capo_ssm.types.string
    import capo_ssm.types.version


class InstanceInformation(TypedDict, closed=True):
    instance_id: NotRequired["capo_ssm.types.instance_id.InstanceId"]
    """<p>The managed node ID. </p>"""
    ping_status: NotRequired["capo_ssm.types.ping_status.PingStatus"]
    """<p>Connection status of SSM Agent. </p> <note> <p>The status <code>Inactive</code> has been deprecated and is no longer in use.</p> </note>"""
    last_ping_date_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date and time when the agent last pinged the Systems Manager service. </p>"""
    agent_version: NotRequired["capo_ssm.types.version.Version"]
    """<p>The version of SSM Agent running on your Linux managed node. </p>"""
    is_latest_version: NotRequired["capo_ssm.types.boolean.Boolean"]
    """<p>Indicates whether the latest version of SSM Agent is running on your Linux managed node. This field doesn't indicate whether or not the latest version is installed on Windows managed nodes, because some older versions of Windows Server use the EC2Config service to process Systems Manager requests.</p>"""
    platform_type: NotRequired["capo_ssm.types.platform_type.PlatformType"]
    """<p>The operating system platform type.</p>"""
    platform_name: NotRequired["capo_ssm.types.string.String"]
    """<p>The name of the operating system platform running on your managed node. </p>"""
    platform_version: NotRequired["capo_ssm.types.string.String"]
    """<p>The version of the OS platform running on your managed node. </p>"""
    activation_id: NotRequired["capo_ssm.types.activation_id.ActivationId"]
    """<p>The activation ID created by Amazon Web Services Systems Manager when the server or virtual machine (VM) was registered.</p>"""
    iam_role: NotRequired["capo_ssm.types.iam_role.IamRole"]
    """<p>The role assigned to an Amazon EC2 instance configured with a Systems Manager Quick Setup host management configuration or the role assigned to an on-premises managed node.</p> <p> This call doesn't return the IAM role for <i>unmanaged</i> Amazon EC2 instances (instances not configured for Systems Manager). To retrieve the role for an unmanaged instance, use the Amazon EC2 <code>DescribeInstances</code> operation. For information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html">DescribeInstances</a> in the <i>Amazon EC2 API Reference</i> or <a href="https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html">describe-instances</a> in the <i>Amazon Web Services CLI Command Reference</i>.</p>"""
    registration_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date the server or VM was registered with Amazon Web Services as a managed node.</p>"""
    resource_type: NotRequired["capo_ssm.types.resource_type.ResourceType"]
    """<p>The type of instance. Instances are either EC2 instances or managed instances. </p>"""
    name: NotRequired["capo_ssm.types.string.String"]
    """<p>The name assigned to an on-premises server, edge device, or virtual machine (VM) when it is activated as a Systems Manager managed node. The name is specified as the <code>DefaultInstanceName</code> property using the <a>CreateActivation</a> command. It is applied to the managed node by specifying the Activation Code and Activation ID when you install SSM Agent on the node, as explained in <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/hybrid-multicloud-ssm-agent-install-linux.html">How to install SSM Agent on hybrid Linux nodes</a> and <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/hybrid-multicloud-ssm-agent-install-windows.html">How to install SSM Agent on hybrid Windows Server nodes</a>. To retrieve the <code>Name</code> tag of an EC2 instance, use the Amazon EC2 <code>DescribeInstances</code> operation. For information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html">DescribeInstances</a> in the <i>Amazon EC2 API Reference</i> or <a href="https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html">describe-instances</a> in the <i>Amazon Web Services CLI Command Reference</i>.</p>"""
    ip_address: NotRequired["capo_ssm.types.ip_address.IPAddress"]
    """<p>The IP address of the managed node.</p>"""
    computer_name: NotRequired["capo_ssm.types.computer_name.ComputerName"]
    """<p>The fully qualified host name of the managed node.</p>"""
    association_status: NotRequired["capo_ssm.types.status_name.StatusName"]
    """<p>The status of the association.</p>"""
    last_association_execution_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date the association was last run.</p>"""
    last_successful_association_execution_date: NotRequired[
        "capo_ssm.types.date_time.DateTime"
    ]
    """<p>The last date the association was successfully run.</p>"""
    association_overview: NotRequired[
        "capo_ssm.types.instance_aggregated_association_overview.InstanceAggregatedAssociationOverview"
    ]
    """<p>Information about the association.</p>"""
    source_id: NotRequired["capo_ssm.types.source_id.SourceId"]
    """<p>The ID of the source resource. For IoT Greengrass devices, <code>SourceId</code> is the Thing name. </p>"""
    source_type: NotRequired["capo_ssm.types.source_type.SourceType"]
    """<p>The type of the source resource. For IoT Greengrass devices, <code>SourceType</code> is <code>AWS::IoT::Thing</code>. For Azure Virtual Machines, <code>SourceType</code> is <code>Microsoft.Compute/virtualMachines</code>.</p>"""
    source_location: NotRequired["capo_ssm.types.source_location.SourceLocation"]
    """<p>The location of the source resource in the third-party cloud environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceInformation) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
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
    if "is_latest_version" in value:
        out["IsLatestVersion"] = value["is_latest_version"]
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
        import capo_ssm.types.resource_type

        out["ResourceType"] = capo_ssm.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "ip_address" in value:
        out["IPAddress"] = value["ip_address"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceInformation:
    out: InstanceInformation = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
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
    if data.get("IsLatestVersion") is not None:
        out["is_latest_version"] = data["IsLatestVersion"]
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
        import capo_ssm.types.resource_type

        out["resource_type"] = capo_ssm.types.resource_type.deserialize_aws_json_1_1(
            data["ResourceType"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("IPAddress") is not None:
        out["ip_address"] = data["IPAddress"]
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
    return out
