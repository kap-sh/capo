"""Generated from Smithy shape ``com.amazonaws.datazone#ListProjectProfilesInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.max_results
    import capo_datazone.types.pagination_token
    import capo_datazone.types.project_profile_name
    import capo_datazone.types.sort_field_project
    import capo_datazone.types.sort_order


class ListProjectProfilesInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to list project profiles.</p>"""
    name: NotRequired["capo_datazone.types.project_profile_name.ProjectProfileName"]
    """<p>The name of a project profile.</p>"""
    sort_by: NotRequired["capo_datazone.types.sort_field_project.SortFieldProject"]
    """<p>Specifies by what to sort project profiles.</p>"""
    sort_order: NotRequired["capo_datazone.types.sort_order.SortOrder"]
    """<p>Specifies the sort order of the project profiles.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of project profiles is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of project profiles, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListProjectProfiles to list the next set of project profiles.</p>"""
    max_results: NotRequired["capo_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of project profiles to return in a single call to ListProjectProfiles. When the number of project profiles to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListProjectProfiles to list the next set of project profiles.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProjectProfilesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProjectProfilesInput:
    out: ListProjectProfilesInput = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: ListProjectProfilesInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
