"""Generated from Smithy shape ``com.amazonaws.codeartifact#DisposePackageVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.package_format
    import capo_codeartifact.types.package_name
    import capo_codeartifact.types.package_namespace
    import capo_codeartifact.types.package_version_list
    import capo_codeartifact.types.package_version_revision_map
    import capo_codeartifact.types.package_version_status
    import capo_codeartifact.types.repository_name


class DisposePackageVersionsRequest(TypedDict, closed=True):
    domain: "capo_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain that contains the repository you want to dispose. </p>"""
    domain_owner: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    repository: "capo_codeartifact.types.repository_name.RepositoryName"
    """<p> The name of the repository that contains the package versions you want to dispose. </p>"""
    format: "capo_codeartifact.types.package_format.PackageFormat"
    """<p> A format that specifies the type of package versions you want to dispose. </p>"""
    namespace: NotRequired["capo_codeartifact.types.package_namespace.PackageNamespace"]
    """<p>The namespace of the package versions to be disposed. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when disposing package versions of the following formats:</p> <ul> <li> <p>Maven</p> </li> <li> <p>Swift</p> </li> <li> <p>generic</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package: "capo_codeartifact.types.package_name.PackageName"
    """<p> The name of the package with the versions you want to dispose. </p>"""
    versions: "capo_codeartifact.types.package_version_list.PackageVersionList"
    """<p> The versions of the package you want to dispose. </p>"""
    version_revisions: NotRequired[
        "capo_codeartifact.types.package_version_revision_map.PackageVersionRevisionMap"
    ]
    """<p> The revisions of the package versions you want to dispose. </p>"""
    expected_status: NotRequired[
        "capo_codeartifact.types.package_version_status.PackageVersionStatus"
    ]
    """<p> The expected status of the package version to dispose. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisposePackageVersionsRequest) -> dict:
    out: dict = {}
    import capo_codeartifact.types.package_version_list

    out["versions"] = capo_codeartifact.types.package_version_list.serialize_json(
        value["versions"]
    )
    if "version_revisions" in value:
        import capo_codeartifact.types.package_version_revision_map

        out["versionRevisions"] = (
            capo_codeartifact.types.package_version_revision_map.serialize_json(
                value["version_revisions"]
            )
        )
    if "expected_status" in value:
        import capo_codeartifact.types.package_version_status

        out["expectedStatus"] = (
            capo_codeartifact.types.package_version_status.serialize_json(
                value["expected_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DisposePackageVersionsRequest:
    out: DisposePackageVersionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("versions") is not None:
        import capo_codeartifact.types.package_version_list

        out["versions"] = capo_codeartifact.types.package_version_list.deserialize_json(
            data["versions"]
        )
    else:
        out["versions"] = []
    if data.get("versionRevisions") is not None:
        import capo_codeartifact.types.package_version_revision_map

        out["version_revisions"] = (
            capo_codeartifact.types.package_version_revision_map.deserialize_json(
                data["versionRevisions"]
            )
        )
    if data.get("expectedStatus") is not None:
        import capo_codeartifact.types.package_version_status

        out["expected_status"] = (
            capo_codeartifact.types.package_version_status.deserialize_json(
                data["expectedStatus"]
            )
        )
    return out
