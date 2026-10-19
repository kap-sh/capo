"""Generated from Smithy shape ``com.amazonaws.panorama#PackageObject``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.node_package_name
    import capo_panorama.types.node_package_patch_version
    import capo_panorama.types.node_package_version


class PackageObject(TypedDict, closed=True):
    name: "capo_panorama.types.node_package_name.NodePackageName"
    """<p>The object's name.</p>"""
    package_version: "capo_panorama.types.node_package_version.NodePackageVersion"
    """<p>The object's package version.</p>"""
    patch_version: (
        "capo_panorama.types.node_package_patch_version.NodePackagePatchVersion"
    )
    """<p>The object's patch version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageObject) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["PackageVersion"] = value["package_version"]
    out["PatchVersion"] = value["patch_version"]
    return out


def deserialize_json(data: dict) -> PackageObject:
    out: PackageObject = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("PackageVersion") is not None:
        out["package_version"] = data["PackageVersion"]
    else:
        out["package_version"] = ""
    if data.get("PatchVersion") is not None:
        out["patch_version"] = data["PatchVersion"]
    else:
        out["patch_version"] = ""
    return out
