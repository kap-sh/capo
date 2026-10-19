"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ExecuteCommandSessionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.execute_command_session_configuration_arguments


class ExecuteCommandSessionConfiguration(TypedDict, closed=True):
    command: "str"
    """<p>The command used at the beginning of the SSH session to a Dev Environment.</p>"""
    arguments: NotRequired[
        "capo_codecatalyst.types.execute_command_session_configuration_arguments.ExecuteCommandSessionConfigurationArguments"
    ]
    """<p>An array of arguments containing arguments and members.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteCommandSessionConfiguration) -> dict:
    out: dict = {}
    out["command"] = value["command"]
    if "arguments" in value:
        import capo_codecatalyst.types.execute_command_session_configuration_arguments

        out["arguments"] = (
            capo_codecatalyst.types.execute_command_session_configuration_arguments.serialize_json(
                value["arguments"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExecuteCommandSessionConfiguration:
    out: ExecuteCommandSessionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("command") is not None:
        out["command"] = data["command"]
    else:
        out["command"] = ""
    if data.get("arguments") is not None:
        import capo_codecatalyst.types.execute_command_session_configuration_arguments

        out["arguments"] = (
            capo_codecatalyst.types.execute_command_session_configuration_arguments.deserialize_json(
                data["arguments"]
            )
        )
    return out
