"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#CreateStreamUrlInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_gameliftstreams.errors import DeserializationError

if TYPE_CHECKING:
    import capo_gameliftstreams.types.client_token
    import capo_gameliftstreams.types.description
    import capo_gameliftstreams.types.display_configuration
    import capo_gameliftstreams.types.environment_variables
    import capo_gameliftstreams.types.game_launch_arg_list
    import capo_gameliftstreams.types.iam_role_arn
    import capo_gameliftstreams.types.identifier
    import capo_gameliftstreams.types.location_list
    import capo_gameliftstreams.types.protocol
    import capo_gameliftstreams.types.session_length_seconds
    import capo_gameliftstreams.types.url_expires_after_minutes
    import capo_gameliftstreams.types.usage_limit


class CreateStreamUrlInput(TypedDict, closed=True):
    identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p>An <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p> <p>The stream session runs in this stream group.</p>"""
    application_identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p>An <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p> <p>This application must be associated with the stream group.</p>"""
    protocol: "capo_gameliftstreams.types.protocol.Protocol"
    """<p>The data transport protocol for the stream session. Amazon GameLift Streams supports <code>WebRTC</code>.</p>"""
    url_expires_after_minutes: (
        "capo_gameliftstreams.types.url_expires_after_minutes.UrlExpiresAfterMinutes"
    )
    """<p>The number of minutes after creation that the stream URL remains valid. After this period, the status of the stream URL changes to <code>EXPIRED</code> and it can no longer start stream sessions. The minimum is 1 minute. For the maximum, see <a href="https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html">Regions, quotas, and limitations</a> in the <i>Amazon GameLift Streams Developer Guide</i>.</p>"""
    usage_limit: NotRequired["capo_gameliftstreams.types.usage_limit.UsageLimit"]
    """<p>The maximum number of times the stream URL can start a stream session. Each successful use reduces the remaining uses by one. The minimum is 1, and the default is 1. For the maximum, see <a href="https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html">Regions, quotas, and limitations</a> in the <i>Amazon GameLift Streams Developer Guide</i>.</p>"""
    description: NotRequired["capo_gameliftstreams.types.description.Description"]
    """<p>A descriptive label for the stream URL.</p>"""
    locations: "capo_gameliftstreams.types.location_list.LocationList"
    """<p>A list of locations, in order of preference, where Amazon GameLift Streams can place the stream session. Specify each location by its Amazon Web Services Region code, for example <code>us-east-1</code>. For a complete list of locations that Amazon GameLift Streams supports, refer to <a href="https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html">Regions, quotas, and limitations</a> in the <i>Amazon GameLift Streams Developer Guide</i>. </p>"""
    session_length_seconds: NotRequired[
        "capo_gameliftstreams.types.session_length_seconds.SessionLengthSeconds"
    ]
    """<p>The maximum length of time, in seconds, that a stream session started from this stream URL can run. Valid values are 1-86400 seconds (1 second to 24 hours). The default is 43200 seconds (12 hours).</p>"""
    additional_launch_args: NotRequired[
        "capo_gameliftstreams.types.game_launch_arg_list.GameLaunchArgList"
    ]
    """<p>A list of CLI arguments that are sent to the streaming server when a stream session launches. You can use this to configure the application or stream session details. You can also provide custom arguments that Amazon GameLift Streams passes to your game client.</p> <p> <code>AdditionalEnvironmentVariables</code> and <code>AdditionalLaunchArgs</code> have similar purposes. <code>AdditionalEnvironmentVariables</code> passes data using environment variables; while <code>AdditionalLaunchArgs</code> passes data using command-line arguments.</p>"""
    additional_environment_variables: NotRequired[
        "capo_gameliftstreams.types.environment_variables.EnvironmentVariables"
    ]
    """<p>A set of options that you can use to control the stream session runtime environment, expressed as a set of key-value pairs. You can use this to configure the application or stream session details. You can also provide custom environment variables that Amazon GameLift Streams passes to your game client.</p> <note> <p>If you want to debug your application with environment variables, we recommend that you do so in a local environment outside of Amazon GameLift Streams. For more information, refer to the Compatibility Guidance in the troubleshooting section of the Developer Guide.</p> </note> <p> <code>AdditionalEnvironmentVariables</code> and <code>AdditionalLaunchArgs</code> have similar purposes. <code>AdditionalEnvironmentVariables</code> passes data using environment variables; while <code>AdditionalLaunchArgs</code> passes data using command-line arguments.</p>"""
    role_arn: NotRequired["capo_gameliftstreams.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that Amazon GameLift Streams assumes during stream sessions started from this stream URL. For more information, see <a href="https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/session-credentials.html">Provide AWS credentials to your streaming application</a> in the <i>Amazon GameLift Streams Developer Guide</i>.</p>"""
    display_configuration: NotRequired[
        "capo_gameliftstreams.types.display_configuration.DisplayConfiguration"
    ]
    """<p>The display settings, such as resolution, for stream sessions started from this stream URL.</p>"""
    client_token: NotRequired["capo_gameliftstreams.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure this request is idempotent. If you retry a request with the same <code>ClientToken</code>, Amazon GameLift Streams returns the original response without performing the operation again.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateStreamUrlInput) -> dict:
    out: dict = {}
    out["ApplicationIdentifier"] = value["application_identifier"]
    import capo_gameliftstreams.types.protocol

    out["Protocol"] = capo_gameliftstreams.types.protocol.serialize_json(
        value["protocol"]
    )
    out["UrlExpiresAfterMinutes"] = value["url_expires_after_minutes"]
    if "usage_limit" in value:
        out["UsageLimit"] = value["usage_limit"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_gameliftstreams.types.location_list

    out["Locations"] = capo_gameliftstreams.types.location_list.serialize_json(
        value["locations"]
    )
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
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "display_configuration" in value:
        import capo_gameliftstreams.types.display_configuration

        out["DisplayConfiguration"] = (
            capo_gameliftstreams.types.display_configuration.serialize_json(
                value["display_configuration"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateStreamUrlInput:
    out: CreateStreamUrlInput = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationIdentifier") is not None:
        out["application_identifier"] = data["ApplicationIdentifier"]
    else:
        raise DeserializationError(
            "CreateStreamUrlInput.application_identifier required"
        )
    if data.get("Protocol") is not None:
        import capo_gameliftstreams.types.protocol

        out["protocol"] = capo_gameliftstreams.types.protocol.deserialize_json(
            data["Protocol"]
        )
    else:
        raise DeserializationError("CreateStreamUrlInput.protocol required")
    if data.get("UrlExpiresAfterMinutes") is not None:
        out["url_expires_after_minutes"] = data["UrlExpiresAfterMinutes"]
    else:
        raise DeserializationError(
            "CreateStreamUrlInput.url_expires_after_minutes required"
        )
    if data.get("UsageLimit") is not None:
        out["usage_limit"] = data["UsageLimit"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Locations") is not None:
        import capo_gameliftstreams.types.location_list

        out["locations"] = capo_gameliftstreams.types.location_list.deserialize_json(
            data["Locations"]
        )
    else:
        raise DeserializationError("CreateStreamUrlInput.locations required")
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
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("DisplayConfiguration") is not None:
        import capo_gameliftstreams.types.display_configuration

        out["display_configuration"] = (
            capo_gameliftstreams.types.display_configuration.deserialize_json(
                data["DisplayConfiguration"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
