"""Generated from Smithy shape ``com.amazonaws.datazone#ListProjectsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.max_results
    import capo_datazone.types.pagination_token
    import capo_datazone.types.project_name


class ListProjectsInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain.</p>"""
    user_identifier: NotRequired["str"]
    """<p>The identifier of the Amazon DataZone user.</p>"""
    group_identifier: NotRequired["str"]
    """<p>The identifier of a group.</p>"""
    name: NotRequired["capo_datazone.types.project_name.ProjectName"]
    """<p>The name of the project.</p>"""
    project_category: NotRequired["str"]
    """<p>A parameter to filter projects by their category.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of projects is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of projects, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListProjects</code> to list the next set of projects.</p>"""
    max_results: NotRequired["capo_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of projects to return in a single call to <code>ListProjects</code>. When the number of projects to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListProjects</code> to list the next set of projects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProjectsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProjectsInput:
    out: ListProjectsInput = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: ListProjectsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
