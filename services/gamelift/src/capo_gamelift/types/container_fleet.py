"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerFleet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.connection_port_range
    import capo_gamelift.types.container_fleet_billing_type
    import capo_gamelift.types.container_fleet_location_attributes_list
    import capo_gamelift.types.container_fleet_status
    import capo_gamelift.types.container_group_definition_arn
    import capo_gamelift.types.container_group_definition_name
    import capo_gamelift.types.deployment_details
    import capo_gamelift.types.fleet_arn
    import capo_gamelift.types.fleet_id
    import capo_gamelift.types.game_server_container_groups_per_instance
    import capo_gamelift.types.game_session_creation_limit_policy
    import capo_gamelift.types.iam_role_arn
    import capo_gamelift.types.ip_permissions_list
    import capo_gamelift.types.log_configuration
    import capo_gamelift.types.maximum_game_server_container_groups_per_instance
    import capo_gamelift.types.metric_group_list
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.player_gateway_mode
    import capo_gamelift.types.protection_policy
    import capo_gamelift.types.timestamp


class ContainerFleet(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the container fleet to retrieve. </p>"""
    fleet_arn: NotRequired["capo_gamelift.types.fleet_arn.FleetArn"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>. In a GameLift fleet ARN, the resource ID matches the <code>FleetId</code> value.</p>"""
    fleet_role_arn: NotRequired["capo_gamelift.types.iam_role_arn.IamRoleArn"]
    """<p>The unique identifier for an Identity and Access Management (IAM) role with permissions to run your containers on resources that are managed by Amazon GameLift Servers. See <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/setting-up-role.html">Set up an IAM service role</a>. This fleet property can't be changed.</p>"""
    game_server_container_group_definition_name: NotRequired[
        "capo_gamelift.types.container_group_definition_name.ContainerGroupDefinitionName"
    ]
    """<p>The name of the fleet's game server container group definition, which describes how to deploy containers with your game server build and support software onto each fleet instance. </p>"""
    game_server_container_group_definition_arn: NotRequired[
        "capo_gamelift.types.container_group_definition_arn.ContainerGroupDefinitionArn"
    ]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to the fleet's game server container group. The ARN value also identifies the specific container group definition version in use.</p>"""
    per_instance_container_group_definition_name: NotRequired[
        "capo_gamelift.types.container_group_definition_name.ContainerGroupDefinitionName"
    ]
    """<p>The name of the fleet's per-instance container group definition. </p>"""
    per_instance_container_group_definition_arn: NotRequired[
        "capo_gamelift.types.container_group_definition_arn.ContainerGroupDefinitionArn"
    ]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to the fleet's per-instance container group. The ARN value also identifies the specific container group definition version in use.</p>"""
    instance_connection_port_range: NotRequired[
        "capo_gamelift.types.connection_port_range.ConnectionPortRange"
    ]
    instance_inbound_permissions: NotRequired[
        "capo_gamelift.types.ip_permissions_list.IpPermissionsList"
    ]
    """<p>The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet. </p>"""
    game_server_container_groups_per_instance: NotRequired[
        "capo_gamelift.types.game_server_container_groups_per_instance.GameServerContainerGroupsPerInstance"
    ]
    """<p>The number of times to replicate the game server container group on each fleet instance. </p>"""
    maximum_game_server_container_groups_per_instance: NotRequired[
        "capo_gamelift.types.maximum_game_server_container_groups_per_instance.MaximumGameServerContainerGroupsPerInstance"
    ]
    """<p>The calculated maximum number of game server container groups that can be deployed on each fleet instance. The calculation depends on the resource needs of the container group and the CPU and memory resources of the fleet's instance type.</p>"""
    instance_type: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>The Amazon EC2 instance type to use for all instances in the fleet. Instance type determines the computing resources and processing power that's available to host your game servers. This includes CPU, memory, storage, and networking capacity. You can't update this fleet property.</p>"""
    billing_type: NotRequired[
        "capo_gamelift.types.container_fleet_billing_type.ContainerFleetBillingType"
    ]
    """<p>Indicates whether the fleet uses On-Demand or Spot instances for this fleet. Learn more about when to use <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot"> On-Demand versus Spot Instances</a>. You can't update this fleet property.</p> <p>By default, this property is set to <code>ON_DEMAND</code>.</p>"""
    description: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A meaningful description of the container fleet.</p>"""
    creation_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>).</p>"""
    metric_groups: NotRequired["capo_gamelift.types.metric_group_list.MetricGroupList"]
    """<p>The name of an Amazon Web Services CloudWatch metric group to add this fleet to. Metric groups aggregate metrics for multiple fleets. </p>"""
    new_game_session_protection_policy: NotRequired[
        "capo_gamelift.types.protection_policy.ProtectionPolicy"
    ]
    """<p>Determines whether Amazon GameLift Servers can shut down game sessions on the fleet that are actively running and hosting players. Amazon GameLift Servers might prompt an instance shutdown when scaling down fleet capacity or when retiring unhealthy instances. You can also set game session protection for individual game sessions using <a href="gamelift/latest/apireference/API_UpdateGameSession.html">UpdateGameSession</a>.</p> <ul> <li> <p> <b>NoProtection</b> -- Game sessions can be shut down during active gameplay. </p> </li> <li> <p> <b>FullProtection</b> -- Game sessions in <code>ACTIVE</code> status can't be shut down.</p> </li> </ul>"""
    game_session_creation_limit_policy: NotRequired[
        "capo_gamelift.types.game_session_creation_limit_policy.GameSessionCreationLimitPolicy"
    ]
    """<p>A policy that limits the number of game sessions that each individual player can create on instances in this fleet. The limit applies for a specified span of time.</p>"""
    status: NotRequired[
        "capo_gamelift.types.container_fleet_status.ContainerFleetStatus"
    ]
    """<p>The current status of the container fleet.</p> <ul> <li> <p> <code>PENDING</code> -- A new container fleet has been requested.</p> </li> <li> <p> <code>CREATING</code> -- A new container fleet resource is being created. </p> </li> <li> <p> <code>CREATED</code> -- A new container fleet resource has been created. No fleet instances have been deployed.</p> </li> <li> <p> <code>ACTIVATING</code> -- New container fleet instances are being deployed.</p> </li> <li> <p> <code>ACTIVE</code> -- The container fleet has been deployed and is ready to host game sessions.</p> </li> <li> <p> <code>UPDATING</code> -- The container fleet is being updated. A deployment is in progress.</p> </li> <li> <p> <code>EXPIRED</code> -- The container fleet has been expired. The fleet is scaled down to zero instances and cannot host new game sessions.</p> </li> </ul>"""
    deployment_details: NotRequired[
        "capo_gamelift.types.deployment_details.DeploymentDetails"
    ]
    """<p>Information about the most recent deployment for the container fleet.</p>"""
    log_configuration: NotRequired[
        "capo_gamelift.types.log_configuration.LogConfiguration"
    ]
    """<p>The method that is used to collect container logs for the fleet. Amazon GameLift Servers saves all standard output for each container in logs, including game session logs. </p> <ul> <li> <p> <code>CLOUDWATCH</code> -- Send logs to an Amazon CloudWatch log group that you define. Each container emits a log stream, which is organized in the log group. </p> </li> <li> <p> <code>S3</code> -- Store logs in an Amazon S3 bucket that you define.</p> </li> <li> <p> <code>NONE</code> -- Don't collect container logs.</p> </li> </ul>"""
    location_attributes: NotRequired[
        "capo_gamelift.types.container_fleet_location_attributes_list.ContainerFleetLocationAttributesList"
    ]
    """<p>Information about the container fleet's remote locations where fleet instances are deployed.</p>"""
    player_gateway_mode: NotRequired[
        "capo_gamelift.types.player_gateway_mode.PlayerGatewayMode"
    ]
    """<p>Indicates whether player gateway is enabled for this container fleet. Player gateway provides benefits such as DDoS protection with negligible impact to latency.</p> <p>If <code>ENABLED</code> or <code>REQUIRED</code>, game clients can use player gateway to connect with the game server. If <code>DISABLED</code>, game clients cannot use player gateway. Instead, they have to directly connect to the game server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerFleet) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "fleet_arn" in value:
        out["FleetArn"] = value["fleet_arn"]
    if "fleet_role_arn" in value:
        out["FleetRoleArn"] = value["fleet_role_arn"]
    if "game_server_container_group_definition_name" in value:
        out["GameServerContainerGroupDefinitionName"] = value[
            "game_server_container_group_definition_name"
        ]
    if "game_server_container_group_definition_arn" in value:
        out["GameServerContainerGroupDefinitionArn"] = value[
            "game_server_container_group_definition_arn"
        ]
    if "per_instance_container_group_definition_name" in value:
        out["PerInstanceContainerGroupDefinitionName"] = value[
            "per_instance_container_group_definition_name"
        ]
    if "per_instance_container_group_definition_arn" in value:
        out["PerInstanceContainerGroupDefinitionArn"] = value[
            "per_instance_container_group_definition_arn"
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
    if "maximum_game_server_container_groups_per_instance" in value:
        out["MaximumGameServerContainerGroupsPerInstance"] = value[
            "maximum_game_server_container_groups_per_instance"
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
    if "description" in value:
        out["Description"] = value["description"]
    if "creation_time" in value:
        import capo_gamelift.types.timestamp

        out["CreationTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
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
    if "status" in value:
        import capo_gamelift.types.container_fleet_status

        out["Status"] = (
            capo_gamelift.types.container_fleet_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "deployment_details" in value:
        import capo_gamelift.types.deployment_details

        out["DeploymentDetails"] = (
            capo_gamelift.types.deployment_details.serialize_aws_json_1_1(
                value["deployment_details"]
            )
        )
    if "log_configuration" in value:
        import capo_gamelift.types.log_configuration

        out["LogConfiguration"] = (
            capo_gamelift.types.log_configuration.serialize_aws_json_1_1(
                value["log_configuration"]
            )
        )
    if "location_attributes" in value:
        import capo_gamelift.types.container_fleet_location_attributes_list

        out["LocationAttributes"] = (
            capo_gamelift.types.container_fleet_location_attributes_list.serialize_aws_json_1_1(
                value["location_attributes"]
            )
        )
    if "player_gateway_mode" in value:
        import capo_gamelift.types.player_gateway_mode

        out["PlayerGatewayMode"] = (
            capo_gamelift.types.player_gateway_mode.serialize_aws_json_1_1(
                value["player_gateway_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerFleet:
    out: ContainerFleet = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("FleetArn") is not None:
        out["fleet_arn"] = data["FleetArn"]
    if data.get("FleetRoleArn") is not None:
        out["fleet_role_arn"] = data["FleetRoleArn"]
    if data.get("GameServerContainerGroupDefinitionName") is not None:
        out["game_server_container_group_definition_name"] = data[
            "GameServerContainerGroupDefinitionName"
        ]
    if data.get("GameServerContainerGroupDefinitionArn") is not None:
        out["game_server_container_group_definition_arn"] = data[
            "GameServerContainerGroupDefinitionArn"
        ]
    if data.get("PerInstanceContainerGroupDefinitionName") is not None:
        out["per_instance_container_group_definition_name"] = data[
            "PerInstanceContainerGroupDefinitionName"
        ]
    if data.get("PerInstanceContainerGroupDefinitionArn") is not None:
        out["per_instance_container_group_definition_arn"] = data[
            "PerInstanceContainerGroupDefinitionArn"
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
    if data.get("MaximumGameServerContainerGroupsPerInstance") is not None:
        out["maximum_game_server_container_groups_per_instance"] = data[
            "MaximumGameServerContainerGroupsPerInstance"
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
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreationTime") is not None:
        import capo_gamelift.types.timestamp

        out["creation_time"] = capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
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
    if data.get("Status") is not None:
        import capo_gamelift.types.container_fleet_status

        out["status"] = (
            capo_gamelift.types.container_fleet_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("DeploymentDetails") is not None:
        import capo_gamelift.types.deployment_details

        out["deployment_details"] = (
            capo_gamelift.types.deployment_details.deserialize_aws_json_1_1(
                data["DeploymentDetails"]
            )
        )
    if data.get("LogConfiguration") is not None:
        import capo_gamelift.types.log_configuration

        out["log_configuration"] = (
            capo_gamelift.types.log_configuration.deserialize_aws_json_1_1(
                data["LogConfiguration"]
            )
        )
    if data.get("LocationAttributes") is not None:
        import capo_gamelift.types.container_fleet_location_attributes_list

        out["location_attributes"] = (
            capo_gamelift.types.container_fleet_location_attributes_list.deserialize_aws_json_1_1(
                data["LocationAttributes"]
            )
        )
    if data.get("PlayerGatewayMode") is not None:
        import capo_gamelift.types.player_gateway_mode

        out["player_gateway_mode"] = (
            capo_gamelift.types.player_gateway_mode.deserialize_aws_json_1_1(
                data["PlayerGatewayMode"]
            )
        )
    return out
