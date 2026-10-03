"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListPackagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.allow_publish
    import capo_codeartifact.types.allow_upstream
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.list_packages_max_results
    import capo_codeartifact.types.package_format
    import capo_codeartifact.types.package_name
    import capo_codeartifact.types.package_namespace
    import capo_codeartifact.types.pagination_token
    import capo_codeartifact.types.repository_name


class ListPackagesRequest(TypedDict, closed=True):
    domain: "capo_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain that contains the repository that contains the requested packages. </p>"""
    domain_owner: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    repository: "capo_codeartifact.types.repository_name.RepositoryName"
    """<p> The name of the repository that contains the requested packages. </p>"""
    format: NotRequired["capo_codeartifact.types.package_format.PackageFormat"]
    """<p>The format used to filter requested packages. Only packages from the provided format will be returned.</p>"""
    namespace: NotRequired["capo_codeartifact.types.package_namespace.PackageNamespace"]
    """<p>The namespace prefix used to filter requested packages. Only packages with a namespace that starts with the provided string value are returned. Note that although this option is called <code>--namespace</code> and not <code>--namespace-prefix</code>, it has prefix-matching behavior.</p> <p>Each package format uses namespace as follows:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package_prefix: NotRequired["capo_codeartifact.types.package_name.PackageName"]
    """<p> A prefix used to filter requested packages. Only packages with names that start with <code>packagePrefix</code> are returned. </p>"""
    max_results: NotRequired[
        "capo_codeartifact.types.list_packages_max_results.ListPackagesMaxResults"
    ]
    """<p> The maximum number of results to return per page. </p>"""
    next_token: NotRequired["capo_codeartifact.types.pagination_token.PaginationToken"]
    """<p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    publish: NotRequired["capo_codeartifact.types.allow_publish.AllowPublish"]
    """<p>The value of the <code>Publish</code> package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see <a href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html">PackageOriginRestrictions</a>.</p>"""
    upstream: NotRequired["capo_codeartifact.types.allow_upstream.AllowUpstream"]
    """<p>The value of the <code>Upstream</code> package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see <a href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html">PackageOriginRestrictions</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackagesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPackagesRequest:
    out: ListPackagesRequest = {}  # type: ignore[typeddict-item]
    return out
