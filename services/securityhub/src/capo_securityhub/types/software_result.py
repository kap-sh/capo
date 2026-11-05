"""Generated from Smithy shape ``com.amazonaws.securityhub#SoftwareResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class SoftwareResult(TypedDict, closed=True):
    package_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the software package.</p>"""
    package_version: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The version of the software package.</p>"""
    package_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of the software package, for example <code>operating-system</code>, <code>application</code>, or <code>library</code>.</p>"""
    resource_count: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of resources that contain this software package. To list these resources, call <code>GetSoftwareResourcesV2</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareResult) -> dict:
    out: dict = {}
    if "package_name" in value:
        out["PackageName"] = value["package_name"]
    if "package_version" in value:
        out["PackageVersion"] = value["package_version"]
    if "package_type" in value:
        out["PackageType"] = value["package_type"]
    if "resource_count" in value:
        out["ResourceCount"] = value["resource_count"]
    return out


def deserialize_json(data: dict) -> SoftwareResult:
    out: SoftwareResult = {}  # type: ignore[typeddict-item]
    if data.get("PackageName") is not None:
        out["package_name"] = data["PackageName"]
    if data.get("PackageVersion") is not None:
        out["package_version"] = data["PackageVersion"]
    if data.get("PackageType") is not None:
        out["package_type"] = data["PackageType"]
    if data.get("ResourceCount") is not None:
        out["resource_count"] = data["ResourceCount"]
    return out
