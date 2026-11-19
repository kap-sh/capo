"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RtmpPushSourceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.rtmp_push_naming_type


class RtmpPushSourceSettings(TypedDict, closed=True):
    application_name: NotRequired["str"]
    """<p>The name of the RTMP application. Together with the stream name, the application name forms the RTMP URL path, in the pattern <code>rtmp://ingestAddress/applicationName/streamName</code>.</p>"""
    stream_name: NotRequired["str"]
    """<p>The name of the RTMP stream. The stream name forms the final segment of the RTMP URL path.</p>"""
    naming_type: NotRequired[
        "capo_mediaconnect.types.rtmp_push_naming_type.RtmpPushNamingType"
    ]
    """<p>The naming type that the source uses. With <code>AUTOMATIC</code> naming, MediaConnect generates the application and stream names.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RtmpPushSourceSettings) -> dict:
    out: dict = {}
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "stream_name" in value:
        out["streamName"] = value["stream_name"]
    if "naming_type" in value:
        import capo_mediaconnect.types.rtmp_push_naming_type

        out["namingType"] = (
            capo_mediaconnect.types.rtmp_push_naming_type.serialize_json(
                value["naming_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> RtmpPushSourceSettings:
    out: RtmpPushSourceSettings = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    if data.get("streamName") is not None:
        out["stream_name"] = data["streamName"]
    if data.get("namingType") is not None:
        import capo_mediaconnect.types.rtmp_push_naming_type

        out["naming_type"] = (
            capo_mediaconnect.types.rtmp_push_naming_type.deserialize_json(
                data["namingType"]
            )
        )
    return out
