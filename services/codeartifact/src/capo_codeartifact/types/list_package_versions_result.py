"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListPackageVersionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.package_format
    import capo_codeartifact.types.package_name
    import capo_codeartifact.types.package_namespace
    import capo_codeartifact.types.package_version
    import capo_codeartifact.types.package_version_summary_list
    import capo_codeartifact.types.pagination_token


class ListPackageVersionsResult(TypedDict, closed=True):
    default_display_version: NotRequired[
        "capo_codeartifact.types.package_version.PackageVersion"
    ]
    """<p> The default package version to display. This depends on the package format: </p> <ul> <li> <p> For Maven and PyPI packages, it's the most recently published package version. </p> </li> <li> <p> For npm packages, it's the version referenced by the <code>latest</code> tag. If the <code>latest</code> tag is not set, it's the most recently published package version. </p> </li> </ul>"""
    format: NotRequired["capo_codeartifact.types.package_format.PackageFormat"]
    """<p> A format of the package. </p>"""
    namespace: NotRequired["capo_codeartifact.types.package_namespace.PackageNamespace"]
    """<p>The namespace of the package that contains the requested package versions. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package: NotRequired["capo_codeartifact.types.package_name.PackageName"]
    """<p> The name of the package. </p>"""
    versions: NotRequired[
        "capo_codeartifact.types.package_version_summary_list.PackageVersionSummaryList"
    ]
    """<p> The returned list of <a href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionSummary.html">PackageVersionSummary</a> objects. </p>"""
    next_token: NotRequired["capo_codeartifact.types.pagination_token.PaginationToken"]
    """<p> If there are additional results, this is the token for the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackageVersionsResult) -> dict:
    out: dict = {}
    if "default_display_version" in value:
        out["defaultDisplayVersion"] = value["default_display_version"]
    if "format" in value:
        import capo_codeartifact.types.package_format

        out["format"] = capo_codeartifact.types.package_format.serialize_json(
            value["format"]
        )
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "package" in value:
        out["package"] = value["package"]
    if "versions" in value:
        import capo_codeartifact.types.package_version_summary_list

        out["versions"] = (
            capo_codeartifact.types.package_version_summary_list.serialize_json(
                value["versions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPackageVersionsResult:
    out: ListPackageVersionsResult = {}  # type: ignore[typeddict-item]
    if data.get("defaultDisplayVersion") is not None:
        out["default_display_version"] = data["defaultDisplayVersion"]
    if data.get("format") is not None:
        import capo_codeartifact.types.package_format

        out["format"] = capo_codeartifact.types.package_format.deserialize_json(
            data["format"]
        )
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    if data.get("package") is not None:
        out["package"] = data["package"]
    if data.get("versions") is not None:
        import capo_codeartifact.types.package_version_summary_list

        out["versions"] = (
            capo_codeartifact.types.package_version_summary_list.deserialize_json(
                data["versions"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
