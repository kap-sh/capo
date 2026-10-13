"""Generated from Smithy shape ``com.amazonaws.iot#GetPackageResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.creation_date
    import capo_iot.types.last_modified_date
    import capo_iot.types.package_arn
    import capo_iot.types.package_name
    import capo_iot.types.resource_description
    import capo_iot.types.version_name


class GetPackageResponse(TypedDict, closed=True):
    package_name: NotRequired["capo_iot.types.package_name.PackageName"]
    """<p>The name of the software package.</p>"""
    package_arn: NotRequired["capo_iot.types.package_arn.PackageArn"]
    """<p>The ARN for the package.</p>"""
    description: NotRequired["capo_iot.types.resource_description.ResourceDescription"]
    """<p>The package description.</p>"""
    default_version_name: NotRequired["capo_iot.types.version_name.VersionName"]
    """<p>The name of the default package version.</p>"""
    creation_date: NotRequired["capo_iot.types.creation_date.CreationDate"]
    """<p>The date the package was created.</p>"""
    last_modified_date: NotRequired[
        "capo_iot.types.last_modified_date.LastModifiedDate"
    ]
    """<p>The date when the package was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPackageResponse) -> dict:
    out: dict = {}
    if "package_name" in value:
        out["packageName"] = value["package_name"]
    if "package_arn" in value:
        out["packageArn"] = value["package_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "default_version_name" in value:
        out["defaultVersionName"] = value["default_version_name"]
    if "creation_date" in value:
        import capo_iot.types.creation_date

        out["creationDate"] = capo_iot.types.creation_date.serialize_json(
            value["creation_date"]
        )
    if "last_modified_date" in value:
        import capo_iot.types.last_modified_date

        out["lastModifiedDate"] = capo_iot.types.last_modified_date.serialize_json(
            value["last_modified_date"]
        )
    return out


def deserialize_json(data: dict) -> GetPackageResponse:
    out: GetPackageResponse = {}  # type: ignore[typeddict-item]
    if data.get("packageName") is not None:
        out["package_name"] = data["packageName"]
    if data.get("packageArn") is not None:
        out["package_arn"] = data["packageArn"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("defaultVersionName") is not None:
        out["default_version_name"] = data["defaultVersionName"]
    if data.get("creationDate") is not None:
        import capo_iot.types.creation_date

        out["creation_date"] = capo_iot.types.creation_date.deserialize_json(
            data["creationDate"]
        )
    if data.get("lastModifiedDate") is not None:
        import capo_iot.types.last_modified_date

        out["last_modified_date"] = capo_iot.types.last_modified_date.deserialize_json(
            data["lastModifiedDate"]
        )
    return out


def redact_sensitive(value: GetPackageResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
