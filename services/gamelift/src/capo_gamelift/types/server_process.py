"""Generated from Smithy shape ``com.amazonaws.gamelift#ServerProcess``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.launch_parameters_string_model
    import capo_gamelift.types.launch_path_string_model
    import capo_gamelift.types.positive_integer


class ServerProcess(TypedDict, closed=True):
    launch_path: NotRequired[
        "capo_gamelift.types.launch_path_string_model.LaunchPathStringModel"
    ]
    r"""<p>The location of a game build executable or Realtime script. Game builds and Realtime scripts are installed on instances at the root: </p> <ul> <li> <p>Windows (custom game builds only): <code>C:\game</code>. Example: "<code>C:\game\MyGame\server.exe</code>" </p> </li> <li> <p>Linux: <code>/local/game</code>. Examples: "<code>/local/game/MyGame/server.exe</code>" or "<code>/local/game/MyRealtimeScript.js</code>"</p> </li> </ul> <note> <p>Amazon GameLift Servers doesn't support the use of setup scripts that launch the game executable. For custom game builds, this parameter must indicate the executable that calls the server SDK operations <code>initSDK()</code> and <code>ProcessReady()</code>. </p> </note>"""
    parameters: NotRequired[
        "capo_gamelift.types.launch_parameters_string_model.LaunchParametersStringModel"
    ]
    """<p>An optional list of parameters to pass to the server executable or Realtime script on launch.</p>"""
    concurrent_executions: NotRequired[
        "capo_gamelift.types.positive_integer.PositiveInteger"
    ]
    """<p>The number of server processes using this configuration that run concurrently on each instance or compute.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServerProcess) -> dict:
    out: dict = {}
    if "launch_path" in value:
        out["LaunchPath"] = value["launch_path"]
    if "parameters" in value:
        out["Parameters"] = value["parameters"]
    if "concurrent_executions" in value:
        out["ConcurrentExecutions"] = value["concurrent_executions"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServerProcess:
    out: ServerProcess = {}  # type: ignore[typeddict-item]
    if data.get("LaunchPath") is not None:
        out["launch_path"] = data["LaunchPath"]
    if data.get("Parameters") is not None:
        out["parameters"] = data["Parameters"]
    if data.get("ConcurrentExecutions") is not None:
        out["concurrent_executions"] = data["ConcurrentExecutions"]
    return out
