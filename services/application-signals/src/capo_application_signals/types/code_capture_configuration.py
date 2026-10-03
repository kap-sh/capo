"""Generated from Smithy shape ``com.amazonaws.applicationsignals#CodeCaptureConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_signals.types.capture_limits_config
    import capo_application_signals.types.string_list


class CodeCaptureConfiguration(TypedDict, closed=True):
    capture_arguments: NotRequired[
        "capo_application_signals.types.string_list.StringList"
    ]
    """<p>The function arguments to capture. Omit to capture defaults, use an empty list to capture none, use <code>["*"]</code> to capture all arguments, or specify argument names to capture selectively (up to 10 entries).</p>"""
    capture_return: NotRequired["bool"]
    """<p>Whether to capture the return value. Defaults to false.</p>"""
    capture_stack_trace: NotRequired["bool"]
    """<p>Whether to capture a stack trace when the instrumentation point is hit. Defaults to true.</p>"""
    capture_locals: NotRequired["capo_application_signals.types.string_list.StringList"]
    """<p>The local variables to capture by name. Omit or pass an empty list to capture none. You can specify up to 20 names.</p>"""
    capture_limits: (
        "capo_application_signals.types.capture_limits_config.CaptureLimitsConfig"
    )
    """<p>Safety limits that bound what is captured, including hit counts, string length, collection depth, and stack trace size.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeCaptureConfiguration) -> dict:
    out: dict = {}
    if "capture_arguments" in value:
        import capo_application_signals.types.string_list

        out["CaptureArguments"] = (
            capo_application_signals.types.string_list.serialize_json(
                value["capture_arguments"]
            )
        )
    if "capture_return" in value:
        out["CaptureReturn"] = value["capture_return"]
    if "capture_stack_trace" in value:
        out["CaptureStackTrace"] = value["capture_stack_trace"]
    if "capture_locals" in value:
        import capo_application_signals.types.string_list

        out["CaptureLocals"] = (
            capo_application_signals.types.string_list.serialize_json(
                value["capture_locals"]
            )
        )
    import capo_application_signals.types.capture_limits_config

    out["CaptureLimits"] = (
        capo_application_signals.types.capture_limits_config.serialize_json(
            value["capture_limits"]
        )
    )
    return out


def deserialize_json(data: dict) -> CodeCaptureConfiguration:
    out: CodeCaptureConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("CaptureArguments") is not None:
        import capo_application_signals.types.string_list

        out["capture_arguments"] = (
            capo_application_signals.types.string_list.deserialize_json(
                data["CaptureArguments"]
            )
        )
    if data.get("CaptureReturn") is not None:
        out["capture_return"] = data["CaptureReturn"]
    if data.get("CaptureStackTrace") is not None:
        out["capture_stack_trace"] = data["CaptureStackTrace"]
    if data.get("CaptureLocals") is not None:
        import capo_application_signals.types.string_list

        out["capture_locals"] = (
            capo_application_signals.types.string_list.deserialize_json(
                data["CaptureLocals"]
            )
        )
    if data.get("CaptureLimits") is not None:
        import capo_application_signals.types.capture_limits_config

        out["capture_limits"] = (
            capo_application_signals.types.capture_limits_config.deserialize_json(
                data["CaptureLimits"]
            )
        )
    else:
        raise DeserializationError("CodeCaptureConfiguration.capture_limits required")
    return out
