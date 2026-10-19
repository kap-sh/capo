"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyInstanceProfileMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.string_list


class ModifyInstanceProfileMessage(TypedDict, closed=True):
    instance_profile_identifier: "capo_database_migration_service.types.string.String"
    """<p>The identifier of the instance profile. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.</p>"""
    availability_zone: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Availability Zone where the instance profile runs.</p>"""
    kms_key_arn: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the KMS key that is used to encrypt the connection parameters for the instance profile.</p> <p>If you don't specify a value for the <code>KmsKeyArn</code> parameter, then DMS uses an Amazon Web Services owned encryption key to encrypt your resources.</p>"""
    publicly_accessible: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies the accessibility options for the instance profile. A value of <code>true</code> represents an instance profile with a public IP address. A value of <code>false</code> represents an instance profile with a private IP address. The default value is <code>true</code>.</p>"""
    network_type: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Specifies the network type for the instance profile. A value of <code>IPV4</code> represents an instance profile with IPv4 network type and only supports IPv4 addressing. A value of <code>IPV6</code> represents an instance profile with IPv6 network type and only supports IPv6 addressing. A value of <code>DUAL</code> represents an instance profile with dual network type that supports IPv4 and IPv6 addressing.</p>"""
    instance_profile_name: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>A user-friendly name for the instance profile.</p>"""
    description: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>A user-friendly description for the instance profile.</p>"""
    subnet_group_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>A subnet group to associate with the instance profile.</p>"""
    vpc_security_groups: NotRequired[
        "capo_database_migration_service.types.string_list.StringList"
    ]
    """<p>Specifies the VPC security groups to be used with the instance profile. The VPC security group must work with the VPC containing the instance profile.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyInstanceProfileMessage) -> dict:
    out: dict = {}
    out["InstanceProfileIdentifier"] = value["instance_profile_identifier"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "publicly_accessible" in value:
        out["PubliclyAccessible"] = value["publicly_accessible"]
    if "network_type" in value:
        out["NetworkType"] = value["network_type"]
    if "instance_profile_name" in value:
        out["InstanceProfileName"] = value["instance_profile_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "subnet_group_identifier" in value:
        out["SubnetGroupIdentifier"] = value["subnet_group_identifier"]
    if "vpc_security_groups" in value:
        import capo_database_migration_service.types.string_list

        out["VpcSecurityGroups"] = (
            capo_database_migration_service.types.string_list.serialize_aws_json_1_1(
                value["vpc_security_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyInstanceProfileMessage:
    out: ModifyInstanceProfileMessage = {}  # type: ignore[typeddict-item]
    if data.get("InstanceProfileIdentifier") is not None:
        out["instance_profile_identifier"] = data["InstanceProfileIdentifier"]
    else:
        out["instance_profile_identifier"] = ""
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if data.get("PubliclyAccessible") is not None:
        out["publicly_accessible"] = data["PubliclyAccessible"]
    if data.get("NetworkType") is not None:
        out["network_type"] = data["NetworkType"]
    if data.get("InstanceProfileName") is not None:
        out["instance_profile_name"] = data["InstanceProfileName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("SubnetGroupIdentifier") is not None:
        out["subnet_group_identifier"] = data["SubnetGroupIdentifier"]
    if data.get("VpcSecurityGroups") is not None:
        import capo_database_migration_service.types.string_list

        out["vpc_security_groups"] = (
            capo_database_migration_service.types.string_list.deserialize_aws_json_1_1(
                data["VpcSecurityGroups"]
            )
        )
    return out
