"""Generated from Smithy shape ``com.amazonaws.iot#PackageVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.creation_date
    import capo_iot.types.last_modified_date
    import capo_iot.types.package_name
    import capo_iot.types.package_version_status
    import capo_iot.types.version_name


class PackageVersionSummary(TypedDict, closed=True):
    package_name: NotRequired["capo_iot.types.package_name.PackageName"]
    """<p>The name of the associated software package.</p>"""
    version_name: NotRequired["capo_iot.types.version_name.VersionName"]
    """<p>The name of the target package version.</p>"""
    status: NotRequired["capo_iot.types.package_version_status.PackageVersionStatus"]
    """<p>The status of the package version. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle">Package version lifecycle</a>.</p>"""
    creation_date: NotRequired["capo_iot.types.creation_date.CreationDate"]
    """<p>The date that the package version was created.</p>"""
    last_modified_date: NotRequired[
        "capo_iot.types.last_modified_date.LastModifiedDate"
    ]
    """<p>The date that the package version was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionSummary) -> dict:
    out: dict = {}
    if "package_name" in value:
        out["packageName"] = value["package_name"]
    if "version_name" in value:
        out["versionName"] = value["version_name"]
    if "status" in value:
        import capo_iot.types.package_version_status

        out["status"] = capo_iot.types.package_version_status.serialize_json(
            value["status"]
        )
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


def deserialize_json(data: dict) -> PackageVersionSummary:
    out: PackageVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("packageName") is not None:
        out["package_name"] = data["packageName"]
    if data.get("versionName") is not None:
        out["version_name"] = data["versionName"]
    if data.get("status") is not None:
        import capo_iot.types.package_version_status

        out["status"] = capo_iot.types.package_version_status.deserialize_json(
            data["status"]
        )
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
