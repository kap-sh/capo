"""Generated from Smithy shape ``com.amazonaws.s3#GetObjectTorrentOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3.types.request_charged
    import capo_s3.types.streaming_blob


class GetObjectTorrentOutput(TypedDict, closed=True):
    body: "capo_s3.types.streaming_blob.StreamingBlob"
    """<p>A Bencoded dictionary as defined by the BitTorrent specification</p>"""
    request_charged: NotRequired["capo_s3.types.request_charged.RequestCharged"]


def redact_sensitive(value: GetObjectTorrentOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "body" in value:
        out["body"] = "*** Streaming Data Redacted ***"
    return out
