"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ManualRtmpPushNamingConfiguration``."""

from typing_extensions import TypedDict


class ManualRtmpPushNamingConfiguration(TypedDict, closed=True):
    application_name: "str"
    """<p>The name of the RTMP application. Together with the stream name, the application name forms the RTMP URL path, in the pattern <code>rtmp://ingestAddress/applicationName/streamName</code>.</p>"""
    stream_name: "str"
    """<p>The name of the RTMP stream. The stream name forms the final segment of the RTMP URL path.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManualRtmpPushNamingConfiguration) -> dict:
    out: dict = {}
    out["applicationName"] = value["application_name"]
    out["streamName"] = value["stream_name"]
    return out


def deserialize_json(data: dict) -> ManualRtmpPushNamingConfiguration:
    out: ManualRtmpPushNamingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    else:
        out["application_name"] = ""
    if data.get("streamName") is not None:
        out["stream_name"] = data["streamName"]
    else:
        out["stream_name"] = ""
    return out
