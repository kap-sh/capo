"""Generated from Smithy shape ``com.amazonaws.iot#GetPackageVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.creation_date
    import capo_iot.types.last_modified_date
    import capo_iot.types.package_name
    import capo_iot.types.package_version_arn
    import capo_iot.types.package_version_artifact
    import capo_iot.types.package_version_error_reason
    import capo_iot.types.package_version_recipe
    import capo_iot.types.package_version_status
    import capo_iot.types.resource_attributes
    import capo_iot.types.resource_description
    import capo_iot.types.sbom
    import capo_iot.types.sbom_validation_status
    import capo_iot.types.version_name


class GetPackageVersionResponse(TypedDict, closed=True):
    package_version_arn: NotRequired[
        "capo_iot.types.package_version_arn.PackageVersionArn"
    ]
    """<p>The ARN for the package version.</p>"""
    package_name: NotRequired["capo_iot.types.package_name.PackageName"]
    """<p>The name of the software package.</p>"""
    version_name: NotRequired["capo_iot.types.version_name.VersionName"]
    """<p>The name of the package version.</p>"""
    description: NotRequired["capo_iot.types.resource_description.ResourceDescription"]
    """<p>The package version description.</p>"""
    attributes: NotRequired["capo_iot.types.resource_attributes.ResourceAttributes"]
    """<p>Metadata that were added to the package version that can be used to define a package version’s configuration.</p>"""
    artifact: NotRequired[
        "capo_iot.types.package_version_artifact.PackageVersionArtifact"
    ]
    """<p>The various components that make up a software package version.</p>"""
    status: NotRequired["capo_iot.types.package_version_status.PackageVersionStatus"]
    """<p>The status associated to the package version. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle">Package version lifecycle</a>.</p>"""
    error_reason: NotRequired[
        "capo_iot.types.package_version_error_reason.PackageVersionErrorReason"
    ]
    """<p>Error reason for a package version failure during creation or update.</p>"""
    creation_date: NotRequired["capo_iot.types.creation_date.CreationDate"]
    """<p>The date when the package version was created.</p>"""
    last_modified_date: NotRequired[
        "capo_iot.types.last_modified_date.LastModifiedDate"
    ]
    """<p>The date when the package version was last updated.</p>"""
    sbom: NotRequired["capo_iot.types.sbom.Sbom"]
    """<p>The software bill of materials for a software package version.</p>"""
    sbom_validation_status: NotRequired[
        "capo_iot.types.sbom_validation_status.SbomValidationStatus"
    ]
    """<p>The status of the validation for a new software bill of materials added to a software package version.</p>"""
    recipe: NotRequired["capo_iot.types.package_version_recipe.PackageVersionRecipe"]
    """<p>The inline job document associated with a software package version used for a quick job deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPackageVersionResponse) -> dict:
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
    if "artifact" in value:
        import capo_iot.types.package_version_artifact

        out["artifact"] = capo_iot.types.package_version_artifact.serialize_json(
            value["artifact"]
        )
    if "status" in value:
        import capo_iot.types.package_version_status

        out["status"] = capo_iot.types.package_version_status.serialize_json(
            value["status"]
        )
    if "error_reason" in value:
        out["errorReason"] = value["error_reason"]
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
    if "sbom" in value:
        import capo_iot.types.sbom

        out["sbom"] = capo_iot.types.sbom.serialize_json(value["sbom"])
    if "sbom_validation_status" in value:
        import capo_iot.types.sbom_validation_status

        out["sbomValidationStatus"] = (
            capo_iot.types.sbom_validation_status.serialize_json(
                value["sbom_validation_status"]
            )
        )
    if "recipe" in value:
        out["recipe"] = value["recipe"]
    return out


def deserialize_json(data: dict) -> GetPackageVersionResponse:
    out: GetPackageVersionResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("artifact") is not None:
        import capo_iot.types.package_version_artifact

        out["artifact"] = capo_iot.types.package_version_artifact.deserialize_json(
            data["artifact"]
        )
    if data.get("status") is not None:
        import capo_iot.types.package_version_status

        out["status"] = capo_iot.types.package_version_status.deserialize_json(
            data["status"]
        )
    if data.get("errorReason") is not None:
        out["error_reason"] = data["errorReason"]
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
    if data.get("sbom") is not None:
        import capo_iot.types.sbom

        out["sbom"] = capo_iot.types.sbom.deserialize_json(data["sbom"])
    if data.get("sbomValidationStatus") is not None:
        import capo_iot.types.sbom_validation_status

        out["sbom_validation_status"] = (
            capo_iot.types.sbom_validation_status.deserialize_json(
                data["sbomValidationStatus"]
            )
        )
    if data.get("recipe") is not None:
        out["recipe"] = data["recipe"]
    return out
