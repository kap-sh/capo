"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ScteHls``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.ad_marker_hls
    import capo_mediapackagev2.types.scte_in_manifests


class ScteHls(TypedDict, closed=True):
    ad_marker_hls: NotRequired["capo_mediapackagev2.types.ad_marker_hls.AdMarkerHls"]
    """<p>Ad markers indicate when ads should be inserted during playback. If you include ad markers in the content stream in your upstream encoders, then you need to inform MediaPackage what to do with the ad markers in the output. Choose what you want MediaPackage to do with the ad markers.</p> <p>Value description: </p> <ul> <li> <p>SCTE35_ENHANCED - Generate industry-standard CUE tag ad markers in HLS manifests based on SCTE-35 input messages from the input stream.</p> </li> <li> <p>DATERANGE - Insert EXT-X-DATERANGE tags to signal ad and program transition events in TS and CMAF manifests. If you use DATERANGE, you must set a programDateTimeIntervalSeconds value of 1 or higher. To learn more about DATERANGE, see <a href="http://docs.aws.amazon.com/mediapackage/latest/ug/scte-35-ad-marker-ext-x-daterange.html">SCTE-35 Ad Marker EXT-X-DATERANGE</a>.</p> </li> </ul>"""
    scte_in_manifests: NotRequired[
        "capo_mediapackagev2.types.scte_in_manifests.ScteInManifests"
    ]
    """<p>Controls which SCTE-35 events appear in HLS manifests. <code>ALL</code> includes all non-implicit SCTE-35 events. <code>MATCHES_FILTER</code> includes only events whose type matches the configured <code>ScteFilter</code>.</p> <p>If you don't specify a value, the default is <code>ALL</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScteHls) -> dict:
    out: dict = {}
    if "ad_marker_hls" in value:
        import capo_mediapackagev2.types.ad_marker_hls

        out["AdMarkerHls"] = capo_mediapackagev2.types.ad_marker_hls.serialize_json(
            value["ad_marker_hls"]
        )
    if "scte_in_manifests" in value:
        import capo_mediapackagev2.types.scte_in_manifests

        out["ScteInManifests"] = (
            capo_mediapackagev2.types.scte_in_manifests.serialize_json(
                value["scte_in_manifests"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScteHls:
    out: ScteHls = {}  # type: ignore[typeddict-item]
    if data.get("AdMarkerHls") is not None:
        import capo_mediapackagev2.types.ad_marker_hls

        out["ad_marker_hls"] = capo_mediapackagev2.types.ad_marker_hls.deserialize_json(
            data["AdMarkerHls"]
        )
    if data.get("ScteInManifests") is not None:
        import capo_mediapackagev2.types.scte_in_manifests

        out["scte_in_manifests"] = (
            capo_mediapackagev2.types.scte_in_manifests.deserialize_json(
                data["ScteInManifests"]
            )
        )
    return out
