"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeLocationFsxWindowsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.cmk_secret_config
    import capo_datasync.types.custom_secret_config
    import capo_datasync.types.ec2_security_group_arn_list
    import capo_datasync.types.location_arn
    import capo_datasync.types.location_uri
    import capo_datasync.types.managed_secret_config
    import capo_datasync.types.smb_domain
    import capo_datasync.types.smb_user
    import capo_datasync.types.time


class DescribeLocationFsxWindowsResponse(TypedDict, closed=True):
    location_arn: NotRequired["capo_datasync.types.location_arn.LocationArn"]
    """<p>The ARN of the FSx for Windows File Server location.</p>"""
    location_uri: NotRequired["capo_datasync.types.location_uri.LocationUri"]
    """<p>The uniform resource identifier (URI) of the FSx for Windows File Server location.</p>"""
    security_group_arns: NotRequired[
        "capo_datasync.types.ec2_security_group_arn_list.Ec2SecurityGroupArnList"
    ]
    """<p>The ARNs of the Amazon EC2 security groups that provide access to your file system's preferred subnet.</p> <p>For information about configuring security groups for file system access, see the <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/limit-access-security-groups.html"> <i>Amazon FSx for Windows File Server User Guide</i> </a>.</p>"""
    creation_time: NotRequired["capo_datasync.types.time.Time"]
    """<p>The time that the FSx for Windows File Server location was created.</p>"""
    user: NotRequired["capo_datasync.types.smb_user.SmbUser"]
    """<p>The user with the permissions to mount and access the FSx for Windows File Server file system.</p>"""
    domain: NotRequired["capo_datasync.types.smb_domain.SmbDomain"]
    """<p>The name of the Microsoft Active Directory domain that the FSx for Windows File Server file system belongs to.</p>"""
    managed_secret_config: NotRequired[
        "capo_datasync.types.managed_secret_config.ManagedSecretConfig"
    ]
    """<p>Describes configuration information for a DataSync-managed secret, such as a <code>Password</code> that DataSync uses to access a specific storage location. DataSync uses the default Amazon Web Services-managed KMS key to encrypt this secret in Secrets Manager.</p>"""
    cmk_secret_config: NotRequired[
        "capo_datasync.types.cmk_secret_config.CmkSecretConfig"
    ]
    """<p>Describes configuration information for a DataSync-managed secret, such as a <code>Password</code> that DataSync uses to access a specific storage location, with a customer-managed KMS key.</p>"""
    custom_secret_config: NotRequired[
        "capo_datasync.types.custom_secret_config.CustomSecretConfig"
    ]
    """<p>Describes configuration information for a customer-managed secret, such as a <code>Password</code> that DataSync uses to access a specific storage location, with a customer-managed Identity and Access Management (IAM) role that provides access to the secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLocationFsxWindowsResponse) -> dict:
    out: dict = {}
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
    if "security_group_arns" in value:
        import capo_datasync.types.ec2_security_group_arn_list

        out["SecurityGroupArns"] = (
            capo_datasync.types.ec2_security_group_arn_list.serialize_aws_json_1_1(
                value["security_group_arns"]
            )
        )
    if "creation_time" in value:
        import capo_datasync.types.time

        out["CreationTime"] = capo_datasync.types.time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "user" in value:
        out["User"] = value["user"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "managed_secret_config" in value:
        import capo_datasync.types.managed_secret_config

        out["ManagedSecretConfig"] = (
            capo_datasync.types.managed_secret_config.serialize_aws_json_1_1(
                value["managed_secret_config"]
            )
        )
    if "cmk_secret_config" in value:
        import capo_datasync.types.cmk_secret_config

        out["CmkSecretConfig"] = (
            capo_datasync.types.cmk_secret_config.serialize_aws_json_1_1(
                value["cmk_secret_config"]
            )
        )
    if "custom_secret_config" in value:
        import capo_datasync.types.custom_secret_config

        out["CustomSecretConfig"] = (
            capo_datasync.types.custom_secret_config.serialize_aws_json_1_1(
                value["custom_secret_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLocationFsxWindowsResponse:
    out: DescribeLocationFsxWindowsResponse = {}  # type: ignore[typeddict-item]
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    if data.get("LocationUri") is not None:
        out["location_uri"] = data["LocationUri"]
    if data.get("SecurityGroupArns") is not None:
        import capo_datasync.types.ec2_security_group_arn_list

        out["security_group_arns"] = (
            capo_datasync.types.ec2_security_group_arn_list.deserialize_aws_json_1_1(
                data["SecurityGroupArns"]
            )
        )
    if data.get("CreationTime") is not None:
        import capo_datasync.types.time

        out["creation_time"] = capo_datasync.types.time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("User") is not None:
        out["user"] = data["User"]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    if data.get("ManagedSecretConfig") is not None:
        import capo_datasync.types.managed_secret_config

        out["managed_secret_config"] = (
            capo_datasync.types.managed_secret_config.deserialize_aws_json_1_1(
                data["ManagedSecretConfig"]
            )
        )
    if data.get("CmkSecretConfig") is not None:
        import capo_datasync.types.cmk_secret_config

        out["cmk_secret_config"] = (
            capo_datasync.types.cmk_secret_config.deserialize_aws_json_1_1(
                data["CmkSecretConfig"]
            )
        )
    if data.get("CustomSecretConfig") is not None:
        import capo_datasync.types.custom_secret_config

        out["custom_secret_config"] = (
            capo_datasync.types.custom_secret_config.deserialize_aws_json_1_1(
                data["CustomSecretConfig"]
            )
        )
    return out
