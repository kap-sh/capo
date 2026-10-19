"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#HarvestedHlsManifest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.resource_name


class HarvestedHlsManifest(TypedDict, closed=True):
    manifest_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the harvested HLS manifest.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarvestedHlsManifest) -> dict:
    out: dict = {}
    out["ManifestName"] = value["manifest_name"]
    return out


def deserialize_json(data: dict) -> HarvestedHlsManifest:
    out: HarvestedHlsManifest = {}  # type: ignore[typeddict-item]
    if data.get("ManifestName") is not None:
        out["manifest_name"] = data["ManifestName"]
    else:
        out["manifest_name"] = ""
    return out
