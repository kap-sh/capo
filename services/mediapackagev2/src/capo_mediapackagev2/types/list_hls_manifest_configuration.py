"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ListHlsManifestConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.resource_name


class ListHlsManifestConfiguration(TypedDict, closed=True):
    manifest_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>A short short string that's appended to the endpoint URL. The manifest name creates a unique path to this endpoint. If you don't enter a value, MediaPackage uses the default manifest name, index. MediaPackage automatically inserts the format extension, such as .m3u8. You can't use the same manifest name if you use HLS manifest and low-latency HLS manifest. The manifestName on the HLSManifest object overrides the manifestName you provided on the originEndpoint object.</p>"""
    child_manifest_name: NotRequired[
        "capo_mediapackagev2.types.resource_name.ResourceName"
    ]
    """<p>A short string that's appended to the endpoint URL. The child manifest name creates a unique path to this endpoint. If you don't enter a value, MediaPackage uses the default child manifest name, index_1. The manifestName on the HLSManifest object overrides the manifestName you provided on the originEndpoint object.</p>"""
    url: NotRequired["str"]
    """<p>The egress domain URL for stream delivery from MediaPackage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListHlsManifestConfiguration) -> dict:
    out: dict = {}
    out["ManifestName"] = value["manifest_name"]
    if "child_manifest_name" in value:
        out["ChildManifestName"] = value["child_manifest_name"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> ListHlsManifestConfiguration:
    out: ListHlsManifestConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ManifestName") is not None:
        out["manifest_name"] = data["ManifestName"]
    else:
        out["manifest_name"] = ""
    if data.get("ChildManifestName") is not None:
        out["child_manifest_name"] = data["ChildManifestName"]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    return out
