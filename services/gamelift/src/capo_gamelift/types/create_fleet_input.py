"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateFleetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.anywhere_configuration
    import capo_gamelift.types.build_id_or_arn
    import capo_gamelift.types.certificate_configuration
    import capo_gamelift.types.compute_type
    import capo_gamelift.types.ec2_instance_type
    import capo_gamelift.types.fleet_type
    import capo_gamelift.types.instance_role_credentials_provider
    import capo_gamelift.types.ip_permissions_list
    import capo_gamelift.types.launch_parameters_string_model
    import capo_gamelift.types.launch_path_string_model
    import capo_gamelift.types.location_configuration_list
    import capo_gamelift.types.metric_group_list
    import capo_gamelift.types.non_empty_string
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.player_gateway_configuration
    import capo_gamelift.types.player_gateway_mode
    import capo_gamelift.types.protection_policy
    import capo_gamelift.types.resource_creation_limit_policy
    import capo_gamelift.types.runtime_configuration
    import capo_gamelift.types.script_id_or_arn
    import capo_gamelift.types.string_list
    import capo_gamelift.types.tag_list


class CreateFleetInput(TypedDict, closed=True):
    name: NotRequired["capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"]
    """<p>A descriptive label that is associated with a fleet. Fleet names do not need to be unique.</p>"""
    description: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A description for the fleet.</p>"""
    build_id: NotRequired["capo_gamelift.types.build_id_or_arn.BuildIdOrArn"]
    """<p>The unique identifier for a custom game server build to be deployed to a fleet with compute type <code>EC2</code>. You can use either the build ID or ARN. The build must be uploaded to Amazon GameLift Servers and in <code>READY</code> status. This fleet property can't be changed after the fleet is created.</p>"""
    script_id: NotRequired["capo_gamelift.types.script_id_or_arn.ScriptIdOrArn"]
    """<p>The unique identifier for a Realtime configuration script to be deployed to a fleet with compute type <code>EC2</code>. You can use either the script ID or ARN. Scripts must be uploaded to Amazon GameLift Servers prior to creating the fleet. This fleet property can't be changed after the fleet is created.</p>"""
    server_launch_path: NotRequired[
        "capo_gamelift.types.launch_path_string_model.LaunchPathStringModel"
    ]
    """<p> <b>This parameter is no longer used.</b> Specify a server launch path using the <code>RuntimeConfiguration</code> parameter. Requests that use this parameter instead continue to be valid.</p>"""
    server_launch_parameters: NotRequired[
        "capo_gamelift.types.launch_parameters_string_model.LaunchParametersStringModel"
    ]
    """<p> <b>This parameter is no longer used.</b> Specify server launch parameters using the <code>RuntimeConfiguration</code> parameter. Requests that use this parameter instead continue to be valid.</p>"""
    log_paths: NotRequired["capo_gamelift.types.string_list.StringList"]
    """<p> <b>This parameter is no longer used.</b> To specify where Amazon GameLift Servers should store log files once a server process shuts down, use the Amazon GameLift Servers server API <code>ProcessReady()</code> and specify one or more directory paths in <code>logParameters</code>. For more information, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-initialize">Initialize the server process</a> in the <i>Amazon GameLift Servers Developer Guide</i>. </p>"""
    ec2_instance_type: NotRequired[
        "capo_gamelift.types.ec2_instance_type.EC2InstanceType"
    ]
    """<p>The Amazon GameLift Servers-supported Amazon EC2 instance type to use with managed EC2 fleets. Instance type determines the computing resources that will be used to host your game servers, including CPU, memory, storage, and networking capacity. See <a href="http://aws.amazon.com/ec2/instance-types/">Amazon Elastic Compute Cloud Instance Types</a> for detailed descriptions of Amazon EC2 instance types.</p>"""
    ec2_inbound_permissions: NotRequired[
        "capo_gamelift.types.ip_permissions_list.IpPermissionsList"
    ]
    """<p>The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet. Set this parameter for managed EC2 fleets. You can leave this parameter empty when creating the fleet, but you must call <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetPortSettings">https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetPortSettings</a> to set it before players can connect to game sessions. As a best practice, we recommend opening ports for remote access only when you need them and closing them when you're finished. For Amazon GameLift Servers Realtime fleets, Amazon GameLift Servers automatically sets TCP and UDP ranges.</p>"""
    new_game_session_protection_policy: NotRequired[
        "capo_gamelift.types.protection_policy.ProtectionPolicy"
    ]
    """<p>The status of termination protection for active game sessions on the fleet. By default, this property is set to <code>NoProtection</code>. You can also set game session protection for an individual game session by calling <a href="gamelift/latest/apireference/API_UpdateGameSession.html">UpdateGameSession</a>.</p> <ul> <li> <p> <b>NoProtection</b> - Game sessions can be terminated during active gameplay as a result of a scale-down event. </p> </li> <li> <p> <b>FullProtection</b> - Game sessions in <code>ACTIVE</code> status cannot be terminated during a scale-down event.</p> </li> </ul>"""
    runtime_configuration: NotRequired[
        "capo_gamelift.types.runtime_configuration.RuntimeConfiguration"
    ]
    """<p>Instructions for how to launch and run server processes on the fleet. Set runtime configuration for managed EC2 fleets. For an Anywhere fleet, set this parameter only if the fleet is running the Amazon GameLift Servers Agent. The runtime configuration defines one or more server process configurations. Each server process identifies a game executable or Realtime script file and the number of processes to run concurrently. </p> <note> <p>This parameter replaces the parameters <code>ServerLaunchPath</code> and <code>ServerLaunchParameters</code>, which are still supported for backward compatibility.</p> </note>"""
    resource_creation_limit_policy: NotRequired[
        "capo_gamelift.types.resource_creation_limit_policy.ResourceCreationLimitPolicy"
    ]
    """<p>A policy that limits the number of game sessions that an individual player can create on instances in this fleet within a specified span of time.</p>"""
    metric_groups: NotRequired["capo_gamelift.types.metric_group_list.MetricGroupList"]
    """<p>The name of an Amazon Web Services CloudWatch metric group to add this fleet to. A metric group is used to aggregate the metrics for multiple fleets. You can specify an existing metric group name or set a new name to create a new metric group. A fleet can be included in only one metric group at a time. </p>"""
    peer_vpc_aws_account_id: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>Used when peering your Amazon GameLift Servers fleet with a VPC, the unique identifier for the Amazon Web Services account that owns the VPC. You can find your account ID in the Amazon Web Services Management Console under account settings. </p>"""
    peer_vpc_id: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A unique identifier for a VPC with resources to be accessed by your Amazon GameLift Servers fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the <a href="https://console.aws.amazon.com/vpc/">VPC Dashboard</a> in the Amazon Web Services Management Console. Learn more about VPC peering in <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html">VPC Peering with Amazon GameLift Servers Fleets</a>.</p>"""
    fleet_type: NotRequired["capo_gamelift.types.fleet_type.FleetType"]
    """<p>Indicates whether to use On-Demand or Spot instances for this fleet. By default, this property is set to <code>ON_DEMAND</code>. Learn more about when to use <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot"> On-Demand versus Spot Instances</a>. This fleet property can't be changed after the fleet is created.</p>"""
    instance_role_arn: NotRequired[
        "capo_gamelift.types.non_empty_string.NonEmptyString"
    ]
    """<p>A unique identifier for an IAM role that manages access to your Amazon Web Services services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role's ARN by using the <a href="https://console.aws.amazon.com/iam/">IAM dashboard</a> in the Amazon Web Services Management Console. Learn more about using on-box credentials for your game servers at <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html"> Access external resources from a game server</a>. This fleet property can't be changed after the fleet is created.</p>"""
    certificate_configuration: NotRequired[
        "capo_gamelift.types.certificate_configuration.CertificateConfiguration"
    ]
    """<p>Prompts Amazon GameLift Servers to generate a TLS/SSL certificate for the fleet. Amazon GameLift Servers uses the certificates to encrypt traffic between game clients and the game servers running on Amazon GameLift Servers. By default, the <code>CertificateConfiguration</code> is <code>DISABLED</code>. You can't change this property after you create the fleet. </p> <p>Certificate Manager (ACM) certificates expire after 13 months. Certificate expiration can cause fleets to fail, preventing players from connecting to instances in the fleet. We recommend you replace fleets before 13 months, consider using fleet aliases for a smooth transition.</p> <note> <p>ACM isn't available in all Amazon Web Services regions. A fleet creation request with certificate generation enabled in an unsupported Region, fails with a 4xx error. For more information about the supported Regions, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-regions.html">Supported Regions</a> in the <i>Certificate Manager User Guide</i>.</p> </note>"""
    locations: NotRequired[
        "capo_gamelift.types.location_configuration_list.LocationConfigurationList"
    ]
    """<p>A set of remote locations to deploy additional instances to and manage as a multi-location fleet. Use this parameter when creating a fleet in Amazon Web Services Regions that support multiple locations. You can add any Amazon Web Services Region or Local Zone that's supported by Amazon GameLift Servers. Provide a list of one or more Amazon Web Services Region codes, such as <code>us-west-2</code>, or Local Zone names. When using this parameter, Amazon GameLift Servers requires you to include your home location in the request. For a list of supported Regions and Local Zones, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html"> Amazon GameLift Servers service locations</a> for managed hosting.</p>"""
    tags: NotRequired["capo_gamelift.types.tag_list.TagList"]
    """<p>A list of labels to assign to the new fleet resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    compute_type: NotRequired["capo_gamelift.types.compute_type.ComputeType"]
    """<p>The type of compute resource used to host your game servers. </p> <ul> <li> <p> <code>EC2</code> – The game server build is deployed to Amazon EC2 instances for cloud hosting. This is the default setting.</p> </li> <li> <p> <code>ANYWHERE</code> – Game servers and supporting software are deployed to compute resources that you provide and manage. With this compute type, you can also set the <code>AnywhereConfiguration</code> parameter.</p> </li> </ul>"""
    anywhere_configuration: NotRequired[
        "capo_gamelift.types.anywhere_configuration.AnywhereConfiguration"
    ]
    """<p>Amazon GameLift Servers Anywhere configuration options.</p>"""
    instance_role_credentials_provider: NotRequired[
        "capo_gamelift.types.instance_role_credentials_provider.InstanceRoleCredentialsProvider"
    ]
    """<p>Prompts Amazon GameLift Servers to generate a shared credentials file for the IAM role that's defined in <code>InstanceRoleArn</code>. The shared credentials file is stored on each fleet instance and refreshed as needed. Use shared credentials for applications that are deployed along with the game server executable, if the game server is integrated with server SDK version 5.x. For more information about using shared credentials, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html"> Communicate with other Amazon Web Services resources from your fleets</a>.</p>"""
    player_gateway_mode: NotRequired[
        "capo_gamelift.types.player_gateway_mode.PlayerGatewayMode"
    ]
    """<p>Configures player gateway for your fleet. Player gateway provides benefits such as DDoS protection by rate limiting and validating traffic before it reaches game servers, hiding game server IP addresses from players, and providing updated endpoints when relay endpoints become unhealthy. Note, player gateway is only available for fleets using server SDK 5.x or later game server builds.</p> <p> <b>How it works:</b> When enabled, game clients connect to relay endpoints instead of to your game servers. Player gateway validates player gateway tokens and routes traffic to the appropriate game server. Your game backend calls <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetPlayerConnectionDetails.html">GetPlayerConnectionDetails</a> to retrieve relay endpoints and player gateway tokens for your game clients. To learn more about this topic, see <a href="https://docs.aws.amazon.com/gameliftservers/latest/developerguide/ddos-protection-intro.html">DDoS protection with Amazon GameLift Servers player gateway</a>.</p> <p>Possible values include:</p> <ul> <li> <p> <code>DISABLED</code> (default) -- Game clients connect to the game server endpoint. Use this when you do not intend to integrate your game with player gateway.</p> </li> <li> <p> <code>ENABLED</code> -- Player gateway is available in fleet locations where it is supported. Your game backend can call <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetPlayerConnectionDetails.html">GetPlayerConnectionDetails</a> to obtain a player gateway token and endpoints for game clients.</p> </li> <li> <p> <code>REQUIRED</code> -- Player gateway is available in fleet locations where it is supported, and the fleet can only use locations that support this feature. Attempting to add a remote location to your fleet which does not support player gateway will result in an <code>InvalidRequestException</code>.</p> </li> </ul>"""
    player_gateway_configuration: NotRequired[
        "capo_gamelift.types.player_gateway_configuration.PlayerGatewayConfiguration"
    ]
    """<p>Configuration settings for player gateway. Use this to specify advanced options for how player gateway handles connections.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFleetInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "build_id" in value:
        out["BuildId"] = value["build_id"]
    if "script_id" in value:
        out["ScriptId"] = value["script_id"]
    if "server_launch_path" in value:
        out["ServerLaunchPath"] = value["server_launch_path"]
    if "server_launch_parameters" in value:
        out["ServerLaunchParameters"] = value["server_launch_parameters"]
    if "log_paths" in value:
        import capo_gamelift.types.string_list

        out["LogPaths"] = capo_gamelift.types.string_list.serialize_aws_json_1_1(
            value["log_paths"]
        )
    if "ec2_instance_type" in value:
        import capo_gamelift.types.ec2_instance_type

        out["EC2InstanceType"] = (
            capo_gamelift.types.ec2_instance_type.serialize_aws_json_1_1(
                value["ec2_instance_type"]
            )
        )
    if "ec2_inbound_permissions" in value:
        import capo_gamelift.types.ip_permissions_list

        out["EC2InboundPermissions"] = (
            capo_gamelift.types.ip_permissions_list.serialize_aws_json_1_1(
                value["ec2_inbound_permissions"]
            )
        )
    if "new_game_session_protection_policy" in value:
        import capo_gamelift.types.protection_policy

        out["NewGameSessionProtectionPolicy"] = (
            capo_gamelift.types.protection_policy.serialize_aws_json_1_1(
                value["new_game_session_protection_policy"]
            )
        )
    if "runtime_configuration" in value:
        import capo_gamelift.types.runtime_configuration

        out["RuntimeConfiguration"] = (
            capo_gamelift.types.runtime_configuration.serialize_aws_json_1_1(
                value["runtime_configuration"]
            )
        )
    if "resource_creation_limit_policy" in value:
        import capo_gamelift.types.resource_creation_limit_policy

        out["ResourceCreationLimitPolicy"] = (
            capo_gamelift.types.resource_creation_limit_policy.serialize_aws_json_1_1(
                value["resource_creation_limit_policy"]
            )
        )
    if "metric_groups" in value:
        import capo_gamelift.types.metric_group_list

        out["MetricGroups"] = (
            capo_gamelift.types.metric_group_list.serialize_aws_json_1_1(
                value["metric_groups"]
            )
        )
    if "peer_vpc_aws_account_id" in value:
        out["PeerVpcAwsAccountId"] = value["peer_vpc_aws_account_id"]
    if "peer_vpc_id" in value:
        out["PeerVpcId"] = value["peer_vpc_id"]
    if "fleet_type" in value:
        import capo_gamelift.types.fleet_type

        out["FleetType"] = capo_gamelift.types.fleet_type.serialize_aws_json_1_1(
            value["fleet_type"]
        )
    if "instance_role_arn" in value:
        out["InstanceRoleArn"] = value["instance_role_arn"]
    if "certificate_configuration" in value:
        import capo_gamelift.types.certificate_configuration

        out["CertificateConfiguration"] = (
            capo_gamelift.types.certificate_configuration.serialize_aws_json_1_1(
                value["certificate_configuration"]
            )
        )
    if "locations" in value:
        import capo_gamelift.types.location_configuration_list

        out["Locations"] = (
            capo_gamelift.types.location_configuration_list.serialize_aws_json_1_1(
                value["locations"]
            )
        )
    if "tags" in value:
        import capo_gamelift.types.tag_list

        out["Tags"] = capo_gamelift.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "compute_type" in value:
        import capo_gamelift.types.compute_type

        out["ComputeType"] = capo_gamelift.types.compute_type.serialize_aws_json_1_1(
            value["compute_type"]
        )
    if "anywhere_configuration" in value:
        import capo_gamelift.types.anywhere_configuration

        out["AnywhereConfiguration"] = (
            capo_gamelift.types.anywhere_configuration.serialize_aws_json_1_1(
                value["anywhere_configuration"]
            )
        )
    if "instance_role_credentials_provider" in value:
        import capo_gamelift.types.instance_role_credentials_provider

        out["InstanceRoleCredentialsProvider"] = (
            capo_gamelift.types.instance_role_credentials_provider.serialize_aws_json_1_1(
                value["instance_role_credentials_provider"]
            )
        )
    if "player_gateway_mode" in value:
        import capo_gamelift.types.player_gateway_mode

        out["PlayerGatewayMode"] = (
            capo_gamelift.types.player_gateway_mode.serialize_aws_json_1_1(
                value["player_gateway_mode"]
            )
        )
    if "player_gateway_configuration" in value:
        import capo_gamelift.types.player_gateway_configuration

        out["PlayerGatewayConfiguration"] = (
            capo_gamelift.types.player_gateway_configuration.serialize_aws_json_1_1(
                value["player_gateway_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFleetInput:
    out: CreateFleetInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("BuildId") is not None:
        out["build_id"] = data["BuildId"]
    if data.get("ScriptId") is not None:
        out["script_id"] = data["ScriptId"]
    if data.get("ServerLaunchPath") is not None:
        out["server_launch_path"] = data["ServerLaunchPath"]
    if data.get("ServerLaunchParameters") is not None:
        out["server_launch_parameters"] = data["ServerLaunchParameters"]
    if data.get("LogPaths") is not None:
        import capo_gamelift.types.string_list

        out["log_paths"] = capo_gamelift.types.string_list.deserialize_aws_json_1_1(
            data["LogPaths"]
        )
    if data.get("EC2InstanceType") is not None:
        import capo_gamelift.types.ec2_instance_type

        out["ec2_instance_type"] = (
            capo_gamelift.types.ec2_instance_type.deserialize_aws_json_1_1(
                data["EC2InstanceType"]
            )
        )
    if data.get("EC2InboundPermissions") is not None:
        import capo_gamelift.types.ip_permissions_list

        out["ec2_inbound_permissions"] = (
            capo_gamelift.types.ip_permissions_list.deserialize_aws_json_1_1(
                data["EC2InboundPermissions"]
            )
        )
    if data.get("NewGameSessionProtectionPolicy") is not None:
        import capo_gamelift.types.protection_policy

        out["new_game_session_protection_policy"] = (
            capo_gamelift.types.protection_policy.deserialize_aws_json_1_1(
                data["NewGameSessionProtectionPolicy"]
            )
        )
    if data.get("RuntimeConfiguration") is not None:
        import capo_gamelift.types.runtime_configuration

        out["runtime_configuration"] = (
            capo_gamelift.types.runtime_configuration.deserialize_aws_json_1_1(
                data["RuntimeConfiguration"]
            )
        )
    if data.get("ResourceCreationLimitPolicy") is not None:
        import capo_gamelift.types.resource_creation_limit_policy

        out["resource_creation_limit_policy"] = (
            capo_gamelift.types.resource_creation_limit_policy.deserialize_aws_json_1_1(
                data["ResourceCreationLimitPolicy"]
            )
        )
    if data.get("MetricGroups") is not None:
        import capo_gamelift.types.metric_group_list

        out["metric_groups"] = (
            capo_gamelift.types.metric_group_list.deserialize_aws_json_1_1(
                data["MetricGroups"]
            )
        )
    if data.get("PeerVpcAwsAccountId") is not None:
        out["peer_vpc_aws_account_id"] = data["PeerVpcAwsAccountId"]
    if data.get("PeerVpcId") is not None:
        out["peer_vpc_id"] = data["PeerVpcId"]
    if data.get("FleetType") is not None:
        import capo_gamelift.types.fleet_type

        out["fleet_type"] = capo_gamelift.types.fleet_type.deserialize_aws_json_1_1(
            data["FleetType"]
        )
    if data.get("InstanceRoleArn") is not None:
        out["instance_role_arn"] = data["InstanceRoleArn"]
    if data.get("CertificateConfiguration") is not None:
        import capo_gamelift.types.certificate_configuration

        out["certificate_configuration"] = (
            capo_gamelift.types.certificate_configuration.deserialize_aws_json_1_1(
                data["CertificateConfiguration"]
            )
        )
    if data.get("Locations") is not None:
        import capo_gamelift.types.location_configuration_list

        out["locations"] = (
            capo_gamelift.types.location_configuration_list.deserialize_aws_json_1_1(
                data["Locations"]
            )
        )
    if data.get("Tags") is not None:
        import capo_gamelift.types.tag_list

        out["tags"] = capo_gamelift.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("ComputeType") is not None:
        import capo_gamelift.types.compute_type

        out["compute_type"] = capo_gamelift.types.compute_type.deserialize_aws_json_1_1(
            data["ComputeType"]
        )
    if data.get("AnywhereConfiguration") is not None:
        import capo_gamelift.types.anywhere_configuration

        out["anywhere_configuration"] = (
            capo_gamelift.types.anywhere_configuration.deserialize_aws_json_1_1(
                data["AnywhereConfiguration"]
            )
        )
    if data.get("InstanceRoleCredentialsProvider") is not None:
        import capo_gamelift.types.instance_role_credentials_provider

        out["instance_role_credentials_provider"] = (
            capo_gamelift.types.instance_role_credentials_provider.deserialize_aws_json_1_1(
                data["InstanceRoleCredentialsProvider"]
            )
        )
    if data.get("PlayerGatewayMode") is not None:
        import capo_gamelift.types.player_gateway_mode

        out["player_gateway_mode"] = (
            capo_gamelift.types.player_gateway_mode.deserialize_aws_json_1_1(
                data["PlayerGatewayMode"]
            )
        )
    if data.get("PlayerGatewayConfiguration") is not None:
        import capo_gamelift.types.player_gateway_configuration

        out["player_gateway_configuration"] = (
            capo_gamelift.types.player_gateway_configuration.deserialize_aws_json_1_1(
                data["PlayerGatewayConfiguration"]
            )
        )
    return out
