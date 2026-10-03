"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#StartStreamSessionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_gameliftstreams.errors import DeserializationError

if TYPE_CHECKING:
    import capo_gameliftstreams.types.client_token
    import capo_gameliftstreams.types.connection_timeout_seconds
    import capo_gameliftstreams.types.description
    import capo_gameliftstreams.types.display_configuration
    import capo_gameliftstreams.types.environment_variables
    import capo_gameliftstreams.types.game_launch_arg_list
    import capo_gameliftstreams.types.iam_role_arn
    import capo_gameliftstreams.types.identifier
    import capo_gameliftstreams.types.location_list
    import capo_gameliftstreams.types.performance_stats_configuration
    import capo_gameliftstreams.types.protocol
    import capo_gameliftstreams.types.session_length_seconds
    import capo_gameliftstreams.types.signal_request
    import capo_gameliftstreams.types.user_id


class StartStreamSessionInput(TypedDict, closed=True):
    client_token: NotRequired["capo_gameliftstreams.types.client_token.ClientToken"]
    """<p> A unique identifier that represents a client request. The request is idempotent, which ensures that an API request completes only once. When users send a request, Amazon GameLift Streams automatically populates this field. </p>"""
    description: NotRequired["capo_gameliftstreams.types.description.Description"]
    """<p>A human-readable label for the stream session. You can update this value later.</p>"""
    identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p>The stream group to run this stream session with.</p> <p>This value is an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>"""
    protocol: "capo_gameliftstreams.types.protocol.Protocol"
    """<p>The data transport protocol to use for the stream session.</p>"""
    signal_request: "capo_gameliftstreams.types.signal_request.SignalRequest"
    """<p>A WebRTC ICE offer string to use when initializing a WebRTC connection. Typically, the offer is a very long JSON string. Provide the string as a text value in quotes.</p> <p>Amazon GameLift Streams also supports setting the field to "NO_CLIENT_CONNECTION". This will create a session without needing any browser request or Web SDK integration. The session starts up as usual and waits for a reconnection from a browser, which is accomplished using <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamSessionConnection.html">CreateStreamSessionConnection</a>.</p>"""
    application_identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p>An <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>"""
    user_id: NotRequired["capo_gameliftstreams.types.user_id.UserId"]
    """<p> An opaque, unique identifier for an end-user, defined by the developer. </p>"""
    locations: NotRequired["capo_gameliftstreams.types.location_list.LocationList"]
    """<p> A list of locations, in order of priority, where you want Amazon GameLift Streams to start a stream from. For example, <code>us-east-1</code>. Amazon GameLift Streams selects the location with the next available capacity to start a single stream session in. If this value is empty, Amazon GameLift Streams attempts to start a stream session in the primary location. </p> <p> For a complete list of locations that Amazon GameLift Streams supports, refer to <a href="https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html">Regions, quotas, and limitations</a> in the <i>Amazon GameLift Streams Developer Guide</i>. </p>"""
    connection_timeout_seconds: NotRequired[
        "capo_gameliftstreams.types.connection_timeout_seconds.ConnectionTimeoutSeconds"
    ]
    """<p>Length of time (in seconds) that Amazon GameLift Streams should wait for a client to connect or reconnect to the stream session. Applies to both connection and reconnection scenarios. This time span starts when the stream session reaches <code>ACTIVE</code> state. If no client connects before the timeout, Amazon GameLift Streams terminates the stream session. Default value is 120.</p>"""
    session_length_seconds: NotRequired[
        "capo_gameliftstreams.types.session_length_seconds.SessionLengthSeconds"
    ]
    """<p>The maximum duration of a session. Amazon GameLift Streams will automatically terminate a session after this amount of time has elapsed, regardless of any existing client connections. Default value is 43200 (12 hours).</p>"""
    additional_launch_args: NotRequired[
        "capo_gameliftstreams.types.game_launch_arg_list.GameLaunchArgList"
    ]
    """<p>A list of CLI arguments that are sent to the streaming server when a stream session launches. You can use this to configure the application or stream session details. You can also provide custom arguments that Amazon GameLift Streams passes to your game client.</p> <p> <code>AdditionalEnvironmentVariables</code> and <code>AdditionalLaunchArgs</code> have similar purposes. <code>AdditionalEnvironmentVariables</code> passes data using environment variables; while <code>AdditionalLaunchArgs</code> passes data using command-line arguments.</p>"""
    additional_environment_variables: NotRequired[
        "capo_gameliftstreams.types.environment_variables.EnvironmentVariables"
    ]
    """<p>A set of options that you can use to control the stream session runtime environment, expressed as a set of key-value pairs. You can use this to configure the application or stream session details. You can also provide custom environment variables that Amazon GameLift Streams passes to your game client.</p> <note> <p>If you want to debug your application with environment variables, we recommend that you do so in a local environment outside of Amazon GameLift Streams. For more information, refer to the Compatibility Guidance in the troubleshooting section of the Developer Guide.</p> </note> <p> <code>AdditionalEnvironmentVariables</code> and <code>AdditionalLaunchArgs</code> have similar purposes. <code>AdditionalEnvironmentVariables</code> passes data using environment variables; while <code>AdditionalLaunchArgs</code> passes data using command-line arguments.</p>"""
    performance_stats_configuration: NotRequired[
        "capo_gameliftstreams.types.performance_stats_configuration.PerformanceStatsConfiguration"
    ]
    """<p>Configuration settings for sharing the stream session's performance stats with the client</p>"""
    role_arn: NotRequired["capo_gameliftstreams.types.iam_role_arn.IamRoleArn"]
    """<p>The ARN of an AWS Identity and Access Management (IAM) role that Amazon GameLift Streams assumes on your behalf during the stream session. The role grants Amazon GameLift Streams permission to obtain temporary credentials for your application. The role's trust policy must allow the <code>gameliftstreams.amazonaws.com</code> service principal to assume it. The role name must start with <code>GameLiftStreams-</code>.</p>"""
    display_configuration: NotRequired[
        "capo_gameliftstreams.types.display_configuration.DisplayConfiguration"
    ]
    """<p>The configuration for the stream session's virtual monitor, including the resolution settings.</p> <p>If not specified, Amazon GameLift Streams uses the default resolution of 1920 × 1080.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartStreamSessionInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_gameliftstreams.types.protocol

    out["Protocol"] = capo_gameliftstreams.types.protocol.serialize_json(
        value["protocol"]
    )
    out["SignalRequest"] = value["signal_request"]
    out["ApplicationIdentifier"] = value["application_identifier"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "locations" in value:
        import capo_gameliftstreams.types.location_list

        out["Locations"] = capo_gameliftstreams.types.location_list.serialize_json(
            value["locations"]
        )
    if "connection_timeout_seconds" in value:
        out["ConnectionTimeoutSeconds"] = value["connection_timeout_seconds"]
    if "session_length_seconds" in value:
        out["SessionLengthSeconds"] = value["session_length_seconds"]
    if "additional_launch_args" in value:
        import capo_gameliftstreams.types.game_launch_arg_list

        out["AdditionalLaunchArgs"] = (
            capo_gameliftstreams.types.game_launch_arg_list.serialize_json(
                value["additional_launch_args"]
            )
        )
    if "additional_environment_variables" in value:
        import capo_gameliftstreams.types.environment_variables

        out["AdditionalEnvironmentVariables"] = (
            capo_gameliftstreams.types.environment_variables.serialize_json(
                value["additional_environment_variables"]
            )
        )
    if "performance_stats_configuration" in value:
        import capo_gameliftstreams.types.performance_stats_configuration

        out["PerformanceStatsConfiguration"] = (
            capo_gameliftstreams.types.performance_stats_configuration.serialize_json(
                value["performance_stats_configuration"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "display_configuration" in value:
        import capo_gameliftstreams.types.display_configuration

        out["DisplayConfiguration"] = (
            capo_gameliftstreams.types.display_configuration.serialize_json(
                value["display_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartStreamSessionInput:
    out: StartStreamSessionInput = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Protocol") is not None:
        import capo_gameliftstreams.types.protocol

        out["protocol"] = capo_gameliftstreams.types.protocol.deserialize_json(
            data["Protocol"]
        )
    else:
        raise DeserializationError("StartStreamSessionInput.protocol required")
    if data.get("SignalRequest") is not None:
        out["signal_request"] = data["SignalRequest"]
    else:
        raise DeserializationError("StartStreamSessionInput.signal_request required")
    if data.get("ApplicationIdentifier") is not None:
        out["application_identifier"] = data["ApplicationIdentifier"]
    else:
        raise DeserializationError(
            "StartStreamSessionInput.application_identifier required"
        )
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    if data.get("Locations") is not None:
        import capo_gameliftstreams.types.location_list

        out["locations"] = capo_gameliftstreams.types.location_list.deserialize_json(
            data["Locations"]
        )
    if data.get("ConnectionTimeoutSeconds") is not None:
        out["connection_timeout_seconds"] = data["ConnectionTimeoutSeconds"]
    if data.get("SessionLengthSeconds") is not None:
        out["session_length_seconds"] = data["SessionLengthSeconds"]
    if data.get("AdditionalLaunchArgs") is not None:
        import capo_gameliftstreams.types.game_launch_arg_list

        out["additional_launch_args"] = (
            capo_gameliftstreams.types.game_launch_arg_list.deserialize_json(
                data["AdditionalLaunchArgs"]
            )
        )
    if data.get("AdditionalEnvironmentVariables") is not None:
        import capo_gameliftstreams.types.environment_variables

        out["additional_environment_variables"] = (
            capo_gameliftstreams.types.environment_variables.deserialize_json(
                data["AdditionalEnvironmentVariables"]
            )
        )
    if data.get("PerformanceStatsConfiguration") is not None:
        import capo_gameliftstreams.types.performance_stats_configuration

        out["performance_stats_configuration"] = (
            capo_gameliftstreams.types.performance_stats_configuration.deserialize_json(
                data["PerformanceStatsConfiguration"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("DisplayConfiguration") is not None:
        import capo_gameliftstreams.types.display_configuration

        out["display_configuration"] = (
            capo_gameliftstreams.types.display_configuration.deserialize_json(
                data["DisplayConfiguration"]
            )
        )
    return out
