"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#InvokeEndpointWithBidirectionalStreamOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_runtime_http2.types.response_stream_event


class InvokeEndpointWithBidirectionalStreamOutput(TypedDict, closed=True):
    body: "capo_sagemaker_runtime_http2.types.response_stream_event.ResponseStreamEvent"
    """<p>The response payload stream.</p>"""
    invoked_production_variant: NotRequired["str"]
    """<p>The invoked production variant.</p>"""


def redact_sensitive(
    value: InvokeEndpointWithBidirectionalStreamOutput,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "body" in value:
        out["body"] = "*** Streaming Data Redacted ***"
    return out
