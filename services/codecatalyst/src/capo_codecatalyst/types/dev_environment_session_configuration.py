"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DevEnvironmentSessionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.dev_environment_session_type
    import capo_codecatalyst.types.execute_command_session_configuration


class DevEnvironmentSessionConfiguration(TypedDict, closed=True):
    session_type: (
        "capo_codecatalyst.types.dev_environment_session_type.DevEnvironmentSessionType"
    )
    """<p>The type of the session.</p>"""
    execute_command_session_configuration: NotRequired[
        "capo_codecatalyst.types.execute_command_session_configuration.ExecuteCommandSessionConfiguration"
    ]
    """<p>Information about optional commands that will be run on the Dev Environment when the SSH session begins.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DevEnvironmentSessionConfiguration) -> dict:
    out: dict = {}
    out["sessionType"] = value["session_type"]
    if "execute_command_session_configuration" in value:
        import capo_codecatalyst.types.execute_command_session_configuration

        out["executeCommandSessionConfiguration"] = (
            capo_codecatalyst.types.execute_command_session_configuration.serialize_json(
                value["execute_command_session_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DevEnvironmentSessionConfiguration:
    out: DevEnvironmentSessionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("sessionType") is not None:
        out["session_type"] = data["sessionType"]
    else:
        out["session_type"] = ""
    if data.get("executeCommandSessionConfiguration") is not None:
        import capo_codecatalyst.types.execute_command_session_configuration

        out["execute_command_session_configuration"] = (
            capo_codecatalyst.types.execute_command_session_configuration.deserialize_json(
                data["executeCommandSessionConfiguration"]
            )
        )
    return out
