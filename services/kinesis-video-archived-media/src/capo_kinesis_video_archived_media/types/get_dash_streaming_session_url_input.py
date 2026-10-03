"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#GetDASHStreamingSessionURLInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video_archived_media.types.dash_display_fragment_number
    import capo_kinesis_video_archived_media.types.dash_display_fragment_timestamp
    import capo_kinesis_video_archived_media.types.dash_fragment_selector
    import capo_kinesis_video_archived_media.types.dash_max_results
    import capo_kinesis_video_archived_media.types.dash_playback_mode
    import capo_kinesis_video_archived_media.types.expires
    import capo_kinesis_video_archived_media.types.resource_arn
    import capo_kinesis_video_archived_media.types.stream_name


class GetDASHStreamingSessionURLInput(TypedDict, closed=True):
    stream_name: NotRequired[
        "capo_kinesis_video_archived_media.types.stream_name.StreamName"
    ]
    """<p>The name of the stream for which to retrieve the MPEG-DASH manifest URL.</p> <p>You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>"""
    stream_arn: NotRequired[
        "capo_kinesis_video_archived_media.types.resource_arn.ResourceARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the stream for which to retrieve the MPEG-DASH manifest URL.</p> <p>You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>"""
    playback_mode: NotRequired[
        "capo_kinesis_video_archived_media.types.dash_playback_mode.DASHPlaybackMode"
    ]
    """<p>Whether to retrieve live, live replay, or archived, on-demand data.</p> <p>Features of the three types of sessions include the following:</p> <ul> <li> <p> <b> <code>LIVE</code> </b>: For sessions of this type, the MPEG-DASH manifest is continually updated with the latest fragments as they become available. We recommend that the media player retrieve a new manifest on a one-second interval. When this type of session is played in a media player, the user interface typically displays a "live" notification, with no scrubber control for choosing the position in the playback window to display.</p> <note> <p>In <code>LIVE</code> mode, the newest available fragments are included in an MPEG-DASH manifest, even if there is a gap between fragments (that is, if a fragment is missing). A gap like this might cause a media player to halt or cause a jump in playback. In this mode, fragments are not added to the MPEG-DASH manifest if they are older than the newest fragment in the playlist. If the missing fragment becomes available after a subsequent fragment is added to the manifest, the older fragment is not added, and the gap is not filled.</p> </note> </li> <li> <p> <b> <code>LIVE_REPLAY</code> </b>: For sessions of this type, the MPEG-DASH manifest is updated similarly to how it is updated for <code>LIVE</code> mode except that it starts by including fragments from a given start time. Instead of fragments being added as they are ingested, fragments are added as the duration of the next fragment elapses. For example, if the fragments in the session are two seconds long, then a new fragment is added to the manifest every two seconds. This mode is useful to be able to start playback from when an event is detected and continue live streaming media that has not yet been ingested as of the time of the session creation. This mode is also useful to stream previously archived media without being limited by the 1,000 fragment limit in the <code>ON_DEMAND</code> mode. </p> </li> <li> <p> <b> <code>ON_DEMAND</code> </b>: For sessions of this type, the MPEG-DASH manifest contains all the fragments for the session, up to the number that is specified in <code>MaxManifestFragmentResults</code>. The manifest must be retrieved only once for each session. When this type of session is played in a media player, the user interface typically displays a scrubber control for choosing the position in the playback window to display.</p> </li> </ul> <p>In all playback modes, if <code>FragmentSelectorType</code> is <code>PRODUCER_TIMESTAMP</code>, and if there are multiple fragments with the same start timestamp, the fragment that has the larger fragment number (that is, the newer fragment) is included in the MPEG-DASH manifest. The other fragments are not included. Fragments that have different timestamps but have overlapping durations are still included in the MPEG-DASH manifest. This can lead to unexpected behavior in the media player.</p> <p>The default is <code>LIVE</code>.</p>"""
    display_fragment_timestamp: NotRequired[
        "capo_kinesis_video_archived_media.types.dash_display_fragment_timestamp.DASHDisplayFragmentTimestamp"
    ]
    """<p>Per the MPEG-DASH specification, the wall-clock time of fragments in the manifest file can be derived using attributes in the manifest itself. However, typically, MPEG-DASH compatible media players do not properly handle gaps in the media timeline. Kinesis Video Streams adjusts the media timeline in the manifest file to enable playback of media with discontinuities. Therefore, the wall-clock time derived from the manifest file may be inaccurate. If DisplayFragmentTimestamp is set to <code>ALWAYS</code>, the accurate fragment timestamp is added to each S element in the manifest file with the attribute name “kvs:ts”. A custom MPEG-DASH media player is necessary to leverage this custom attribute.</p> <p>The default value is <code>NEVER</code>. When <a>DASHFragmentSelector</a> is <code>SERVER_TIMESTAMP</code>, the timestamps will be the server start timestamps. Similarly, when <a>DASHFragmentSelector</a> is <code>PRODUCER_TIMESTAMP</code>, the timestamps will be the producer start timestamps. </p>"""
    display_fragment_number: NotRequired[
        "capo_kinesis_video_archived_media.types.dash_display_fragment_number.DASHDisplayFragmentNumber"
    ]
    """<p>Fragments are identified in the manifest file based on their sequence number in the session. If DisplayFragmentNumber is set to <code>ALWAYS</code>, the Kinesis Video Streams fragment number is added to each S element in the manifest file with the attribute name “kvs:fn”. These fragment numbers can be used for logging or for use with other APIs (e.g. <code>GetMedia</code> and <code>GetMediaForFragmentList</code>). A custom MPEG-DASH media player is necessary to leverage these this custom attribute.</p> <p>The default value is <code>NEVER</code>.</p>"""
    dash_fragment_selector: NotRequired[
        "capo_kinesis_video_archived_media.types.dash_fragment_selector.DASHFragmentSelector"
    ]
    """<p>The time range of the requested fragment and the source of the timestamps.</p> <p>This parameter is required if <code>PlaybackMode</code> is <code>ON_DEMAND</code> or <code>LIVE_REPLAY</code>. This parameter is optional if PlaybackMode is<code></code> <code>LIVE</code>. If <code>PlaybackMode</code> is <code>LIVE</code>, the <code>FragmentSelectorType</code> can be set, but the <code>TimestampRange</code> should not be set. If <code>PlaybackMode</code> is <code>ON_DEMAND</code> or <code>LIVE_REPLAY</code>, both <code>FragmentSelectorType</code> and <code>TimestampRange</code> must be set.</p>"""
    expires: NotRequired["capo_kinesis_video_archived_media.types.expires.Expires"]
    """<p>The time in seconds until the requested session expires. This value can be between 300 (5 minutes) and 43200 (12 hours).</p> <p>When a session expires, no new calls to <code>GetDashManifest</code>, <code>GetMP4InitFragment</code>, or <code>GetMP4MediaFragment</code> can be made for that session.</p> <p>The default is 300 (5 minutes).</p>"""
    max_manifest_fragment_results: NotRequired[
        "capo_kinesis_video_archived_media.types.dash_max_results.DASHMaxResults"
    ]
    """<p>The maximum number of fragments that are returned in the MPEG-DASH manifest.</p> <p>When the <code>PlaybackMode</code> is <code>LIVE</code>, the most recent fragments are returned up to this value. When the <code>PlaybackMode</code> is <code>ON_DEMAND</code>, the oldest fragments are returned, up to this maximum number.</p> <p>When there are a higher number of fragments available in a live MPEG-DASH manifest, video players often buffer content before starting playback. Increasing the buffer size increases the playback latency, but it decreases the likelihood that rebuffering will occur during playback. We recommend that a live MPEG-DASH manifest have a minimum of 3 fragments and a maximum of 10 fragments.</p> <p>The default is 5 fragments if <code>PlaybackMode</code> is <code>LIVE</code> or <code>LIVE_REPLAY</code>, and 1,000 if <code>PlaybackMode</code> is <code>ON_DEMAND</code>. </p> <p>The maximum value of 1,000 fragments corresponds to more than 16 minutes of video on streams with 1-second fragments, and more than 2 1/2 hours of video on streams with 10-second fragments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDASHStreamingSessionURLInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "playback_mode" in value:
        import capo_kinesis_video_archived_media.types.dash_playback_mode

        out["PlaybackMode"] = (
            capo_kinesis_video_archived_media.types.dash_playback_mode.serialize_json(
                value["playback_mode"]
            )
        )
    if "display_fragment_timestamp" in value:
        import capo_kinesis_video_archived_media.types.dash_display_fragment_timestamp

        out["DisplayFragmentTimestamp"] = (
            capo_kinesis_video_archived_media.types.dash_display_fragment_timestamp.serialize_json(
                value["display_fragment_timestamp"]
            )
        )
    if "display_fragment_number" in value:
        import capo_kinesis_video_archived_media.types.dash_display_fragment_number

        out["DisplayFragmentNumber"] = (
            capo_kinesis_video_archived_media.types.dash_display_fragment_number.serialize_json(
                value["display_fragment_number"]
            )
        )
    if "dash_fragment_selector" in value:
        import capo_kinesis_video_archived_media.types.dash_fragment_selector

        out["DASHFragmentSelector"] = (
            capo_kinesis_video_archived_media.types.dash_fragment_selector.serialize_json(
                value["dash_fragment_selector"]
            )
        )
    if "expires" in value:
        out["Expires"] = value["expires"]
    if "max_manifest_fragment_results" in value:
        out["MaxManifestFragmentResults"] = value["max_manifest_fragment_results"]
    return out


def deserialize_json(data: dict) -> GetDASHStreamingSessionURLInput:
    out: GetDASHStreamingSessionURLInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("PlaybackMode") is not None:
        import capo_kinesis_video_archived_media.types.dash_playback_mode

        out["playback_mode"] = (
            capo_kinesis_video_archived_media.types.dash_playback_mode.deserialize_json(
                data["PlaybackMode"]
            )
        )
    if data.get("DisplayFragmentTimestamp") is not None:
        import capo_kinesis_video_archived_media.types.dash_display_fragment_timestamp

        out["display_fragment_timestamp"] = (
            capo_kinesis_video_archived_media.types.dash_display_fragment_timestamp.deserialize_json(
                data["DisplayFragmentTimestamp"]
            )
        )
    if data.get("DisplayFragmentNumber") is not None:
        import capo_kinesis_video_archived_media.types.dash_display_fragment_number

        out["display_fragment_number"] = (
            capo_kinesis_video_archived_media.types.dash_display_fragment_number.deserialize_json(
                data["DisplayFragmentNumber"]
            )
        )
    if data.get("DASHFragmentSelector") is not None:
        import capo_kinesis_video_archived_media.types.dash_fragment_selector

        out["dash_fragment_selector"] = (
            capo_kinesis_video_archived_media.types.dash_fragment_selector.deserialize_json(
                data["DASHFragmentSelector"]
            )
        )
    if data.get("Expires") is not None:
        out["expires"] = data["Expires"]
    if data.get("MaxManifestFragmentResults") is not None:
        out["max_manifest_fragment_results"] = data["MaxManifestFragmentResults"]
    return out
