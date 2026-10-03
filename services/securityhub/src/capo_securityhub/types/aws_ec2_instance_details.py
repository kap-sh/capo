"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2InstanceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_instance_metadata_options
    import capo_securityhub.types.aws_ec2_instance_monitoring_details
    import capo_securityhub.types.aws_ec2_instance_network_interfaces_list
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.string_list


class AwsEc2InstanceDetails(TypedDict, closed=True):
    type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The instance type of the instance. </p>"""
    image_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Machine Image (AMI) ID of the instance.</p>"""
    ip_v4_addresses: NotRequired["capo_securityhub.types.string_list.StringList"]
    """<p>The IPv4 addresses associated with the instance.</p>"""
    ip_v6_addresses: NotRequired["capo_securityhub.types.string_list.StringList"]
    """<p>The IPv6 addresses associated with the instance.</p>"""
    key_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The key name associated with the instance.</p>"""
    iam_instance_profile_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The IAM profile ARN of the instance.</p>"""
    vpc_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the VPC that the instance was launched in.</p>"""
    subnet_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the subnet that the instance was launched in.</p>"""
    launched_at: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the instance was launched.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    network_interfaces: NotRequired[
        "capo_securityhub.types.aws_ec2_instance_network_interfaces_list.AwsEc2InstanceNetworkInterfacesList"
    ]
    """<p>The identifiers of the network interfaces for the EC2 instance. The details for each network interface are in a corresponding <code>AwsEc2NetworkInterfacesDetails</code> object.</p>"""
    virtualization_type: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The virtualization type of the Amazon Machine Image (AMI) required to launch the instance. </p>"""
    metadata_options: NotRequired[
        "capo_securityhub.types.aws_ec2_instance_metadata_options.AwsEc2InstanceMetadataOptions"
    ]
    """<p>Details about the metadata options for the Amazon EC2 instance. </p>"""
    monitoring: NotRequired[
        "capo_securityhub.types.aws_ec2_instance_monitoring_details.AwsEc2InstanceMonitoringDetails"
    ]
    """<p> Describes the type of monitoring that’s turned on for an instance. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2InstanceDetails) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    if "ip_v4_addresses" in value:
        import capo_securityhub.types.string_list

        out["IpV4Addresses"] = capo_securityhub.types.string_list.serialize_json(
            value["ip_v4_addresses"]
        )
    if "ip_v6_addresses" in value:
        import capo_securityhub.types.string_list

        out["IpV6Addresses"] = capo_securityhub.types.string_list.serialize_json(
            value["ip_v6_addresses"]
        )
    if "key_name" in value:
        out["KeyName"] = value["key_name"]
    if "iam_instance_profile_arn" in value:
        out["IamInstanceProfileArn"] = value["iam_instance_profile_arn"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "launched_at" in value:
        out["LaunchedAt"] = value["launched_at"]
    if "network_interfaces" in value:
        import capo_securityhub.types.aws_ec2_instance_network_interfaces_list

        out["NetworkInterfaces"] = (
            capo_securityhub.types.aws_ec2_instance_network_interfaces_list.serialize_json(
                value["network_interfaces"]
            )
        )
    if "virtualization_type" in value:
        out["VirtualizationType"] = value["virtualization_type"]
    if "metadata_options" in value:
        import capo_securityhub.types.aws_ec2_instance_metadata_options

        out["MetadataOptions"] = (
            capo_securityhub.types.aws_ec2_instance_metadata_options.serialize_json(
                value["metadata_options"]
            )
        )
    if "monitoring" in value:
        import capo_securityhub.types.aws_ec2_instance_monitoring_details

        out["Monitoring"] = (
            capo_securityhub.types.aws_ec2_instance_monitoring_details.serialize_json(
                value["monitoring"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEc2InstanceDetails:
    out: AwsEc2InstanceDetails = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("ImageId") is not None:
        out["image_id"] = data["ImageId"]
    if data.get("IpV4Addresses") is not None:
        import capo_securityhub.types.string_list

        out["ip_v4_addresses"] = capo_securityhub.types.string_list.deserialize_json(
            data["IpV4Addresses"]
        )
    if data.get("IpV6Addresses") is not None:
        import capo_securityhub.types.string_list

        out["ip_v6_addresses"] = capo_securityhub.types.string_list.deserialize_json(
            data["IpV6Addresses"]
        )
    if data.get("KeyName") is not None:
        out["key_name"] = data["KeyName"]
    if data.get("IamInstanceProfileArn") is not None:
        out["iam_instance_profile_arn"] = data["IamInstanceProfileArn"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("SubnetId") is not None:
        out["subnet_id"] = data["SubnetId"]
    if data.get("LaunchedAt") is not None:
        out["launched_at"] = data["LaunchedAt"]
    if data.get("NetworkInterfaces") is not None:
        import capo_securityhub.types.aws_ec2_instance_network_interfaces_list

        out["network_interfaces"] = (
            capo_securityhub.types.aws_ec2_instance_network_interfaces_list.deserialize_json(
                data["NetworkInterfaces"]
            )
        )
    if data.get("VirtualizationType") is not None:
        out["virtualization_type"] = data["VirtualizationType"]
    if data.get("MetadataOptions") is not None:
        import capo_securityhub.types.aws_ec2_instance_metadata_options

        out["metadata_options"] = (
            capo_securityhub.types.aws_ec2_instance_metadata_options.deserialize_json(
                data["MetadataOptions"]
            )
        )
    if data.get("Monitoring") is not None:
        import capo_securityhub.types.aws_ec2_instance_monitoring_details

        out["monitoring"] = (
            capo_securityhub.types.aws_ec2_instance_monitoring_details.deserialize_json(
                data["Monitoring"]
            )
        )
    return out
