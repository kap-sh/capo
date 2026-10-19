"""Generated from Smithy shape ``com.amazonaws.pcs#NodeLifecycleScript``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pcs.types.execution_policy
    import capo_pcs.types.node_lifecycle_script_arguments
    import capo_pcs.types.on_error
    import capo_pcs.types.script_source


class NodeLifecycleScript(TypedDict, closed=True):
    name: "str"
    """<p>A unique name for the script. The name can be up to 64 characters long. Valid characters are letters, numbers, spaces, underscores (<code>_</code>), and hyphens (<code>-</code>). The first character must be a letter or a number.</p>"""
    script_source: "capo_pcs.types.script_source.ScriptSource"
    """<p>The source location and integrity information for the script.</p>"""
    arguments: NotRequired[
        "capo_pcs.types.node_lifecycle_script_arguments.NodeLifecycleScriptArguments"
    ]
    """<p>The command-line arguments to pass to the script. You can specify up to 20 arguments, and each argument can be up to 256 characters long.</p>"""
    on_error: "capo_pcs.types.on_error.OnError"
    """<p>The behavior when the script fails. The default value is <code>TERMINATE</code>. Valid values:</p> <ul> <li> <p> <code>TERMINATE</code> – Terminates the compute node.</p> </li> <li> <p> <code>STOP_SEQUENCE</code> – Stops running subsequent scripts in the sequence but doesn't terminate the compute node.</p> </li> <li> <p> <code>CONTINUE</code> – Ignores the error and continues running the next script.</p> </li> </ul>"""
    execution_policy: "capo_pcs.types.execution_policy.ExecutionPolicy"
    """<p>The policy that determines when the script runs. The default value is <code>FIRST_BOOT_ONLY</code>. Valid values:</p> <ul> <li> <p> <code>FIRST_BOOT_ONLY</code> – Runs the script only the first time the compute node boots.</p> </li> <li> <p> <code>EVERY_BOOT</code> – Runs the script every time the compute node boots, including reboots.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NodeLifecycleScript) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_pcs.types.script_source

    out["scriptSource"] = capo_pcs.types.script_source.serialize_aws_json_1_0(
        value["script_source"]
    )
    if "arguments" in value:
        import capo_pcs.types.node_lifecycle_script_arguments

        out["arguments"] = (
            capo_pcs.types.node_lifecycle_script_arguments.serialize_aws_json_1_0(
                value["arguments"]
            )
        )
    import capo_pcs.types.on_error

    out["onError"] = capo_pcs.types.on_error.serialize_aws_json_1_0(
        value.get("on_error", "TERMINATE")
    )
    import capo_pcs.types.execution_policy

    out["executionPolicy"] = capo_pcs.types.execution_policy.serialize_aws_json_1_0(
        value.get("execution_policy", "FIRST_BOOT_ONLY")
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> NodeLifecycleScript:
    out: NodeLifecycleScript = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("scriptSource") is not None:
        import capo_pcs.types.script_source

        out["script_source"] = capo_pcs.types.script_source.deserialize_aws_json_1_0(
            data["scriptSource"]
        )
    else:
        raise DeserializationError("NodeLifecycleScript.script_source required")
    if data.get("arguments") is not None:
        import capo_pcs.types.node_lifecycle_script_arguments

        out["arguments"] = (
            capo_pcs.types.node_lifecycle_script_arguments.deserialize_aws_json_1_0(
                data["arguments"]
            )
        )
    if data.get("onError") is not None:
        import capo_pcs.types.on_error

        out["on_error"] = capo_pcs.types.on_error.deserialize_aws_json_1_0(
            data["onError"]
        )
    else:
        out["on_error"] = "TERMINATE"
    if data.get("executionPolicy") is not None:
        import capo_pcs.types.execution_policy

        out["execution_policy"] = (
            capo_pcs.types.execution_policy.deserialize_aws_json_1_0(
                data["executionPolicy"]
            )
        )
    else:
        out["execution_policy"] = "FIRST_BOOT_ONLY"
    return out
