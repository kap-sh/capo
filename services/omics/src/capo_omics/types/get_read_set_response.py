"""Generated from Smithy shape ``com.amazonaws.omics#GetReadSetResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.read_set_streaming_blob


class GetReadSetResponse(TypedDict, closed=True):
    payload: "capo_omics.types.read_set_streaming_blob.ReadSetStreamingBlob"
    """<p>The read set file payload.</p>"""


def redact_sensitive(value: GetReadSetResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        out["payload"] = "*** Streaming Data Redacted ***"
    return out
