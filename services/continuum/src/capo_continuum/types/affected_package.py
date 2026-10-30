"""Generated from Smithy shape ``com.amazonaws.continuum#AffectedPackage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.package_manager
    import capo_continuum.types.package_name
    import capo_continuum.types.package_version


class AffectedPackage(TypedDict, closed=True):
    name: "capo_continuum.types.package_name.PackageName"
    """The package name."""
    version: NotRequired["capo_continuum.types.package_version.PackageVersion"]
    """The affected version."""
    fixed_in_version: NotRequired["capo_continuum.types.package_version.PackageVersion"]
    """The earliest version that resolves the issue, when one is known."""
    package_manager: NotRequired["capo_continuum.types.package_manager.PackageManager"]
    """The ecosystem supplying the package."""


# --- restJson1 ser/de ---
def serialize_json(value: AffectedPackage) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "version" in value:
        out["version"] = value["version"]
    if "fixed_in_version" in value:
        out["fixedInVersion"] = value["fixed_in_version"]
    if "package_manager" in value:
        out["packageManager"] = value["package_manager"]
    return out


def deserialize_json(data: dict) -> AffectedPackage:
    out: AffectedPackage = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("fixedInVersion") is not None:
        out["fixed_in_version"] = data["fixedInVersion"]
    if data.get("packageManager") is not None:
        out["package_manager"] = data["packageManager"]
    return out
