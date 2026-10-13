"""Generated from Smithy shape ``com.amazonaws.omics#GetReferenceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.reference_streaming_blob


class GetReferenceResponse(TypedDict, closed=True):
    payload: "capo_omics.types.reference_streaming_blob.ReferenceStreamingBlob"
    """<p>The reference file payload.</p>"""


def redact_sensitive(value: GetReferenceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        out["payload"] = "*** Streaming Data Redacted ***"
    return out
