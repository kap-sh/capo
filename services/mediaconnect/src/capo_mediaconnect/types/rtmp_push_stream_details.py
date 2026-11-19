"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RtmpPushStreamDetails``."""

from typing_extensions import TypedDict


class RtmpPushStreamDetails(TypedDict, closed=True):
    application_name: "str"
    """<p>The name of the RTMP application.</p>"""
    stream_name: "str"
    """<p>The name of the RTMP stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RtmpPushStreamDetails) -> dict:
    out: dict = {}
    out["applicationName"] = value["application_name"]
    out["streamName"] = value["stream_name"]
    return out


def deserialize_json(data: dict) -> RtmpPushStreamDetails:
    out: RtmpPushStreamDetails = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    else:
        out["application_name"] = ""
    if data.get("streamName") is not None:
        out["stream_name"] = data["streamName"]
    else:
        out["stream_name"] = ""
    return out
