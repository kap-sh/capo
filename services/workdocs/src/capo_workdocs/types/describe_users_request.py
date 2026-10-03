"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeUsersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.field_names_type
    import capo_workdocs.types.id_type
    import capo_workdocs.types.limit_type
    import capo_workdocs.types.order_type
    import capo_workdocs.types.page_marker_type
    import capo_workdocs.types.search_query_type
    import capo_workdocs.types.user_filter_type
    import capo_workdocs.types.user_ids_type
    import capo_workdocs.types.user_sort_type


class DescribeUsersRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    organization_id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the organization.</p>"""
    user_ids: NotRequired["capo_workdocs.types.user_ids_type.UserIdsType"]
    """<p>The IDs of the users.</p>"""
    query: NotRequired["capo_workdocs.types.search_query_type.SearchQueryType"]
    """<p>A query to filter users by user name. Remember the following about the <code>Userids</code> and <code>Query</code> parameters:</p> <ul> <li> <p>If you don't use either parameter, the API returns a paginated list of all users on the site.</p> </li> <li> <p>If you use both parameters, the API ignores the <code>Query</code> parameter.</p> </li> <li> <p>The <code>Userid</code> parameter only returns user names that match a corresponding user ID.</p> </li> <li> <p>The <code>Query</code> parameter runs a "prefix" search for users by the <code>GivenName</code>, <code>SurName</code>, or <code>UserName</code> fields included in a <a href="https://docs.aws.amazon.com/workdocs/latest/APIReference/API_CreateUser.html">CreateUser</a> API call. For example, querying on <code>Ma</code> returns Márcia Oliveira, María García, and Mateo Jackson. If you use multiple characters, the API only returns data that matches all characters. For example, querying on <code>Ma J</code> only returns Mateo Jackson.</p> </li> </ul>"""
    include: NotRequired["capo_workdocs.types.user_filter_type.UserFilterType"]
    """<p>The state of the users. Specify "ALL" to include inactive users.</p>"""
    order: NotRequired["capo_workdocs.types.order_type.OrderType"]
    """<p>The order for the results.</p>"""
    sort: NotRequired["capo_workdocs.types.user_sort_type.UserSortType"]
    """<p>The sorting criteria.</p>"""
    marker: NotRequired["capo_workdocs.types.page_marker_type.PageMarkerType"]
    """<p>The marker for the next set of results. (You received this marker from a previous call.)</p>"""
    limit: NotRequired["capo_workdocs.types.limit_type.LimitType"]
    """<p>The maximum number of items to return.</p>"""
    fields: NotRequired["capo_workdocs.types.field_names_type.FieldNamesType"]
    """<p>A comma-separated list of values. Specify "STORAGE_METADATA" to include the user storage quota and utilization information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeUsersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeUsersRequest:
    out: DescribeUsersRequest = {}  # type: ignore[typeddict-item]
    return out
