"""Generated from Smithy shape ``com.amazonaws.grafana#CreateWorkspaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import capo_grafana.types.account_access_type
    import capo_grafana.types.authentication_providers
    import capo_grafana.types.client_token
    import capo_grafana.types.data_source_types_list
    import capo_grafana.types.description
    import capo_grafana.types.grafana_version
    import capo_grafana.types.iam_role_arn
    import capo_grafana.types.ip_address_type
    import capo_grafana.types.kms_key_id
    import capo_grafana.types.network_access_configuration
    import capo_grafana.types.notification_destinations_list
    import capo_grafana.types.organization_role_name
    import capo_grafana.types.organizational_unit_list
    import capo_grafana.types.overridable_configuration_json
    import capo_grafana.types.permission_type
    import capo_grafana.types.stack_set_name
    import capo_grafana.types.tag_map
    import capo_grafana.types.vpc_configuration
    import capo_grafana.types.workspace_name


class CreateWorkspaceRequest(TypedDict, closed=True):
    account_access_type: "capo_grafana.types.account_access_type.AccountAccessType"
    """<p>Specifies whether the workspace can access Amazon Web Services resources in this Amazon Web Services account only, or whether it can also access Amazon Web Services resources in other accounts in the same organization. If you specify <code>ORGANIZATION</code>, you must specify which organizational units the workspace can access in the <code>workspaceOrganizationalUnits</code> parameter.</p>"""
    client_token: NotRequired["capo_grafana.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive, user-provided identifier to ensure the idempotency of the request.</p>"""
    organization_role_name: NotRequired[
        "capo_grafana.types.organization_role_name.OrganizationRoleName"
    ]
    """<p>The name of an IAM role that already exists to use with Organizations to access Amazon Web Services data sources and notification channels in other accounts in an organization.</p>"""
    permission_type: "capo_grafana.types.permission_type.PermissionType"
    """<p>When creating a workspace through the Amazon Web Services API, CLI or Amazon Web Services CloudFormation, you must manage IAM roles and provision the permissions that the workspace needs to use Amazon Web Services data sources and notification channels.</p> <p>You must also specify a <code>workspaceRoleArn</code> for a role that you will manage for the workspace to use when accessing those datasources and notification channels.</p> <p>The ability for Amazon Managed Grafana to create and update IAM roles on behalf of the user is supported only in the Amazon Managed Grafana console, where this value may be set to <code>SERVICE_MANAGED</code>.</p> <note> <p>Use only the <code>CUSTOMER_MANAGED</code> permission type when creating a workspace with the API, CLI or Amazon Web Services CloudFormation. </p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/AMG-manage-permissions.html">Amazon Managed Grafana permissions and policies for Amazon Web Services data sources and notification channels</a>.</p>"""
    stack_set_name: NotRequired["capo_grafana.types.stack_set_name.StackSetName"]
    """<p>The name of the CloudFormation stack set to use to generate IAM roles to be used for this workspace.</p>"""
    workspace_data_sources: NotRequired[
        "capo_grafana.types.data_source_types_list.DataSourceTypesList"
    ]
    """<p>This parameter is for internal use only, and should not be used.</p>"""
    workspace_description: NotRequired["capo_grafana.types.description.Description"]
    r"""<p>A description for the workspace. This is used only to help you identify this workspace.</p> <p>Pattern: <code>^[\\p{L}\\p{Z}\\p{N}\\p{P}]{0,2048}$</code> </p>"""
    workspace_name: NotRequired["capo_grafana.types.workspace_name.WorkspaceName"]
    """<p>The name for the workspace. It does not have to be unique.</p>"""
    workspace_notification_destinations: NotRequired[
        "capo_grafana.types.notification_destinations_list.NotificationDestinationsList"
    ]
    """<p>Specify the Amazon Web Services notification channels that you plan to use in this workspace. Specifying these data sources here enables Amazon Managed Grafana to create IAM roles and permissions that allow Amazon Managed Grafana to use these channels.</p>"""
    workspace_organizational_units: NotRequired[
        "capo_grafana.types.organizational_unit_list.OrganizationalUnitList"
    ]
    """<p>Specifies the organizational units that this workspace is allowed to use data sources from, if this workspace is in an account that is part of an organization.</p>"""
    workspace_role_arn: NotRequired["capo_grafana.types.iam_role_arn.IamRoleArn"]
    """<p>Specified the IAM role that grants permissions to the Amazon Web Services resources that the workspace will view data from, including both data sources and notification channels. You are responsible for managing the permissions for this role as new data sources or notification channels are added. </p>"""
    authentication_providers: (
        "capo_grafana.types.authentication_providers.AuthenticationProviders"
    )
    """<p>Specifies whether this workspace uses SAML 2.0, IAM Identity Center, or both to authenticate users for using the Grafana console within a workspace. For more information, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/authentication-in-AMG.html">User authentication in Amazon Managed Grafana</a>.</p>"""
    tags: NotRequired["capo_grafana.types.tag_map.TagMap"]
    """<p>The list of tags associated with the workspace.</p>"""
    vpc_configuration: NotRequired[
        "capo_grafana.types.vpc_configuration.VpcConfiguration"
    ]
    """<p>The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.</p> <note> <p>Connecting to a private VPC is not yet available in the Asia Pacific (Seoul) Region (ap-northeast-2).</p> </note>"""
    configuration: NotRequired[
        "capo_grafana.types.overridable_configuration_json.OverridableConfigurationJson"
    ]
    """<p>The configuration string for the workspace that you create. For more information about the format and configuration options available, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-workspace.html">Working in your Grafana workspace</a>.</p>"""
    network_access_control: NotRequired[
        "capo_grafana.types.network_access_configuration.NetworkAccessConfiguration"
    ]
    """<p>Configuration for network access to your workspace.</p> <p>When this is configured, only listed IP addresses and VPC endpoints will be able to access your workspace. Standard Grafana authentication and authorization will still be required.</p> <p>If this is not configured, or is removed, then all IP addresses and VPC endpoints will be allowed. Standard Grafana authentication and authorization will still be required.</p>"""
    grafana_version: NotRequired["capo_grafana.types.grafana_version.GrafanaVersion"]
    """<p>Specifies the version of Grafana to support in the new workspace. If not specified, defaults to the latest version (for example, 10.4).</p> <p>To get a list of supported versions, use the <code>ListVersions</code> operation.</p>"""
    ip_address_type: NotRequired["capo_grafana.types.ip_address_type.IPAddressType"]
    """<p>Specifies whether the workspace supports IPv4 only, or IPv4 and IPv6. Valid values are <code>IPv4</code> and <code>DualStack</code>. For more information about IP address types, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-nac.html">Network access control</a>.</p>"""
    kms_key_id: NotRequired["capo_grafana.types.kms_key_id.KmsKeyId"]
    """<p>The ID or ARN of the Key Management Service key to use for encrypting workspace data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspaceRequest) -> dict:
    out: dict = {}
    out["accountAccessType"] = value["account_access_type"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "organization_role_name" in value:
        out["organizationRoleName"] = value["organization_role_name"]
    out["permissionType"] = value["permission_type"]
    if "stack_set_name" in value:
        out["stackSetName"] = value["stack_set_name"]
    if "workspace_data_sources" in value:
        import capo_grafana.types.data_source_types_list

        out["workspaceDataSources"] = (
            capo_grafana.types.data_source_types_list.serialize_json(
                value["workspace_data_sources"]
            )
        )
    if "workspace_description" in value:
        out["workspaceDescription"] = value["workspace_description"]
    if "workspace_name" in value:
        out["workspaceName"] = value["workspace_name"]
    if "workspace_notification_destinations" in value:
        import capo_grafana.types.notification_destinations_list

        out["workspaceNotificationDestinations"] = (
            capo_grafana.types.notification_destinations_list.serialize_json(
                value["workspace_notification_destinations"]
            )
        )
    if "workspace_organizational_units" in value:
        import capo_grafana.types.organizational_unit_list

        out["workspaceOrganizationalUnits"] = (
            capo_grafana.types.organizational_unit_list.serialize_json(
                value["workspace_organizational_units"]
            )
        )
    if "workspace_role_arn" in value:
        out["workspaceRoleArn"] = value["workspace_role_arn"]
    import capo_grafana.types.authentication_providers

    out["authenticationProviders"] = (
        capo_grafana.types.authentication_providers.serialize_json(
            value["authentication_providers"]
        )
    )
    if "tags" in value:
        import capo_grafana.types.tag_map

        out["tags"] = capo_grafana.types.tag_map.serialize_json(value["tags"])
    if "vpc_configuration" in value:
        import capo_grafana.types.vpc_configuration

        out["vpcConfiguration"] = capo_grafana.types.vpc_configuration.serialize_json(
            value["vpc_configuration"]
        )
    if "configuration" in value:
        out["configuration"] = value["configuration"]
    if "network_access_control" in value:
        import capo_grafana.types.network_access_configuration

        out["networkAccessControl"] = (
            capo_grafana.types.network_access_configuration.serialize_json(
                value["network_access_control"]
            )
        )
    if "grafana_version" in value:
        out["grafanaVersion"] = value["grafana_version"]
    if "ip_address_type" in value:
        out["ipAddressType"] = value["ip_address_type"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> CreateWorkspaceRequest:
    out: CreateWorkspaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountAccessType") is not None:
        out["account_access_type"] = data["accountAccessType"]
    else:
        raise DeserializationError(
            "CreateWorkspaceRequest.account_access_type required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("organizationRoleName") is not None:
        out["organization_role_name"] = data["organizationRoleName"]
    if data.get("permissionType") is not None:
        out["permission_type"] = data["permissionType"]
    else:
        raise DeserializationError("CreateWorkspaceRequest.permission_type required")
    if data.get("stackSetName") is not None:
        out["stack_set_name"] = data["stackSetName"]
    if data.get("workspaceDataSources") is not None:
        import capo_grafana.types.data_source_types_list

        out["workspace_data_sources"] = (
            capo_grafana.types.data_source_types_list.deserialize_json(
                data["workspaceDataSources"]
            )
        )
    if data.get("workspaceDescription") is not None:
        out["workspace_description"] = data["workspaceDescription"]
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    if data.get("workspaceNotificationDestinations") is not None:
        import capo_grafana.types.notification_destinations_list

        out["workspace_notification_destinations"] = (
            capo_grafana.types.notification_destinations_list.deserialize_json(
                data["workspaceNotificationDestinations"]
            )
        )
    if data.get("workspaceOrganizationalUnits") is not None:
        import capo_grafana.types.organizational_unit_list

        out["workspace_organizational_units"] = (
            capo_grafana.types.organizational_unit_list.deserialize_json(
                data["workspaceOrganizationalUnits"]
            )
        )
    if data.get("workspaceRoleArn") is not None:
        out["workspace_role_arn"] = data["workspaceRoleArn"]
    if data.get("authenticationProviders") is not None:
        import capo_grafana.types.authentication_providers

        out["authentication_providers"] = (
            capo_grafana.types.authentication_providers.deserialize_json(
                data["authenticationProviders"]
            )
        )
    else:
        raise DeserializationError(
            "CreateWorkspaceRequest.authentication_providers required"
        )
    if data.get("tags") is not None:
        import capo_grafana.types.tag_map

        out["tags"] = capo_grafana.types.tag_map.deserialize_json(data["tags"])
    if data.get("vpcConfiguration") is not None:
        import capo_grafana.types.vpc_configuration

        out["vpc_configuration"] = (
            capo_grafana.types.vpc_configuration.deserialize_json(
                data["vpcConfiguration"]
            )
        )
    if data.get("configuration") is not None:
        out["configuration"] = data["configuration"]
    if data.get("networkAccessControl") is not None:
        import capo_grafana.types.network_access_configuration

        out["network_access_control"] = (
            capo_grafana.types.network_access_configuration.deserialize_json(
                data["networkAccessControl"]
            )
        )
    if data.get("grafanaVersion") is not None:
        out["grafana_version"] = data["grafanaVersion"]
    if data.get("ipAddressType") is not None:
        out["ip_address_type"] = data["ipAddressType"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
