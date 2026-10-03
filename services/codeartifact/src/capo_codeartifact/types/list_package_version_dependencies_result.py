"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListPackageVersionDependenciesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.package_dependency_list
    import capo_codeartifact.types.package_format
    import capo_codeartifact.types.package_name
    import capo_codeartifact.types.package_namespace
    import capo_codeartifact.types.package_version
    import capo_codeartifact.types.package_version_revision
    import capo_codeartifact.types.pagination_token


class ListPackageVersionDependenciesResult(TypedDict, closed=True):
    format: NotRequired["capo_codeartifact.types.package_format.PackageFormat"]
    """<p> A format that specifies the type of the package that contains the returned dependencies. </p>"""
    namespace: NotRequired["capo_codeartifact.types.package_namespace.PackageNamespace"]
    """<p>The namespace of the package version that contains the returned dependencies. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when listing dependencies from package versions of the following formats:</p> <ul> <li> <p>Maven</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package: NotRequired["capo_codeartifact.types.package_name.PackageName"]
    """<p> The name of the package that contains the returned package versions dependencies. </p>"""
    version: NotRequired["capo_codeartifact.types.package_version.PackageVersion"]
    """<p> The version of the package that is specified in the request. </p>"""
    version_revision: NotRequired[
        "capo_codeartifact.types.package_version_revision.PackageVersionRevision"
    ]
    """<p> The current revision associated with the package version. </p>"""
    next_token: NotRequired["capo_codeartifact.types.pagination_token.PaginationToken"]
    """<p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    dependencies: NotRequired[
        "capo_codeartifact.types.package_dependency_list.PackageDependencyList"
    ]
    """<p> The returned list of <a href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDependency.html">PackageDependency</a> objects. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackageVersionDependenciesResult) -> dict:
    out: dict = {}
    if "format" in value:
        import capo_codeartifact.types.package_format

        out["format"] = capo_codeartifact.types.package_format.serialize_json(
            value["format"]
        )
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "package" in value:
        out["package"] = value["package"]
    if "version" in value:
        out["version"] = value["version"]
    if "version_revision" in value:
        out["versionRevision"] = value["version_revision"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "dependencies" in value:
        import capo_codeartifact.types.package_dependency_list

        out["dependencies"] = (
            capo_codeartifact.types.package_dependency_list.serialize_json(
                value["dependencies"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListPackageVersionDependenciesResult:
    out: ListPackageVersionDependenciesResult = {}  # type: ignore[typeddict-item]
    if data.get("format") is not None:
        import capo_codeartifact.types.package_format

        out["format"] = capo_codeartifact.types.package_format.deserialize_json(
            data["format"]
        )
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    if data.get("package") is not None:
        out["package"] = data["package"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("versionRevision") is not None:
        out["version_revision"] = data["versionRevision"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("dependencies") is not None:
        import capo_codeartifact.types.package_dependency_list

        out["dependencies"] = (
            capo_codeartifact.types.package_dependency_list.deserialize_json(
                data["dependencies"]
            )
        )
    return out
