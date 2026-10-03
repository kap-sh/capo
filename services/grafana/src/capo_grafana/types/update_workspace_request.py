"""Generated from Smithy shape ``com.amazonaws.grafana#UpdateWorkspaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.account_access_type
    import capo_grafana.types.data_source_types_list
    import capo_grafana.types.description
    import capo_grafana.types.iam_role_arn
    import capo_grafana.types.ip_address_type
    import capo_grafana.types.network_access_configuration
    import capo_grafana.types.notification_destinations_list
    import capo_grafana.types.organization_role_name
    import capo_grafana.types.organizational_unit_list
    import capo_grafana.types.permission_type
    import capo_grafana.types.stack_set_name
    import capo_grafana.types.vpc_configuration
    import capo_grafana.types.workspace_id
    import capo_grafana.types.workspace_name


class UpdateWorkspaceRequest(TypedDict, closed=True):
    account_access_type: NotRequired[
        "capo_grafana.types.account_access_type.AccountAccessType"
    ]
    """<p>Specifies whether the workspace can access Amazon Web Services resources in this Amazon Web Services account only, or whether it can also access Amazon Web Services resources in other accounts in the same organization. If you specify <code>ORGANIZATION</code>, you must specify which organizational units the workspace can access in the <code>workspaceOrganizationalUnits</code> parameter.</p>"""
    organization_role_name: NotRequired[
        "capo_grafana.types.organization_role_name.OrganizationRoleName"
    ]
    """<p>The name of an IAM role that already exists to use to access resources through Organizations. This can only be used with a workspace that has the <code>permissionType</code> set to <code>CUSTOMER_MANAGED</code>.</p>"""
    permission_type: NotRequired["capo_grafana.types.permission_type.PermissionType"]
    """<p>Use this parameter if you want to change a workspace from <code>SERVICE_MANAGED</code> to <code>CUSTOMER_MANAGED</code>. This allows you to manage the permissions that the workspace uses to access datasources and notification channels. If the workspace is in a member Amazon Web Services account of an organization, and that account is not a delegated administrator account, and you want the workspace to access data sources in other Amazon Web Services accounts in the organization, you must choose <code>CUSTOMER_MANAGED</code>.</p> <p>If you specify this as <code>CUSTOMER_MANAGED</code>, you must also specify a <code>workspaceRoleArn</code> that the workspace will use for accessing Amazon Web Services resources.</p> <p>For more information on the role and permissions needed, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/AMG-manage-permissions.html">Amazon Managed Grafana permissions and policies for Amazon Web Services data sources and notification channels</a> </p> <note> <p>Do not use this to convert a <code>CUSTOMER_MANAGED</code> workspace to <code>SERVICE_MANAGED</code>. Do not include this parameter if you want to leave the workspace as <code>SERVICE_MANAGED</code>.</p> <p>You can convert a <code>CUSTOMER_MANAGED</code> workspace to <code>SERVICE_MANAGED</code> using the Amazon Managed Grafana console. For more information, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/AMG-datasource-and-notification.html">Managing permissions for data sources and notification channels</a>.</p> </note>"""
    stack_set_name: NotRequired["capo_grafana.types.stack_set_name.StackSetName"]
    """<p>The name of the CloudFormation stack set to use to generate IAM roles to be used for this workspace.</p>"""
    workspace_data_sources: NotRequired[
        "capo_grafana.types.data_source_types_list.DataSourceTypesList"
    ]
    """<p>This parameter is for internal use only, and should not be used.</p>"""
    workspace_description: NotRequired["capo_grafana.types.description.Description"]
    """<p>A description for the workspace. This is used only to help you identify this workspace.</p>"""
    workspace_id: "capo_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to update.</p>"""
    workspace_name: NotRequired["capo_grafana.types.workspace_name.WorkspaceName"]
    """<p>A new name for the workspace to update.</p>"""
    workspace_notification_destinations: NotRequired[
        "capo_grafana.types.notification_destinations_list.NotificationDestinationsList"
    ]
    """<p>Specify the Amazon Web Services notification channels that you plan to use in this workspace. Specifying these data sources here enables Amazon Managed Grafana to create IAM roles and permissions that allow Amazon Managed Grafana to use these channels.</p>"""
    workspace_organizational_units: NotRequired[
        "capo_grafana.types.organizational_unit_list.OrganizationalUnitList"
    ]
    """<p>Specifies the organizational units that this workspace is allowed to use data sources from, if this workspace is in an account that is part of an organization.</p>"""
    workspace_role_arn: NotRequired["capo_grafana.types.iam_role_arn.IamRoleArn"]
    """<p>Specifies an IAM role that grants permissions to Amazon Web Services resources that the workspace accesses, such as data sources and notification channels. If this workspace has <code>permissionType</code> <code>CUSTOMER_MANAGED</code>, then this role is required.</p>"""
    vpc_configuration: NotRequired[
        "capo_grafana.types.vpc_configuration.VpcConfiguration"
    ]
    """<p>The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.</p>"""
    remove_vpc_configuration: NotRequired["bool"]
    """<p>Whether to remove the VPC configuration from the workspace.</p> <p>Setting this to <code>true</code> and providing a <code>vpcConfiguration</code> to set will return an error.</p>"""
    network_access_control: NotRequired[
        "capo_grafana.types.network_access_configuration.NetworkAccessConfiguration"
    ]
    """<p>The configuration settings for network access to your workspace.</p> <p>When this is configured, only listed IP addresses and VPC endpoints will be able to access your workspace. Standard Grafana authentication and authorization will still be required.</p> <p>If this is not configured, or is removed, then all IP addresses and VPC endpoints will be allowed. Standard Grafana authentication and authorization will still be required.</p>"""
    remove_network_access_configuration: NotRequired["bool"]
    """<p>Whether to remove the network access configuration from the workspace.</p> <p>Setting this to <code>true</code> and providing a <code>networkAccessControl</code> to set will return an error.</p> <p>If you remove this configuration by setting this to <code>true</code>, then all IP addresses and VPC endpoints will be allowed. Standard Grafana authentication and authorization will still be required.</p>"""
    ip_address_type: NotRequired["capo_grafana.types.ip_address_type.IPAddressType"]
    """<p>Specifies whether the workspace supports IPv4 only, or IPv4 and IPv6. Valid values are <code>IPv4</code> and <code>DualStack</code>. For more information about IP address types, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-nac.html">Network access control</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspaceRequest) -> dict:
    out: dict = {}
    if "account_access_type" in value:
        out["accountAccessType"] = value["account_access_type"]
    if "organization_role_name" in value:
        out["organizationRoleName"] = value["organization_role_name"]
    if "permission_type" in value:
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
    if "vpc_configuration" in value:
        import capo_grafana.types.vpc_configuration

        out["vpcConfiguration"] = capo_grafana.types.vpc_configuration.serialize_json(
            value["vpc_configuration"]
        )
    if "remove_vpc_configuration" in value:
        out["removeVpcConfiguration"] = value["remove_vpc_configuration"]
    if "network_access_control" in value:
        import capo_grafana.types.network_access_configuration

        out["networkAccessControl"] = (
            capo_grafana.types.network_access_configuration.serialize_json(
                value["network_access_control"]
            )
        )
    if "remove_network_access_configuration" in value:
        out["removeNetworkAccessConfiguration"] = value[
            "remove_network_access_configuration"
        ]
    if "ip_address_type" in value:
        out["ipAddressType"] = value["ip_address_type"]
    return out


def deserialize_json(data: dict) -> UpdateWorkspaceRequest:
    out: UpdateWorkspaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountAccessType") is not None:
        out["account_access_type"] = data["accountAccessType"]
    if data.get("organizationRoleName") is not None:
        out["organization_role_name"] = data["organizationRoleName"]
    if data.get("permissionType") is not None:
        out["permission_type"] = data["permissionType"]
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
    if data.get("vpcConfiguration") is not None:
        import capo_grafana.types.vpc_configuration

        out["vpc_configuration"] = (
            capo_grafana.types.vpc_configuration.deserialize_json(
                data["vpcConfiguration"]
            )
        )
    if data.get("removeVpcConfiguration") is not None:
        out["remove_vpc_configuration"] = data["removeVpcConfiguration"]
    if data.get("networkAccessControl") is not None:
        import capo_grafana.types.network_access_configuration

        out["network_access_control"] = (
            capo_grafana.types.network_access_configuration.deserialize_json(
                data["networkAccessControl"]
            )
        )
    if data.get("removeNetworkAccessConfiguration") is not None:
        out["remove_network_access_configuration"] = data[
            "removeNetworkAccessConfiguration"
        ]
    if data.get("ipAddressType") is not None:
        out["ip_address_type"] = data["ipAddressType"]
    return out
