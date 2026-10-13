"""Generated from Smithy shape ``com.amazonaws.lambda#ErrorObject``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.error_data
    import capo_lambda.types.error_message
    import capo_lambda.types.error_type
    import capo_lambda.types.stack_trace_entries


class ErrorObject(TypedDict, closed=True):
    error_message: NotRequired["capo_lambda.types.error_message.ErrorMessage"]
    """<p>A human-readable error message.</p>"""
    error_type: NotRequired["capo_lambda.types.error_type.ErrorType"]
    """<p>The error type.</p>"""
    error_data: NotRequired["capo_lambda.types.error_data.ErrorData"]
    """<p>Machine-readable error data.</p>"""
    stack_trace: NotRequired["capo_lambda.types.stack_trace_entries.StackTraceEntries"]
    """<p>Stack trace information for the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorObject) -> dict:
    out: dict = {}
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "error_type" in value:
        out["ErrorType"] = value["error_type"]
    if "error_data" in value:
        out["ErrorData"] = value["error_data"]
    if "stack_trace" in value:
        import capo_lambda.types.stack_trace_entries

        out["StackTrace"] = capo_lambda.types.stack_trace_entries.serialize_json(
            value["stack_trace"]
        )
    return out


def deserialize_json(data: dict) -> ErrorObject:
    out: ErrorObject = {}  # type: ignore[typeddict-item]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("ErrorType") is not None:
        out["error_type"] = data["ErrorType"]
    if data.get("ErrorData") is not None:
        out["error_data"] = data["ErrorData"]
    if data.get("StackTrace") is not None:
        import capo_lambda.types.stack_trace_entries

        out["stack_trace"] = capo_lambda.types.stack_trace_entries.deserialize_json(
            data["StackTrace"]
        )
    return out


def redact_sensitive(value: ErrorObject) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "error_message" in value:
        out["error_message"] = "*** Sensitive Data Redacted ***"
    if "error_type" in value:
        out["error_type"] = "*** Sensitive Data Redacted ***"
    if "error_data" in value:
        out["error_data"] = "*** Sensitive Data Redacted ***"
    if "stack_trace" in value:
        import capo_lambda.types.stack_trace_entries

        out["stack_trace"] = capo_lambda.types.stack_trace_entries.redact_sensitive(
            value["stack_trace"]
        )
    return out
