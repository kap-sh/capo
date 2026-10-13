"""Generated from Smithy shape ``com.amazonaws.lambda#InvocationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.blob
    import capo_lambda.types.durable_execution_arn
    import capo_lambda.types.integer
    import capo_lambda.types.string
    import capo_lambda.types.version


class InvocationResponse(TypedDict, closed=True):
    status_code: "capo_lambda.types.integer.Integer"
    """<p>The HTTP status code is in the 200 range for a successful request. For the <code>RequestResponse</code> invocation type, this status code is 200. For the <code>Event</code> invocation type, this status code is 202. For the <code>DryRun</code> invocation type, the status code is 204.</p>"""
    function_error: NotRequired["capo_lambda.types.string.String"]
    """<p>If present, indicates that an error occurred during function execution. Details about the error are included in the response payload.</p>"""
    log_result: NotRequired["capo_lambda.types.string.String"]
    """<p>The last 4 KB of the execution log, which is base64-encoded.</p>"""
    payload: NotRequired["capo_lambda.types.blob.Blob"]
    """<p>The response from the function, or an error object.</p>"""
    executed_version: NotRequired["capo_lambda.types.version.Version"]
    """<p>The version of the function that executed. When you invoke a function with an alias, this indicates which version the alias resolved to.</p>"""
    durable_execution_arn: NotRequired[
        "capo_lambda.types.durable_execution_arn.DurableExecutionArn"
    ]
    """<p>The ARN of the durable execution that was started. This is returned when invoking a durable function and provides a unique identifier for tracking the execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvocationResponse) -> dict:
    out: dict = {}
    if "payload" in value:
        import capo_lambda.types.blob

        out["Payload"] = capo_lambda.types.blob.serialize_json(value["payload"])
    return out


def deserialize_json(data: dict) -> InvocationResponse:
    out: InvocationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Payload") is not None:
        import capo_lambda.types.blob

        out["payload"] = capo_lambda.types.blob.deserialize_json(data["Payload"])
    return out


def redact_sensitive(value: InvocationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        out["payload"] = "*** Sensitive Data Redacted ***"
    return out
