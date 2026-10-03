"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ListProfilingGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.max_results
    import capo_codeguruprofiler.types.pagination_token


class ListProfilingGroupsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_codeguruprofiler.types.pagination_token.PaginationToken"
    ]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>ListProfilingGroups</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. </p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    max_results: NotRequired["capo_codeguruprofiler.types.max_results.MaxResults"]
    """<p>The maximum number of profiling groups results returned by <code>ListProfilingGroups</code> in paginated output. When this parameter is used, <code>ListProfilingGroups</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListProfilingGroups</code> request with the returned <code>nextToken</code> value. </p>"""
    include_description: NotRequired["bool"]
    """<p>A <code>Boolean</code> value indicating whether to include a description. If <code>true</code>, then a list of <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html"> <code>ProfilingGroupDescription</code> </a> objects that contain detailed information about profiling groups is returned. If <code>false</code>, then a list of profiling group names is returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfilingGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProfilingGroupsRequest:
    out: ListProfilingGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
