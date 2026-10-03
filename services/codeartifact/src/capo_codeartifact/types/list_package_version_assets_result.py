"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListPackageVersionAssetsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.asset_summary_list
    import capo_codeartifact.types.package_format
    import capo_codeartifact.types.package_name
    import capo_codeartifact.types.package_namespace
    import capo_codeartifact.types.package_version
    import capo_codeartifact.types.package_version_revision
    import capo_codeartifact.types.pagination_token


class ListPackageVersionAssetsResult(TypedDict, closed=True):
    format: NotRequired["capo_codeartifact.types.package_format.PackageFormat"]
    """<p> The format of the package that contains the requested package version assets. </p>"""
    namespace: NotRequired["capo_codeartifact.types.package_namespace.PackageNamespace"]
    """<p>The namespace of the package version that contains the requested package version assets. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package: NotRequired["capo_codeartifact.types.package_name.PackageName"]
    """<p> The name of the package that contains the requested package version assets. </p>"""
    version: NotRequired["capo_codeartifact.types.package_version.PackageVersion"]
    """<p> The version of the package associated with the requested assets. </p>"""
    version_revision: NotRequired[
        "capo_codeartifact.types.package_version_revision.PackageVersionRevision"
    ]
    """<p> The current revision associated with the package version. </p>"""
    next_token: NotRequired["capo_codeartifact.types.pagination_token.PaginationToken"]
    """<p> If there are additional results, this is the token for the next set of results. </p>"""
    assets: NotRequired["capo_codeartifact.types.asset_summary_list.AssetSummaryList"]
    """<p> The returned list of <a href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssetSummary.html">AssetSummary</a> objects. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackageVersionAssetsResult) -> dict:
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
    if "assets" in value:
        import capo_codeartifact.types.asset_summary_list

        out["assets"] = capo_codeartifact.types.asset_summary_list.serialize_json(
            value["assets"]
        )
    return out


def deserialize_json(data: dict) -> ListPackageVersionAssetsResult:
    out: ListPackageVersionAssetsResult = {}  # type: ignore[typeddict-item]
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
    if data.get("assets") is not None:
        import capo_codeartifact.types.asset_summary_list

        out["assets"] = capo_codeartifact.types.asset_summary_list.deserialize_json(
            data["assets"]
        )
    return out
