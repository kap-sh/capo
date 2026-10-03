"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateContainerFleetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.connection_port_range
    import capo_gamelift.types.container_fleet_billing_type
    import capo_gamelift.types.container_group_definition_name_or_arn
    import capo_gamelift.types.game_server_container_groups_per_instance
    import capo_gamelift.types.game_session_creation_limit_policy
    import capo_gamelift.types.iam_role_arn
    import capo_gamelift.types.ip_permissions_list
    import capo_gamelift.types.location_configuration_list
    import capo_gamelift.types.log_configuration
    import capo_gamelift.types.metric_group_list
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.player_gateway_mode
    import capo_gamelift.types.protection_policy
    import capo_gamelift.types.tag_list


class CreateContainerFleetInput(TypedDict, closed=True):
    fleet_role_arn: NotRequired["capo_gamelift.types.iam_role_arn.IamRoleArn"]
    """<p>The unique identifier for an Identity and Access Management (IAM) role with permissions to run your containers on resources that are managed by Amazon GameLift Servers. Use an IAM service role with the <code>GameLiftContainerFleetPolicy</code> managed policy attached. For more information, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/setting-up-role.html">Set up an IAM service role</a>. You can't change this fleet property after the fleet is created.</p> <p>IAM role ARN values use the following pattern: <code>arn:aws:iam::[Amazon Web Services account]:role/[role name]</code>.</p>"""
    description: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A meaningful description of the container fleet.</p>"""
    game_server_container_group_definition_name: NotRequired[
        "capo_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
    ]
    """<p>A container group definition resource that describes how to deploy containers with your game server build and support software onto each fleet instance. You can specify the container group definition's name to use the latest version. Alternatively, provide an ARN value with a specific version number.</p> <p>Create a container group definition by calling <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html">CreateContainerGroupDefinition</a>. This operation creates a <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html">ContainerGroupDefinition</a> resource. </p>"""
    per_instance_container_group_definition_name: NotRequired[
        "capo_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
    ]
    """<p>The name of a container group definition resource that describes a set of axillary software. A fleet instance has one process for executables in this container group. A per-instance container group is optional. You can update the fleet to add or remove a per-instance container group at any time. You can specify the container group definition's name to use the latest version. Alternatively, provide an ARN value with a specific version number. </p> <p>Create a container group definition by calling <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html">https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html</a>. This operation creates a <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html">https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html</a> resource.</p>"""
    instance_connection_port_range: NotRequired[
        "capo_gamelift.types.connection_port_range.ConnectionPortRange"
    ]
    """<p>The set of port numbers to open on each fleet instance. A fleet's connection ports map to container ports that are configured in the fleet's container group definitions. </p> <p>By default, Amazon GameLift Servers calculates an optimal port range based on your fleet configuration. To use the calculated range, don't set this parameter. The values are:</p> <ul> <li> <p>Port range: 4192 to a number calculated based on your fleet configuration. Amazon GameLift Servers uses the following formula: <code>4192 + [# of game server container groups per fleet instance] * [# of container ports in the game server container group definition] + [# of container ports in the per instance container group definition]</code> </p> </li> </ul> <p>You can also choose to manually set this parameter. When manually setting this parameter, you must use port numbers that match the fleet's inbound permissions port range.</p> <note> <p>If you set values manually, Amazon GameLift Servers no longer calculates a port range for you, even if you later remove the manual settings. </p> </note> <p>The port range must not overlap with the Amazon GameLift Servers reserved port range <code>4092-4191</code>. This range is reserved for internal Amazon GameLift Servers services.</p>"""
    instance_inbound_permissions: NotRequired[
        "capo_gamelift.types.ip_permissions_list.IpPermissionsList"
    ]
    """<p>The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet. As a best practice, when remotely accessing a fleet instance, we recommend opening ports only when you need them and closing them when you're finished.</p> <p>By default, Amazon GameLift Servers calculates an optimal port range based on your fleet configuration. To use the calculated range, don't set this parameter. The values are:</p> <ul> <li> <p>Protocol: UDP</p> </li> <li> <p>Port range: 4192 to a number calculated based on your fleet configuration. Amazon GameLift Servers uses the following formula: <code>4192 + [# of game server container groups per fleet instance] * [# of container ports in the game server container group definition] + [# of container ports in the per instance container group definition]</code> </p> </li> </ul> <p>You can also choose to manually set this parameter. When manually setting this parameter, you must use port numbers that match the fleet's connection port range.</p> <note> <p>If you set values manually, Amazon GameLift Servers no longer calculates a port range for you, even if you later remove the manual settings. </p> </note> <p>The port range must not overlap with the Amazon GameLift Servers reserved port range <code>4092-4191</code>. This range is reserved for internal Amazon GameLift Servers services.</p>"""
    game_server_container_groups_per_instance: NotRequired[
        "capo_gamelift.types.game_server_container_groups_per_instance.GameServerContainerGroupsPerInstance"
    ]
    """<p>The number of times to replicate the game server container group on each fleet instance. </p> <p>By default, Amazon GameLift Servers calculates the maximum number of game server container groups that can fit on each instance. This calculation is based on the CPU and memory resources of the fleet's instance type). To use the calculated maximum, don't set this parameter. If you set this number manually, Amazon GameLift Servers uses your value as long as it's less than the calculated maximum.</p>"""
    instance_type: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>The Amazon EC2 instance type to use for all instances in the fleet. For multi-location fleets, the instance type must be available in the home region and all remote locations. Instance type determines the computing resources and processing power that's available to host your game servers. This includes including CPU, memory, storage, and networking capacity. </p> <p>By default, Amazon GameLift Servers uses the <code>c5.large</code> instance type. If this instance type does not have sufficient resources for your container groups, you can choose a different instance type that better fits your needs. See <a href="http://aws.amazon.com/ec2/instance-types/">Amazon Elastic Compute Cloud Instance Types</a> for detailed descriptions of Amazon EC2 instance types.</p> <p>You can't update this fleet property later.</p>"""
    billing_type: NotRequired[
        "capo_gamelift.types.container_fleet_billing_type.ContainerFleetBillingType"
    ]
    """<p>Indicates whether to use On-Demand or Spot instances for this fleet. Learn more about when to use <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot"> On-Demand versus Spot Instances</a>. This fleet property can't be changed after the fleet is created.</p> <p>By default, this property is set to <code>ON_DEMAND</code>.</p> <p>You can't update this fleet property later.</p>"""
    locations: NotRequired[
        "capo_gamelift.types.location_configuration_list.LocationConfigurationList"
    ]
    """<p>A set of locations to deploy container fleet instances to. You can add any Amazon Web Services Region or Local Zone that's supported by Amazon GameLift Servers. Provide a list of one or more Amazon Web Services Region codes, such as <code>us-west-2</code>, or Local Zone names. Also include the fleet's home Region, which is the Amazon Web Services Region where the fleet is created. For a list of supported Regions and Local Zones, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html"> Amazon GameLift Servers service locations</a> for managed hosting.</p>"""
    metric_groups: NotRequired["capo_gamelift.types.metric_group_list.MetricGroupList"]
    """<p>The name of an Amazon Web Services CloudWatch metric group to add this fleet to. You can use a metric group to aggregate metrics for multiple fleets. You can specify an existing metric group name or use a new name to create a new metric group. Each fleet can have only one metric group, but you can change this value at any time. </p>"""
    new_game_session_protection_policy: NotRequired[
        "capo_gamelift.types.protection_policy.ProtectionPolicy"
    ]
    """<p>Determines whether Amazon GameLift Servers can shut down game sessions on the fleet that are actively running and hosting players. Amazon GameLift Servers might prompt an instance shutdown when scaling down fleet capacity or when retiring unhealthy instances. You can also set game session protection for individual game sessions using <a href="gamelift/latest/apireference/API_UpdateGameSession.html">UpdateGameSession</a>.</p> <ul> <li> <p> <b>NoProtection</b> -- Game sessions can be shut down during active gameplay. </p> </li> <li> <p> <b>FullProtection</b> -- Game sessions in <code>ACTIVE</code> status can't be shut down.</p> </li> </ul> <p>By default, this property is set to <code>NoProtection</code>. </p>"""
    game_session_creation_limit_policy: NotRequired[
        "capo_gamelift.types.game_session_creation_limit_policy.GameSessionCreationLimitPolicy"
    ]
    """<p>A policy that limits the number of game sessions that each individual player can create on instances in this fleet. The limit applies for a specified span of time.</p>"""
    log_configuration: NotRequired[
        "capo_gamelift.types.log_configuration.LogConfiguration"
    ]
    """<p>A method for collecting container logs for the fleet. Amazon GameLift Servers saves all standard output for each container in logs, including game session logs. You can select from the following methods: </p> <ul> <li> <p> <code>CLOUDWATCH</code> -- Send logs to an Amazon CloudWatch log group that you define. Each container emits a log stream, which is organized in the log group. </p> </li> <li> <p> <code>S3</code> -- Store logs in an Amazon S3 bucket that you define.</p> </li> <li> <p> <code>NONE</code> -- Don't collect container logs.</p> </li> </ul> <p>By default, this property is set to <code>CLOUDWATCH</code>. </p> <p>Amazon GameLift Servers requires permissions to send logs other Amazon Web Services services in your account. These permissions are included in the IAM fleet role for this container fleet (see <code>FleetRoleArn)</code>.</p>"""
    tags: NotRequired["capo_gamelift.types.tag_list.TagList"]
    """<p>A list of labels to assign to the new fleet resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources are useful for resource management, access management and cost allocation. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    player_gateway_mode: NotRequired[
        "capo_gamelift.types.player_gateway_mode.PlayerGatewayMode"
    ]
    """<p>Configures player gateway for your fleet. Player gateway provides benefits such as DDoS protection by rate limiting and validating traﬃc before it reaches game servers, hiding game server IP addresses from players, and providing updated endpoints when relay endpoints become unhealthy.</p> <p> <b>How it works:</b> When enabled, game clients connect to relay endpoints instead of to your game servers. Player gateway validates player gateway tokens and routes traffic to the appropriate game server. Your game backend calls <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetPlayerConnectionDetails.html">GetPlayerConnectionDetails</a> to retrieve relay endpoints and player gateway tokens for your game clients. To learn more about this topic, see <a href="https://docs.aws.amazon.com/gameliftservers/latest/developerguide/ddos-protection-intro.html">DDoS protection with Amazon GameLift Servers player gateway</a>.</p> <p>Possible values include:</p> <ul> <li> <p> <code>DISABLED</code> (default) -- Game clients connect to the game server endpoint. Use this when you do not intend to integrate your game with player gateway.</p> </li> <li> <p> <code>ENABLED</code> -- Player gateway is available in fleet locations where it is supported. Your game backend can call <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetPlayerConnectionDetails.html">GetPlayerConnectionDetails</a> to obtain a player gateway token and endpoints for game clients.</p> </li> <li> <p> <code>REQUIRED</code> -- Player gateway is available in fleet locations where it is supported, and the fleet can only use locations that support this feature. Attempting to add a remote location to your fleet which does not support player gateway will result in an <code>InvalidRequestException</code>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContainerFleetInput) -> dict:
    out: dict = {}
    if "fleet_role_arn" in value:
        out["FleetRoleArn"] = value["fleet_role_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "game_server_container_group_definition_name" in value:
        out["GameServerContainerGroupDefinitionName"] = value[
            "game_server_container_group_definition_name"
        ]
    if "per_instance_container_group_definition_name" in value:
        out["PerInstanceContainerGroupDefinitionName"] = value[
            "per_instance_container_group_definition_name"
        ]
    if "instance_connection_port_range" in value:
        import capo_gamelift.types.connection_port_range

        out["InstanceConnectionPortRange"] = (
            capo_gamelift.types.connection_port_range.serialize_aws_json_1_1(
                value["instance_connection_port_range"]
            )
        )
    if "instance_inbound_permissions" in value:
        import capo_gamelift.types.ip_permissions_list

        out["InstanceInboundPermissions"] = (
            capo_gamelift.types.ip_permissions_list.serialize_aws_json_1_1(
                value["instance_inbound_permissions"]
            )
        )
    if "game_server_container_groups_per_instance" in value:
        out["GameServerContainerGroupsPerInstance"] = value[
            "game_server_container_groups_per_instance"
        ]
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "billing_type" in value:
        import capo_gamelift.types.container_fleet_billing_type

        out["BillingType"] = (
            capo_gamelift.types.container_fleet_billing_type.serialize_aws_json_1_1(
                value["billing_type"]
            )
        )
    if "locations" in value:
        import capo_gamelift.types.location_configuration_list

        out["Locations"] = (
            capo_gamelift.types.location_configuration_list.serialize_aws_json_1_1(
                value["locations"]
            )
        )
    if "metric_groups" in value:
        import capo_gamelift.types.metric_group_list

        out["MetricGroups"] = (
            capo_gamelift.types.metric_group_list.serialize_aws_json_1_1(
                value["metric_groups"]
            )
        )
    if "new_game_session_protection_policy" in value:
        import capo_gamelift.types.protection_policy

        out["NewGameSessionProtectionPolicy"] = (
            capo_gamelift.types.protection_policy.serialize_aws_json_1_1(
                value["new_game_session_protection_policy"]
            )
        )
    if "game_session_creation_limit_policy" in value:
        import capo_gamelift.types.game_session_creation_limit_policy

        out["GameSessionCreationLimitPolicy"] = (
            capo_gamelift.types.game_session_creation_limit_policy.serialize_aws_json_1_1(
                value["game_session_creation_limit_policy"]
            )
        )
    if "log_configuration" in value:
        import capo_gamelift.types.log_configuration

        out["LogConfiguration"] = (
            capo_gamelift.types.log_configuration.serialize_aws_json_1_1(
                value["log_configuration"]
            )
        )
    if "tags" in value:
        import capo_gamelift.types.tag_list

        out["Tags"] = capo_gamelift.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "player_gateway_mode" in value:
        import capo_gamelift.types.player_gateway_mode

        out["PlayerGatewayMode"] = (
            capo_gamelift.types.player_gateway_mode.serialize_aws_json_1_1(
                value["player_gateway_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContainerFleetInput:
    out: CreateContainerFleetInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetRoleArn") is not None:
        out["fleet_role_arn"] = data["FleetRoleArn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("GameServerContainerGroupDefinitionName") is not None:
        out["game_server_container_group_definition_name"] = data[
            "GameServerContainerGroupDefinitionName"
        ]
    if data.get("PerInstanceContainerGroupDefinitionName") is not None:
        out["per_instance_container_group_definition_name"] = data[
            "PerInstanceContainerGroupDefinitionName"
        ]
    if data.get("InstanceConnectionPortRange") is not None:
        import capo_gamelift.types.connection_port_range

        out["instance_connection_port_range"] = (
            capo_gamelift.types.connection_port_range.deserialize_aws_json_1_1(
                data["InstanceConnectionPortRange"]
            )
        )
    if data.get("InstanceInboundPermissions") is not None:
        import capo_gamelift.types.ip_permissions_list

        out["instance_inbound_permissions"] = (
            capo_gamelift.types.ip_permissions_list.deserialize_aws_json_1_1(
                data["InstanceInboundPermissions"]
            )
        )
    if data.get("GameServerContainerGroupsPerInstance") is not None:
        out["game_server_container_groups_per_instance"] = data[
            "GameServerContainerGroupsPerInstance"
        ]
    if data.get("InstanceType") is not None:
        out["instance_type"] = data["InstanceType"]
    if data.get("BillingType") is not None:
        import capo_gamelift.types.container_fleet_billing_type

        out["billing_type"] = (
            capo_gamelift.types.container_fleet_billing_type.deserialize_aws_json_1_1(
                data["BillingType"]
            )
        )
    if data.get("Locations") is not None:
        import capo_gamelift.types.location_configuration_list

        out["locations"] = (
            capo_gamelift.types.location_configuration_list.deserialize_aws_json_1_1(
                data["Locations"]
            )
        )
    if data.get("MetricGroups") is not None:
        import capo_gamelift.types.metric_group_list

        out["metric_groups"] = (
            capo_gamelift.types.metric_group_list.deserialize_aws_json_1_1(
                data["MetricGroups"]
            )
        )
    if data.get("NewGameSessionProtectionPolicy") is not None:
        import capo_gamelift.types.protection_policy

        out["new_game_session_protection_policy"] = (
            capo_gamelift.types.protection_policy.deserialize_aws_json_1_1(
                data["NewGameSessionProtectionPolicy"]
            )
        )
    if data.get("GameSessionCreationLimitPolicy") is not None:
        import capo_gamelift.types.game_session_creation_limit_policy

        out["game_session_creation_limit_policy"] = (
            capo_gamelift.types.game_session_creation_limit_policy.deserialize_aws_json_1_1(
                data["GameSessionCreationLimitPolicy"]
            )
        )
    if data.get("LogConfiguration") is not None:
        import capo_gamelift.types.log_configuration

        out["log_configuration"] = (
            capo_gamelift.types.log_configuration.deserialize_aws_json_1_1(
                data["LogConfiguration"]
            )
        )
    if data.get("Tags") is not None:
        import capo_gamelift.types.tag_list

        out["tags"] = capo_gamelift.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("PlayerGatewayMode") is not None:
        import capo_gamelift.types.player_gateway_mode

        out["player_gateway_mode"] = (
            capo_gamelift.types.player_gateway_mode.deserialize_aws_json_1_1(
                data["PlayerGatewayMode"]
            )
        )
    return out
