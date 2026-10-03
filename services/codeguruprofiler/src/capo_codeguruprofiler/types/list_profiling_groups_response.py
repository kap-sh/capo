"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ListProfilingGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.pagination_token
    import capo_codeguruprofiler.types.profiling_group_descriptions
    import capo_codeguruprofiler.types.profiling_group_names


class ListProfilingGroupsResponse(TypedDict, closed=True):
    profiling_group_names: (
        "capo_codeguruprofiler.types.profiling_group_names.ProfilingGroupNames"
    )
    """<p> A returned list of profiling group names. A list of the names is returned only if <code>includeDescription</code> is <code>false</code>, otherwise a list of <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html"> <code>ProfilingGroupDescription</code> </a> objects is returned. </p>"""
    profiling_groups: NotRequired[
        "capo_codeguruprofiler.types.profiling_group_descriptions.ProfilingGroupDescriptions"
    ]
    """<p> A returned list <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html"> <code>ProfilingGroupDescription</code> </a> objects. A list of <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html"> <code>ProfilingGroupDescription</code> </a> objects is returned only if <code>includeDescription</code> is <code>true</code>, otherwise a list of profiling group names is returned. </p>"""
    next_token: NotRequired[
        "capo_codeguruprofiler.types.pagination_token.PaginationToken"
    ]
    """<p>The <code>nextToken</code> value to include in a future <code>ListProfilingGroups</code> request. When the results of a <code>ListProfilingGroups</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfilingGroupsResponse) -> dict:
    out: dict = {}
    import capo_codeguruprofiler.types.profiling_group_names

    out["profilingGroupNames"] = (
        capo_codeguruprofiler.types.profiling_group_names.serialize_json(
            value["profiling_group_names"]
        )
    )
    if "profiling_groups" in value:
        import capo_codeguruprofiler.types.profiling_group_descriptions

        out["profilingGroups"] = (
            capo_codeguruprofiler.types.profiling_group_descriptions.serialize_json(
                value["profiling_groups"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProfilingGroupsResponse:
    out: ListProfilingGroupsResponse = {}  # type: ignore[typeddict-item]
    if data.get("profilingGroupNames") is not None:
        import capo_codeguruprofiler.types.profiling_group_names

        out["profiling_group_names"] = (
            capo_codeguruprofiler.types.profiling_group_names.deserialize_json(
                data["profilingGroupNames"]
            )
        )
    else:
        raise DeserializationError(
            "ListProfilingGroupsResponse.profiling_group_names required"
        )
    if data.get("profilingGroups") is not None:
        import capo_codeguruprofiler.types.profiling_group_descriptions

        out["profiling_groups"] = (
            capo_codeguruprofiler.types.profiling_group_descriptions.deserialize_json(
                data["profilingGroups"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
