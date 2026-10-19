"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#GetMssManifestConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.filter_configuration
    import capo_mediapackagev2.types.manifest_name
    import capo_mediapackagev2.types.mss_manifest_layout


class GetMssManifestConfiguration(TypedDict, closed=True):
    manifest_name: "capo_mediapackagev2.types.manifest_name.ManifestName"
    """<p>The name of the MSS manifest. This name is appended to the origin endpoint URL to create the unique path for accessing this specific MSS manifest.</p>"""
    url: "str"
    """<p>The complete URL for accessing the MSS manifest. Client players use this URL to retrieve the manifest and begin streaming the Microsoft Smooth Streaming content.</p>"""
    filter_configuration: NotRequired[
        "capo_mediapackagev2.types.filter_configuration.FilterConfiguration"
    ]
    manifest_window_seconds: NotRequired["int"]
    """<p>The duration (in seconds) of the manifest window. This represents the total amount of content available in the manifest at any given time.</p>"""
    manifest_layout: NotRequired[
        "capo_mediapackagev2.types.mss_manifest_layout.MssManifestLayout"
    ]
    """<p>The layout format of the MSS manifest, which determines how the manifest is structured for client compatibility.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMssManifestConfiguration) -> dict:
    out: dict = {}
    out["ManifestName"] = value["manifest_name"]
    out["Url"] = value["url"]
    if "filter_configuration" in value:
        import capo_mediapackagev2.types.filter_configuration

        out["FilterConfiguration"] = (
            capo_mediapackagev2.types.filter_configuration.serialize_json(
                value["filter_configuration"]
            )
        )
    if "manifest_window_seconds" in value:
        out["ManifestWindowSeconds"] = value["manifest_window_seconds"]
    if "manifest_layout" in value:
        import capo_mediapackagev2.types.mss_manifest_layout

        out["ManifestLayout"] = (
            capo_mediapackagev2.types.mss_manifest_layout.serialize_json(
                value["manifest_layout"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMssManifestConfiguration:
    out: GetMssManifestConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ManifestName") is not None:
        out["manifest_name"] = data["ManifestName"]
    else:
        out["manifest_name"] = ""
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    else:
        out["url"] = ""
    if data.get("FilterConfiguration") is not None:
        import capo_mediapackagev2.types.filter_configuration

        out["filter_configuration"] = (
            capo_mediapackagev2.types.filter_configuration.deserialize_json(
                data["FilterConfiguration"]
            )
        )
    if data.get("ManifestWindowSeconds") is not None:
        out["manifest_window_seconds"] = data["ManifestWindowSeconds"]
    if data.get("ManifestLayout") is not None:
        import capo_mediapackagev2.types.mss_manifest_layout

        out["manifest_layout"] = (
            capo_mediapackagev2.types.mss_manifest_layout.deserialize_json(
                data["ManifestLayout"]
            )
        )
    return out
