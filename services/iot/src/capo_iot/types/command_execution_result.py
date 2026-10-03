"""Generated from Smithy shape ``com.amazonaws.iot#CommandExecutionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.binary_command_execution_result
    import capo_iot.types.boolean_command_execution_result
    import capo_iot.types.string_command_execution_result


class CommandExecutionResult(TypedDict, closed=True):
    s: NotRequired[
        "capo_iot.types.string_command_execution_result.StringCommandExecutionResult"
    ]
    """<p>An attribute of type String. For example:</p> <p> <code>"S": "Hello"</code> </p>"""
    b: NotRequired[
        "capo_iot.types.boolean_command_execution_result.BooleanCommandExecutionResult"
    ]
    """<p>An attribute of type Boolean. For example:</p> <p> <code>"BOOL": true</code> </p>"""
    bin: NotRequired[
        "capo_iot.types.binary_command_execution_result.BinaryCommandExecutionResult"
    ]
    """<p>An attribute of type Binary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommandExecutionResult) -> dict:
    out: dict = {}
    if "s" in value:
        out["S"] = value["s"]
    if "b" in value:
        out["B"] = value["b"]
    if "bin" in value:
        import capo_iot.types.binary_command_execution_result

        out["BIN"] = capo_iot.types.binary_command_execution_result.serialize_json(
            value["bin"]
        )
    return out


def deserialize_json(data: dict) -> CommandExecutionResult:
    out: CommandExecutionResult = {}  # type: ignore[typeddict-item]
    if data.get("S") is not None:
        out["s"] = data["S"]
    if data.get("B") is not None:
        out["b"] = data["B"]
    if data.get("BIN") is not None:
        import capo_iot.types.binary_command_execution_result

        out["bin"] = capo_iot.types.binary_command_execution_result.deserialize_json(
            data["BIN"]
        )
    return out
