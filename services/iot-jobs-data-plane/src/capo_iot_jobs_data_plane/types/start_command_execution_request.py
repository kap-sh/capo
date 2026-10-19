"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#StartCommandExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_jobs_data_plane.types.client_request_token_v2
    import capo_iot_jobs_data_plane.types.command_arn
    import capo_iot_jobs_data_plane.types.command_execution_parameter_map
    import capo_iot_jobs_data_plane.types.command_execution_timeout_in_seconds
    import capo_iot_jobs_data_plane.types.target_arn


class StartCommandExecutionRequest(TypedDict, closed=True):
    target_arn: "capo_iot_jobs_data_plane.types.target_arn.TargetArn"
    """<p>The Amazon Resource Number (ARN) of the device where the command execution is occurring.</p>"""
    command_arn: "capo_iot_jobs_data_plane.types.command_arn.CommandArn"
    """<p>The Amazon Resource Number (ARN) of the command. For example, <code>arn:aws:iot:<region>:<accountid>:command/<commandName></code> </p>"""
    parameters: NotRequired[
        "capo_iot_jobs_data_plane.types.command_execution_parameter_map.CommandExecutionParameterMap"
    ]
    """<p>A list of parameters that are required by the <code>StartCommandExecution</code> API when performing the command on a device.</p>"""
    execution_timeout_seconds: NotRequired[
        "capo_iot_jobs_data_plane.types.command_execution_timeout_in_seconds.CommandExecutionTimeoutInSeconds"
    ]
    """<p>Specifies the amount of time in second the device has to finish the command execution. A timer is started as soon as the command execution is created. If the command execution status is not set to another terminal state before the timer expires, it will automatically update to <code>TIMED_OUT</code>.</p>"""
    client_token: NotRequired[
        "capo_iot_jobs_data_plane.types.client_request_token_v2.ClientRequestTokenV2"
    ]
    """<p>The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you retry the request using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, Amazon Web Services SDKs will automatically generate a unique client request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCommandExecutionRequest) -> dict:
    out: dict = {}
    out["targetArn"] = value["target_arn"]
    out["commandArn"] = value["command_arn"]
    if "parameters" in value:
        import capo_iot_jobs_data_plane.types.command_execution_parameter_map

        out["parameters"] = (
            capo_iot_jobs_data_plane.types.command_execution_parameter_map.serialize_json(
                value["parameters"]
            )
        )
    if "execution_timeout_seconds" in value:
        out["executionTimeoutSeconds"] = value["execution_timeout_seconds"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartCommandExecutionRequest:
    out: StartCommandExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("targetArn") is not None:
        out["target_arn"] = data["targetArn"]
    else:
        out["target_arn"] = ""
    if data.get("commandArn") is not None:
        out["command_arn"] = data["commandArn"]
    else:
        out["command_arn"] = ""
    if data.get("parameters") is not None:
        import capo_iot_jobs_data_plane.types.command_execution_parameter_map

        out["parameters"] = (
            capo_iot_jobs_data_plane.types.command_execution_parameter_map.deserialize_json(
                data["parameters"]
            )
        )
    if data.get("executionTimeoutSeconds") is not None:
        out["execution_timeout_seconds"] = data["executionTimeoutSeconds"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
