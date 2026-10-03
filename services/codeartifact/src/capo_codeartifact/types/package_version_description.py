"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageVersionDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.license_info_list
    import capo_codeartifact.types.package_format
    import capo_codeartifact.types.package_name
    import capo_codeartifact.types.package_namespace
    import capo_codeartifact.types.package_version
    import capo_codeartifact.types.package_version_origin
    import capo_codeartifact.types.package_version_revision
    import capo_codeartifact.types.package_version_status
    import capo_codeartifact.types.string
    import capo_codeartifact.types.string255
    import capo_codeartifact.types.timestamp


class PackageVersionDescription(TypedDict, closed=True):
    format: NotRequired["capo_codeartifact.types.package_format.PackageFormat"]
    """<p> The format of the package version. </p>"""
    namespace: NotRequired["capo_codeartifact.types.package_namespace.PackageNamespace"]
    """<p>The namespace of the package version. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package_name: NotRequired["capo_codeartifact.types.package_name.PackageName"]
    """<p> The name of the requested package. </p>"""
    display_name: NotRequired["capo_codeartifact.types.string255.String255"]
    """<p> The name of the package that is displayed. The <code>displayName</code> varies depending on the package version's format. For example, if an npm package is named <code>ui</code>, is in the namespace <code>vue</code>, and has the format <code>npm</code>, then the <code>displayName</code> is <code>@vue/ui</code>. </p>"""
    version: NotRequired["capo_codeartifact.types.package_version.PackageVersion"]
    """<p> The version of the package. </p>"""
    summary: NotRequired["capo_codeartifact.types.string.String"]
    """<p> A summary of the package version. The summary is extracted from the package. The information in and detail level of the summary depends on the package version's format. </p>"""
    home_page: NotRequired["capo_codeartifact.types.string.String"]
    """<p> The homepage associated with the package. </p>"""
    source_code_repository: NotRequired["capo_codeartifact.types.string.String"]
    """<p> The repository for the source code in the package version, or the source code used to build it. </p>"""
    published_time: NotRequired["capo_codeartifact.types.timestamp.Timestamp"]
    """<p> A timestamp that contains the date and time the package version was published. </p>"""
    licenses: NotRequired["capo_codeartifact.types.license_info_list.LicenseInfoList"]
    """<p> Information about licenses associated with the package version. </p>"""
    revision: NotRequired[
        "capo_codeartifact.types.package_version_revision.PackageVersionRevision"
    ]
    """<p> The revision of the package version. </p>"""
    status: NotRequired[
        "capo_codeartifact.types.package_version_status.PackageVersionStatus"
    ]
    """<p> A string that contains the status of the package version. </p>"""
    origin: NotRequired[
        "capo_codeartifact.types.package_version_origin.PackageVersionOrigin"
    ]
    """<p>A <a href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionOrigin.html">PackageVersionOrigin</a> object that contains information about how the package version was added to the repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionDescription) -> dict:
    out: dict = {}
    if "format" in value:
        import capo_codeartifact.types.package_format

        out["format"] = capo_codeartifact.types.package_format.serialize_json(
            value["format"]
        )
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "package_name" in value:
        out["packageName"] = value["package_name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "version" in value:
        out["version"] = value["version"]
    if "summary" in value:
        out["summary"] = value["summary"]
    if "home_page" in value:
        out["homePage"] = value["home_page"]
    if "source_code_repository" in value:
        out["sourceCodeRepository"] = value["source_code_repository"]
    if "published_time" in value:
        import capo_codeartifact.types.timestamp

        out["publishedTime"] = capo_codeartifact.types.timestamp.serialize_json(
            value["published_time"]
        )
    if "licenses" in value:
        import capo_codeartifact.types.license_info_list

        out["licenses"] = capo_codeartifact.types.license_info_list.serialize_json(
            value["licenses"]
        )
    if "revision" in value:
        out["revision"] = value["revision"]
    if "status" in value:
        import capo_codeartifact.types.package_version_status

        out["status"] = capo_codeartifact.types.package_version_status.serialize_json(
            value["status"]
        )
    if "origin" in value:
        import capo_codeartifact.types.package_version_origin

        out["origin"] = capo_codeartifact.types.package_version_origin.serialize_json(
            value["origin"]
        )
    return out


def deserialize_json(data: dict) -> PackageVersionDescription:
    out: PackageVersionDescription = {}  # type: ignore[typeddict-item]
    if data.get("format") is not None:
        import capo_codeartifact.types.package_format

        out["format"] = capo_codeartifact.types.package_format.deserialize_json(
            data["format"]
        )
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    if data.get("packageName") is not None:
        out["package_name"] = data["packageName"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    if data.get("homePage") is not None:
        out["home_page"] = data["homePage"]
    if data.get("sourceCodeRepository") is not None:
        out["source_code_repository"] = data["sourceCodeRepository"]
    if data.get("publishedTime") is not None:
        import capo_codeartifact.types.timestamp

        out["published_time"] = capo_codeartifact.types.timestamp.deserialize_json(
            data["publishedTime"]
        )
    if data.get("licenses") is not None:
        import capo_codeartifact.types.license_info_list

        out["licenses"] = capo_codeartifact.types.license_info_list.deserialize_json(
            data["licenses"]
        )
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    if data.get("status") is not None:
        import capo_codeartifact.types.package_version_status

        out["status"] = capo_codeartifact.types.package_version_status.deserialize_json(
            data["status"]
        )
    if data.get("origin") is not None:
        import capo_codeartifact.types.package_version_origin

        out["origin"] = capo_codeartifact.types.package_version_origin.deserialize_json(
            data["origin"]
        )
    return out
