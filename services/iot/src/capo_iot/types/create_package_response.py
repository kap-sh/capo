"""Generated from Smithy shape ``com.amazonaws.iot#CreatePackageResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.package_arn
    import capo_iot.types.package_name
    import capo_iot.types.resource_description


class CreatePackageResponse(TypedDict, closed=True):
    package_name: NotRequired["capo_iot.types.package_name.PackageName"]
    """<p>The name of the software package.</p>"""
    package_arn: NotRequired["capo_iot.types.package_arn.PackageArn"]
    """<p>The Amazon Resource Name (ARN) for the package.</p>"""
    description: NotRequired["capo_iot.types.resource_description.ResourceDescription"]
    """<p>The package description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePackageResponse) -> dict:
    out: dict = {}
    if "package_name" in value:
        out["packageName"] = value["package_name"]
    if "package_arn" in value:
        out["packageArn"] = value["package_arn"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreatePackageResponse:
    out: CreatePackageResponse = {}  # type: ignore[typeddict-item]
    if data.get("packageName") is not None:
        out["package_name"] = data["packageName"]
    if data.get("packageArn") is not None:
        out["package_arn"] = data["packageArn"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: CreatePackageResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
