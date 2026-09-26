"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#MicrovmImageHooks``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_microvms.types.hook_state


class MicrovmImageHooks(TypedDict, closed=True):
    ready: "capo_lambda_microvms.types.hook_state.HookState"
    """<p>The path of the hook invoked when the MicroVM image build is ready.</p>"""
    ready_timeout_in_seconds: "int"
    """<p>The maximum time in seconds for the ready hook to complete.</p>"""
    validate: "capo_lambda_microvms.types.hook_state.HookState"
    """<p>The path of the hook invoked to validate the MicroVM image build.</p>"""
    validate_timeout_in_seconds: "int"
    """<p>The maximum time in seconds for the validate hook to complete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MicrovmImageHooks) -> dict:
    out: dict = {}
    import capo_lambda_microvms.types.hook_state

    out["ready"] = capo_lambda_microvms.types.hook_state.serialize_json(
        value.get("ready", "DISABLED")
    )
    out["readyTimeoutInSeconds"] = value.get("ready_timeout_in_seconds", 30)
    import capo_lambda_microvms.types.hook_state

    out["validate"] = capo_lambda_microvms.types.hook_state.serialize_json(
        value.get("validate", "DISABLED")
    )
    out["validateTimeoutInSeconds"] = value.get("validate_timeout_in_seconds", 30)
    return out


def deserialize_json(data: dict) -> MicrovmImageHooks:
    out: MicrovmImageHooks = {}  # type: ignore[typeddict-item]
    if data.get("ready") is not None:
        import capo_lambda_microvms.types.hook_state

        out["ready"] = capo_lambda_microvms.types.hook_state.deserialize_json(
            data["ready"]
        )
    else:
        out["ready"] = "DISABLED"
    if data.get("readyTimeoutInSeconds") is not None:
        out["ready_timeout_in_seconds"] = data["readyTimeoutInSeconds"]
    else:
        out["ready_timeout_in_seconds"] = 30
    if data.get("validate") is not None:
        import capo_lambda_microvms.types.hook_state

        out["validate"] = capo_lambda_microvms.types.hook_state.deserialize_json(
            data["validate"]
        )
    else:
        out["validate"] = "DISABLED"
    if data.get("validateTimeoutInSeconds") is not None:
        out["validate_timeout_in_seconds"] = data["validateTimeoutInSeconds"]
    else:
        out["validate_timeout_in_seconds"] = 30
    return out
