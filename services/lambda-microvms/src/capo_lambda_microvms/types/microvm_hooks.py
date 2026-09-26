"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#MicrovmHooks``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_microvms.types.hook_state


class MicrovmHooks(TypedDict, closed=True):
    run: "capo_lambda_microvms.types.hook_state.HookState"
    """<p>The path of the hook invoked when the MicroVM starts running.</p>"""
    run_timeout_in_seconds: "int"
    """<p>The maximum time in seconds for the run hook to complete.</p>"""
    resume: "capo_lambda_microvms.types.hook_state.HookState"
    """<p>The path of the hook invoked when the MicroVM resumes from a suspended state.</p>"""
    resume_timeout_in_seconds: "int"
    """<p>The maximum time in seconds for the resume hook to complete.</p>"""
    suspend: "capo_lambda_microvms.types.hook_state.HookState"
    """<p>The path of the hook invoked when the MicroVM is suspended.</p>"""
    suspend_timeout_in_seconds: "int"
    """<p>The maximum time in seconds for the suspend hook to complete.</p>"""
    terminate: "capo_lambda_microvms.types.hook_state.HookState"
    """<p>The path of the hook invoked when the MicroVM is terminated.</p>"""
    terminate_timeout_in_seconds: "int"
    """<p>The maximum time in seconds for the terminate hook to complete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MicrovmHooks) -> dict:
    out: dict = {}
    import capo_lambda_microvms.types.hook_state

    out["run"] = capo_lambda_microvms.types.hook_state.serialize_json(
        value.get("run", "DISABLED")
    )
    out["runTimeoutInSeconds"] = value.get("run_timeout_in_seconds", 1)
    import capo_lambda_microvms.types.hook_state

    out["resume"] = capo_lambda_microvms.types.hook_state.serialize_json(
        value.get("resume", "DISABLED")
    )
    out["resumeTimeoutInSeconds"] = value.get("resume_timeout_in_seconds", 1)
    import capo_lambda_microvms.types.hook_state

    out["suspend"] = capo_lambda_microvms.types.hook_state.serialize_json(
        value.get("suspend", "DISABLED")
    )
    out["suspendTimeoutInSeconds"] = value.get("suspend_timeout_in_seconds", 1)
    import capo_lambda_microvms.types.hook_state

    out["terminate"] = capo_lambda_microvms.types.hook_state.serialize_json(
        value.get("terminate", "DISABLED")
    )
    out["terminateTimeoutInSeconds"] = value.get("terminate_timeout_in_seconds", 1)
    return out


def deserialize_json(data: dict) -> MicrovmHooks:
    out: MicrovmHooks = {}  # type: ignore[typeddict-item]
    if data.get("run") is not None:
        import capo_lambda_microvms.types.hook_state

        out["run"] = capo_lambda_microvms.types.hook_state.deserialize_json(data["run"])
    else:
        out["run"] = "DISABLED"
    if data.get("runTimeoutInSeconds") is not None:
        out["run_timeout_in_seconds"] = data["runTimeoutInSeconds"]
    else:
        out["run_timeout_in_seconds"] = 1
    if data.get("resume") is not None:
        import capo_lambda_microvms.types.hook_state

        out["resume"] = capo_lambda_microvms.types.hook_state.deserialize_json(
            data["resume"]
        )
    else:
        out["resume"] = "DISABLED"
    if data.get("resumeTimeoutInSeconds") is not None:
        out["resume_timeout_in_seconds"] = data["resumeTimeoutInSeconds"]
    else:
        out["resume_timeout_in_seconds"] = 1
    if data.get("suspend") is not None:
        import capo_lambda_microvms.types.hook_state

        out["suspend"] = capo_lambda_microvms.types.hook_state.deserialize_json(
            data["suspend"]
        )
    else:
        out["suspend"] = "DISABLED"
    if data.get("suspendTimeoutInSeconds") is not None:
        out["suspend_timeout_in_seconds"] = data["suspendTimeoutInSeconds"]
    else:
        out["suspend_timeout_in_seconds"] = 1
    if data.get("terminate") is not None:
        import capo_lambda_microvms.types.hook_state

        out["terminate"] = capo_lambda_microvms.types.hook_state.deserialize_json(
            data["terminate"]
        )
    else:
        out["terminate"] = "DISABLED"
    if data.get("terminateTimeoutInSeconds") is not None:
        out["terminate_timeout_in_seconds"] = data["terminateTimeoutInSeconds"]
    else:
        out["terminate_timeout_in_seconds"] = 1
    return out
