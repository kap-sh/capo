"""Generated from Smithy shape ``com.amazonaws.codeartifact#PutPackageOriginConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codeartifact.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.package_format
    import capo_codeartifact.types.package_name
    import capo_codeartifact.types.package_namespace
    import capo_codeartifact.types.package_origin_restrictions
    import capo_codeartifact.types.repository_name


class PutPackageOriginConfigurationRequest(TypedDict, closed=True):
    domain: "capo_codeartifact.types.domain_name.DomainName"
    """<p>The name of the domain that contains the repository that contains the package.</p>"""
    domain_owner: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    repository: "capo_codeartifact.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the package.</p>"""
    format: "capo_codeartifact.types.package_format.PackageFormat"
    """<p>A format that specifies the type of the package to be updated.</p>"""
    namespace: NotRequired["capo_codeartifact.types.package_namespace.PackageNamespace"]
    """<p>The namespace of the package to be updated. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package: "capo_codeartifact.types.package_name.PackageName"
    """<p>The name of the package to be updated.</p>"""
    restrictions: (
        "capo_codeartifact.types.package_origin_restrictions.PackageOriginRestrictions"
    )
    """<p>A <a href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html">PackageOriginRestrictions</a> object that contains information about the <code>upstream</code> and <code>publish</code> package origin restrictions. The <code>upstream</code> restriction determines if new package versions can be ingested or retained from external connections or upstream repositories. The <code>publish</code> restriction determines if new package versions can be published directly to the repository.</p> <p>You must include both the desired <code>upstream</code> and <code>publish</code> restrictions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutPackageOriginConfigurationRequest) -> dict:
    out: dict = {}
    import capo_codeartifact.types.package_origin_restrictions

    out["restrictions"] = (
        capo_codeartifact.types.package_origin_restrictions.serialize_json(
            value["restrictions"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutPackageOriginConfigurationRequest:
    out: PutPackageOriginConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("restrictions") is not None:
        import capo_codeartifact.types.package_origin_restrictions

        out["restrictions"] = (
            capo_codeartifact.types.package_origin_restrictions.deserialize_json(
                data["restrictions"]
            )
        )
    else:
        raise DeserializationError(
            "PutPackageOriginConfigurationRequest.restrictions required"
        )
    return out
