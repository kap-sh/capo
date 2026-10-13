"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#InvokeEndpointWithBidirectionalStreamInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_runtime_http2.types.request_stream_event


class InvokeEndpointWithBidirectionalStreamInput(TypedDict, closed=True):
    endpoint_name: "str"
    """<p>The name of the endpoint to invoke.</p>"""
    body: "capo_sagemaker_runtime_http2.types.request_stream_event.RequestStreamEvent"
    """<p>The request payload stream.</p>"""
    target_variant: NotRequired["str"]
    """<p>Target variant for the request.</p>"""
    model_invocation_path: NotRequired["str"]
    """<p>Model invocation path.</p>"""
    model_query_string: NotRequired["str"]
    """<p>Model query string.</p>"""


def redact_sensitive(
    value: InvokeEndpointWithBidirectionalStreamInput,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "body" in value:
        out["body"] = "*** Streaming Data Redacted ***"
    return out
