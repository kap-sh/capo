"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DescribeFlowSourceMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mediaconnect.types.__list_of_message_detail
    import capo_mediaconnect.types.ndi_source_metadata_info
    import capo_mediaconnect.types.rtmp_source_metadata_info
    import capo_mediaconnect.types.transport_media_info


class DescribeFlowSourceMetadataResponse(TypedDict, closed=True):
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that DescribeFlowSourceMetadata was performed on.</p>"""
    messages: NotRequired[
        "capo_mediaconnect.types.__list_of_message_detail.__listOfMessageDetail"
    ]
    """<p> Provides a status code and message regarding issues found with the flow source metadata.</p>"""
    timestamp: NotRequired["datetime.datetime"]
    """<p> The timestamp of the most recent change in metadata for this flow’s source.</p>"""
    transport_media_info: NotRequired[
        "capo_mediaconnect.types.transport_media_info.TransportMediaInfo"
    ]
    """<p> Information about the flow's transport media. </p>"""
    ndi_info: NotRequired[
        "capo_mediaconnect.types.ndi_source_metadata_info.NdiSourceMetadataInfo"
    ]
    """<p> The NDI® specific information about the flow's source. This includes the current active NDI sender, a list of all discovered NDI senders, the associated media streams for the active NDI sender, and any relevant status messages. </p>"""
    rtmp_info: NotRequired[
        "capo_mediaconnect.types.rtmp_source_metadata_info.RtmpSourceMetadataInfo"
    ]
    """<p>The RTMP (Real-Time Messaging Protocol) specific information about the flow's source. This includes the application name, the stream name, and the associated audio and video streams.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFlowSourceMetadataResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "messages" in value:
        import capo_mediaconnect.types.__list_of_message_detail

        out["messages"] = (
            capo_mediaconnect.types.__list_of_message_detail.serialize_json(
                value["messages"]
            )
        )
    if "timestamp" in value:
        import capo_mediaconnect._protocol.serialize

        out["timestamp"] = capo_mediaconnect._protocol.serialize.fmt_date_time(
            value["timestamp"]
        )
    if "transport_media_info" in value:
        import capo_mediaconnect.types.transport_media_info

        out["transportMediaInfo"] = (
            capo_mediaconnect.types.transport_media_info.serialize_json(
                value["transport_media_info"]
            )
        )
    if "ndi_info" in value:
        import capo_mediaconnect.types.ndi_source_metadata_info

        out["ndiInfo"] = (
            capo_mediaconnect.types.ndi_source_metadata_info.serialize_json(
                value["ndi_info"]
            )
        )
    if "rtmp_info" in value:
        import capo_mediaconnect.types.rtmp_source_metadata_info

        out["rtmpInfo"] = (
            capo_mediaconnect.types.rtmp_source_metadata_info.serialize_json(
                value["rtmp_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeFlowSourceMetadataResponse:
    out: DescribeFlowSourceMetadataResponse = {}  # type: ignore[typeddict-item]
    if data.get("flowArn") is not None:
        out["flow_arn"] = data["flowArn"]
    if data.get("messages") is not None:
        import capo_mediaconnect.types.__list_of_message_detail

        out["messages"] = (
            capo_mediaconnect.types.__list_of_message_detail.deserialize_json(
                data["messages"]
            )
        )
    if data.get("timestamp") is not None:
        import datetime

        out["timestamp"] = datetime.datetime.fromisoformat(
            data["timestamp"].replace("Z", "+00:00")
        )
    if data.get("transportMediaInfo") is not None:
        import capo_mediaconnect.types.transport_media_info

        out["transport_media_info"] = (
            capo_mediaconnect.types.transport_media_info.deserialize_json(
                data["transportMediaInfo"]
            )
        )
    if data.get("ndiInfo") is not None:
        import capo_mediaconnect.types.ndi_source_metadata_info

        out["ndi_info"] = (
            capo_mediaconnect.types.ndi_source_metadata_info.deserialize_json(
                data["ndiInfo"]
            )
        )
    if data.get("rtmpInfo") is not None:
        import capo_mediaconnect.types.rtmp_source_metadata_info

        out["rtmp_info"] = (
            capo_mediaconnect.types.rtmp_source_metadata_info.deserialize_json(
                data["rtmpInfo"]
            )
        )
    return out
