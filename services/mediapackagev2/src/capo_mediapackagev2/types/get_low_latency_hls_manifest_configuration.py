"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#GetLowLatencyHlsManifestConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediapackagev2.types.filter_configuration
    import capo_mediapackagev2.types.resource_name
    import capo_mediapackagev2.types.scte_hls
    import capo_mediapackagev2.types.start_tag
    import capo_mediapackagev2.types.uri_path_type


class GetLowLatencyHlsManifestConfiguration(TypedDict, closed=True):
    manifest_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>A short short string that's appended to the endpoint URL. The manifest name creates a unique path to this endpoint. If you don't enter a value, MediaPackage uses the default manifest name, index. MediaPackage automatically inserts the format extension, such as .m3u8. You can't use the same manifest name if you use HLS manifest and low-latency HLS manifest. The manifestName on the HLSManifest object overrides the manifestName you provided on the originEndpoint object.</p>"""
    url: "str"
    """<p>The egress domain URL for stream delivery from MediaPackage.</p>"""
    child_manifest_name: NotRequired[
        "capo_mediapackagev2.types.resource_name.ResourceName"
    ]
    """<p>A short string that's appended to the endpoint URL. The child manifest name creates a unique path to this endpoint. If you don't enter a value, MediaPackage uses the default child manifest name, index_1. The manifestName on the HLSManifest object overrides the manifestName you provided on the originEndpoint object.</p>"""
    manifest_window_seconds: NotRequired["int"]
    """<p>The total duration (in seconds) of the manifest's content.</p>"""
    program_date_time_interval_seconds: NotRequired["int"]
    """<p>Inserts EXT-X-PROGRAM-DATE-TIME tags in the output manifest at the interval that you specify. If you don't enter an interval, EXT-X-PROGRAM-DATE-TIME tags aren't included in the manifest. The tags sync the stream to the wall clock so that viewers can seek to a specific time in the playback timeline on the player.</p> <p>Irrespective of this parameter, if any ID3Timed metadata is in the HLS input, it is passed through to the HLS output.</p>"""
    scte_hls: NotRequired["capo_mediapackagev2.types.scte_hls.ScteHls"]
    filter_configuration: NotRequired[
        "capo_mediapackagev2.types.filter_configuration.FilterConfiguration"
    ]
    start_tag: NotRequired["capo_mediapackagev2.types.start_tag.StartTag"]
    url_encode_child_manifest: NotRequired["bool"]
    """<p>When enabled, MediaPackage URL-encodes the query string for API requests for LL-HLS child manifests to comply with Amazon Web Services Signature Version 4 (SigV4) signature signing protocol. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html">Amazon Web Services Signature Version 4 for API requests</a> in <i>Identity and Access Management User Guide</i>.</p>"""
    uri_path_type: NotRequired["capo_mediapackagev2.types.uri_path_type.UriPathType"]
    """<p>The type of path used in manifest URIs. <code>LEAF</code> indicates leaf-relative paths. <code>ROOT</code> indicates root-relative paths that include the full path from root.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLowLatencyHlsManifestConfiguration) -> dict:
    out: dict = {}
    out["ManifestName"] = value["manifest_name"]
    out["Url"] = value["url"]
    if "child_manifest_name" in value:
        out["ChildManifestName"] = value["child_manifest_name"]
    if "manifest_window_seconds" in value:
        out["ManifestWindowSeconds"] = value["manifest_window_seconds"]
    if "program_date_time_interval_seconds" in value:
        out["ProgramDateTimeIntervalSeconds"] = value[
            "program_date_time_interval_seconds"
        ]
    if "scte_hls" in value:
        import capo_mediapackagev2.types.scte_hls

        out["ScteHls"] = capo_mediapackagev2.types.scte_hls.serialize_json(
            value["scte_hls"]
        )
    if "filter_configuration" in value:
        import capo_mediapackagev2.types.filter_configuration

        out["FilterConfiguration"] = (
            capo_mediapackagev2.types.filter_configuration.serialize_json(
                value["filter_configuration"]
            )
        )
    if "start_tag" in value:
        import capo_mediapackagev2.types.start_tag

        out["StartTag"] = capo_mediapackagev2.types.start_tag.serialize_json(
            value["start_tag"]
        )
    if "url_encode_child_manifest" in value:
        out["UrlEncodeChildManifest"] = value["url_encode_child_manifest"]
    if "uri_path_type" in value:
        import capo_mediapackagev2.types.uri_path_type

        out["UriPathType"] = capo_mediapackagev2.types.uri_path_type.serialize_json(
            value["uri_path_type"]
        )
    return out


def deserialize_json(data: dict) -> GetLowLatencyHlsManifestConfiguration:
    out: GetLowLatencyHlsManifestConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ManifestName") is not None:
        out["manifest_name"] = data["ManifestName"]
    else:
        raise DeserializationError(
            "GetLowLatencyHlsManifestConfiguration.manifest_name required"
        )
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    else:
        raise DeserializationError("GetLowLatencyHlsManifestConfiguration.url required")
    if data.get("ChildManifestName") is not None:
        out["child_manifest_name"] = data["ChildManifestName"]
    if data.get("ManifestWindowSeconds") is not None:
        out["manifest_window_seconds"] = data["ManifestWindowSeconds"]
    if data.get("ProgramDateTimeIntervalSeconds") is not None:
        out["program_date_time_interval_seconds"] = data[
            "ProgramDateTimeIntervalSeconds"
        ]
    if data.get("ScteHls") is not None:
        import capo_mediapackagev2.types.scte_hls

        out["scte_hls"] = capo_mediapackagev2.types.scte_hls.deserialize_json(
            data["ScteHls"]
        )
    if data.get("FilterConfiguration") is not None:
        import capo_mediapackagev2.types.filter_configuration

        out["filter_configuration"] = (
            capo_mediapackagev2.types.filter_configuration.deserialize_json(
                data["FilterConfiguration"]
            )
        )
    if data.get("StartTag") is not None:
        import capo_mediapackagev2.types.start_tag

        out["start_tag"] = capo_mediapackagev2.types.start_tag.deserialize_json(
            data["StartTag"]
        )
    if data.get("UrlEncodeChildManifest") is not None:
        out["url_encode_child_manifest"] = data["UrlEncodeChildManifest"]
    if data.get("UriPathType") is not None:
        import capo_mediapackagev2.types.uri_path_type

        out["uri_path_type"] = capo_mediapackagev2.types.uri_path_type.deserialize_json(
            data["UriPathType"]
        )
    return out
