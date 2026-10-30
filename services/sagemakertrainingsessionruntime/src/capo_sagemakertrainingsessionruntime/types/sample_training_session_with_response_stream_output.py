"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#SampleTrainingSessionWithResponseStreamOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.sample_response_stream


class SampleTrainingSessionWithResponseStreamOutput(TypedDict, closed=True):
    content_type: NotRequired["str"]
    """<p>The MIME type of the streaming inference result.</p>"""
    body: "capo_sagemakertrainingsessionruntime.types.sample_response_stream.SampleResponseStream"
    """<p>The streaming inference response from the model, delivered as a series of chunks.</p>"""


def redact_sensitive(
    value: SampleTrainingSessionWithResponseStreamOutput,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "body" in value:
        out["body"] = "*** Sensitive Data Redacted ***"
    return out
