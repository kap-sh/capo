"""Generated from Smithy shape ``com.amazonaws.codeartifact#PutRepositoryPermissionsPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.policy_document
    import capo_codeartifact.types.policy_revision
    import capo_codeartifact.types.repository_name


class PutRepositoryPermissionsPolicyRequest(TypedDict, closed=True):
    domain: "capo_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain containing the repository to set the resource policy on. </p>"""
    domain_owner: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    repository: "capo_codeartifact.types.repository_name.RepositoryName"
    """<p> The name of the repository to set the resource policy on. </p>"""
    policy_revision: NotRequired[
        "capo_codeartifact.types.policy_revision.PolicyRevision"
    ]
    """<p> Sets the revision of the resource policy that specifies permissions to access the repository. This revision is used for optimistic locking, which prevents others from overwriting your changes to the repository's resource policy. </p>"""
    policy_document: "capo_codeartifact.types.policy_document.PolicyDocument"
    """<p> A valid displayable JSON Aspen policy string to be set as the access control resource policy on the provided repository. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutRepositoryPermissionsPolicyRequest) -> dict:
    out: dict = {}
    if "policy_revision" in value:
        out["policyRevision"] = value["policy_revision"]
    out["policyDocument"] = value["policy_document"]
    return out


def deserialize_json(data: dict) -> PutRepositoryPermissionsPolicyRequest:
    out: PutRepositoryPermissionsPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("policyRevision") is not None:
        out["policy_revision"] = data["policyRevision"]
    if data.get("policyDocument") is not None:
        out["policy_document"] = data["policyDocument"]
    else:
        out["policy_document"] = ""
    return out
