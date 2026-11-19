"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FailoverRouterInputIndexedStreamDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.rtmp_push_stream_details


class FailoverRouterInputIndexedStreamDetails(TypedDict, closed=True):
    source_index: "int"
    """<p>The index number (0 or 1) assigned to this source in the failover configuration.</p>"""
    source_ip_address: NotRequired["str"]
    """<p>The IP address of the source for this indexed stream.</p>"""
    rtmp_push: NotRequired[
        "capo_mediaconnect.types.rtmp_push_stream_details.RtmpPushStreamDetails"
    ]
    """<p>The RTMP stream details for this indexed stream, including the application and stream names.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailoverRouterInputIndexedStreamDetails) -> dict:
    out: dict = {}
    out["sourceIndex"] = value["source_index"]
    if "source_ip_address" in value:
        out["sourceIpAddress"] = value["source_ip_address"]
    if "rtmp_push" in value:
        import capo_mediaconnect.types.rtmp_push_stream_details

        out["rtmpPush"] = (
            capo_mediaconnect.types.rtmp_push_stream_details.serialize_json(
                value["rtmp_push"]
            )
        )
    return out


def deserialize_json(data: dict) -> FailoverRouterInputIndexedStreamDetails:
    out: FailoverRouterInputIndexedStreamDetails = {}  # type: ignore[typeddict-item]
    if data.get("sourceIndex") is not None:
        out["source_index"] = data["sourceIndex"]
    else:
        out["source_index"] = 0
    if data.get("sourceIpAddress") is not None:
        out["source_ip_address"] = data["sourceIpAddress"]
    if data.get("rtmpPush") is not None:
        import capo_mediaconnect.types.rtmp_push_stream_details

        out["rtmp_push"] = (
            capo_mediaconnect.types.rtmp_push_stream_details.deserialize_json(
                data["rtmpPush"]
            )
        )
    return out
