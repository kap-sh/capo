"""Generated from Smithy shape ``com.amazonaws.lambda#InvokeWithResponseStreamResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.integer
    import capo_lambda.types.invoke_with_response_stream_response_event
    import capo_lambda.types.string
    import capo_lambda.types.version


class InvokeWithResponseStreamResponse(TypedDict, closed=True):
    status_code: "capo_lambda.types.integer.Integer"
    """<p>For a successful request, the HTTP status code is in the 200 range. For the <code>RequestResponse</code> invocation type, this status code is 200. For the <code>DryRun</code> invocation type, this status code is 204.</p>"""
    executed_version: NotRequired["capo_lambda.types.version.Version"]
    """<p>The version of the function that executed. When you invoke a function with an alias, this indicates which version the alias resolved to.</p>"""
    event_stream: NotRequired[
        "capo_lambda.types.invoke_with_response_stream_response_event.InvokeWithResponseStreamResponseEvent"
    ]
    """<p>The stream of response payloads.</p>"""
    response_stream_content_type: NotRequired["capo_lambda.types.string.String"]
    """<p>The type of data the stream is returning.</p>"""


def redact_sensitive(value: InvokeWithResponseStreamResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "event_stream" in value:
        out["event_stream"] = "*** Streaming Data Redacted ***"
    return out
