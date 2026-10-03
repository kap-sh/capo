"""Generated from Smithy shape ``com.amazonaws.mediapackage#HlsPackage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage.types.__boolean
    import capo_mediapackage.types.__integer
    import capo_mediapackage.types.ad_markers
    import capo_mediapackage.types.ad_triggers
    import capo_mediapackage.types.ads_on_delivery_restrictions
    import capo_mediapackage.types.hls_encryption
    import capo_mediapackage.types.playlist_type
    import capo_mediapackage.types.stream_selection


class HlsPackage(TypedDict, closed=True):
    ad_markers: NotRequired["capo_mediapackage.types.ad_markers.AdMarkers"]
    """This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source. "DATERANGE" inserts EXT-X-DATERANGE tags to signal ad and program transition events in HLS and CMAF manifests. For this option, you must set a programDateTimeIntervalSeconds value that is greater than 0."""
    ad_triggers: NotRequired["capo_mediapackage.types.ad_triggers.AdTriggers"]
    ads_on_delivery_restrictions: NotRequired[
        "capo_mediapackage.types.ads_on_delivery_restrictions.AdsOnDeliveryRestrictions"
    ]
    encryption: NotRequired["capo_mediapackage.types.hls_encryption.HlsEncryption"]
    include_dvb_subtitles: NotRequired["capo_mediapackage.types.__boolean.__boolean"]
    """When enabled, MediaPackage passes through digital video broadcasting (DVB) subtitles into the output."""
    include_iframe_only_stream: NotRequired[
        "capo_mediapackage.types.__boolean.__boolean"
    ]
    """When enabled, an I-Frame only stream will be included in the output."""
    playlist_type: NotRequired["capo_mediapackage.types.playlist_type.PlaylistType"]
    """The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD" is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist."""
    playlist_window_seconds: NotRequired["capo_mediapackage.types.__integer.__integer"]
    """Time window (in seconds) contained in each parent manifest."""
    program_date_time_interval_seconds: NotRequired[
        "capo_mediapackage.types.__integer.__integer"
    ]
    """The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output."""
    segment_duration_seconds: NotRequired["capo_mediapackage.types.__integer.__integer"]
    """Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration."""
    stream_selection: NotRequired[
        "capo_mediapackage.types.stream_selection.StreamSelection"
    ]
    use_audio_rendition_group: NotRequired[
        "capo_mediapackage.types.__boolean.__boolean"
    ]
    """When enabled, audio streams will be placed in rendition groups in the output."""


# --- restJson1 ser/de ---
def serialize_json(value: HlsPackage) -> dict:
    out: dict = {}
    if "ad_markers" in value:
        import capo_mediapackage.types.ad_markers

        out["adMarkers"] = capo_mediapackage.types.ad_markers.serialize_json(
            value["ad_markers"]
        )
    if "ad_triggers" in value:
        import capo_mediapackage.types.ad_triggers

        out["adTriggers"] = capo_mediapackage.types.ad_triggers.serialize_json(
            value["ad_triggers"]
        )
    if "ads_on_delivery_restrictions" in value:
        import capo_mediapackage.types.ads_on_delivery_restrictions

        out["adsOnDeliveryRestrictions"] = (
            capo_mediapackage.types.ads_on_delivery_restrictions.serialize_json(
                value["ads_on_delivery_restrictions"]
            )
        )
    if "encryption" in value:
        import capo_mediapackage.types.hls_encryption

        out["encryption"] = capo_mediapackage.types.hls_encryption.serialize_json(
            value["encryption"]
        )
    if "include_dvb_subtitles" in value:
        out["includeDvbSubtitles"] = value["include_dvb_subtitles"]
    if "include_iframe_only_stream" in value:
        out["includeIframeOnlyStream"] = value["include_iframe_only_stream"]
    if "playlist_type" in value:
        import capo_mediapackage.types.playlist_type

        out["playlistType"] = capo_mediapackage.types.playlist_type.serialize_json(
            value["playlist_type"]
        )
    if "playlist_window_seconds" in value:
        out["playlistWindowSeconds"] = value["playlist_window_seconds"]
    if "program_date_time_interval_seconds" in value:
        out["programDateTimeIntervalSeconds"] = value[
            "program_date_time_interval_seconds"
        ]
    if "segment_duration_seconds" in value:
        out["segmentDurationSeconds"] = value["segment_duration_seconds"]
    if "stream_selection" in value:
        import capo_mediapackage.types.stream_selection

        out["streamSelection"] = (
            capo_mediapackage.types.stream_selection.serialize_json(
                value["stream_selection"]
            )
        )
    if "use_audio_rendition_group" in value:
        out["useAudioRenditionGroup"] = value["use_audio_rendition_group"]
    return out


def deserialize_json(data: dict) -> HlsPackage:
    out: HlsPackage = {}  # type: ignore[typeddict-item]
    if data.get("adMarkers") is not None:
        import capo_mediapackage.types.ad_markers

        out["ad_markers"] = capo_mediapackage.types.ad_markers.deserialize_json(
            data["adMarkers"]
        )
    if data.get("adTriggers") is not None:
        import capo_mediapackage.types.ad_triggers

        out["ad_triggers"] = capo_mediapackage.types.ad_triggers.deserialize_json(
            data["adTriggers"]
        )
    if data.get("adsOnDeliveryRestrictions") is not None:
        import capo_mediapackage.types.ads_on_delivery_restrictions

        out["ads_on_delivery_restrictions"] = (
            capo_mediapackage.types.ads_on_delivery_restrictions.deserialize_json(
                data["adsOnDeliveryRestrictions"]
            )
        )
    if data.get("encryption") is not None:
        import capo_mediapackage.types.hls_encryption

        out["encryption"] = capo_mediapackage.types.hls_encryption.deserialize_json(
            data["encryption"]
        )
    if data.get("includeDvbSubtitles") is not None:
        out["include_dvb_subtitles"] = data["includeDvbSubtitles"]
    if data.get("includeIframeOnlyStream") is not None:
        out["include_iframe_only_stream"] = data["includeIframeOnlyStream"]
    if data.get("playlistType") is not None:
        import capo_mediapackage.types.playlist_type

        out["playlist_type"] = capo_mediapackage.types.playlist_type.deserialize_json(
            data["playlistType"]
        )
    if data.get("playlistWindowSeconds") is not None:
        out["playlist_window_seconds"] = data["playlistWindowSeconds"]
    if data.get("programDateTimeIntervalSeconds") is not None:
        out["program_date_time_interval_seconds"] = data[
            "programDateTimeIntervalSeconds"
        ]
    if data.get("segmentDurationSeconds") is not None:
        out["segment_duration_seconds"] = data["segmentDurationSeconds"]
    if data.get("streamSelection") is not None:
        import capo_mediapackage.types.stream_selection

        out["stream_selection"] = (
            capo_mediapackage.types.stream_selection.deserialize_json(
                data["streamSelection"]
            )
        )
    if data.get("useAudioRenditionGroup") is not None:
        out["use_audio_rendition_group"] = data["useAudioRenditionGroup"]
    return out
