"""Generated from Smithy shape ``com.amazonaws.emr#Ec2InstanceAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.string
    import capo_emr.types.string_list
    import capo_emr.types.xml_string_max_len256_list


class Ec2InstanceAttributes(TypedDict, closed=True):
    ec2_key_name: NotRequired["capo_emr.types.string.String"]
    """<p>The name of the Amazon EC2 key pair to use when connecting with SSH into the master node as a user named "hadoop".</p>"""
    ec2_subnet_id: NotRequired["capo_emr.types.string.String"]
    """<p>Set this parameter to the identifier of the Amazon VPC subnet where you want the cluster to launch. If you do not specify this value, and your account supports EC2-Classic, the cluster launches in EC2-Classic.</p>"""
    requested_ec2_subnet_ids: NotRequired[
        "capo_emr.types.xml_string_max_len256_list.XmlStringMaxLen256List"
    ]
    """<p>Applies to clusters configured with the instance fleets option. Specifies the unique identifier of one or more Amazon EC2 subnets in which to launch Amazon EC2 cluster instances. Subnets must exist within the same VPC. Amazon EMR chooses the Amazon EC2 subnet with the best fit from among the list of <code>RequestedEc2SubnetIds</code>, and then launches all cluster instances within that Subnet. If this value is not specified, and the account and Region support EC2-Classic networks, the cluster launches instances in the EC2-Classic network and uses <code>RequestedEc2AvailabilityZones</code> instead of this setting. If EC2-Classic is not supported, and no Subnet is specified, Amazon EMR chooses the subnet for you. <code>RequestedEc2SubnetIDs</code> and <code>RequestedEc2AvailabilityZones</code> cannot be specified together.</p>"""
    ec2_availability_zone: NotRequired["capo_emr.types.string.String"]
    """<p>The Availability Zone in which the cluster will run. </p>"""
    requested_ec2_availability_zones: NotRequired[
        "capo_emr.types.xml_string_max_len256_list.XmlStringMaxLen256List"
    ]
    """<p>Applies to clusters configured with the instance fleets option. Specifies one or more Availability Zones in which to launch Amazon EC2 cluster instances when the EC2-Classic network configuration is supported. Amazon EMR chooses the Availability Zone with the best fit from among the list of <code>RequestedEc2AvailabilityZones</code>, and then launches all cluster instances within that Availability Zone. If you do not specify this value, Amazon EMR chooses the Availability Zone for you. <code>RequestedEc2SubnetIDs</code> and <code>RequestedEc2AvailabilityZones</code> cannot be specified together.</p>"""
    iam_instance_profile: NotRequired["capo_emr.types.string.String"]
    """<p>The IAM role that was specified when the cluster was launched. The Amazon EC2 instances of the cluster assume this role.</p>"""
    emr_managed_master_security_group: NotRequired["capo_emr.types.string.String"]
    """<p>The identifier of the Amazon EC2 security group for the master node.</p>"""
    emr_managed_slave_security_group: NotRequired["capo_emr.types.string.String"]
    """<p>The identifier of the Amazon EC2 security group for the core and task nodes.</p>"""
    service_access_security_group: NotRequired["capo_emr.types.string.String"]
    """<p>The identifier of the Amazon EC2 security group for the Amazon EMR service to access clusters in VPC private subnets.</p>"""
    additional_master_security_groups: NotRequired[
        "capo_emr.types.string_list.StringList"
    ]
    """<p>A list of additional Amazon EC2 security group IDs for the master node.</p>"""
    additional_slave_security_groups: NotRequired[
        "capo_emr.types.string_list.StringList"
    ]
    """<p>A list of additional Amazon EC2 security group IDs for the core and task nodes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Ec2InstanceAttributes) -> dict:
    out: dict = {}
    if "ec2_key_name" in value:
        out["Ec2KeyName"] = value["ec2_key_name"]
    if "ec2_subnet_id" in value:
        out["Ec2SubnetId"] = value["ec2_subnet_id"]
    if "requested_ec2_subnet_ids" in value:
        import capo_emr.types.xml_string_max_len256_list

        out["RequestedEc2SubnetIds"] = (
            capo_emr.types.xml_string_max_len256_list.serialize_aws_json_1_1(
                value["requested_ec2_subnet_ids"]
            )
        )
    if "ec2_availability_zone" in value:
        out["Ec2AvailabilityZone"] = value["ec2_availability_zone"]
    if "requested_ec2_availability_zones" in value:
        import capo_emr.types.xml_string_max_len256_list

        out["RequestedEc2AvailabilityZones"] = (
            capo_emr.types.xml_string_max_len256_list.serialize_aws_json_1_1(
                value["requested_ec2_availability_zones"]
            )
        )
    if "iam_instance_profile" in value:
        out["IamInstanceProfile"] = value["iam_instance_profile"]
    if "emr_managed_master_security_group" in value:
        out["EmrManagedMasterSecurityGroup"] = value[
            "emr_managed_master_security_group"
        ]
    if "emr_managed_slave_security_group" in value:
        out["EmrManagedSlaveSecurityGroup"] = value["emr_managed_slave_security_group"]
    if "service_access_security_group" in value:
        out["ServiceAccessSecurityGroup"] = value["service_access_security_group"]
    if "additional_master_security_groups" in value:
        import capo_emr.types.string_list

        out["AdditionalMasterSecurityGroups"] = (
            capo_emr.types.string_list.serialize_aws_json_1_1(
                value["additional_master_security_groups"]
            )
        )
    if "additional_slave_security_groups" in value:
        import capo_emr.types.string_list

        out["AdditionalSlaveSecurityGroups"] = (
            capo_emr.types.string_list.serialize_aws_json_1_1(
                value["additional_slave_security_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Ec2InstanceAttributes:
    out: Ec2InstanceAttributes = {}  # type: ignore[typeddict-item]
    if data.get("Ec2KeyName") is not None:
        out["ec2_key_name"] = data["Ec2KeyName"]
    if data.get("Ec2SubnetId") is not None:
        out["ec2_subnet_id"] = data["Ec2SubnetId"]
    if data.get("RequestedEc2SubnetIds") is not None:
        import capo_emr.types.xml_string_max_len256_list

        out["requested_ec2_subnet_ids"] = (
            capo_emr.types.xml_string_max_len256_list.deserialize_aws_json_1_1(
                data["RequestedEc2SubnetIds"]
            )
        )
    if data.get("Ec2AvailabilityZone") is not None:
        out["ec2_availability_zone"] = data["Ec2AvailabilityZone"]
    if data.get("RequestedEc2AvailabilityZones") is not None:
        import capo_emr.types.xml_string_max_len256_list

        out["requested_ec2_availability_zones"] = (
            capo_emr.types.xml_string_max_len256_list.deserialize_aws_json_1_1(
                data["RequestedEc2AvailabilityZones"]
            )
        )
    if data.get("IamInstanceProfile") is not None:
        out["iam_instance_profile"] = data["IamInstanceProfile"]
    if data.get("EmrManagedMasterSecurityGroup") is not None:
        out["emr_managed_master_security_group"] = data["EmrManagedMasterSecurityGroup"]
    if data.get("EmrManagedSlaveSecurityGroup") is not None:
        out["emr_managed_slave_security_group"] = data["EmrManagedSlaveSecurityGroup"]
    if data.get("ServiceAccessSecurityGroup") is not None:
        out["service_access_security_group"] = data["ServiceAccessSecurityGroup"]
    if data.get("AdditionalMasterSecurityGroups") is not None:
        import capo_emr.types.string_list

        out["additional_master_security_groups"] = (
            capo_emr.types.string_list.deserialize_aws_json_1_1(
                data["AdditionalMasterSecurityGroups"]
            )
        )
    if data.get("AdditionalSlaveSecurityGroups") is not None:
        import capo_emr.types.string_list

        out["additional_slave_security_groups"] = (
            capo_emr.types.string_list.deserialize_aws_json_1_1(
                data["AdditionalSlaveSecurityGroups"]
            )
        )
    return out
