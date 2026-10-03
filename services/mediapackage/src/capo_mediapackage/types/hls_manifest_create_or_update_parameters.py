"""Generated from Smithy shape ``com.amazonaws.mediapackage#HlsManifestCreateOrUpdateParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage.types.__boolean
    import capo_mediapackage.types.__integer
    import capo_mediapackage.types.__string
    import capo_mediapackage.types.ad_markers
    import capo_mediapackage.types.ad_triggers
    import capo_mediapackage.types.ads_on_delivery_restrictions
    import capo_mediapackage.types.playlist_type


class HlsManifestCreateOrUpdateParameters(TypedDict, closed=True):
    ad_markers: NotRequired["capo_mediapackage.types.ad_markers.AdMarkers"]
    """This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source. "DATERANGE" inserts EXT-X-DATERANGE tags to signal ad and program transition events in HLS and CMAF manifests. For this option, you must set a programDateTimeIntervalSeconds value that is greater than 0."""
    ad_triggers: NotRequired["capo_mediapackage.types.ad_triggers.AdTriggers"]
    ads_on_delivery_restrictions: NotRequired[
        "capo_mediapackage.types.ads_on_delivery_restrictions.AdsOnDeliveryRestrictions"
    ]
    id: NotRequired["capo_mediapackage.types.__string.__string"]
    """The ID of the manifest. The ID must be unique within the OriginEndpoint and it cannot be changed after it is created."""
    include_iframe_only_stream: NotRequired[
        "capo_mediapackage.types.__boolean.__boolean"
    ]
    """When enabled, an I-Frame only stream will be included in the output."""
    manifest_name: NotRequired["capo_mediapackage.types.__string.__string"]
    """An optional short string appended to the end of the OriginEndpoint URL. If not specified, defaults to the manifestName for the OriginEndpoint."""
    playlist_type: NotRequired["capo_mediapackage.types.playlist_type.PlaylistType"]
    """The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD" is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist."""
    playlist_window_seconds: NotRequired["capo_mediapackage.types.__integer.__integer"]
    """Time window (in seconds) contained in each parent manifest."""
    program_date_time_interval_seconds: NotRequired[
        "capo_mediapackage.types.__integer.__integer"
    ]
    """The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output."""


# --- restJson1 ser/de ---
def serialize_json(value: HlsManifestCreateOrUpdateParameters) -> dict:
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
    if "id" in value:
        out["id"] = value["id"]
    if "include_iframe_only_stream" in value:
        out["includeIframeOnlyStream"] = value["include_iframe_only_stream"]
    if "manifest_name" in value:
        out["manifestName"] = value["manifest_name"]
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
    return out


def deserialize_json(data: dict) -> HlsManifestCreateOrUpdateParameters:
    out: HlsManifestCreateOrUpdateParameters = {}  # type: ignore[typeddict-item]
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
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("includeIframeOnlyStream") is not None:
        out["include_iframe_only_stream"] = data["includeIframeOnlyStream"]
    if data.get("manifestName") is not None:
        out["manifest_name"] = data["manifestName"]
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
    return out
