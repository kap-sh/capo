"""Generated from Smithy shape ``com.amazonaws.connect#ListRealtimeContactAnalysisSegmentsV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.large_next_token
    import capo_connect.types.real_time_contact_analysis_status
    import capo_connect.types.real_time_contact_analysis_supported_channel
    import capo_connect.types.realtime_contact_analysis_segments


class ListRealtimeContactAnalysisSegmentsV2Response(TypedDict, closed=True):
    channel: "capo_connect.types.real_time_contact_analysis_supported_channel.RealTimeContactAnalysisSupportedChannel"
    """<p>The channel of the contact. </p> <important> <p>Only <code>CHAT</code> is supported. This API does not support <code>VOICE</code>. If you attempt to use it for the VOICE channel, an <code>InvalidRequestException</code> error occurs.</p> </important>"""
    status: "capo_connect.types.real_time_contact_analysis_status.RealTimeContactAnalysisStatus"
    """<p>Status of real-time contact analysis.</p>"""
    segments: "capo_connect.types.realtime_contact_analysis_segments.RealtimeContactAnalysisSegments"
    """<p>An analyzed transcript or category.</p>"""
    next_token: NotRequired["capo_connect.types.large_next_token.LargeNextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRealtimeContactAnalysisSegmentsV2Response) -> dict:
    out: dict = {}
    import capo_connect.types.real_time_contact_analysis_supported_channel

    out["Channel"] = (
        capo_connect.types.real_time_contact_analysis_supported_channel.serialize_json(
            value["channel"]
        )
    )
    import capo_connect.types.real_time_contact_analysis_status

    out["Status"] = capo_connect.types.real_time_contact_analysis_status.serialize_json(
        value["status"]
    )
    import capo_connect.types.realtime_contact_analysis_segments

    out["Segments"] = (
        capo_connect.types.realtime_contact_analysis_segments.serialize_json(
            value["segments"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRealtimeContactAnalysisSegmentsV2Response:
    out: ListRealtimeContactAnalysisSegmentsV2Response = {}  # type: ignore[typeddict-item]
    if data.get("Channel") is not None:
        import capo_connect.types.real_time_contact_analysis_supported_channel

        out["channel"] = (
            capo_connect.types.real_time_contact_analysis_supported_channel.deserialize_json(
                data["Channel"]
            )
        )
    else:
        import typing

        out["channel"] = typing.cast(
            "capo_connect.types.real_time_contact_analysis_supported_channel.RealTimeContactAnalysisSupportedChannel",
            "",
        )
    if data.get("Status") is not None:
        import capo_connect.types.real_time_contact_analysis_status

        out["status"] = (
            capo_connect.types.real_time_contact_analysis_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_connect.types.real_time_contact_analysis_status.RealTimeContactAnalysisStatus",
            "",
        )
    if data.get("Segments") is not None:
        import capo_connect.types.realtime_contact_analysis_segments

        out["segments"] = (
            capo_connect.types.realtime_contact_analysis_segments.deserialize_json(
                data["Segments"]
            )
        )
    else:
        out["segments"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
