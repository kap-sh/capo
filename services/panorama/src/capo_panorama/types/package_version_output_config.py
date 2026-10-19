"""Generated from Smithy shape ``com.amazonaws.panorama#PackageVersionOutputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.mark_latest_patch
    import capo_panorama.types.node_package_name
    import capo_panorama.types.node_package_version


class PackageVersionOutputConfig(TypedDict, closed=True):
    package_name: "capo_panorama.types.node_package_name.NodePackageName"
    """<p>The output's package name.</p>"""
    package_version: "capo_panorama.types.node_package_version.NodePackageVersion"
    """<p>The output's package version.</p>"""
    mark_latest: "capo_panorama.types.mark_latest_patch.MarkLatestPatch"
    """<p>Indicates that the version is recommended for all users.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionOutputConfig) -> dict:
    out: dict = {}
    out["PackageName"] = value["package_name"]
    out["PackageVersion"] = value["package_version"]
    out["MarkLatest"] = value.get("mark_latest", False)
    return out


def deserialize_json(data: dict) -> PackageVersionOutputConfig:
    out: PackageVersionOutputConfig = {}  # type: ignore[typeddict-item]
    if data.get("PackageName") is not None:
        out["package_name"] = data["PackageName"]
    else:
        out["package_name"] = ""
    if data.get("PackageVersion") is not None:
        out["package_version"] = data["PackageVersion"]
    else:
        out["package_version"] = ""
    if data.get("MarkLatest") is not None:
        out["mark_latest"] = data["MarkLatest"]
    else:
        out["mark_latest"] = False
    return out
