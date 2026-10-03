"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#ListRepositoryAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.max_results
    import capo_codeguru_reviewer.types.names
    import capo_codeguru_reviewer.types.next_token
    import capo_codeguru_reviewer.types.owners
    import capo_codeguru_reviewer.types.provider_types
    import capo_codeguru_reviewer.types.repository_association_states


class ListRepositoryAssociationsRequest(TypedDict, closed=True):
    provider_types: NotRequired[
        "capo_codeguru_reviewer.types.provider_types.ProviderTypes"
    ]
    """<p>List of provider types to use as a filter.</p>"""
    states: NotRequired[
        "capo_codeguru_reviewer.types.repository_association_states.RepositoryAssociationStates"
    ]
    """<p>List of repository association states to use as a filter.</p> <p>The valid repository association states are:</p> <ul> <li> <p> <b>Associated</b>: The repository association is complete.</p> </li> <li> <p> <b>Associating</b>: CodeGuru Reviewer is:</p> <ul> <li> <p>Setting up pull request notifications. This is required for pull requests to trigger a CodeGuru Reviewer review.</p> <note> <p>If your repository <code>ProviderType</code> is <code>GitHub</code>, <code>GitHub Enterprise Server</code>, or <code>Bitbucket</code>, CodeGuru Reviewer creates webhooks in your repository to trigger CodeGuru Reviewer reviews. If you delete these webhooks, reviews of code in your repository cannot be triggered.</p> </note> </li> <li> <p>Setting up source code access. This is required for CodeGuru Reviewer to securely clone code in your repository.</p> </li> </ul> </li> <li> <p> <b>Failed</b>: The repository failed to associate or disassociate.</p> </li> <li> <p> <b>Disassociating</b>: CodeGuru Reviewer is removing the repository's pull request notifications and source code access.</p> </li> <li> <p> <b>Disassociated</b>: CodeGuru Reviewer successfully disassociated the repository. You can create a new association with this repository if you want to review source code in it later. You can control access to code reviews created in anassociated repository with tags after it has been disassociated. For more information, see <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/auth-and-access-control-using-tags.html">Using tags to control access to associated repositories</a> in the <i>Amazon CodeGuru Reviewer User Guide</i>.</p> </li> </ul>"""
    names: NotRequired["capo_codeguru_reviewer.types.names.Names"]
    """<p>List of repository names to use as a filter.</p>"""
    owners: NotRequired["capo_codeguru_reviewer.types.owners.Owners"]
    """<p>List of owners to use as a filter. For Amazon Web Services CodeCommit, it is the name of the CodeCommit account that was used to associate the repository. For other repository source providers, such as Bitbucket and GitHub Enterprise Server, this is name of the account that was used to associate the repository. </p>"""
    max_results: NotRequired["capo_codeguru_reviewer.types.max_results.MaxResults"]
    """<p>The maximum number of repository association results returned by <code>ListRepositoryAssociations</code> in paginated output. When this parameter is used, <code>ListRepositoryAssociations</code> only returns <code>maxResults</code> results in a single page with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListRepositoryAssociations</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter is not used, <code>ListRepositoryAssociations</code> returns up to 100 results and a <code>nextToken</code> value if applicable. </p>"""
    next_token: NotRequired["capo_codeguru_reviewer.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>ListRepositoryAssociations</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. </p> <note> <p>Treat this token as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRepositoryAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRepositoryAssociationsRequest:
    out: ListRepositoryAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
