"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ListMssManifestConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.resource_name


class ListMssManifestConfiguration(TypedDict, closed=True):
    manifest_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the MSS manifest configuration.</p>"""
    url: NotRequired["str"]
    """<p>The URL for accessing the MSS manifest.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMssManifestConfiguration) -> dict:
    out: dict = {}
    out["ManifestName"] = value["manifest_name"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> ListMssManifestConfiguration:
    out: ListMssManifestConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ManifestName") is not None:
        out["manifest_name"] = data["ManifestName"]
    else:
        out["manifest_name"] = ""
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    return out
