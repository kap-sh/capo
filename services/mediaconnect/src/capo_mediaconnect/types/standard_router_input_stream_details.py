"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StandardRouterInputStreamDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.rtmp_push_stream_details


class StandardRouterInputStreamDetails(TypedDict, closed=True):
    source_ip_address: NotRequired["str"]
    """<p>The source IP address for the standard router input stream.</p>"""
    rtmp_push: NotRequired[
        "capo_mediaconnect.types.rtmp_push_stream_details.RtmpPushStreamDetails"
    ]
    """<p>The RTMP stream details for the standard router input stream, including the application and stream names.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StandardRouterInputStreamDetails) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> StandardRouterInputStreamDetails:
    out: StandardRouterInputStreamDetails = {}  # type: ignore[typeddict-item]
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
