"""Generated from Smithy shape ``com.amazonaws.codeartifact#RepositoryDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.arn
    import capo_codeartifact.types.description
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.repository_external_connection_info_list
    import capo_codeartifact.types.repository_name
    import capo_codeartifact.types.timestamp
    import capo_codeartifact.types.upstream_repository_info_list


class RepositoryDescription(TypedDict, closed=True):
    name: NotRequired["capo_codeartifact.types.repository_name.RepositoryName"]
    """<p> The name of the repository. </p>"""
    administrator_account: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that manages the repository. </p>"""
    domain_name: NotRequired["capo_codeartifact.types.domain_name.DomainName"]
    """<p> The name of the domain that contains the repository. </p>"""
    domain_owner: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain that contains the repository. It does not include dashes or spaces. </p>"""
    arn: NotRequired["capo_codeartifact.types.arn.Arn"]
    """<p> The Amazon Resource Name (ARN) of the repository. </p>"""
    description: NotRequired["capo_codeartifact.types.description.Description"]
    """<p> A text description of the repository. </p>"""
    upstreams: NotRequired[
        "capo_codeartifact.types.upstream_repository_info_list.UpstreamRepositoryInfoList"
    ]
    """<p> A list of upstream repositories to associate with the repository. The order of the upstream repositories in the list determines their priority order when CodeArtifact looks for a requested package version. For more information, see <a href="https://docs.aws.amazon.com/codeartifact/latest/ug/repos-upstream.html">Working with upstream repositories</a>. </p>"""
    external_connections: NotRequired[
        "capo_codeartifact.types.repository_external_connection_info_list.RepositoryExternalConnectionInfoList"
    ]
    """<p> An array of external connections associated with the repository. </p>"""
    created_time: NotRequired["capo_codeartifact.types.timestamp.Timestamp"]
    """<p>A timestamp that represents the date and time the repository was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RepositoryDescription) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "administrator_account" in value:
        out["administratorAccount"] = value["administrator_account"]
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "domain_owner" in value:
        out["domainOwner"] = value["domain_owner"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "upstreams" in value:
        import capo_codeartifact.types.upstream_repository_info_list

        out["upstreams"] = (
            capo_codeartifact.types.upstream_repository_info_list.serialize_json(
                value["upstreams"]
            )
        )
    if "external_connections" in value:
        import capo_codeartifact.types.repository_external_connection_info_list

        out["externalConnections"] = (
            capo_codeartifact.types.repository_external_connection_info_list.serialize_json(
                value["external_connections"]
            )
        )
    if "created_time" in value:
        import capo_codeartifact.types.timestamp

        out["createdTime"] = capo_codeartifact.types.timestamp.serialize_json(
            value["created_time"]
        )
    return out


def deserialize_json(data: dict) -> RepositoryDescription:
    out: RepositoryDescription = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("administratorAccount") is not None:
        out["administrator_account"] = data["administratorAccount"]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    if data.get("domainOwner") is not None:
        out["domain_owner"] = data["domainOwner"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("upstreams") is not None:
        import capo_codeartifact.types.upstream_repository_info_list

        out["upstreams"] = (
            capo_codeartifact.types.upstream_repository_info_list.deserialize_json(
                data["upstreams"]
            )
        )
    if data.get("externalConnections") is not None:
        import capo_codeartifact.types.repository_external_connection_info_list

        out["external_connections"] = (
            capo_codeartifact.types.repository_external_connection_info_list.deserialize_json(
                data["externalConnections"]
            )
        )
    if data.get("createdTime") is not None:
        import capo_codeartifact.types.timestamp

        out["created_time"] = capo_codeartifact.types.timestamp.deserialize_json(
            data["createdTime"]
        )
    return out
