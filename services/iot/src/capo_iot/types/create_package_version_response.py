"""Generated from Smithy shape ``com.amazonaws.iot#CreatePackageVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.package_name
    import capo_iot.types.package_version_arn
    import capo_iot.types.package_version_error_reason
    import capo_iot.types.package_version_status
    import capo_iot.types.resource_attributes
    import capo_iot.types.resource_description
    import capo_iot.types.version_name


class CreatePackageVersionResponse(TypedDict, closed=True):
    package_version_arn: NotRequired[
        "capo_iot.types.package_version_arn.PackageVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) for the package.</p>"""
    package_name: NotRequired["capo_iot.types.package_name.PackageName"]
    """<p>The name of the associated software package.</p>"""
    version_name: NotRequired["capo_iot.types.version_name.VersionName"]
    """<p>The name of the new package version.</p>"""
    description: NotRequired["capo_iot.types.resource_description.ResourceDescription"]
    """<p>The package version description.</p>"""
    attributes: NotRequired["capo_iot.types.resource_attributes.ResourceAttributes"]
    """<p>Metadata that were added to the package version that can be used to define a package version’s configuration.</p>"""
    status: NotRequired["capo_iot.types.package_version_status.PackageVersionStatus"]
    """<p>The status of the package version. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle">Package version lifecycle</a>.</p>"""
    error_reason: NotRequired[
        "capo_iot.types.package_version_error_reason.PackageVersionErrorReason"
    ]
    """<p>Error reason for a package version failure during creation or update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePackageVersionResponse) -> dict:
    out: dict = {}
    if "package_version_arn" in value:
        out["packageVersionArn"] = value["package_version_arn"]
    if "package_name" in value:
        out["packageName"] = value["package_name"]
    if "version_name" in value:
        out["versionName"] = value["version_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "attributes" in value:
        import capo_iot.types.resource_attributes

        out["attributes"] = capo_iot.types.resource_attributes.serialize_json(
            value["attributes"]
        )
    if "status" in value:
        import capo_iot.types.package_version_status

        out["status"] = capo_iot.types.package_version_status.serialize_json(
            value["status"]
        )
    if "error_reason" in value:
        out["errorReason"] = value["error_reason"]
    return out


def deserialize_json(data: dict) -> CreatePackageVersionResponse:
    out: CreatePackageVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("packageVersionArn") is not None:
        out["package_version_arn"] = data["packageVersionArn"]
    if data.get("packageName") is not None:
        out["package_name"] = data["packageName"]
    if data.get("versionName") is not None:
        out["version_name"] = data["versionName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("attributes") is not None:
        import capo_iot.types.resource_attributes

        out["attributes"] = capo_iot.types.resource_attributes.deserialize_json(
            data["attributes"]
        )
    if data.get("status") is not None:
        import capo_iot.types.package_version_status

        out["status"] = capo_iot.types.package_version_status.deserialize_json(
            data["status"]
        )
    if data.get("errorReason") is not None:
        out["error_reason"] = data["errorReason"]
    return out
