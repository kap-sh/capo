"""Generated from Smithy shape ``com.amazonaws.gamelift#TerminateGameSessionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.arn_string_model
    import capo_gamelift.types.termination_mode


class TerminateGameSessionInput(TypedDict, closed=True):
    game_session_id: NotRequired["capo_gamelift.types.arn_string_model.ArnStringModel"]
    """<p>An identifier for the game session that is unique across all regions to be terminated. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>.</p>"""
    termination_mode: NotRequired[
        "capo_gamelift.types.termination_mode.TerminationMode"
    ]
    """<p>The method to use to terminate the game session. Available methods include: </p> <ul> <li> <p> <code>TRIGGER_ON_PROCESS_TERMINATE</code> – Prompts the Amazon GameLift Servers service to send an <code>OnProcessTerminate()</code> callback to the server process and initiate the normal game session shutdown sequence. The <code>OnProcessTerminate</code> method, which is implemented in the game server code, must include a call to the server SDK action <code>ProcessEnding()</code>, which is how the server process signals to Amazon GameLift Servers that a game session is ending. If the server process doesn't call <code>ProcessEnding()</code>, the game session termination won't conclude successfully.</p> </li> <li> <p> <code>FORCE_TERMINATE</code> – Prompts the Amazon GameLift Servers service to stop the server process immediately. Amazon GameLift Servers takes action (depending on the type of fleet) to shut down the server process without the normal game session shutdown sequence. </p> <note> <p>This method is not available for game sessions that are running on Anywhere fleets unless the fleet is deployed with the Amazon GameLift Servers Agent. In this scenario, a force terminate request results in an invalid or bad request exception.</p> </note> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateGameSessionInput) -> dict:
    out: dict = {}
    if "game_session_id" in value:
        out["GameSessionId"] = value["game_session_id"]
    if "termination_mode" in value:
        import capo_gamelift.types.termination_mode

        out["TerminationMode"] = (
            capo_gamelift.types.termination_mode.serialize_aws_json_1_1(
                value["termination_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateGameSessionInput:
    out: TerminateGameSessionInput = {}  # type: ignore[typeddict-item]
    if data.get("GameSessionId") is not None:
        out["game_session_id"] = data["GameSessionId"]
    if data.get("TerminationMode") is not None:
        import capo_gamelift.types.termination_mode

        out["termination_mode"] = (
            capo_gamelift.types.termination_mode.deserialize_aws_json_1_1(
                data["TerminationMode"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TerminateGameSessionInput) -> dict:
    out: dict = {}
    if "game_session_id" in value:
        out["GameSessionId"] = value["game_session_id"]
    if "termination_mode" in value:
        import capo_gamelift.types.termination_mode

        out["TerminationMode"] = capo_gamelift.types.termination_mode.serialize_cbor(
            value["termination_mode"]
        )
    return out


def deserialize_cbor(data: dict) -> TerminateGameSessionInput:
    out: TerminateGameSessionInput = {}  # type: ignore[typeddict-item]
    if data.get("GameSessionId") is not None:
        out["game_session_id"] = data["GameSessionId"]
    if data.get("TerminationMode") is not None:
        import capo_gamelift.types.termination_mode

        out["termination_mode"] = capo_gamelift.types.termination_mode.deserialize_cbor(
            data["TerminationMode"]
        )
    return out
