"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceDirectory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.active_directory_config
    import capo_workspaces.types.alias
    import capo_workspaces.types.arn
    import capo_workspaces.types.certificate_based_auth_properties
    import capo_workspaces.types.default_workspace_creation_properties
    import capo_workspaces.types.description
    import capo_workspaces.types.directory_id
    import capo_workspaces.types.directory_name
    import capo_workspaces.types.dns_ip_addresses
    import capo_workspaces.types.dns_ipv6_addresses
    import capo_workspaces.types.endpoint_encryption_mode
    import capo_workspaces.types.idc_config
    import capo_workspaces.types.ip_group_id_list
    import capo_workspaces.types.microsoft_entra_config
    import capo_workspaces.types.registration_code
    import capo_workspaces.types.saml_properties
    import capo_workspaces.types.security_group_id
    import capo_workspaces.types.selfservice_permissions
    import capo_workspaces.types.streaming_properties
    import capo_workspaces.types.subnet_ids
    import capo_workspaces.types.tenancy
    import capo_workspaces.types.user_identity_type
    import capo_workspaces.types.user_name
    import capo_workspaces.types.workspace_access_properties
    import capo_workspaces.types.workspace_directory_description
    import capo_workspaces.types.workspace_directory_name
    import capo_workspaces.types.workspace_directory_state
    import capo_workspaces.types.workspace_directory_type
    import capo_workspaces.types.workspace_type


class WorkspaceDirectory(TypedDict, closed=True):
    directory_id: NotRequired["capo_workspaces.types.directory_id.DirectoryId"]
    """<p>The directory identifier.</p>"""
    alias: NotRequired["capo_workspaces.types.alias.Alias"]
    """<p>The directory alias.</p>"""
    directory_name: NotRequired["capo_workspaces.types.directory_name.DirectoryName"]
    """<p>The name of the directory.</p>"""
    registration_code: NotRequired[
        "capo_workspaces.types.registration_code.RegistrationCode"
    ]
    """<p>The registration code for the directory. This is the code that users enter in their Amazon WorkSpaces client application to connect to the directory.</p>"""
    subnet_ids: NotRequired["capo_workspaces.types.subnet_ids.SubnetIds"]
    """<p>The identifiers of the subnets used with the directory.</p>"""
    dns_ip_addresses: NotRequired[
        "capo_workspaces.types.dns_ip_addresses.DnsIpAddresses"
    ]
    """<p>The IP addresses of the DNS servers for the directory.</p>"""
    dns_ipv6_addresses: NotRequired[
        "capo_workspaces.types.dns_ipv6_addresses.DnsIpv6Addresses"
    ]
    """<p>The IPv6 addresses of the DNS servers for the directory.</p>"""
    customer_user_name: NotRequired["capo_workspaces.types.user_name.UserName"]
    """<p>The user name for the service account.</p>"""
    iam_role_id: NotRequired["capo_workspaces.types.arn.ARN"]
    """<p>The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make calls to other services, such as Amazon EC2, on your behalf.</p>"""
    directory_type: NotRequired[
        "capo_workspaces.types.workspace_directory_type.WorkspaceDirectoryType"
    ]
    """<p>The directory type.</p>"""
    workspace_security_group_id: NotRequired[
        "capo_workspaces.types.security_group_id.SecurityGroupId"
    ]
    """<p>The identifier of the security group that is assigned to new WorkSpaces.</p>"""
    state: NotRequired[
        "capo_workspaces.types.workspace_directory_state.WorkspaceDirectoryState"
    ]
    """<p>The state of the directory's registration with Amazon WorkSpaces. After a directory is deregistered, the <code>DEREGISTERED</code> state is returned very briefly before the directory metadata is cleaned up, so this state is rarely returned. To confirm that a directory is deregistered, check for the directory ID by using <a href="https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceDirectories.html"> DescribeWorkspaceDirectories</a>. If the directory ID isn't returned, then the directory has been successfully deregistered.</p>"""
    workspace_creation_properties: NotRequired[
        "capo_workspaces.types.default_workspace_creation_properties.DefaultWorkspaceCreationProperties"
    ]
    """<p>The default creation properties for all WorkSpaces in the directory.</p>"""
    ip_group_ids: NotRequired["capo_workspaces.types.ip_group_id_list.IpGroupIdList"]
    """<p>The identifiers of the IP access control groups associated with the directory.</p>"""
    workspace_access_properties: NotRequired[
        "capo_workspaces.types.workspace_access_properties.WorkspaceAccessProperties"
    ]
    """<p>The devices and operating systems that users can use to access WorkSpaces.</p>"""
    tenancy: NotRequired["capo_workspaces.types.tenancy.Tenancy"]
    """<p>Specifies whether the directory is dedicated or shared. To use Bring Your Own License (BYOL), this value must be set to <code>DEDICATED</code>. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html">Bring Your Own Windows Desktop Images</a>.</p>"""
    selfservice_permissions: NotRequired[
        "capo_workspaces.types.selfservice_permissions.SelfservicePermissions"
    ]
    """<p>The default self-service permissions for WorkSpaces in the directory.</p>"""
    saml_properties: NotRequired["capo_workspaces.types.saml_properties.SamlProperties"]
    """<p>Describes the enablement status, user access URL, and relay state parameter name that are used for configuring federation with an SAML 2.0 identity provider.</p>"""
    certificate_based_auth_properties: NotRequired[
        "capo_workspaces.types.certificate_based_auth_properties.CertificateBasedAuthProperties"
    ]
    """<p>The certificate-based authentication properties used to authenticate SAML 2.0 Identity Provider (IdP) user identities to Active Directory for WorkSpaces login.</p>"""
    endpoint_encryption_mode: NotRequired[
        "capo_workspaces.types.endpoint_encryption_mode.EndpointEncryptionMode"
    ]
    """<p>Endpoint encryption mode that allows you to configure the specified directory between Standard TLS and FIPS 140-2 validated mode.</p>"""
    microsoft_entra_config: NotRequired[
        "capo_workspaces.types.microsoft_entra_config.MicrosoftEntraConfig"
    ]
    """<p>Specifies details about Microsoft Entra configurations.</p>"""
    workspace_directory_name: NotRequired[
        "capo_workspaces.types.workspace_directory_name.WorkspaceDirectoryName"
    ]
    """<p>The name fo the WorkSpace directory.</p>"""
    workspace_directory_description: NotRequired[
        "capo_workspaces.types.workspace_directory_description.WorkspaceDirectoryDescription"
    ]
    """<p>The description of the WorkSpace directory</p>"""
    user_identity_type: NotRequired[
        "capo_workspaces.types.user_identity_type.UserIdentityType"
    ]
    """<p>Indicates the identity type of the specifired user.</p>"""
    workspace_type: NotRequired["capo_workspaces.types.workspace_type.WorkspaceType"]
    """<p>Indicates whether the directory's WorkSpace type is personal or pools.</p>"""
    idc_config: NotRequired["capo_workspaces.types.idc_config.IDCConfig"]
    """<p>Specifies details about identity center configurations.</p>"""
    active_directory_config: NotRequired[
        "capo_workspaces.types.active_directory_config.ActiveDirectoryConfig"
    ]
    """<p>Information about the Active Directory config.</p>"""
    streaming_properties: NotRequired[
        "capo_workspaces.types.streaming_properties.StreamingProperties"
    ]
    """<p>The streaming properties to configure.</p>"""
    error_message: NotRequired["capo_workspaces.types.description.Description"]
    """<p>The error message returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceDirectory) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "alias" in value:
        out["Alias"] = value["alias"]
    if "directory_name" in value:
        out["DirectoryName"] = value["directory_name"]
    if "registration_code" in value:
        out["RegistrationCode"] = value["registration_code"]
    if "subnet_ids" in value:
        import capo_workspaces.types.subnet_ids

        out["SubnetIds"] = capo_workspaces.types.subnet_ids.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    if "dns_ip_addresses" in value:
        import capo_workspaces.types.dns_ip_addresses

        out["DnsIpAddresses"] = (
            capo_workspaces.types.dns_ip_addresses.serialize_aws_json_1_1(
                value["dns_ip_addresses"]
            )
        )
    if "dns_ipv6_addresses" in value:
        import capo_workspaces.types.dns_ipv6_addresses

        out["DnsIpv6Addresses"] = (
            capo_workspaces.types.dns_ipv6_addresses.serialize_aws_json_1_1(
                value["dns_ipv6_addresses"]
            )
        )
    if "customer_user_name" in value:
        out["CustomerUserName"] = value["customer_user_name"]
    if "iam_role_id" in value:
        out["IamRoleId"] = value["iam_role_id"]
    if "directory_type" in value:
        import capo_workspaces.types.workspace_directory_type

        out["DirectoryType"] = (
            capo_workspaces.types.workspace_directory_type.serialize_aws_json_1_1(
                value["directory_type"]
            )
        )
    if "workspace_security_group_id" in value:
        out["WorkspaceSecurityGroupId"] = value["workspace_security_group_id"]
    if "state" in value:
        import capo_workspaces.types.workspace_directory_state

        out["State"] = (
            capo_workspaces.types.workspace_directory_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "workspace_creation_properties" in value:
        import capo_workspaces.types.default_workspace_creation_properties

        out["WorkspaceCreationProperties"] = (
            capo_workspaces.types.default_workspace_creation_properties.serialize_aws_json_1_1(
                value["workspace_creation_properties"]
            )
        )
    if "ip_group_ids" in value:
        import capo_workspaces.types.ip_group_id_list

        out["ipGroupIds"] = (
            capo_workspaces.types.ip_group_id_list.serialize_aws_json_1_1(
                value["ip_group_ids"]
            )
        )
    if "workspace_access_properties" in value:
        import capo_workspaces.types.workspace_access_properties

        out["WorkspaceAccessProperties"] = (
            capo_workspaces.types.workspace_access_properties.serialize_aws_json_1_1(
                value["workspace_access_properties"]
            )
        )
    if "tenancy" in value:
        import capo_workspaces.types.tenancy

        out["Tenancy"] = capo_workspaces.types.tenancy.serialize_aws_json_1_1(
            value["tenancy"]
        )
    if "selfservice_permissions" in value:
        import capo_workspaces.types.selfservice_permissions

        out["SelfservicePermissions"] = (
            capo_workspaces.types.selfservice_permissions.serialize_aws_json_1_1(
                value["selfservice_permissions"]
            )
        )
    if "saml_properties" in value:
        import capo_workspaces.types.saml_properties

        out["SamlProperties"] = (
            capo_workspaces.types.saml_properties.serialize_aws_json_1_1(
                value["saml_properties"]
            )
        )
    if "certificate_based_auth_properties" in value:
        import capo_workspaces.types.certificate_based_auth_properties

        out["CertificateBasedAuthProperties"] = (
            capo_workspaces.types.certificate_based_auth_properties.serialize_aws_json_1_1(
                value["certificate_based_auth_properties"]
            )
        )
    if "endpoint_encryption_mode" in value:
        import capo_workspaces.types.endpoint_encryption_mode

        out["EndpointEncryptionMode"] = (
            capo_workspaces.types.endpoint_encryption_mode.serialize_aws_json_1_1(
                value["endpoint_encryption_mode"]
            )
        )
    if "microsoft_entra_config" in value:
        import capo_workspaces.types.microsoft_entra_config

        out["MicrosoftEntraConfig"] = (
            capo_workspaces.types.microsoft_entra_config.serialize_aws_json_1_1(
                value["microsoft_entra_config"]
            )
        )
    if "workspace_directory_name" in value:
        out["WorkspaceDirectoryName"] = value["workspace_directory_name"]
    if "workspace_directory_description" in value:
        out["WorkspaceDirectoryDescription"] = value["workspace_directory_description"]
    if "user_identity_type" in value:
        import capo_workspaces.types.user_identity_type

        out["UserIdentityType"] = (
            capo_workspaces.types.user_identity_type.serialize_aws_json_1_1(
                value["user_identity_type"]
            )
        )
    if "workspace_type" in value:
        import capo_workspaces.types.workspace_type

        out["WorkspaceType"] = (
            capo_workspaces.types.workspace_type.serialize_aws_json_1_1(
                value["workspace_type"]
            )
        )
    if "idc_config" in value:
        import capo_workspaces.types.idc_config

        out["IDCConfig"] = capo_workspaces.types.idc_config.serialize_aws_json_1_1(
            value["idc_config"]
        )
    if "active_directory_config" in value:
        import capo_workspaces.types.active_directory_config

        out["ActiveDirectoryConfig"] = (
            capo_workspaces.types.active_directory_config.serialize_aws_json_1_1(
                value["active_directory_config"]
            )
        )
    if "streaming_properties" in value:
        import capo_workspaces.types.streaming_properties

        out["StreamingProperties"] = (
            capo_workspaces.types.streaming_properties.serialize_aws_json_1_1(
                value["streaming_properties"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkspaceDirectory:
    out: WorkspaceDirectory = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    if data.get("DirectoryName") is not None:
        out["directory_name"] = data["DirectoryName"]
    if data.get("RegistrationCode") is not None:
        out["registration_code"] = data["RegistrationCode"]
    if data.get("SubnetIds") is not None:
        import capo_workspaces.types.subnet_ids

        out["subnet_ids"] = capo_workspaces.types.subnet_ids.deserialize_aws_json_1_1(
            data["SubnetIds"]
        )
    if data.get("DnsIpAddresses") is not None:
        import capo_workspaces.types.dns_ip_addresses

        out["dns_ip_addresses"] = (
            capo_workspaces.types.dns_ip_addresses.deserialize_aws_json_1_1(
                data["DnsIpAddresses"]
            )
        )
    if data.get("DnsIpv6Addresses") is not None:
        import capo_workspaces.types.dns_ipv6_addresses

        out["dns_ipv6_addresses"] = (
            capo_workspaces.types.dns_ipv6_addresses.deserialize_aws_json_1_1(
                data["DnsIpv6Addresses"]
            )
        )
    if data.get("CustomerUserName") is not None:
        out["customer_user_name"] = data["CustomerUserName"]
    if data.get("IamRoleId") is not None:
        out["iam_role_id"] = data["IamRoleId"]
    if data.get("DirectoryType") is not None:
        import capo_workspaces.types.workspace_directory_type

        out["directory_type"] = (
            capo_workspaces.types.workspace_directory_type.deserialize_aws_json_1_1(
                data["DirectoryType"]
            )
        )
    if data.get("WorkspaceSecurityGroupId") is not None:
        out["workspace_security_group_id"] = data["WorkspaceSecurityGroupId"]
    if data.get("State") is not None:
        import capo_workspaces.types.workspace_directory_state

        out["state"] = (
            capo_workspaces.types.workspace_directory_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if data.get("WorkspaceCreationProperties") is not None:
        import capo_workspaces.types.default_workspace_creation_properties

        out["workspace_creation_properties"] = (
            capo_workspaces.types.default_workspace_creation_properties.deserialize_aws_json_1_1(
                data["WorkspaceCreationProperties"]
            )
        )
    if data.get("ipGroupIds") is not None:
        import capo_workspaces.types.ip_group_id_list

        out["ip_group_ids"] = (
            capo_workspaces.types.ip_group_id_list.deserialize_aws_json_1_1(
                data["ipGroupIds"]
            )
        )
    if data.get("WorkspaceAccessProperties") is not None:
        import capo_workspaces.types.workspace_access_properties

        out["workspace_access_properties"] = (
            capo_workspaces.types.workspace_access_properties.deserialize_aws_json_1_1(
                data["WorkspaceAccessProperties"]
            )
        )
    if data.get("Tenancy") is not None:
        import capo_workspaces.types.tenancy

        out["tenancy"] = capo_workspaces.types.tenancy.deserialize_aws_json_1_1(
            data["Tenancy"]
        )
    if data.get("SelfservicePermissions") is not None:
        import capo_workspaces.types.selfservice_permissions

        out["selfservice_permissions"] = (
            capo_workspaces.types.selfservice_permissions.deserialize_aws_json_1_1(
                data["SelfservicePermissions"]
            )
        )
    if data.get("SamlProperties") is not None:
        import capo_workspaces.types.saml_properties

        out["saml_properties"] = (
            capo_workspaces.types.saml_properties.deserialize_aws_json_1_1(
                data["SamlProperties"]
            )
        )
    if data.get("CertificateBasedAuthProperties") is not None:
        import capo_workspaces.types.certificate_based_auth_properties

        out["certificate_based_auth_properties"] = (
            capo_workspaces.types.certificate_based_auth_properties.deserialize_aws_json_1_1(
                data["CertificateBasedAuthProperties"]
            )
        )
    if data.get("EndpointEncryptionMode") is not None:
        import capo_workspaces.types.endpoint_encryption_mode

        out["endpoint_encryption_mode"] = (
            capo_workspaces.types.endpoint_encryption_mode.deserialize_aws_json_1_1(
                data["EndpointEncryptionMode"]
            )
        )
    if data.get("MicrosoftEntraConfig") is not None:
        import capo_workspaces.types.microsoft_entra_config

        out["microsoft_entra_config"] = (
            capo_workspaces.types.microsoft_entra_config.deserialize_aws_json_1_1(
                data["MicrosoftEntraConfig"]
            )
        )
    if data.get("WorkspaceDirectoryName") is not None:
        out["workspace_directory_name"] = data["WorkspaceDirectoryName"]
    if data.get("WorkspaceDirectoryDescription") is not None:
        out["workspace_directory_description"] = data["WorkspaceDirectoryDescription"]
    if data.get("UserIdentityType") is not None:
        import capo_workspaces.types.user_identity_type

        out["user_identity_type"] = (
            capo_workspaces.types.user_identity_type.deserialize_aws_json_1_1(
                data["UserIdentityType"]
            )
        )
    if data.get("WorkspaceType") is not None:
        import capo_workspaces.types.workspace_type

        out["workspace_type"] = (
            capo_workspaces.types.workspace_type.deserialize_aws_json_1_1(
                data["WorkspaceType"]
            )
        )
    if data.get("IDCConfig") is not None:
        import capo_workspaces.types.idc_config

        out["idc_config"] = capo_workspaces.types.idc_config.deserialize_aws_json_1_1(
            data["IDCConfig"]
        )
    if data.get("ActiveDirectoryConfig") is not None:
        import capo_workspaces.types.active_directory_config

        out["active_directory_config"] = (
            capo_workspaces.types.active_directory_config.deserialize_aws_json_1_1(
                data["ActiveDirectoryConfig"]
            )
        )
    if data.get("StreamingProperties") is not None:
        import capo_workspaces.types.streaming_properties

        out["streaming_properties"] = (
            capo_workspaces.types.streaming_properties.deserialize_aws_json_1_1(
                data["StreamingProperties"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
