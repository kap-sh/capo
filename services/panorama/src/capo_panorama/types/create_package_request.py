"""Generated from Smithy shape ``com.amazonaws.panorama#CreatePackageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.node_package_name
    import capo_panorama.types.tag_map


class CreatePackageRequest(TypedDict, closed=True):
    package_name: "capo_panorama.types.node_package_name.NodePackageName"
    """<p>A name for the package.</p>"""
    tags: NotRequired["capo_panorama.types.tag_map.TagMap"]
    """<p>Tags for the package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePackageRequest) -> dict:
    out: dict = {}
    out["PackageName"] = value["package_name"]
    if "tags" in value:
        import capo_panorama.types.tag_map

        out["Tags"] = capo_panorama.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePackageRequest:
    out: CreatePackageRequest = {}  # type: ignore[typeddict-item]
    if data.get("PackageName") is not None:
        out["package_name"] = data["PackageName"]
    else:
        out["package_name"] = ""
    if data.get("Tags") is not None:
        import capo_panorama.types.tag_map

        out["tags"] = capo_panorama.types.tag_map.deserialize_json(data["Tags"])
    return out
