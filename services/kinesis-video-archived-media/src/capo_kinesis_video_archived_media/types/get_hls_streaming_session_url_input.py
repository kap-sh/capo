"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#GetHLSStreamingSessionURLInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video_archived_media.types.container_format
    import capo_kinesis_video_archived_media.types.expires
    import capo_kinesis_video_archived_media.types.hls_discontinuity_mode
    import capo_kinesis_video_archived_media.types.hls_display_fragment_timestamp
    import capo_kinesis_video_archived_media.types.hls_fragment_selector
    import capo_kinesis_video_archived_media.types.hls_max_results
    import capo_kinesis_video_archived_media.types.hls_playback_mode
    import capo_kinesis_video_archived_media.types.resource_arn
    import capo_kinesis_video_archived_media.types.stream_name


class GetHLSStreamingSessionURLInput(TypedDict, closed=True):
    stream_name: NotRequired[
        "capo_kinesis_video_archived_media.types.stream_name.StreamName"
    ]
    """<p>The name of the stream for which to retrieve the HLS master playlist URL.</p> <p>You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>"""
    stream_arn: NotRequired[
        "capo_kinesis_video_archived_media.types.resource_arn.ResourceARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the stream for which to retrieve the HLS master playlist URL.</p> <p>You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>"""
    playback_mode: NotRequired[
        "capo_kinesis_video_archived_media.types.hls_playback_mode.HLSPlaybackMode"
    ]
    """<p>Whether to retrieve live, live replay, or archived, on-demand data.</p> <p>Features of the three types of sessions include the following:</p> <ul> <li> <p> <b> <code>LIVE</code> </b>: For sessions of this type, the HLS media playlist is continually updated with the latest fragments as they become available. We recommend that the media player retrieve a new playlist on a one-second interval. When this type of session is played in a media player, the user interface typically displays a "live" notification, with no scrubber control for choosing the position in the playback window to display.</p> <note> <p>In <code>LIVE</code> mode, the newest available fragments are included in an HLS media playlist, even if there is a gap between fragments (that is, if a fragment is missing). A gap like this might cause a media player to halt or cause a jump in playback. In this mode, fragments are not added to the HLS media playlist if they are older than the newest fragment in the playlist. If the missing fragment becomes available after a subsequent fragment is added to the playlist, the older fragment is not added, and the gap is not filled.</p> </note> </li> <li> <p> <b> <code>LIVE_REPLAY</code> </b>: For sessions of this type, the HLS media playlist is updated similarly to how it is updated for <code>LIVE</code> mode except that it starts by including fragments from a given start time. Instead of fragments being added as they are ingested, fragments are added as the duration of the next fragment elapses. For example, if the fragments in the session are two seconds long, then a new fragment is added to the media playlist every two seconds. This mode is useful to be able to start playback from when an event is detected and continue live streaming media that has not yet been ingested as of the time of the session creation. This mode is also useful to stream previously archived media without being limited by the 1,000 fragment limit in the <code>ON_DEMAND</code> mode. </p> </li> <li> <p> <b> <code>ON_DEMAND</code> </b>: For sessions of this type, the HLS media playlist contains all the fragments for the session, up to the number that is specified in <code>MaxMediaPlaylistFragmentResults</code>. The playlist must be retrieved only once for each session. When this type of session is played in a media player, the user interface typically displays a scrubber control for choosing the position in the playback window to display.</p> </li> </ul> <p>In all playback modes, if <code>FragmentSelectorType</code> is <code>PRODUCER_TIMESTAMP</code>, and if there are multiple fragments with the same start timestamp, the fragment that has the largest fragment number (that is, the newest fragment) is included in the HLS media playlist. The other fragments are not included. Fragments that have different timestamps but have overlapping durations are still included in the HLS media playlist. This can lead to unexpected behavior in the media player.</p> <p>The default is <code>LIVE</code>.</p>"""
    hls_fragment_selector: NotRequired[
        "capo_kinesis_video_archived_media.types.hls_fragment_selector.HLSFragmentSelector"
    ]
    """<p>The time range of the requested fragment and the source of the timestamps.</p> <p>This parameter is required if <code>PlaybackMode</code> is <code>ON_DEMAND</code> or <code>LIVE_REPLAY</code>. This parameter is optional if PlaybackMode is<code></code> <code>LIVE</code>. If <code>PlaybackMode</code> is <code>LIVE</code>, the <code>FragmentSelectorType</code> can be set, but the <code>TimestampRange</code> should not be set. If <code>PlaybackMode</code> is <code>ON_DEMAND</code> or <code>LIVE_REPLAY</code>, both <code>FragmentSelectorType</code> and <code>TimestampRange</code> must be set.</p>"""
    container_format: NotRequired[
        "capo_kinesis_video_archived_media.types.container_format.ContainerFormat"
    ]
    """<p>Specifies which format should be used for packaging the media. Specifying the <code>FRAGMENTED_MP4</code> container format packages the media into MP4 fragments (fMP4 or CMAF). This is the recommended packaging because there is minimal packaging overhead. The other container format option is <code>MPEG_TS</code>. HLS has supported MPEG TS chunks since it was released and is sometimes the only supported packaging on older HLS players. MPEG TS typically has a 5-25 percent packaging overhead. This means MPEG TS typically requires 5-25 percent more bandwidth and cost than fMP4.</p> <p>The default is <code>FRAGMENTED_MP4</code>.</p>"""
    discontinuity_mode: NotRequired[
        "capo_kinesis_video_archived_media.types.hls_discontinuity_mode.HLSDiscontinuityMode"
    ]
    """<p>Specifies when flags marking discontinuities between fragments are added to the media playlists.</p> <p>Media players typically build a timeline of media content to play, based on the timestamps of each fragment. This means that if there is any overlap or gap between fragments (as is typical if <a>HLSFragmentSelector</a> is set to <code>SERVER_TIMESTAMP</code>), the media player timeline will also have small gaps between fragments in some places, and will overwrite frames in other places. Gaps in the media player timeline can cause playback to stall and overlaps can cause playback to be jittery. When there are discontinuity flags between fragments, the media player is expected to reset the timeline, resulting in the next fragment being played immediately after the previous fragment. </p> <p>The following modes are supported:</p> <ul> <li> <p> <code>ALWAYS</code>: a discontinuity marker is placed between every fragment in the HLS media playlist. It is recommended to use a value of <code>ALWAYS</code> if the fragment timestamps are not accurate.</p> </li> <li> <p> <code>NEVER</code>: no discontinuity markers are placed anywhere. It is recommended to use a value of <code>NEVER</code> to ensure the media player timeline most accurately maps to the producer timestamps. </p> </li> <li> <p> <code>ON_DISCONTINUITY</code>: a discontinuity marker is placed between fragments that have a gap or overlap of more than 50 milliseconds. For most playback scenarios, it is recommended to use a value of <code>ON_DISCONTINUITY</code> so that the media player timeline is only reset when there is a significant issue with the media timeline (e.g. a missing fragment).</p> </li> </ul> <p>The default is <code>ALWAYS</code> when <a>HLSFragmentSelector</a> is set to <code>SERVER_TIMESTAMP</code>, and <code>NEVER</code> when it is set to <code>PRODUCER_TIMESTAMP</code>.</p>"""
    display_fragment_timestamp: NotRequired[
        "capo_kinesis_video_archived_media.types.hls_display_fragment_timestamp.HLSDisplayFragmentTimestamp"
    ]
    """<p>Specifies when the fragment start timestamps should be included in the HLS media playlist. Typically, media players report the playhead position as a time relative to the start of the first fragment in the playback session. However, when the start timestamps are included in the HLS media playlist, some media players might report the current playhead as an absolute time based on the fragment timestamps. This can be useful for creating a playback experience that shows viewers the wall-clock time of the media.</p> <p>The default is <code>NEVER</code>. When <a>HLSFragmentSelector</a> is <code>SERVER_TIMESTAMP</code>, the timestamps will be the server start timestamps. Similarly, when <a>HLSFragmentSelector</a> is <code>PRODUCER_TIMESTAMP</code>, the timestamps will be the producer start timestamps. </p>"""
    expires: NotRequired["capo_kinesis_video_archived_media.types.expires.Expires"]
    """<p>The time in seconds until the requested session expires. This value can be between 300 (5 minutes) and 43200 (12 hours).</p> <p>When a session expires, no new calls to <code>GetHLSMasterPlaylist</code>, <code>GetHLSMediaPlaylist</code>, <code>GetMP4InitFragment</code>, <code>GetMP4MediaFragment</code>, or <code>GetTSFragment</code> can be made for that session.</p> <p>The default is 300 (5 minutes).</p>"""
    max_media_playlist_fragment_results: NotRequired[
        "capo_kinesis_video_archived_media.types.hls_max_results.HLSMaxResults"
    ]
    """<p>The maximum number of fragments that are returned in the HLS media playlists.</p> <p>When the <code>PlaybackMode</code> is <code>LIVE</code>, the most recent fragments are returned up to this value. When the <code>PlaybackMode</code> is <code>ON_DEMAND</code>, the oldest fragments are returned, up to this maximum number.</p> <p>When there are a higher number of fragments available in a live HLS media playlist, video players often buffer content before starting playback. Increasing the buffer size increases the playback latency, but it decreases the likelihood that rebuffering will occur during playback. We recommend that a live HLS media playlist have a minimum of 3 fragments and a maximum of 10 fragments.</p> <p>The default is 5 fragments if <code>PlaybackMode</code> is <code>LIVE</code> or <code>LIVE_REPLAY</code>, and 1,000 if <code>PlaybackMode</code> is <code>ON_DEMAND</code>. </p> <p>The maximum value of 5,000 fragments corresponds to more than 80 minutes of video on streams with 1-second fragments, and more than 13 hours of video on streams with 10-second fragments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetHLSStreamingSessionURLInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "playback_mode" in value:
        import capo_kinesis_video_archived_media.types.hls_playback_mode

        out["PlaybackMode"] = (
            capo_kinesis_video_archived_media.types.hls_playback_mode.serialize_json(
                value["playback_mode"]
            )
        )
    if "hls_fragment_selector" in value:
        import capo_kinesis_video_archived_media.types.hls_fragment_selector

        out["HLSFragmentSelector"] = (
            capo_kinesis_video_archived_media.types.hls_fragment_selector.serialize_json(
                value["hls_fragment_selector"]
            )
        )
    if "container_format" in value:
        import capo_kinesis_video_archived_media.types.container_format

        out["ContainerFormat"] = (
            capo_kinesis_video_archived_media.types.container_format.serialize_json(
                value["container_format"]
            )
        )
    if "discontinuity_mode" in value:
        import capo_kinesis_video_archived_media.types.hls_discontinuity_mode

        out["DiscontinuityMode"] = (
            capo_kinesis_video_archived_media.types.hls_discontinuity_mode.serialize_json(
                value["discontinuity_mode"]
            )
        )
    if "display_fragment_timestamp" in value:
        import capo_kinesis_video_archived_media.types.hls_display_fragment_timestamp

        out["DisplayFragmentTimestamp"] = (
            capo_kinesis_video_archived_media.types.hls_display_fragment_timestamp.serialize_json(
                value["display_fragment_timestamp"]
            )
        )
    if "expires" in value:
        out["Expires"] = value["expires"]
    if "max_media_playlist_fragment_results" in value:
        out["MaxMediaPlaylistFragmentResults"] = value[
            "max_media_playlist_fragment_results"
        ]
    return out


def deserialize_json(data: dict) -> GetHLSStreamingSessionURLInput:
    out: GetHLSStreamingSessionURLInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("PlaybackMode") is not None:
        import capo_kinesis_video_archived_media.types.hls_playback_mode

        out["playback_mode"] = (
            capo_kinesis_video_archived_media.types.hls_playback_mode.deserialize_json(
                data["PlaybackMode"]
            )
        )
    if data.get("HLSFragmentSelector") is not None:
        import capo_kinesis_video_archived_media.types.hls_fragment_selector

        out["hls_fragment_selector"] = (
            capo_kinesis_video_archived_media.types.hls_fragment_selector.deserialize_json(
                data["HLSFragmentSelector"]
            )
        )
    if data.get("ContainerFormat") is not None:
        import capo_kinesis_video_archived_media.types.container_format

        out["container_format"] = (
            capo_kinesis_video_archived_media.types.container_format.deserialize_json(
                data["ContainerFormat"]
            )
        )
    if data.get("DiscontinuityMode") is not None:
        import capo_kinesis_video_archived_media.types.hls_discontinuity_mode

        out["discontinuity_mode"] = (
            capo_kinesis_video_archived_media.types.hls_discontinuity_mode.deserialize_json(
                data["DiscontinuityMode"]
            )
        )
    if data.get("DisplayFragmentTimestamp") is not None:
        import capo_kinesis_video_archived_media.types.hls_display_fragment_timestamp

        out["display_fragment_timestamp"] = (
            capo_kinesis_video_archived_media.types.hls_display_fragment_timestamp.deserialize_json(
                data["DisplayFragmentTimestamp"]
            )
        )
    if data.get("Expires") is not None:
        out["expires"] = data["Expires"]
    if data.get("MaxMediaPlaylistFragmentResults") is not None:
        out["max_media_playlist_fragment_results"] = data[
            "MaxMediaPlaylistFragmentResults"
        ]
    return out
