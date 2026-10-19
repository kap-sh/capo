"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ListDashManifestConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.resource_name


class ListDashManifestConfiguration(TypedDict, closed=True):
    manifest_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>A short string that's appended to the endpoint URL. The manifest name creates a unique path to this endpoint. If you don't enter a value, MediaPackage uses the default manifest name, index. </p>"""
    url: NotRequired["str"]
    """<p>The egress domain URL for stream delivery from MediaPackage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDashManifestConfiguration) -> dict:
    out: dict = {}
    out["ManifestName"] = value["manifest_name"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> ListDashManifestConfiguration:
    out: ListDashManifestConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ManifestName") is not None:
        out["manifest_name"] = data["ManifestName"]
    else:
        out["manifest_name"] = ""
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    return out
