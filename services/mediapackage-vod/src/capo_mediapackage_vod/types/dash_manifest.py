"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#DashManifest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage_vod.types.__integer
    import capo_mediapackage_vod.types.__string
    import capo_mediapackage_vod.types.manifest_layout
    import capo_mediapackage_vod.types.profile
    import capo_mediapackage_vod.types.scte_markers_source
    import capo_mediapackage_vod.types.stream_selection


class DashManifest(TypedDict, closed=True):
    manifest_layout: NotRequired[
        "capo_mediapackage_vod.types.manifest_layout.ManifestLayout"
    ]
    """Determines the position of some tags in the Media Presentation Description (MPD). When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation. When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level."""
    manifest_name: NotRequired["capo_mediapackage_vod.types.__string.__string"]
    """An optional string to include in the name of the manifest."""
    min_buffer_time_seconds: NotRequired[
        "capo_mediapackage_vod.types.__integer.__integer"
    ]
    """Minimum duration (in seconds) that a player will buffer media before starting the presentation."""
    profile: NotRequired["capo_mediapackage_vod.types.profile.Profile"]
    """The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled."""
    scte_markers_source: NotRequired[
        "capo_mediapackage_vod.types.scte_markers_source.ScteMarkersSource"
    ]
    """The source of scte markers used. When set to SEGMENTS, the scte markers are sourced from the segments of the ingested content. When set to MANIFEST, the scte markers are sourced from the manifest of the ingested content."""
    stream_selection: NotRequired[
        "capo_mediapackage_vod.types.stream_selection.StreamSelection"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DashManifest) -> dict:
    out: dict = {}
    if "manifest_layout" in value:
        import capo_mediapackage_vod.types.manifest_layout

        out["manifestLayout"] = (
            capo_mediapackage_vod.types.manifest_layout.serialize_json(
                value["manifest_layout"]
            )
        )
    if "manifest_name" in value:
        out["manifestName"] = value["manifest_name"]
    if "min_buffer_time_seconds" in value:
        out["minBufferTimeSeconds"] = value["min_buffer_time_seconds"]
    if "profile" in value:
        import capo_mediapackage_vod.types.profile

        out["profile"] = capo_mediapackage_vod.types.profile.serialize_json(
            value["profile"]
        )
    if "scte_markers_source" in value:
        import capo_mediapackage_vod.types.scte_markers_source

        out["scteMarkersSource"] = (
            capo_mediapackage_vod.types.scte_markers_source.serialize_json(
                value["scte_markers_source"]
            )
        )
    if "stream_selection" in value:
        import capo_mediapackage_vod.types.stream_selection

        out["streamSelection"] = (
            capo_mediapackage_vod.types.stream_selection.serialize_json(
                value["stream_selection"]
            )
        )
    return out


def deserialize_json(data: dict) -> DashManifest:
    out: DashManifest = {}  # type: ignore[typeddict-item]
    if data.get("manifestLayout") is not None:
        import capo_mediapackage_vod.types.manifest_layout

        out["manifest_layout"] = (
            capo_mediapackage_vod.types.manifest_layout.deserialize_json(
                data["manifestLayout"]
            )
        )
    if data.get("manifestName") is not None:
        out["manifest_name"] = data["manifestName"]
    if data.get("minBufferTimeSeconds") is not None:
        out["min_buffer_time_seconds"] = data["minBufferTimeSeconds"]
    if data.get("profile") is not None:
        import capo_mediapackage_vod.types.profile

        out["profile"] = capo_mediapackage_vod.types.profile.deserialize_json(
            data["profile"]
        )
    if data.get("scteMarkersSource") is not None:
        import capo_mediapackage_vod.types.scte_markers_source

        out["scte_markers_source"] = (
            capo_mediapackage_vod.types.scte_markers_source.deserialize_json(
                data["scteMarkersSource"]
            )
        )
    if data.get("streamSelection") is not None:
        import capo_mediapackage_vod.types.stream_selection

        out["stream_selection"] = (
            capo_mediapackage_vod.types.stream_selection.deserialize_json(
                data["streamSelection"]
            )
        )
    return out
