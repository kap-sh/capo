"""Generated from Smithy shape ``com.amazonaws.gamelift#RuntimeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_session_activation_timeout_seconds
    import capo_gamelift.types.max_concurrent_game_session_activations
    import capo_gamelift.types.server_process_list


class RuntimeConfiguration(TypedDict, closed=True):
    server_processes: NotRequired[
        "capo_gamelift.types.server_process_list.ServerProcessList"
    ]
    """<p>A collection of server process configurations that identify what server processes to run on fleet computes.</p>"""
    max_concurrent_game_session_activations: NotRequired[
        "capo_gamelift.types.max_concurrent_game_session_activations.MaxConcurrentGameSessionActivations"
    ]
    """<p>The number of game sessions in status <code>ACTIVATING</code> to allow on an instance or compute. This setting limits the instance resources that can be used for new game activations at any one time.</p>"""
    game_session_activation_timeout_seconds: NotRequired[
        "capo_gamelift.types.game_session_activation_timeout_seconds.GameSessionActivationTimeoutSeconds"
    ]
    """<p>The maximum amount of time (in seconds) allowed to launch a new game session and have it report ready to host players. During this time, the game session is in status <code>ACTIVATING</code>. If the game session does not become active before the timeout, it is ended and the game session status is changed to <code>TERMINATED</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuntimeConfiguration) -> dict:
    out: dict = {}
    if "server_processes" in value:
        import capo_gamelift.types.server_process_list

        out["ServerProcesses"] = (
            capo_gamelift.types.server_process_list.serialize_aws_json_1_1(
                value["server_processes"]
            )
        )
    if "max_concurrent_game_session_activations" in value:
        out["MaxConcurrentGameSessionActivations"] = value[
            "max_concurrent_game_session_activations"
        ]
    if "game_session_activation_timeout_seconds" in value:
        out["GameSessionActivationTimeoutSeconds"] = value[
            "game_session_activation_timeout_seconds"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> RuntimeConfiguration:
    out: RuntimeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ServerProcesses") is not None:
        import capo_gamelift.types.server_process_list

        out["server_processes"] = (
            capo_gamelift.types.server_process_list.deserialize_aws_json_1_1(
                data["ServerProcesses"]
            )
        )
    if data.get("MaxConcurrentGameSessionActivations") is not None:
        out["max_concurrent_game_session_activations"] = data[
            "MaxConcurrentGameSessionActivations"
        ]
    if data.get("GameSessionActivationTimeoutSeconds") is not None:
        out["game_session_activation_timeout_seconds"] = data[
            "GameSessionActivationTimeoutSeconds"
        ]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuntimeConfiguration) -> dict:
    out: dict = {}
    if "server_processes" in value:
        import capo_gamelift.types.server_process_list

        out["ServerProcesses"] = capo_gamelift.types.server_process_list.serialize_cbor(
            value["server_processes"]
        )
    if "max_concurrent_game_session_activations" in value:
        out["MaxConcurrentGameSessionActivations"] = value[
            "max_concurrent_game_session_activations"
        ]
    if "game_session_activation_timeout_seconds" in value:
        out["GameSessionActivationTimeoutSeconds"] = value[
            "game_session_activation_timeout_seconds"
        ]
    return out


def deserialize_cbor(data: dict) -> RuntimeConfiguration:
    out: RuntimeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ServerProcesses") is not None:
        import capo_gamelift.types.server_process_list

        out["server_processes"] = (
            capo_gamelift.types.server_process_list.deserialize_cbor(
                data["ServerProcesses"]
            )
        )
    if data.get("MaxConcurrentGameSessionActivations") is not None:
        out["max_concurrent_game_session_activations"] = data[
            "MaxConcurrentGameSessionActivations"
        ]
    if data.get("GameSessionActivationTimeoutSeconds") is not None:
        out["game_session_activation_timeout_seconds"] = data[
            "GameSessionActivationTimeoutSeconds"
        ]
    return out
