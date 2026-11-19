"""Generated from Smithy shape ``com.amazonaws.codedeploy#Diagnostics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.lifecycle_error_code
    import capo_codedeploy.types.lifecycle_message
    import capo_codedeploy.types.log_tail
    import capo_codedeploy.types.script_name


class Diagnostics(TypedDict, closed=True):
    error_code: NotRequired[
        "capo_codedeploy.types.lifecycle_error_code.LifecycleErrorCode"
    ]
    """<p>The associated error code:</p> <ul> <li> <p>Success: The specified script ran.</p> </li> <li> <p>ScriptMissing: The specified script was not found in the specified location.</p> </li> <li> <p>ScriptNotExecutable: The specified script is not a recognized executable file type.</p> </li> <li> <p>ScriptTimedOut: The specified script did not finish running in the specified time period.</p> </li> <li> <p>ScriptFailed: The specified script failed to run as expected.</p> </li> <li> <p>UnknownError: The specified script did not run for an unknown reason.</p> </li> </ul>"""
    script_name: NotRequired["capo_codedeploy.types.script_name.ScriptName"]
    """<p>The name of the script.</p>"""
    message: NotRequired["capo_codedeploy.types.lifecycle_message.LifecycleMessage"]
    """<p>The message associated with the error.</p>"""
    log_tail: NotRequired["capo_codedeploy.types.log_tail.LogTail"]
    """<p>The last portion of the diagnostic log.</p> <p>If available, CodeDeploy returns up to the last 4 KB of the diagnostic log.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Diagnostics) -> dict:
    out: dict = {}
    if "error_code" in value:
        import capo_codedeploy.types.lifecycle_error_code

        out["errorCode"] = (
            capo_codedeploy.types.lifecycle_error_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "script_name" in value:
        out["scriptName"] = value["script_name"]
    if "message" in value:
        out["message"] = value["message"]
    if "log_tail" in value:
        out["logTail"] = value["log_tail"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Diagnostics:
    out: Diagnostics = {}  # type: ignore[typeddict-item]
    if data.get("errorCode") is not None:
        import capo_codedeploy.types.lifecycle_error_code

        out["error_code"] = (
            capo_codedeploy.types.lifecycle_error_code.deserialize_aws_json_1_1(
                data["errorCode"]
            )
        )
    if data.get("scriptName") is not None:
        out["script_name"] = data["scriptName"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("logTail") is not None:
        out["log_tail"] = data["logTail"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Diagnostics) -> dict:
    out: dict = {}
    if "error_code" in value:
        import capo_codedeploy.types.lifecycle_error_code

        out["errorCode"] = capo_codedeploy.types.lifecycle_error_code.serialize_cbor(
            value["error_code"]
        )
    if "script_name" in value:
        out["scriptName"] = value["script_name"]
    if "message" in value:
        out["message"] = value["message"]
    if "log_tail" in value:
        out["logTail"] = value["log_tail"]
    return out


def deserialize_cbor(data: dict) -> Diagnostics:
    out: Diagnostics = {}  # type: ignore[typeddict-item]
    if data.get("errorCode") is not None:
        import capo_codedeploy.types.lifecycle_error_code

        out["error_code"] = capo_codedeploy.types.lifecycle_error_code.deserialize_cbor(
            data["errorCode"]
        )
    if data.get("scriptName") is not None:
        out["script_name"] = data["scriptName"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("logTail") is not None:
        out["log_tail"] = data["logTail"]
    return out
