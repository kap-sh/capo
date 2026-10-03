"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#HlsManifest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage_vod.types.__boolean
    import capo_mediapackage_vod.types.__integer
    import capo_mediapackage_vod.types.__string
    import capo_mediapackage_vod.types.ad_markers
    import capo_mediapackage_vod.types.stream_selection


class HlsManifest(TypedDict, closed=True):
    ad_markers: NotRequired["capo_mediapackage_vod.types.ad_markers.AdMarkers"]
    """This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source."""
    include_iframe_only_stream: NotRequired[
        "capo_mediapackage_vod.types.__boolean.__boolean"
    ]
    """When enabled, an I-Frame only stream will be included in the output."""
    manifest_name: NotRequired["capo_mediapackage_vod.types.__string.__string"]
    """An optional string to include in the name of the manifest."""
    program_date_time_interval_seconds: NotRequired[
        "capo_mediapackage_vod.types.__integer.__integer"
    ]
    """The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output."""
    repeat_ext_x_key: NotRequired["capo_mediapackage_vod.types.__boolean.__boolean"]
    """When enabled, the EXT-X-KEY tag will be repeated in output manifests."""
    stream_selection: NotRequired[
        "capo_mediapackage_vod.types.stream_selection.StreamSelection"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: HlsManifest) -> dict:
    out: dict = {}
    if "ad_markers" in value:
        import capo_mediapackage_vod.types.ad_markers

        out["adMarkers"] = capo_mediapackage_vod.types.ad_markers.serialize_json(
            value["ad_markers"]
        )
    if "include_iframe_only_stream" in value:
        out["includeIframeOnlyStream"] = value["include_iframe_only_stream"]
    if "manifest_name" in value:
        out["manifestName"] = value["manifest_name"]
    if "program_date_time_interval_seconds" in value:
        out["programDateTimeIntervalSeconds"] = value[
            "program_date_time_interval_seconds"
        ]
    if "repeat_ext_x_key" in value:
        out["repeatExtXKey"] = value["repeat_ext_x_key"]
    if "stream_selection" in value:
        import capo_mediapackage_vod.types.stream_selection

        out["streamSelection"] = (
            capo_mediapackage_vod.types.stream_selection.serialize_json(
                value["stream_selection"]
            )
        )
    return out


def deserialize_json(data: dict) -> HlsManifest:
    out: HlsManifest = {}  # type: ignore[typeddict-item]
    if data.get("adMarkers") is not None:
        import capo_mediapackage_vod.types.ad_markers

        out["ad_markers"] = capo_mediapackage_vod.types.ad_markers.deserialize_json(
            data["adMarkers"]
        )
    if data.get("includeIframeOnlyStream") is not None:
        out["include_iframe_only_stream"] = data["includeIframeOnlyStream"]
    if data.get("manifestName") is not None:
        out["manifest_name"] = data["manifestName"]
    if data.get("programDateTimeIntervalSeconds") is not None:
        out["program_date_time_interval_seconds"] = data[
            "programDateTimeIntervalSeconds"
        ]
    if data.get("repeatExtXKey") is not None:
        out["repeat_ext_x_key"] = data["repeatExtXKey"]
    if data.get("streamSelection") is not None:
        import capo_mediapackage_vod.types.stream_selection

        out["stream_selection"] = (
            capo_mediapackage_vod.types.stream_selection.deserialize_json(
                data["streamSelection"]
            )
        )
    return out
