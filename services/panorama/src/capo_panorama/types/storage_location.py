"""Generated from Smithy shape ``com.amazonaws.panorama#StorageLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.bucket
    import capo_panorama.types.object


class StorageLocation(TypedDict, closed=True):
    bucket: "capo_panorama.types.bucket.Bucket"
    """<p>The location's bucket.</p>"""
    repo_prefix_location: "capo_panorama.types.object.Object"
    """<p>The location's repo prefix.</p>"""
    generated_prefix_location: "capo_panorama.types.object.Object"
    """<p>The location's generated prefix.</p>"""
    binary_prefix_location: "capo_panorama.types.object.Object"
    """<p>The location's binary prefix.</p>"""
    manifest_prefix_location: "capo_panorama.types.object.Object"
    """<p>The location's manifest prefix.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageLocation) -> dict:
    out: dict = {}
    out["Bucket"] = value["bucket"]
    out["RepoPrefixLocation"] = value["repo_prefix_location"]
    out["GeneratedPrefixLocation"] = value["generated_prefix_location"]
    out["BinaryPrefixLocation"] = value["binary_prefix_location"]
    out["ManifestPrefixLocation"] = value["manifest_prefix_location"]
    return out


def deserialize_json(data: dict) -> StorageLocation:
    out: StorageLocation = {}  # type: ignore[typeddict-item]
    if data.get("Bucket") is not None:
        out["bucket"] = data["Bucket"]
    else:
        out["bucket"] = ""
    if data.get("RepoPrefixLocation") is not None:
        out["repo_prefix_location"] = data["RepoPrefixLocation"]
    else:
        out["repo_prefix_location"] = ""
    if data.get("GeneratedPrefixLocation") is not None:
        out["generated_prefix_location"] = data["GeneratedPrefixLocation"]
    else:
        out["generated_prefix_location"] = ""
    if data.get("BinaryPrefixLocation") is not None:
        out["binary_prefix_location"] = data["BinaryPrefixLocation"]
    else:
        out["binary_prefix_location"] = ""
    if data.get("ManifestPrefixLocation") is not None:
        out["manifest_prefix_location"] = data["ManifestPrefixLocation"]
    else:
        out["manifest_prefix_location"] = ""
    return out
