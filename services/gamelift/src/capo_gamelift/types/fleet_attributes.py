"""Generated from Smithy shape ``com.amazonaws.gamelift#FleetAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.anywhere_configuration
    import capo_gamelift.types.build_arn
    import capo_gamelift.types.build_id
    import capo_gamelift.types.certificate_configuration
    import capo_gamelift.types.compute_type
    import capo_gamelift.types.ec2_instance_type
    import capo_gamelift.types.fleet_action_list
    import capo_gamelift.types.fleet_arn
    import capo_gamelift.types.fleet_id
    import capo_gamelift.types.fleet_status
    import capo_gamelift.types.fleet_type
    import capo_gamelift.types.instance_role_credentials_provider
    import capo_gamelift.types.launch_parameters_string_model
    import capo_gamelift.types.launch_path_string_model
    import capo_gamelift.types.metric_group_list
    import capo_gamelift.types.non_empty_string
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.operating_system
    import capo_gamelift.types.player_gateway_configuration
    import capo_gamelift.types.player_gateway_mode
    import capo_gamelift.types.protection_policy
    import capo_gamelift.types.resource_creation_limit_policy
    import capo_gamelift.types.script_arn
    import capo_gamelift.types.script_id
    import capo_gamelift.types.string_list
    import capo_gamelift.types.timestamp


class FleetAttributes(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the fleet.</p>"""
    fleet_arn: NotRequired["capo_gamelift.types.fleet_arn.FleetArn"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>. In a GameLift fleet ARN, the resource ID matches the <code>FleetId</code> value.</p>"""
    fleet_type: NotRequired["capo_gamelift.types.fleet_type.FleetType"]
    """<p>Indicates whether the fleet uses On-Demand or Spot instances. For more information, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot"> On-Demand versus Spot Instances</a>. This fleet property can't be changed after the fleet is created.</p>"""
    instance_type: NotRequired["capo_gamelift.types.ec2_instance_type.EC2InstanceType"]
    """<p>The Amazon EC2 instance type that the fleet uses. Instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. See <a href="http://aws.amazon.com/ec2/instance-types/">Amazon Elastic Compute Cloud Instance Types</a> for detailed descriptions. This attribute is used with fleets where <code>ComputeType</code> is <code>EC2</code>.</p>"""
    description: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A human-readable description of the fleet.</p>"""
    name: NotRequired["capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"]
    """<p>A descriptive label that is associated with a fleet. Fleet names do not need to be unique.</p>"""
    creation_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>).</p>"""
    termination_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>A time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>).</p>"""
    status: NotRequired["capo_gamelift.types.fleet_status.FleetStatus"]
    """<p>Current status of the fleet. Possible fleet statuses include the following:</p> <ul> <li> <p>NEW -- A new fleet resource has been defined and Amazon GameLift Servers has started creating the fleet. Desired instances is set to 1. </p> </li> <li> <p>DOWNLOADING/VALIDATING/BUILDING -- Amazon GameLift Servers is downloading the game server build, running install scripts, and then validating the build files. When complete, Amazon GameLift Servers launches a fleet instance. </p> </li> <li> <p>ACTIVATING -- Amazon GameLift Servers is launching a game server process and testing its connectivity with the Amazon GameLift Servers service.</p> </li> <li> <p>ACTIVE -- The fleet is now ready to host game sessions.</p> </li> <li> <p>ERROR -- An error occurred when downloading, validating, building, or activating the fleet.</p> </li> <li> <p>EXPIRED -- The fleet has been expired. The fleet is scaled down to zero instances and cannot host new game sessions.</p> </li> <li> <p>DELETING -- Hosts are responding to a delete fleet request.</p> </li> <li> <p>TERMINATED -- The fleet no longer exists.</p> </li> </ul>"""
    build_id: NotRequired["capo_gamelift.types.build_id.BuildId"]
    """<p>A unique identifier for the build resource that is deployed on instances in this fleet. This attribute is used with fleets where <code>ComputeType</code> is "EC2".</p>"""
    build_arn: NotRequired["capo_gamelift.types.build_arn.BuildArn"]
    """<p> The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) associated with the Amazon GameLift Servers build resource that is deployed on instances in this fleet. In a GameLift build ARN, the resource ID matches the <code>BuildId</code> value. This attribute is used with fleets where <code>ComputeType</code> is "EC2".</p>"""
    script_id: NotRequired["capo_gamelift.types.script_id.ScriptId"]
    """<p>A unique identifier for the Realtime script resource that is deployed on instances in this fleet. This attribute is used with fleets where <code>ComputeType</code> is "EC2".</p>"""
    script_arn: NotRequired["capo_gamelift.types.script_arn.ScriptArn"]
    """<p> The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) associated with the GameLift script resource that is deployed on instances in this fleet. In a GameLift script ARN, the resource ID matches the <code>ScriptId</code> value.</p>"""
    server_launch_path: NotRequired[
        "capo_gamelift.types.launch_path_string_model.LaunchPathStringModel"
    ]
    """<p> <b>This parameter is no longer used.</b> Server launch paths are now defined using the fleet's <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/RuntimeConfiguration.html">RuntimeConfiguration</a>. Requests that use this parameter continue to be valid.</p>"""
    server_launch_parameters: NotRequired[
        "capo_gamelift.types.launch_parameters_string_model.LaunchParametersStringModel"
    ]
    """<p> <b>This parameter is no longer used.</b> Server launch parameters are now defined using the fleet's runtime configuration. Requests that use this parameter continue to be valid.</p>"""
    log_paths: NotRequired["capo_gamelift.types.string_list.StringList"]
    """<p> <b>This parameter is no longer used.</b> Game session log paths are now defined using the Amazon GameLift Servers server API <code>ProcessReady()</code> <code>logParameters</code>. See more information in the <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api-ref.html#gamelift-sdk-server-api-ref-dataypes-process">Server API Reference</a>. </p>"""
    new_game_session_protection_policy: NotRequired[
        "capo_gamelift.types.protection_policy.ProtectionPolicy"
    ]
    """<p>The type of game session protection to set on all new instances that are started in the fleet. This attribute is used with fleets where <code>ComputeType</code> is <code>EC2</code>.</p> <ul> <li> <p> <b>NoProtection</b> -- The game session can be terminated during a scale-down event.</p> </li> <li> <p> <b>FullProtection</b> -- If the game session is in an <code>ACTIVE</code> status, it cannot be terminated during a scale-down event.</p> </li> </ul>"""
    operating_system: NotRequired[
        "capo_gamelift.types.operating_system.OperatingSystem"
    ]
    """<p>The operating system of the fleet's computing resources. A fleet's operating system is determined by the OS of the build or script that is deployed on this fleet. This attribute is used with fleets where <code>ComputeType</code> is <code>EC2</code>.</p> <note> <p>Amazon Linux 2 (AL2) will reach end of support on 6/30/2026. See more details in the <a href="http://aws.amazon.com/aws.amazon.com/amazon-linux-2/faqs/">Amazon Linux 2 FAQs</a>. For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html"> Migrate to server SDK version 5.</a> </p> </note>"""
    resource_creation_limit_policy: NotRequired[
        "capo_gamelift.types.resource_creation_limit_policy.ResourceCreationLimitPolicy"
    ]
    metric_groups: NotRequired["capo_gamelift.types.metric_group_list.MetricGroupList"]
    """<p>Name of a metric group that metrics for this fleet are added to. In Amazon CloudWatch, you can view aggregated metrics for fleets that are in a metric group. A fleet can be included in only one metric group at a time. This attribute is used with fleets where <code>ComputeType</code> is <code>EC2</code>.</p>"""
    stopped_actions: NotRequired[
        "capo_gamelift.types.fleet_action_list.FleetActionList"
    ]
    """<p>A list of fleet activity that has been suspended using <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_StopFleetActions.html">StopFleetActions</a>. This includes fleet auto-scaling. This attribute is used with fleets where <code>ComputeType</code> is <code>EC2</code>.</p>"""
    instance_role_arn: NotRequired[
        "capo_gamelift.types.non_empty_string.NonEmptyString"
    ]
    """<p>A unique identifier for an IAM role that manages access to your Amazon Web Services services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role's ARN by using the <a href="https://console.aws.amazon.com/iam/">IAM dashboard</a> in the Amazon Web Services Management Console. Learn more about using on-box credentials for your game servers at <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html"> Access external resources from a game server</a>. This attribute is used with fleets where <code>ComputeType</code> is <code>EC2</code>.</p>"""
    certificate_configuration: NotRequired[
        "capo_gamelift.types.certificate_configuration.CertificateConfiguration"
    ]
    """<p>Determines whether a TLS/SSL certificate is generated for a fleet. This feature must be enabled when creating the fleet. All instances in a fleet share the same certificate.</p>"""
    compute_type: NotRequired["capo_gamelift.types.compute_type.ComputeType"]
    """<p>The type of compute resource used to host your game servers. You can use your own compute resources with Amazon GameLift Servers Anywhere or use Amazon EC2 instances with managed Amazon GameLift Servers.</p>"""
    anywhere_configuration: NotRequired[
        "capo_gamelift.types.anywhere_configuration.AnywhereConfiguration"
    ]
    """<p>A set of attributes that are specific to an Anywhere fleet.</p>"""
    instance_role_credentials_provider: NotRequired[
        "capo_gamelift.types.instance_role_credentials_provider.InstanceRoleCredentialsProvider"
    ]
    """<p>Indicates that fleet instances maintain a shared credentials file for the IAM role defined in <code>InstanceRoleArn</code>. Shared credentials allow applications that are deployed with the game server executable to communicate with other Amazon Web Services resources. This property is used only when the game server is integrated with the server SDK version 5.x. For more information about using shared credentials, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html"> Communicate with other Amazon Web Services resources from your fleets</a>. This attribute is used with fleets where <code>ComputeType</code> is <code>EC2</code>.</p>"""
    player_gateway_mode: NotRequired[
        "capo_gamelift.types.player_gateway_mode.PlayerGatewayMode"
    ]
    """<p>Indicates whether player gateway is enabled for this fleet. Player gateway provides benefits such as DDoS protection with negligible impact to latency.</p> <p>If <code>ENABLED</code> or <code>REQUIRED</code>, game clients can use player gateway to connect with the game server. If <code>DISABLED</code>, game clients cannot use player gateway. Instead, they have to directly connect to the game server.</p>"""
    player_gateway_configuration: NotRequired[
        "capo_gamelift.types.player_gateway_configuration.PlayerGatewayConfiguration"
    ]
    """<p>Configuration settings for player gateway on this fleet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetAttributes) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "fleet_arn" in value:
        out["FleetArn"] = value["fleet_arn"]
    if "fleet_type" in value:
        import capo_gamelift.types.fleet_type

        out["FleetType"] = capo_gamelift.types.fleet_type.serialize_aws_json_1_1(
            value["fleet_type"]
        )
    if "instance_type" in value:
        import capo_gamelift.types.ec2_instance_type

        out["InstanceType"] = (
            capo_gamelift.types.ec2_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "name" in value:
        out["Name"] = value["name"]
    if "creation_time" in value:
        import capo_gamelift.types.timestamp

        out["CreationTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "termination_time" in value:
        import capo_gamelift.types.timestamp

        out["TerminationTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["termination_time"]
        )
    if "status" in value:
        import capo_gamelift.types.fleet_status

        out["Status"] = capo_gamelift.types.fleet_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "build_id" in value:
        out["BuildId"] = value["build_id"]
    if "build_arn" in value:
        out["BuildArn"] = value["build_arn"]
    if "script_id" in value:
        out["ScriptId"] = value["script_id"]
    if "script_arn" in value:
        out["ScriptArn"] = value["script_arn"]
    if "server_launch_path" in value:
        out["ServerLaunchPath"] = value["server_launch_path"]
    if "server_launch_parameters" in value:
        out["ServerLaunchParameters"] = value["server_launch_parameters"]
    if "log_paths" in value:
        import capo_gamelift.types.string_list

        out["LogPaths"] = capo_gamelift.types.string_list.serialize_aws_json_1_1(
            value["log_paths"]
        )
    if "new_game_session_protection_policy" in value:
        import capo_gamelift.types.protection_policy

        out["NewGameSessionProtectionPolicy"] = (
            capo_gamelift.types.protection_policy.serialize_aws_json_1_1(
                value["new_game_session_protection_policy"]
            )
        )
    if "operating_system" in value:
        import capo_gamelift.types.operating_system

        out["OperatingSystem"] = (
            capo_gamelift.types.operating_system.serialize_aws_json_1_1(
                value["operating_system"]
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
    if "stopped_actions" in value:
        import capo_gamelift.types.fleet_action_list

        out["StoppedActions"] = (
            capo_gamelift.types.fleet_action_list.serialize_aws_json_1_1(
                value["stopped_actions"]
            )
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


def deserialize_aws_json_1_1(data: dict) -> FleetAttributes:
    out: FleetAttributes = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("FleetArn") is not None:
        out["fleet_arn"] = data["FleetArn"]
    if data.get("FleetType") is not None:
        import capo_gamelift.types.fleet_type

        out["fleet_type"] = capo_gamelift.types.fleet_type.deserialize_aws_json_1_1(
            data["FleetType"]
        )
    if data.get("InstanceType") is not None:
        import capo_gamelift.types.ec2_instance_type

        out["instance_type"] = (
            capo_gamelift.types.ec2_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("CreationTime") is not None:
        import capo_gamelift.types.timestamp

        out["creation_time"] = capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("TerminationTime") is not None:
        import capo_gamelift.types.timestamp

        out["termination_time"] = (
            capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
                data["TerminationTime"]
            )
        )
    if data.get("Status") is not None:
        import capo_gamelift.types.fleet_status

        out["status"] = capo_gamelift.types.fleet_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("BuildId") is not None:
        out["build_id"] = data["BuildId"]
    if data.get("BuildArn") is not None:
        out["build_arn"] = data["BuildArn"]
    if data.get("ScriptId") is not None:
        out["script_id"] = data["ScriptId"]
    if data.get("ScriptArn") is not None:
        out["script_arn"] = data["ScriptArn"]
    if data.get("ServerLaunchPath") is not None:
        out["server_launch_path"] = data["ServerLaunchPath"]
    if data.get("ServerLaunchParameters") is not None:
        out["server_launch_parameters"] = data["ServerLaunchParameters"]
    if data.get("LogPaths") is not None:
        import capo_gamelift.types.string_list

        out["log_paths"] = capo_gamelift.types.string_list.deserialize_aws_json_1_1(
            data["LogPaths"]
        )
    if data.get("NewGameSessionProtectionPolicy") is not None:
        import capo_gamelift.types.protection_policy

        out["new_game_session_protection_policy"] = (
            capo_gamelift.types.protection_policy.deserialize_aws_json_1_1(
                data["NewGameSessionProtectionPolicy"]
            )
        )
    if data.get("OperatingSystem") is not None:
        import capo_gamelift.types.operating_system

        out["operating_system"] = (
            capo_gamelift.types.operating_system.deserialize_aws_json_1_1(
                data["OperatingSystem"]
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
    if data.get("StoppedActions") is not None:
        import capo_gamelift.types.fleet_action_list

        out["stopped_actions"] = (
            capo_gamelift.types.fleet_action_list.deserialize_aws_json_1_1(
                data["StoppedActions"]
            )
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
